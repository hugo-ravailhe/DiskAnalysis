# -*-coding:Latin-1 -*
import os
import time
from size import *
from change import compar


def main():
    running = True
    while running:
        # demander sur quel os est l'utilisateur
        print("w pour Windows")
        print("l pour Linux")
        ospc = input()

        # v�rification de l'input pour le type d'OS
        if ospc != "w" and ospc != "W" and ospc != "l" and ospc != "L":
            print("Voulez-vous reessayer ? o/n", end=" ")
            again = input()
            if again != "o" and again != "O":
                running = False
        else:
            if ospc == "w" or ospc == "W":
                slash = chr(92)
            elif ospc == "l" or ospc == "L":
                slash = "/"

            # demander s'il faut faire des sauvegardes
            print("Souhaitez-vous faire une sauvegarde du r�sultat afin de pourvoir comparer ce r�sultat plus tard ? "
                  "o/n"
                  , end=" ")
            saveIn= input()
            if saveIn != 'o' and saveIn != 'O' and saveIn != 'n' and saveIn != 'N':
                print("Voulez-vous reessayer ? o/n", end=" ")
                again = input()
                if again != "o" and again != "O":
                    running = False
            else:
                if saveIn == 'o' or saveIn == 'O':
                    save = True
                else:
                    save = False

                # demander le chemin du repertoire
                print("Choisissez le repertoire")
                path = input()

                # v�rification du chemin
                if not os.path.exists(path):
                    raise Exception("Repertoire inexistant")

                # demander s'il veut les fils
                print("Voulez-vous voir les fils ? o/n")
                graphInput = input()

                # v�rification de l'input pour voir les fils
                allfiles = True
                if graphInput == "o" or graphInput == "O":
                    print("Combien de sous-niveaux voulez-vous voir ? (0 pour tous)")
                    want = input()
                    print("Voulez-vous voir uniquement les r�pertoires ? o/n")
                    files = input()

                    # v�rification des inputs pour voir les nombres de niveaux et les repertoires
                    if files == "o" or files == "O":
                        allfiles = False
                    if want == "0":
                        x, y = run(path, True, 0, slash, 0, allfiles, '\t')
                    else:
                        x, y = run(path, False, 0, slash, int(want), allfiles, '\t')
                else:
                    print("Voulez-vous voir uniquement les r�pertoires ? o/n")
                    files = input()

                    # v�rification des inputs pour voir les nombres de niveaux et les repertoires
                    if files == "o" or files == "O":
                        allfiles = False
                        
                    x, y = run(path, False, 0, slash, 0, allfiles, '\t')
                code = path + "*" + str(y) + "\n" + x

                # partie sur les sauvegardes
                if save:

                    # cr�ation d'un dossier diskanalysis s'iln'existe pas
                    if not os.path.exists(path + slash + "diskanalysis"):
                        os.mkdir(path + slash + "diskanalysis")

                    os.chdir(path + slash + "diskanalysis")
                    filesave = os.listdir(path + slash + "diskanalysis")
                    length = len(filesave)

                    # cr�ation et ouverture de la sauvegarde
                    filename = time.time()
                    fichier = open(str(filename), 'x')
                    fichier.write(code)
                    fichier.close()
                    if length > 0:

                        # demander si on doit comparer les r�sultats
                        print("Voulez-vous comparer ce r�sultat avec d'ancien r�sultat ? o/n", end=" ")
                        compare = input()
                        if compare != 'o' and compare != 'O' and compare != 'n' and compare != 'N':
                            print("Voulez-vous reessayer ? o/n", end=" ")
                            again = input()
                            if again != "o" and again != "O":
                                running = False
                        else:
                            if compare == 'o' or compare == 'O':
                                fileoled = open(filesave[length - 1], 'r')
                                codeold = fileoled.read()
                                compar(code, codeold)

                            else:
                                print(decode(code))
                    else:
                        print(decode(code))

                else:
                    print(decode(code))

                print("Voulez-vous reessayer ? o/n", end=" ")
                again = input()

                # v�rification de l'arr�t du programme
                if again != "o" and again != "O":
                    running = False


main()
