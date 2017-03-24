from ukpcode.constants import MAX_LENGTH, MIN_LENGTH
from ukpcode.exceptions import MinLengthException, MaxLengthException, InvalidPostcodeException


def format(code):
    not_formated = code.replace(" ", "")
    if len(not_formated) < MIN_LENGTH:
        raise MinLengthException(code)

    if len(not_formated) > MAX_LENGTH:
        raise MaxLengthException(code)

    if code[-4] == " ":
        return code

    outward = code[:-3]
    inward = code[-3:]
    return "{outward} {inward}".format(outward=outward, inward=inward)