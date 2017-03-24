from ukpcode import constants
from ukpcode.exceptions import MinLengthException, MaxLengthException, InvalidPostcodeException


def _validate_length(code):
    not_formated = code.replace(" ", "")
    if len(not_formated) < constants.MIN_LENGTH:
        raise MinLengthException(code)

    if len(not_formated) > constants.MAX_LENGTH:
        raise MaxLengthException(code)


def _get_inward(code):
    return code[-constants.INWARD_LENGTH:]


def _get_outward(code):
    return code[:-constants.INWARD_LENGTH]

def _is_already_formatted(code):
    return code[constants.SPACE_POSITION] == " "


def format(code):
    _validate_length(code)

    if _is_already_formatted(code):
        return code

    outward = _get_outward(code)
    inward = _get_inward(code)
    return " ".join([outward, inward])