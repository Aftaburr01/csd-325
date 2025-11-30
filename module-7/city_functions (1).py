"""

city_functions.py

Function: city_country
Accepts city and country names (required) and population and language (optional).
Returns a formatted string.
"""

def city_country(city, country, population, language=None):
    """
    Returns a string formatted as 'City, Country - population xxx' or 'City, Country - population xxx, Language'

    The population parameter is required. The language parameter is optional.
    """
    # Format population with commas for readability
    if isinstance(population, int):
        pop_formatted = f"{population:,}"
    else:
        pop_formatted = str(population)
    
    output_string = f"{city.title()}, {country.title()} - population {pop_formatted}"
    
    # Add language if provided
    if language is not None:
        output_string += f", {language.title()}"
    
    return output_string

# --- Required Demonstration Calls ---

if __name__ == '__main__':
    print("--- Demonstration Calls ---")

    # Call 1: City, Country, Population (no language)
    result1 = city_country('santiago', 'chile', 5000000)
    print(f"Call 1 (City, Country, Population): {result1}")

    # Call 2: City, Country, Population (no language)
    result2 = city_country('tokyo', 'japan', 13960000)
    print(f"Call 2 (City, Country, Population): {result2}")

    # Call 3: City, Country, Population, Language
    result3 = city_country('paris', 'france', 2140000, 'french')
    print(f"Call 3 (City, Country, Population, Language): {result3}")

    print("-" * 30)