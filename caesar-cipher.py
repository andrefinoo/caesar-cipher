def encrypt(text: str, key: int) -> str:
    result = ""

    for char in text:
        if char.isalpha():
            if char.islower():
                base = 97
            else:
                base = 65

            pos = ord(char) - base
            new_pos = (pos + key) % 26
            result += chr(new_pos + base)
        else:
            result += char

    return result


def main():
    action = input("Vuoi cifrare o decifrare? ").strip().lower()
    text = input("Inserisci il testo: ")
    key = int(input("Inserisci la chiave: "))

    if action == "cifrare":
        result = encrypt(text, key)
    elif action == "decifrare":
        result = encrypt(text, -key)
    else:
        print("Scelta non valida")
        return

    print("Risultato:", result)


if __name__ == "__main__":
    main()