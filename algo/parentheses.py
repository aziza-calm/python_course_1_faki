def is_valid(s):
    """
    Функция, проверяющая правильность скобочной последовательности. Алгоритм с испльзованием стека.
    :param s: str - скобочная последовательность. Например, "(){}[]"
    :return: bool
    """
    stack = []
    mapping = {")": "(", "]": "[", "}": "{"}
    for char in s:
        if char == "(":
            stack.append(char)
        else:
            top_element = stack.pop() if stack else "!"

    return not stack


def is_valid_str(s):
    """
    Функция, проверяющая правильность скобочной последовательности.
    Алгоритм с использованием строковых методов.
    :param s: str - скобочная последовательность. Например, "(){}[]"
    :return: bool
    """
    while "()" in s or "{}" in s or "[]" in s:
        s = s.replace("{}", "").replace("()", "").replace("[]", "")
    return s == ""


if __name__ == "__main__":
    print(is_valid_str("(]"))
    print(is_valid_str("(]]]]]"))
    print(is_valid_str("{(}"))
    print(is_valid_str("[[]]"))
