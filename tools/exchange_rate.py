import requests
from langchain.tools import tool

@tool
def get_exchanged_amount(amount: float) -> float:
    """
    This function retrieves the exchange rate between dollar and brazilian real and converts a given amount.
    
    Args:
        amount (float): The amount of money to convert.
        
    Returns:
        float: The converted amount rounded to 2 decimal places.
    """
    response = requests.get(f"https://api.frankfurter.dev/v1/latest?from=USD&to=BRL")
    data = response.json()
    converted_amount = amount * data['rates']['BRL']
    return round(converted_amount, 2)
    