import requests
QUESTIONS_AMOUNT = 10
TYPE = "boolean"
# CATEGORY = 14  # Television

params = {
    "amount": QUESTIONS_AMOUNT,
    # "category": CATEGORY,  # Remove for any category
    "type": TYPE
}

response = requests.get("https://opentdb.com/api.php", params=params)
response.raise_for_status()
question_data = response.json()["results"]
