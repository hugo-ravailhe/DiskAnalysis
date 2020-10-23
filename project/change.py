import os


def convert(x):
    output = ""
    if x >= 1000000000:
        x = x // 1000000000
        output += str(x) + " " + "Go"
    elif x >= 1000000:
        x = x // 1000000
        output += str(x) + " " + "Mo"
    elif x >= 1000:
        x = x // 1000
        output += str(x) + " " + "Ko"
    else:
        output += str(x) + " " + "o"
    return output


def compar(code, code_old):
    saveLenght = len(code_old)
    fileName = ""
    fileSize = ""
    numBool = False
    fileLvl = 0
    output = ""
    jSave = 0

    for i in range(0, len(code)):
        if code[i] == '*':
            numBool = True

        elif code[i] == '\t':
            fileLvl += 1
            fileName += '\t'

        elif code[i] == '\n':
            listRemoved = []
            saveName = ""
            saveSize = 0
            saveNumBool = False
            saveLvl = 0
            added = False
            changed = False
            same = False
            j = jSave

            while j < saveLenght and not added and not changed and not same:
                if code_old[j] == '*':
                    saveNumBool = True
                    saveSize = ""

                elif code_old[j] == '\t':
                    saveLvl += 1
                    saveName += '\t'
                    if saveLvl > fileLvl:
                        added = True

                elif code_old[j] == '\n':
                    if fileName == saveName:
                        if fileSize != saveSize:
                            changed = True
                        else:
                            same = True
                    else:
                        listRemoved.append((fileName, saveSize))
                    saveName = ""
                    saveNumBool = False
                    saveLvl = 0

                elif saveNumBool:
                    saveSize += code_old[j]

                else:
                    saveName += code_old[j]

                j += 1
            if not added:
                jSave = j

            # si le fichier a été ajouté depuis la dernière sauvegarde
            if added:
                output += fileName + " " + convert(int(fileSize)) + " ---(Added)---" + '\n'

            # si le fichier a changé de taille et les fichiers supprimés
            elif changed:

                # fichiers supprimés
                for k in range(0, len(listRemoved)):
                    name, size = listRemoved[k]
                    output += name + " " + convert(int(size)) + " ---(Removed)---" + '\n'

                # fichier changé
                changedSize = int(fileSize) - int(saveSize)
                output += fileName + " " + convert(int(saveSize)) + " ---(" + convert(changedSize) + ")--- " + convert(
                    int(fileSize)) + '\n'

            # si le fichier n'a pas changé et les fichiers supprimés
            elif same:
                # fichiers supprimés
                for k in range(0, len(listRemoved)):
                    name, size = listRemoved[k]
                    output += name + " " + convert(int(size)) + " ---(Removed)---" + '\n'

                # le fichier est resté pareil
                output += fileName + " " + convert(int(fileSize)) + " ---(Same)---" + '\n'

            fileName = ""
            fileSize = ""
            numBool = False
            fileLvl = 0

        elif numBool:
            fileSize += code[i]

        else:
            fileName += code[i]

    print(output)
