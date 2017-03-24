from ukpcode.constants import MAX_LENGTH, MIN_LENGTH


class MinLengthException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "'%s' has less than %s characters." % (self.value, MIN_LENGTH)


class MaxLengthException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "'%s' has more than %s characters." % (self.value, MAX_LENGTH)


class InvalidPostcodeException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "'%s' is not a ." % (self.value, MAX_LENGTH)