from ukpcode.constants import MAX_LENGTH, MIN_LENGTH


class InvalidPostcodeException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "'%s' is not a valid post code." % (self.value)


class MinLengthException(InvalidPostcodeException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "'%s' has less than %s characters." % (self.value, MIN_LENGTH)


class MaxLengthException(InvalidPostcodeException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "'%s' has more than %s characters." % (self.value, MAX_LENGTH)


class InvalidInwardException(InvalidPostcodeException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "'%s' is not a valid inward." % self.value


class InvalidOutwardException(InvalidPostcodeException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "'%s' is not a valid outward." % self.value
