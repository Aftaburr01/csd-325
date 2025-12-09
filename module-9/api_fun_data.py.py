"""
api_fun_data.py

Completes the third section of the Module 9 API Assignment:
1. Tests connection to a simple API (Dog Facts).
2. Prints raw response.
3. Prints formatted response.
"""
import requests
import json
import sys

# We'll use the Dog Facts API from the simple API list
FUN_API_URL = 'https://dog-api.kinduff.com/api/facts'

def use_fun_api():
    """Tests connection, prints raw and formatted output from the fun API."""
    print("\n" + "="*50)
    print("--- 3. Using a Simple Fun API (Dog Facts) ---")
    print("="*50)

    # --- 1. Test the connection and get response ---
    try:
        response = requests.get(FUN_API_URL)
        status_code = response.status_code
        print(f"API Connection Status Code: {status_code}")
        
        if status_code != 200:
            print("API connection failed. Exiting.")
            return

    except requests.exceptions.RequestException as e:
        print(f"Error connecting to the API: {e}")
        return

    # --- 2. Print out the response, with no formatting (Raw Text) ---
    print("\n--- Raw Response (No Formatting) ---")
    # Prints the response as a single, unformatted string
    print(response.text) 

    # --- 3. Print out the response with formatting ---
    try:
        data = response.json()
    except json.JSONDecodeError:
        print("\nError: Could not decode JSON response.")
        return

    print("\n--- Formatted Output (from JSON Data) ---")
    
    # Check if the API returned facts and print them nicely
    if data.get('facts'):
        print(f"Successfully retrieved {len(data['facts'])} dog fact(s):")
        # Format similar to the tutorial's style
        for i, fact in enumerate(data['facts']):
            print(f"  Fact {i+1}: {fact}")
    else:
        print("Error: Fact data was not found in the response.")

if __name__ == '__main__':
    use_fun_api()