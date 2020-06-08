def password_level(pas):
    if len(pas) < 6:
        message = "Недопустимый пароль"
    elif pas.isdigit() or pas.isalpha and (pas.islower() or pas.isupper()):
        message = "Ненадежный пароль"
    elif pas.isalpha() and not (pas.islower() or pas.isupper()) or pas.isalnum() and (pas.islower() or pas.isupper()):
        message = "Слабый пароль"
    else:
        message = "Надежный пароль"
    return message


password = input()
print(password_level(password))