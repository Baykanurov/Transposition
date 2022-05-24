# Функция дешифрования кода с помощью перестановки permutation
def decrypt(input_text, permutation):
    text = list(input_text)

    blockSize = len(permutation)
    codeSize = len(text)

    # Дешифрование
    for i in range(0, codeSize, blockSize):
        string = [text[i + j] for j in range(blockSize)]
        for j in range(blockSize):
            text[i + j] = string[permutation[j]]

    return "".join(text)