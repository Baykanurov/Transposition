# Функция шифрования текстом с помощью перестановки permutation
def encrypt(input_text, permutation):
    text = list(input_text)

    blockSize = len(permutation)
    textSize = len(text)

    # Выравнивание текста
    difference = (textSize) % blockSize
    if difference != 0:
        # добить нужным количеством символов
        for i in range(blockSize - difference):
            text.append(".")

        # взять новый размер строки
        textSize = len(text)

    # Шифрование
    for i in range(0, textSize, blockSize):
        string = [text[i + j] for j in range(blockSize)]
        for j in range(blockSize):
            text[i + j] = string[permutation[j]]

    return "".join(text)



