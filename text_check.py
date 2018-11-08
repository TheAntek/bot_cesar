def check(text):
    from re import match, sub

    text = text.rstrip()  # убираем возможный пробел в конце строки
    last_str = text.split()[-1]  # получаем ключ. ex: '[-20]'

    try:
        key = int(sub('[\[\]]', '', last_str))
    except ValueError:
        return False

    if match('\[-?\d+\]', last_str) and -30 <= key <= 30:
        return key

    return False
