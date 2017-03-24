import unittest
import ukpcode
from ukpcode.exceptions import MinLengthException, MaxLengthException, InvalidPostcodeException


class UKPCodeTest(unittest.TestCase):

    def test_format_eight_chars(self):
        self.assertEqual("EC1A 1BB", ukpcode.format("EC1A1BB"))

    def test_format_seven_chars(self):
        self.assertEqual("W1A 0AX", ukpcode.format("W1A0AX"))

    def test_format_five_chars(self):
        self.assertEqual("M1 1AE", ukpcode.format("M11AE"))

    def test_already_formated_six_chars(self):
        self.assertEqual("M1 1AE", ukpcode.format("M1 1AE"))

    def test_already_formated_seven_chars(self):
        self.assertEqual("W1A 0AX", ukpcode.format("W1A 0AX"))

    def test_raise_min_length_exception(self):
        with self.assertRaises(MinLengthException):
            ukpcode.format("M11A")

    def test_formated_raise_min_length_exception(self):
        with self.assertRaises(MinLengthException):
            ukpcode.format("W0AX")

    def test_raise_max_length_exception(self):
        with self.assertRaises(MaxLengthException):
            ukpcode.format("EC1A1BB1")

    def test_formated_raise_max_length_exception(self):
        with self.assertRaises(MaxLengthException):
            ukpcode.format("EC1A1 BB1")

    def test_invalid_inward(self):
        with self.assertRaises(InvalidPostcodeException):
            ukpcode.format("EC1A BBB")



if __name__ == '__main__':
    unittest.main()