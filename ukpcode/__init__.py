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
    if not re.search(constants.INwWARD_PATTERN, inward):
        raise exceptions.InvalidInwardException(code)

    return True


def _validate_outward(code):
    outward = _get_outward(code)
    if not re.search(constants.OUTWARD_PATTERN, outward):
        raise exceptions.InvalidOutwardException(code)

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
