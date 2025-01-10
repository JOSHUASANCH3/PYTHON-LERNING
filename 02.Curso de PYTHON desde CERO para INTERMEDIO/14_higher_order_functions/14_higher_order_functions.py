### HIGH ORDER FUNCTIONS ###
def sum_one(value):
    return value + 1


def sum_five(value):
    return value + 5


def sum_two_values_and_add_one(first_value, second_value, f_sum):
    return f_sum(first_value + second_value)


print(sum_two_values_and_add_one(5, 2, sum_one))
print(sum_two_values_and_add_one(5, 2, sum_five))


###Closures###
def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value

    return add


add_closure = sum_ten(5)
print(add_closure(5))
