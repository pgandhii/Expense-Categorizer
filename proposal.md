# The Big Idea

Accounting teams and employees waste hours each monht manually tagging corporate credit card trasnactions into their accounting GL. Merchant names are cryptic, memo fields vary, and default bank catgeories rarely match a company's custom chart of accounts. 

The goal is to build a python based expense categorization software that takes in a Capital One Excel sheet and a company specific category map, then assigns a best-fit category for each transaction, along with the category code, using a hybrid approach:
* Deterministic rules for high confidence matches, such as known vendors
* LLM embeddings for fuzzy matches and logn tail merchants, with a confidence score

This helps reduce the time to close financial books at month end, results in fewer miscodes, and helps build cleaner budgets.

### MVP
A python file that reads the excel sheet with all the credit card transactions and GL categories, cleans merchant and description text, applies rule-based mapping (dictionary), and uses Open AI to map to the closest category. Finally, it produces an output with the category, confidence score, and flags "review" when confidence < threshold.

### Nice to Have
I would like to have either a web UI/app where this can be done with active learnings, so if the categories are updated, it can allow mapping to the new categories. I would also like to add some encryption in the future to ensure that the company data is not shared on the internet.

# Learning Objective
* Practice problem solving through data cleaning, prompt engineering, evaluation and utilising packages.
* Learn to design a robust process with configuration, logging, and tests.
* Learn OpenAI embeddings and similarity search patterns for classification.
* Finally, practice what I have learnt in class to improve retention and future application.

# Implementation Plan
### Inputs
* CC_expenses.xlsx - from the bank's platform with columns such as Date, Description, Category, Purpose and Amount
* GL_categories.xlsx - a list of company categories and their codes for Acumatica

### Core Components
* Data loader & cleaner: Standardize columns, normalize amounts, strip punctuations/stopwords, collapse repeated whitespaces
* Rule engine: Exact and fuzzy vendor disctionary
* Choose category with the highest confidence through cosine similarity (not entirely sure about how this works, need to look into it)
* Return confidence, category and category code

### Decision & Output
* If rule >= threshold -> accept rule result
* Else, return category with a "Needs Review" tag

### Evaluation
I will evaluate the result using a dataset I have of hand labeled sample set which I created during my internship. I will then create a score, and improve the code accordingly.

### Libraries
From the research I have done using AI, it looks like I will be using the following libraries and services:
* Python 3.11
* pandas
* numpy
* scikit-learn to find similarity and metrics
* openai
* pyyaml for configaration
* pytest to test the output and model
* Need to learn more about uvicorn/FastAPI, loguru, typer

The project seems doable from my conversation with the professor, so I do not have a fallback strategy as of right now.

# Project Schedule
### Week 1 
* I will gather all the information -- the categories and expenses -- and clean up the data to remove confidential information.
* I will learn more about the OpenAI API, and the other programs I am using.

### Week 2
* Build a data loader, text cleaner, rule engine.
* Compute category vectors and implement similarity/ confidence scores.
* Try to run the tests and check out metrics

### Week 3
* Improve prompts
* Look into FastAPI and how I can implement that
* Add thresholds

### Week 4
* Testing and debugging, while improving the project to reach the decised MVP.
* Ensure the output is as expected, and if not, altering that
* Submit project

# Collaboration Plan
I will be working alone on this project.

# Risk and Limitations
* It might be tricky to ensure the company is comfortable with me using their data.
* Overfitting to the data provided

# Additional Course Content
I don't think I am using any information from another course.
