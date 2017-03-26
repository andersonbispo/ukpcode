import re
from ukpcode import constants
from ukpcode import exceptions


def is_valid(code):
    try:
        _validate(code)
        return True
    except exceptions.InvalidPostcodeException:
        return False


def format(code):
    pcode = code.strip()
    _validate(pcode)

    outward = _get_outward(pcode)
    inward = _get_inward(pcode)

    return " ".join([outward, inward])


def _validate_length(code):
    not_formated = code.replace(" ", "")
    if len(not_formated) < constants.MIN_LENGTH:
        raise exceptions.MinLengthException(code)

    if len(not_formated) > constants.MAX_LENGTH:
        raise exceptions.MaxLengthException(code)

    return True


def _validate_inward(code):
    inward = _get_inward(code)
    if not re.search(constants.INWARD_PATTERN, inward):
        raise exceptions.InvalidInwardException(inward)

    return True


def _is_valid_outward_format_one(outward):
    if not re.search(constants.OUTWARD_PATTERN_FORMAT_ONE, outward):
        return False

    return True


def _is_valid_outward_format_two(outward):
    if not re.search(constants.OUTWARD_PATTERN_FORMAT_TWO, outward):
        return False

    return True


def _is_valid_outward_format_three(outward):
    if not re.search(constants.OUTWARD_PATTERN_FORMAT_THREE, outward):
        return False

    return True


def _is_valid_outward_format_four(outward):
    if not re.search(constants.OUTWARD_PATTERN_FORMAT_FOUR, outward):
        return False

    return True


def _is_valid_outward_format_five(outward):
    if not re.search(constants.OUTWARD_PATTERN_FORMAT_FIVE, outward):
        return False

    return True

def _is_valid_outward_format_six(outward):
    if not re.search(constants.OUTWARD_PATTERN_FORMAT_SIX, outward):
        return False

    return True


def _validate_outward(code):
    outward = _get_outward(code)

    if not _is_valid_outward_format_one(outward) and \
       not _is_valid_outward_format_two(outward) and \
       not _is_valid_outward_format_three(outward) and \
       not _is_valid_outward_format_four(outward) and \
       not _is_valid_outward_format_five(outward) and \
       not _is_valid_outward_format_six(outward):
            raise exceptions.InvalidInwardException(outward)
    return True


def _validate(code):
    _validate_length(code)
    _validate_inward(code)
    _validate_outward(code)
    return True


def _get_inward(code):
    inward = code[-constants.INWARD_LENGTH:]
    inward = inward.upper()
    return inward


def _get_outward(code):
    outward = code[:-constants.INWARD_LENGTH]
    outward = outward.strip().upper()
    return outward
