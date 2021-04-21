def is_valid(s):
    """
    Функция, проверяющая правильность скобочной последовательности
    :param s: str - скобочная последовательность. Например, "(){}[]"
    :return: bool
    """
    stack = []
    for char in s:
        if char == "(":
            stack.append(char)
        else:
            top_element = stack.pop() if stack else "!"

    return not stack


if __name__ == "__main__":
    print(is_valid("((((((()))"))
