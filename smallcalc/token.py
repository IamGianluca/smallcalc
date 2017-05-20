class Token:

    def __init__(self, type_, value=None, position=None):
        self.type = type_
        self.value = value
        self.position = position

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if value is None:
            self._value = None
        else:
            self._value = str(value)

    def __len__(self):
        if self.value:
            return len(self.value)
        return 0

    def __bool__(self):
        return True

    def __eq__(self, other):
        if not isinstance(other, Token):
            return False
        return (self.type, self.value) == (other.type, other.value)

    def __str__(self):
        base = "Token({}, '{}'".format(self.type, self.value)
        if self.position:
            optional = ", line={}, col={}".format(self.position[0],
                                                  self.position[1])
            return base + optional + ')'
        return base + ')'

    __repr__ = __str__
