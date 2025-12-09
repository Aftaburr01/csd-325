"""
api_tutorial_opennotify.py

Completes the first two sections of the Module 9 API Assignment:
1. Tests connection to Google.
2. Retrieves and formats current astronaut data from OpenNotify.
"""
import requests
import json
import sys

# --- Section 1: Connection Test to Google ---
def test_google_connection():
    """Tests connection to Google and prints the status code."""
    print("--- 1. Testing Connection to Google ---")
    try:
        response = requests.get('http://www.google.com')
        # A status code of 200 means success
        print(f"Google Connection Status Code: {response.status_code}")
        if response.status_code == 200:
            print("Google connection successful.")
        else:
            print("Google connection failed.")
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to Google: {e}")

# --- Section 2: Retrieving Current Astronauts ---
def get_and_format_astronauts():
    """Retrieves and formats current astronauts from OpenNotify API."""
    ASTROS_URL = 'http://api.open-notify.org/astros.json'
    
    print("\n--- 2. Retrieving and Formatting Astronaut Data ---")
    
    # Test connection to the OpenNotify API first
    try:
        response = requests.get(ASTROS_URL)
        print(f"OpenNotify Status Code: {response.status_code}")
        if response.status_code != 200:
            print("Error: Could not connect to OpenNotify API successfully.")
            return

    except requests.exceptions.RequestException as e:
        print(f"Error connecting to OpenNotify: {e}")
        return

    # Process the JSON response
    try:
        data = response.json()
    except json.JSONDecodeError:
        print("Error: Could not decode JSON response.")
        return

    print(f"\nThere are currently {data['number']} astronauts in space.")
    print("Astronauts and their spacecraft:")

    # Format output based on the tutorial requirement
    for astronaut in data['people']:
        print(f"  Name: {astronaut['name']}, Craft: {astronaut['craft']}")

    # --- Extra: Print raw JSON for comparison (optional but useful) ---
    # print("\n--- Raw JSON Data ---")
    # print(json.dumps(data, indent=4))
    
if __name__ == '__main__':
    test_google_connection()
    get_and_format_astronauts()
