import json
from typing import Dict, Tuple
from openai import OpenAI
from config import OPENAI_API_KEY, OPENAI_MODEL
from categories import build_category_list_string

client = OpenAI(api_key=OPENAI_API_KEY)

def classify_expense(
        merchant: str,
        description: str,
        categories: Dict[str, str]
    ) -> Tuple[str, float]:
    """
    Classifies a single expense using the OpenAI model.
    Returns: (chosen_category_code, confidence_score, reasoning)
    """

    category_list_text = build_category_list_string(categories)

    prompt = f"""

You are an expense categorization assistant.

Given:
Merchant: "{merchant}"
Description: "{description}"

Choose ONE category from the list below based ONLY on meaning:
{category_list_text}

Return ONLY this JSON structure:
{{
  "category": "<CATEGORY_CODE>",
  "confidence": <number between 0 and 100>,
  "reasoning": "<short explanation>"
}}
"""

    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    # Extract the text the model returned
    raw_output = response.choices[0].message.content

    try:
        parsed = json.loads(raw_output)
        return (
            parsed.get("category", "UNKNOWN"),
            parsed.get("confidence", 0),
            parsed.get("reasoning", "No reasoning provided.")
        )
    except json.JSONDecodeError:
        return ("UNKNOWN", 0, f"Bad output from model: {raw_output}")

