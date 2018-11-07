def translate(text, key):
    from bot_cesar.const import alphabet
    result = ''

    for symbol in text:
        symbol_index = alphabet.find(symbol)
        if symbol_index == -1:
            result += symbol
        else:
            symbol_index += key
            if symbol_index >= len(alphabet):
                symbol_index -= len(alphabet)
            elif symbol_index < 0:
                symbol_index += len(alphabet)

            result += alphabet[symbol_index]
    return result


if __name__ == '__main__':
    print(translate(input(), int(input())))