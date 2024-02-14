#!/usr/bin/python3
"""Print a text with two new line"""


def text_indentation(text):
    """print indented test

    Args:
        text (str): text content
    """

    if not isinstance(text, str):
        raise TypeError('text must be a string')
    new_text = ''
    penctuation = '.?:'

    for char in text:
        new_text += char
        for penc in penctuation:
            if penc == char:
                new_text += '\n\n'

    line = [(line.strip()) for line in (new_text.split('\n\n'))]
    final_text = '\n\n'.join(line)

    print(final_text, end="")
