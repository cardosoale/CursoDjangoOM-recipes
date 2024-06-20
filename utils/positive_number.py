def is_positive_number(value):
    try:
        number_string = int(value)
    except ValueError:
        return False

    return number_string > 0


print(is_positive_number(-5))
