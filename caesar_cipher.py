def encrypt(text: str, key: int) -> str:
    result = ""

    for char in text:
        if "a" <= char <= "z":
            pos = ord(char) - 97
            new_pos = (pos + key) % 26
            result += chr(new_pos + 97)

        elif "A" <= char <= "Z":
            pos = ord(char) - 65
            new_pos = (pos + key) % 26
            result += chr(new_pos + 65)

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