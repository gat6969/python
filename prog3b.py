def is_armstrong_no(x):
    original_no = x
    sum_of_cubes = 0

    while x > 0:
        digit = x % 10
        sum_of_cubes += digit ** 3
        x = x // 10
    return sum_of_cubes == original_no


num = int(input("Enter a number: "))
if is_armstrong_no(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
