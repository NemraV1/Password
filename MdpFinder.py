import os
import time
import pyautogui

def saisir_noms_fruits(noms_fruits, chemin_executable):
    # Ouvrir l'exécutable
    os.startfile(chemin_executable)
    time.sleep(2)  # Attendre 2 secondes pour que l'exécutable se charge

    # Saisir les noms de fruits instantanément
    for fruit in noms_fruits:
        pyautogui.typewrite(fruit, interval=0)  # Saisir le nom de fruit instantanément
        pyautogui.press("enter")  # Appuyer sur la touche "Entrée" pour valider la saisie
        time.sleep(0.5)  # Attendre 0.5 seconde avant de saisir le prochain nom de fruit

    # Fermer l'exécutable
    os.system("taskkill /f /im main.exe")  # Fermer l'exécutable en utilisant la commande taskkill

if __name__ == "__main__":
    noms_fruits = ["pomme", "banane", "orange", "fraise", "kiwi"]  # Liste des noms de fruits
    chemin_executable = r"D:\Users\armen\PycharmProjects\NombreMagique\dist\main.exe"

    saisir_noms_fruits(noms_fruits, chemin_executable)
