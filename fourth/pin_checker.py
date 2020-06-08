def check_pin(pin):
    nums = list(map(int, pin.split("-")))
    if is_prime_num(nums[0]) and is_palindrome_num(nums[1]) and is_a_power_of_two(nums[2]):
        message = "Корректен"
    else:
        message = "Некорректен"
    return message


def is_prime_num(num):
    tmp = 2
    while num % tmp != 0:
        tmp += 1
    if tmp == num:
        return True
    else:
        return False


def is_palindrome_num(num):
    if str(num) == str(num)[::-1]:
        return True
    else:
        return False


def is_a_power_of_two(num):
    checker = True
    while num != 1:
        if num % 2:
            checker = False
            break
        num /= 2
    return checker


pin_code = input()
print(check_pin(pin_code))
