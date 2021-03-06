#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:
    if values is None:
        # TODO: demander les valeurs ici
        values = []
        while len(values) < 10:
            values.append(input("Entre une valeur enfoiré: "))
        sorted_values = sorted(values)
        print(sorted_values)


    return sorted(values)


def anagrams(words: list = None) -> bool:
    if words is None:
        # TODO: demander les mots ici
        words = []
        mot_1 = []
        mot_2 = []
        chaine_1 = str(input("entre le premier mot: "))
        chaine_min_1 = chaine_1.upper()
        chaine_2 = str(input("entre le deuxieme mot: "))
        chaine_min_2 = chaine_2.upper()

        for i in range(len(chaine_min_1)):
            mot_1.append(chaine_min_1[i])

        for i in range(len(chaine_min_2)):
            mot_2.append(chaine_min_2[i])

        if sorted(mot_1) == sorted(mot_2):
            print("C'est un anagrame")
        else:
            print("Ce n'est pas un anagrame")

    return print("meh")


def contains_doubles(items: list) -> bool:

    return len(set(items)) != len(items)


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    best_student = {}
    for key, value in student_grades.items():
        avg = sum(value) / len(value)
        if len(best_student) == 0 or list(best_student.values())[0] < avg:
            best_student = {key: avg}


    return best_student


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres
    dictionnaire = {}
    nbr_lettre = 0
    sorted_sentence = sorted(sentence)

    for lettre in range(len(sorted_sentence)):
        dictionnaire[sorted_sentence[lettre]] = nbr_lettre + 1



    return print(sorted_sentence)


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    pass


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    pass


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
