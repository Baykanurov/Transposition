from pathlib import Path


# определяет, является ли символ спецсимволом
def checkSymb(symb):
    badSymbols = ['”', '“', '*', ')', '(', '\t', '¶', '–', ',', '.', ':', ';', '`', '-', '!', '&', '?', '_', '0', '1',
                  '2', '3', '4', '5', '6', '7', '8', '9']
    for s in badSymbols:
        if symb == s:
            return True
    else:
        return False


def processFile(fileName):
    file = open(fileName, 'r', encoding="utf-8")

    text = []
    for line in file:
        text.append(list(line.lower()))

    file.close()

    # Убрать все спец символы, кроме пробелов и перевода строки, и цифры
    for i in range(len(text)):
        for j in range(len(text[i]) - 1):
            if checkSymb(text[i][j]):
                text[i][j] = ''

    newFileName = fileName.replace(".txt", "") + 'New' + ".txt"
    file = open(newFileName, 'w', encoding="utf-8")

    for line in text:
        file.write(''.join(line))

    file.close()

    return newFileName


def findAllBigrammsInFile(fileName):
    file = open(fileName, 'r', encoding="utf-8")

    text = []
    for line in file:
        text.append(list(line))

    file.close()

    allBigrammsInText = []
    for i in range(len(text)):
        for j in range(1, len(text[i]) - 1):
            allBigrammsInText.append(text[i][j - 1] + text[i][j])

    return allBigrammsInText


def getAllBigramms():
    allBigramms = []
    for num in range(ord('а'), ord('я') + 1, 1):
        for secondNum in range(ord('а'), ord('я') + 1, 1):
            allBigramms.append(chr(num) + chr(secondNum))

    for num in range(ord('а'), ord('я') + 1, 1):
        allBigramms.append(chr(num) + ' ')
        allBigramms.append(' ' + chr(num))

    return allBigramms


def bad_bigrams(path):
    file = path
    newFileName = processFile(file)
    allBigrammsInText = findAllBigrammsInFile(newFileName)
    allBigramms = getAllBigramms()

    indexesOfGoodBigramms = []
    for i in range(len(allBigramms)):
        for j in range(len(allBigrammsInText)):
            if allBigramms[i] == allBigrammsInText[j]:
                indexesOfGoodBigramms.append(i)
                break

    badBigramms = []
    for i in range(len(allBigramms)):
        flag = True
        for j in range(len(indexesOfGoodBigramms)):
            if i == indexesOfGoodBigramms[j]:
                flag = False
                break
        if flag:
            badBigramms.append(allBigramms[i])

    file = open('badBigramms', 'w', encoding="utf-8")
    file.write(str(badBigramms))
    file.close()
    return badBigramms


badBigramms = bad_bigrams(str(Path(Path.cwd(), 'badbigrame', 'godFather.txt')))
