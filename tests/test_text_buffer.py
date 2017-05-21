import pytest

from smallcalc.text_buffer import EOFError, EOLError
from smallcalc.text_buffer import TextBuffer


def test_text_buffer_init_empty():
    tb = TextBuffer()

    with pytest.raises(EOFError):
        tb.current_char


def test_text_buffer_init_one_line():
    tb = TextBuffer('abcdef')

    assert tb.current_char == 'a'
    assert tb.next_char == 'b'
    assert tb.current_line == 'abcdef'
    assert tb.line == 0
    assert tb.column == 0


def test_text_buffer_end_of_line_next_char():
    tb = TextBuffer('abcdef')
    tb.column = 5

    assert tb.current_char == 'f'
    with pytest.raises(EOLError):
        tb.next_char


def test_text_buffer_end_of_line_current_char():
    tb = TextBuffer('abcdef')
    tb.column = 200

    with pytest.raises(EOLError):
        tb.current_char


def test_text_buffer_error_at_end_of_file():
    tb = TextBuffer('abcdef')
    tb.line = 1

    with pytest.raises(EOFError):
        tb.current_line


def test_text_buffer_error_after_end_of_file():
    tb = TextBuffer('abcdef')
    tb.line = 100

    with pytest.raises(EOFError):
        tb.current_line


def test_text_buffer_tail():
    ts = TextBuffer('abcdefgh')
    ts.column = 4

    assert ts.tail == 'efgh'


def test_text_buffer_multiple_lines():
    tb = TextBuffer('abc\ndef\nghi')
    tb.line = 1
    tb.column = 1

    assert tb.current_line == 'def'
    assert tb.current_char == 'e'
    assert tb.next_char == 'f'


def test_text_buffer_newline():
    tb = TextBuffer('abc\ndef\nghi')
    tb.line = 1
    tb.column = 2
    tb.newline()

    assert tb.position == (2, 0)


def test_text_buffer_position():
    tb = TextBuffer()
    tb.line = 123
    tb.column = 456

    assert tb.position == (123, 456)


def test_text_buffer_skip_defaults_to_one():
    tb = TextBuffer('abc\ndef\nghi')
    tb.skip()

    assert tb.column == 1


def test_text_buffer_skip_accepts_value():
    tb = TextBuffer('abc\ndef\nghi')
    tb.skip(3)

    assert tb.column == 3


def test_text_buffer_goto():
    tb = TextBuffer()
    tb.goto(12, 45)

    assert tb.position == (12, 45)


def test_text_buffer_goto_default_column():
    tb = TextBuffer()
    tb.goto(12)

    assert tb.position == (12, 0)
