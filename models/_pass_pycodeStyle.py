def calc_sum(a, b):
    """Returns the sum of two numbers."""
    result = a + b
    return result


def main():
    """Main function that calls calc_sum function."""
    num1 = 20
    num2 = 30
    sum_result = calc_sum(num1, num2)
    print("The sum of", num1, "and", num2, "is", sum_result)


if __name__ == "__main__":
    main()

