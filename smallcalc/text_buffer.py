


class EOFError(ValueError):
    """Signals that the buffer is reading after the end of the text."""


class EOLError(ValueError):
    """Signals that the buffer is reading after the end of a line."""


class TextBuffer:

    def __init__(self, text=None):
        self.lines = text.split('\n') if text else []
        self.line = 0
        self.column = 0

    @property
    def current_char(self):
        try:
            return self.current_line[self.column]
        except IndexError as error:
            raise EOLError

    @property
    def next_char(self):
        try:
            return self.current_line[self.column + 1]
        except IndexError as error:
            raise EOLError

    @property
    def current_line(self):
        try:
            return self.lines[self.line]
        except IndexError as error:
            raise EOFError

    @property
    def position(self):
        return (self.line, self.column)

    @property
    def tail(self):
        try:
            return self.current_line[self.column:]
        except IndexError as error:
            raise EOLError

    def newline(self):
        self.line += 1
        self.column = 0

    def goto(self, line, column=0):
        self.line = line
        self.column = column

    def skip(self, lines=1):
        self.column += lines
