# ユーザーに数値を2つ入力させ、それを割り算して結果を表示する。
from logic.input_numbers import InputNumbers


def division_number(input_numbers):
    try:
        num_a, num_b = input_numbers.input_numbers()
        result = num_a / num_b
    except ZeroDivisionError:
        print("0で割ることはできません")
        return None
    return result


def print_result(result):
    if result is not None:
        print(f"割り算の結果: {result:.1f}")


if __name__ == "__main__":
    input_numbers = InputNumbers()
    result = division_number(input_numbers)
    print_result(result)
