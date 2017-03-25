import unittest
import ukpcode
from string import ascii_uppercase
from ukpcode import constants
from ukpcode import exceptions


class UKPCodeTest(unittest.TestCase):

    def get_valid_letters(self, invalid):
        invalid_letters = list(invalid)
        return list(set(ascii_uppercase) - set(invalid_letters))


    def test_valid_min_length(self):
        self.assertTrue(ukpcode._validate_length("M11AS"))

    def test_invalid_min_length(self):
        with self.assertRaises(exceptions.MinLengthException):
            ukpcode._validate_length("M11A")

    def test_valid_formatted_min_length(self):
        self.assertTrue(ukpcode._validate_length("W0 WX3"))

    def test_invalid_formatted_min_length(self):
        with self.assertRaises(exceptions.MinLengthException):
            ukpcode._validate_length("W0 WX")

    def test_valid_max_length(self):
        self.assertTrue(ukpcode._validate_length("EC1ABB1"))

    def test_invalid_max_length(self):
        with self.assertRaises(exceptions.MaxLengthException):
            ukpcode._validate_length("EC1A1BB1")

    def test_valid_formatted_max_length(self):
        self.assertTrue(ukpcode._validate_length("EC1A BB1"))

    def test_invalid_formatted_max_length(self):
        with self.assertRaises(exceptions.MaxLengthException):
            ukpcode._validate_length("EC1A1 BB1")

    def test_valid_inward(self):
        self.assertTrue(ukpcode._validate_inward("EC1A 1BB"))

    def test_invalid_inward(self):
        with self.assertRaises(exceptions.InvalidInwardException):
            ukpcode._validate_inward("EC1A BBB")

    def test_valid_letters_to_inkward(self):
        for valid in self.get_valid_letters(constants.INVALID_LETTERS_TO_INWARD):
            self.assertTrue(ukpcode._validate_inward("EC1A 1%sB" % valid))
            self.assertTrue(ukpcode._validate_inward("EC1A 1B%s" % valid))

    def test_invalid_letters_to_inkward(self):
        for invalid in constants.INVALID_LETTERS_TO_INWARD:
            with self.assertRaises(exceptions.InvalidInwardException):
                ukpcode._validate_inward("EC1A 1%sB" % invalid)
            with self.assertRaises(exceptions.InvalidInwardException):
                ukpcode._validate_inward("EC1A 1B%s" % invalid)

    def test_invalid_outward_first_digit(self):
        for invalid in constants.INVALID_LETTERS_TO_FIRST_DIGIT:
            with self.assertRaises(exceptions.InvalidOutwardException):
                ukpcode._validate_outward("%sC1A 1BB" % invalid)           

    def test_valid_outward_first_digit(self):
        for valid in self.get_valid_letters(constants.INVALID_LETTERS_TO_FIRST_DIGIT):
            self.assertTrue(ukpcode._validate_outward("%sC1A 1BB" % valid))


    def test_get_inward(self):
        self.assertEqual("1BB", ukpcode._get_inward("EC1A1BB"))

    def test_get_downcase_inward(self):
        self.assertEqual("1BB", ukpcode._get_inward("ec1a1bb"))

    def test_get_outward(self):
        self.assertEqual("EC1A", ukpcode._get_outward("EC1A1BB"))

    def test_get_downcase_outward(self):
        self.assertEqual("EC1A", ukpcode._get_outward("ec1a1bb"))


    def test_is_valid(self):
        self.assertTrue(ukpcode.is_valid("EC1A1BB"))

    def test_min_length_is_not_valid(self):
        self.assertFalse(ukpcode.is_valid("E1BB"))

    def test_max_length_is_not_valid(self):
        self.assertFalse(ukpcode.is_valid("EC1AS1BB"))

    def test_inward_is_not_valid(self):
        self.assertFalse(ukpcode.is_valid("EC1ABB1"))


    def test_format_eight_chars(self):
        self.assertEqual("EC1A 1BB", ukpcode.format("EC1A1BB"))

    def test_format_seven_chars(self):
        self.assertEqual("W1A 0AX", ukpcode.format("W1A0AX"))

    def test_format_five_chars(self):
        self.assertEqual("M1 1AE", ukpcode.format("M11AE"))

    def test_format_already_formatted(self):
        self.assertEqual("M1 1AE", ukpcode.format("M1 1AE"))

    def test_format_unnecessary_spaces(self):
        self.assertEqual("M1 1AE", ukpcode.format(" M1  1AE  "))

if __name__ == '__main__':
    unittest.main()
