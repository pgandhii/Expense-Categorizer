import json 
from openai import OpenAI
import sys, os
sys.path.append(os.path.dirname(__file__))

from config import OPENAI_API_KEY, OPENAI_MODEL, CONFIDENCE_THRESHOLD
from categories import load_categories, build_category_list_string

#Initialize client
client = OpenAI(api_key=OPENAI_API_KEY)

def classify_expense(merchant: str, purpose: str):
    """
    Classifies an expense using BOTH merchant name and purpose.
    Loads categories automatically (no need to pass anything in).
    """
    categories = load_categories()
    category_list = build_category_list_string(categories)
    prompt = f"""
You are an AI assistant that helps classify business expenses. You MUST use BOTH the merchant name and 
the purpose when choosing a category. 

Some important rules to follow:
1. Never reply on only the merchange name, unless there is no other information.
2. Purpose is useful in classification. If there is purpose, use your best interpretation of the merchant.
3. Amazon, walmart, target, etc are general merchants that sell everything. You MUST use the purpose to classify expenses from these merchants.
4. If you are not confident in your classification (less than {CONFIDENCE_THRESHOLD}, return NEED TO CHECK.
5. Give me the merchant name priority, and then use the purpose to clarify the purpose. For example, categories such as 
'Travel Meals' and 'Meals and Entertainment' are very confusing without the purpose.

Here is a list of allowed categories (code -> name):
{category_list}

Please classify the following expenses:
Marchant: {merchant}
Purpose: {purpose}

Return ONLY valid JSON:
{{
"category_code":"<code>",
"category_name":"<category name>",
"confidence":<number between 0-100>,
"reason":"<explanation for your choice>"
}}
"""
    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    raw_output = response.choices[0].message.content.strip()

    try:
        data = json.loads(raw_output)
    except json.JSONDecodeError:
        return {
            "category_code": None,
            "category_name": None,
            "confidence": 0,
            "final_result": "unclassified",
            "reason": f"Failed to parse JSON response: {raw_output}"
        }
    
    category_code = data.get("category_code")
    category_name = data.get("category_name")
    confidence = data.get("confidence", 0)
    reason = data.get("reason", "")

    if confidence < CONFIDENCE_THRESHOLD:
        final_result = "NEED TO CHECK"
    else:
        final_result = category_code

    return {
        "category_code": category_code,
        "category_name": category_name,
        "confidence": confidence,
        "final_result": final_result,
        "reason": reason
    }


if __name__ == "__main__":
    #Example usage
    categories = load_categories
    result = classify_expense(
        merchant = "Meteor Cafe",
        purpose = "Coffee"
    )
    print(result)