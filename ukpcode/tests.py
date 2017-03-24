import unittest
import ukpcode
from ukpcode.exceptions import MinLengthException, MaxLengthException, InvalidPostcodeException


class UKPCodeTest(unittest.TestCase):

    def test_get_inward(self):
        self.assertEqual("1BB", ukpcode._get_inward("EC1A1BB"))

    def test_get_outward(self):
        self.assertEqual("EC1A", ukpcode._get_outward("EC1A1BB"))

    def test_is_already_formatted(self):
        self.assertTrue(ukpcode._is_already_formatted("EC1A 1BB"))

    def test_invalid_is_not_already_formatted(self):
        self.assertFalse(ukpcode._is_already_formatted("EC1 A1BB"))

    def test_is_not_already_formatted(self):
        self.assertFalse(ukpcode._is_already_formatted("EC1A1BB"))

    def test_validate_min_length(self):
        with self.assertRaises(MinLengthException):
            ukpcode._validate_length("M11A")

    def test_validate_formatted_min_length(self):
        with self.assertRaises(MinLengthException):
            ukpcode._validate_length("W0AX")

    def test_validate_max_length(self):
        with self.assertRaises(MaxLengthException):
            ukpcode._validate_length("EC1A1BB1")

    def test_validate_formatted_max_length(self):
        with self.assertRaises(MaxLengthException):
            ukpcode._validate_length("EC1A1 BB1")

    def test_invalid_inward(self):
        with self.assertRaises(InvalidPostcodeException):
            ukpcode._validate_length("EC1A BBB")

    def test_format_eight_chars(self):
        self.assertEqual("EC1A 1BB", ukpcode.format("EC1A1BB"))

    def test_format_seven_chars(self):
        self.assertEqual("W1A 0AX", ukpcode.format("W1A0AX"))

    def test_format_five_chars(self):
        self.assertEqual("M1 1AE", ukpcode.format("M11AE"))

    def test_already_formatted_six_chars(self):
        self.assertEqual("M1 1AE", ukpcode.format("M1 1AE"))

    def test_already_formatted_seven_chars(self):
        self.assertEqual("W1A 0AX", ukpcode.format("W1A 0AX"))


if __name__ == '__main__':
    unittest.main()