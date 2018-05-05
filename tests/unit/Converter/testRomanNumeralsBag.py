import unittest
from src.Converter.RomanNumeralsBag import RomanNumeralsBag
from src.Converter.Exception import Exception as RomanNumeralException

class Test(unittest.TestCase):
    """ Tests the RomanNumeralsBag"""

    def test_equals(self):
        """Tests the output of the actual list entries of the Bag"""
        roman_numerals_bag = RomanNumeralsBag()
        roman_numerals_bag.append_numeral('X')
        self.assertEqual(roman_numerals_bag.numeralsList, ['X'])
        roman_numerals_bag.append_numeral('L')
        self.assertEqual(roman_numerals_bag.numeralsList, ['X', 'L'])

    def test_stringify(self):
        """Tests the output after performing basic insert operation on the Bag"""
        roman_numerals_bag = RomanNumeralsBag()
        roman_numerals_bag.append_numeral('X')
        self.assertEqual(str(roman_numerals_bag), 'X')
        roman_numerals_bag.append_numeral('L')
        self.assertEqual(str(roman_numerals_bag), 'XL')

    def test_exception_appending_invalid_numeral(self):
        with self.assertRaises(RomanNumeralException) as context:
            """Tests to make sure an exception is raised upon appending an invalid numeral"""
            roman_numerals_bag = RomanNumeralsBag()
            roman_numerals_bag.append_numeral('II')
