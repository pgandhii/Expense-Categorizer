# The Big Idea

Accounting teams and employees waste hours each monht manually tagging corporate credit card trasnactions into their accounting GL. Merchant names are cryptic, memo fields vary, and default bank catgeories rarely match a company's custom chart of accounts. 

The goal is to build a python based expense categorization software that takes in a Capital One Excel sheet and a company specific category map, then assigns a best-fit category for each transaction, along with the category code, using a hybrid approach:
* Deterministic rules for high confidence matches, such as known vendors
* LLM embeddings for fuzzy matches and logn tail merchants, with a confidence score

This helps reduce the time to close financial books at month end, results in fewer miscodes, and helps build cleaner budgets.

### MVP
A python file that reads the excel sheet with all the credit card transactions and GL categories, cleans merchant and description text, applies rule-based mapping (dictionary), and uses Open AI to map to the closest category. Finally, it produces an output with the category, confidence score, and flags "review" when confidence < threshold.

### Nice to Have
I would like to have either a web UI/app where this can be done with active learnings, so if the categories are updated, it can allow mapping to the new categories. 

# Learning Objective