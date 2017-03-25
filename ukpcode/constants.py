MIN_LENGTH = 5
MAX_LENGTH = 7
INWARD_LENGTH = 3
SPACE_POSITION = -4
INWARD_PATTERN = r"^\d[ABD-HJLNP-UW-Z]{2}$"
INVALID_LETTERS_TO_INWARD = "CIKMOV"
INVALID_LETTERS_TO_FIRST_DIGIT = "QVX"
INVALID_LETTERS_TO_SECOND_DIGIT = "IJZ"
VALID_LETTERS_TO_THIRD_DIGIT = "ABCDEFGHJKPSTUW"
VALID_LETTERS_TO_FORTH_DIGIT = "ABEHMNPRVWXY"
OUTWARD_FIRST_DIGIT_PATTERN = r"[A-PR-UWYZ]"
OUTWARD_SECOND_DIGIT_PATTERN = r"[A-HK-Y]"
OUTWARD_PATTERN_FORMAT_ONE = r"^{first_digit}{second_digit}\d[{forth_digit}]".format(
    first_digit=OUTWARD_FIRST_DIGIT_PATTERN,
    second_digit=OUTWARD_SECOND_DIGIT_PATTERN,
    forth_digit=VALID_LETTERS_TO_FORTH_DIGIT,
)
OUTWARD_PATTERN_FORMAT_TWO = r"^{first_digit}\d[{third_digit}]".format(
    first_digit=OUTWARD_FIRST_DIGIT_PATTERN,
    third_digit=VALID_LETTERS_TO_THIRD_DIGIT,
)
