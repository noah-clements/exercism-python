import re
import operator

OPERATORS = {
    'plus': operator.add,
    'minus': operator.sub,
    'multiplied by': operator.mul,
    'divided by': operator.floordiv
}

# stolen from GlennJ - https://exercism.org/tracks/python/exercises/wordy/solutions/glennj
REGEX = {
    'num': re.compile(r'([-0-9]+)'),
    'op': re.compile(r'(plus|minus|multiplied by|divided by)')
}

def get_num(string):
    match = REGEX['num'].match(string)
    if not match:
        raise ValueError('syntax error')
    return int(match.group()), string[match.end():].strip()

def get_op(string):
    match = REGEX['op'].match(string)
    if not match:
        raise ValueError('unknown operation')
    return OPERATORS[match.group()], string[match.end():].strip()

def answer(question):
    if not question.startswith('What is') or not question.endswith('?'):
        raise ValueError('unknown operation')
    math = question.replace('What is', '').replace('?', '').lstrip()
    answer, math = get_num(math)
    while len(math) > 0:
        # two numbers in a row
        if REGEX['num'].match(math):
            raise ValueError('syntax error')

        op, math = get_op(math)
        num, math = get_num(math)
        answer = op(answer, num)
    return answer