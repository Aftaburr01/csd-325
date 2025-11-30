"""
test_cities.py

Tests for the city_country function in city_functions.py.
"""
import unittest
from city_functions import city_country

class CitiesTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_city_country_simple(self):
        """Test for the 'City, Country - population xxx' format."""
        formatted_name = city_country('santiago', 'chile', 5000000)
        self.assertEqual(formatted_name, 'Santiago, Chile - population 5,000,000')

    def test_city_country_population(self):
        """Test for the 'City, Country - population xxx' format."""
        formatted_name = city_country('tokyo', 'japan', 13960000)
        expected_output = 'Tokyo, Japan - population 13,960,000'
        self.assertEqual(formatted_name, expected_output)

    def test_city_country_all_params(self):
        """Test for the 'City, Country - population xxx, Language' format."""
        formatted_name = city_country('paris', 'france', 2140000, 'french')
        expected_output = 'Paris, France - population 2,140,000, French'
        self.assertEqual(formatted_name, expected_output)

    def test_city_country_only_language(self):
        """Test for the case where only City, Country, and Language are provided."""
        formatted_name = city_country('madrid', 'spain', 6400000, 'spanish')
        expected_output = 'Madrid, Spain - population 6,400,000, Spanish'
        self.assertEqual(formatted_name, expected_output)

if __name__ == '__main__':
    unittest.main()