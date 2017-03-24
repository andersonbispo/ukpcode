import unittest
import ukpcode
from ukpcode.exceptions import MinLengthException, MaxLengthException, InvalidPostcodeException


class UKPCodeTest(unittest.TestCase):

    def test_validate_min_length(self):
        ukpcode._validate_length("M11AS")
        with self.assertRaises(MinLengthException):
            ukpcode._validate_length("M11A")

    def test_validate_formatted_min_length(self):
        ukpcode._validate_length("W0 WX3")
        with self.assertRaises(MinLengthException):
            ukpcode._validate_length("W0 WX")

    def test_validate_max_length(self):
        ukpcode._validate_length("EC1ABB1")
        with self.assertRaises(MaxLengthException):
            ukpcode._validate_length("EC1A1BB1")

    def test_validate_formatted_max_length(self):
        ukpcode._validate_length("EC1A BB1")
        with self.assertRaises(MaxLengthException):
            ukpcode._validate_length("EC1A1 BB1")

    def test_validate_inward(self):
        ukpcode._validate_inward("EC1A 1BB")
        with self.assertRaises(InvalidPostcodeException):
            ukpcode._validate_inward("EC1A BBB")


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