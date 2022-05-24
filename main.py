from transposition_encrypt import encrypt
from transposition_decrypt import decrypt
from transposition_hack import hack
from input_text import all_text
from profilehooks import profile


@profile
def main():
    with open("result.txt", 'w', encoding="utf-8") as f:
        text_encrypt = encrypt(all_text, [3, 1, 2, 0])

        print(f"Зашифрованный текст:\n{text_encrypt}\n\n\n\n", file=f)

        print(f"Расшифрованный текст:\n{decrypt(text_encrypt, [3, 1, 2, 0])}\n\n\n\n", file=f)

        print("Взлом:\n", file=f)
        print(hack(text_encrypt), file=f)


if __name__ == '__main__':
    main()
