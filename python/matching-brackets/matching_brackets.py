def is_paired(input_string):
    opening_brackets = ('(', '{', '[')
    closing_brackets = (')', '}', ']')
    stack = []
    for char in input_string:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack:
                return False
            last_opening_bracket = stack.pop()
            if opening_brackets.index(last_opening_bracket) != closing_brackets.index(char):
                return False
    return not stack