import unittest
import ukpcode
from string import ascii_uppercase
from ukpcode import constants
from ukpcode import exceptions


class UKPCodeTest(unittest.TestCase):

    def get_inverted_letters(self, letters):
        letters_list = list(letters)
        return list(set(ascii_uppercase) - set(letters_list))


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
            ukpcode._validate_length("EC1A1 BBB")


    def test_valid_inward(self):
        self.assertTrue(ukpcode._validate_inward("EC1A 1BB"))

    def test_invalid_inward(self):
        with self.assertRaises(exceptions.InvalidInwardException):
            ukpcode._validate_inward("EC1A BBB")
        with self.assertRaises(exceptions.InvalidInwardException):
            ukpcode._validate_inward("EC1A 1B1")
        with self.assertRaises(exceptions.InvalidInwardException):
            ukpcode._validate_inward("EC1A 11B")

    def test_valid_letters_to_inkward(self):
        invalid_letters = constants.INVALID_LETTERS_TO_INWARD
        for valid in self.get_inverted_letters(invalid_letters):
            self.assertTrue(ukpcode._validate_inward("EC1A 1%sB" % valid))
            self.assertTrue(ukpcode._validate_inward("EC1A 1B%s" % valid))

    def test_valid_numbers_to_inkward(self):
        for valid in range(10):
            self.assertTrue(ukpcode._validate_inward("EC1A %sBB" % valid))

    def test_invalid_letters_to_inkward(self):
        for invalid in constants.INVALID_LETTERS_TO_INWARD:
            with self.assertRaises(exceptions.InvalidInwardException):
                ukpcode._validate_inward("EC1A 1%sB" % invalid)
            with self.assertRaises(exceptions.InvalidInwardException):
                ukpcode._validate_inward("EC1A 1B%s" % invalid)


    def test_valid_outward_first_digit(self):
        invalid_letters = constants.INVALID_LETTERS_TO_FIRST_DIGIT
        for valid in self.get_inverted_letters(invalid_letters):
            self.assertTrue(
                ukpcode._is_valid_outward_format_one("%sC1A" % valid)
            )

    def test_invalid_outward_first_digit(self):
        for invalid in constants.INVALID_LETTERS_TO_FIRST_DIGIT:
            self.assertFalse(
                ukpcode._is_valid_outward_format_one("%sC1A" % invalid)
            )

    def test_outward_first_format_valid_second_digit(self):
        invalid_letters = constants.INVALID_LETTERS_TO_SECOND_DIGIT
        for valid in self.get_inverted_letters(invalid_letters):
            outward = "E%s1A" % valid
            self.assertTrue(ukpcode._is_valid_outward_format_one(outward))

    def test_outward_first_format_invalid_second_digit(self):
        for invalid in constants.INVALID_LETTERS_TO_SECOND_DIGIT:
            self.assertFalse(
                ukpcode._is_valid_outward_format_one("E%s1A" % invalid)
            )

    def test_outward_first_format_valid_third_digit(self):
        for valid in range(10):
            outward = "EC%sA" % valid
            self.assertTrue(ukpcode._is_valid_outward_format_one(outward))

    def test_outward_first_format_invalid_third_digit(self):
        self.assertFalse(ukpcode._is_valid_outward_format_one("ECAA"))

    def test_outward_first_format_valid_forth_digit(self):
        for valid in constants.VALID_LETTERS_TO_FORTH_DIGIT:
            outward = "EC1%s" % valid
            self.assertTrue(ukpcode._is_valid_outward_format_one(outward))

    def test_outward_first_format_invalid_forth_digit(self):
        valid_letters = constants.VALID_LETTERS_TO_FORTH_DIGIT
        for invalid in self.get_inverted_letters(valid_letters):
            self.assertFalse(
                ukpcode._is_valid_outward_format_one("EC1%s" % invalid)
            )

    def test_outward_second_format_valid_second_digit(self):
        for valid in range(10):
            outward = "W%sA" % valid
            self.assertTrue(ukpcode._is_valid_outward_format_two(outward))

    def test_outward_second_format_invalid_second_digit(self):
        self.assertFalse(ukpcode._is_valid_outward_format_two("WAA"))

    def test_outward_second_format_valid_third_digit(self):
        for valid in constants.VALID_LETTERS_TO_THIRD_DIGIT:
            outward = "W1%s" % valid
            self.assertTrue(ukpcode._is_valid_outward_format_two(outward))

    def test_outward_second_format_invalid_third_digit(self):
        valid_letters = constants.VALID_LETTERS_TO_THIRD_DIGIT
        for invalid in self.get_inverted_letters(valid_letters):
            self.assertFalse(
                ukpcode._is_valid_outward_format_two("W1%s" % invalid)
            )

    def test_outward_third_format_valid(self):
        self.assertTrue(ukpcode._is_valid_outward_format_three("M1"))

    def test_outward_third_format_invalid(self):
        self.assertFalse(ukpcode._is_valid_outward_format_three("ME"))

    def test_outward_forth_format_valid(self):
        self.assertTrue(ukpcode._is_valid_outward_format_four("B33"))

    def test_outward_forth_format_invalid(self):
        self.assertFalse(ukpcode._is_valid_outward_format_four("BE3"))
        self.assertFalse(ukpcode._is_valid_outward_format_four("B3E"))

    def test_outward_fifth_format_valid(self):
        self.assertTrue(ukpcode._is_valid_outward_format_five("CR2"))

    def test_outward_fifth_format_invalid(self):
        self.assertFalse(ukpcode._is_valid_outward_format_five("CI2"))
        self.assertFalse(ukpcode._is_valid_outward_format_five("CRR"))

    def test_outward_sixth_format_valid(self):
        self.assertTrue(ukpcode._is_valid_outward_format_six("DN55"))

    def test_outward_sixth_format_invalid(self):
        self.assertFalse(ukpcode._is_valid_outward_format_six("DI55"))
        self.assertFalse(ukpcode._is_valid_outward_format_six("DNU5"))
        self.assertFalse(ukpcode._is_valid_outward_format_six("DN5U"))


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

    def test_outward_is_not_valid(self):
        self.assertFalse(ukpcode.is_valid("DI551BB"))


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
