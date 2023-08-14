import pickle
import time

def enregistrer_mot_de_passe(mot_de_passe):
    with open("mot_de_passe.pkl", "wb") as fichier:
        pickle.dump(mot_de_passe, fichier)

def charger_mot_de_passe():
    try:
        with open("mot_de_passe.pkl", "rb") as fichier:
            return pickle.load(fichier)
    except FileNotFoundError:
        return None

def demander_mot_de_passe():
    return input("Entrez votre mot de passe : ")

def main():
    mot_de_passe_enregistre = charger_mot_de_passe()

    while True:
        if mot_de_passe_enregistre:
            mot_de_passe_entre = demander_mot_de_passe()
            if mot_de_passe_entre == mot_de_passe_enregistre:
                print("Connexion réussie !")
                break
            else:
                print("Mot de passe incorrect. Réessayez.")
                time.sleep(1)  # Ajout d'une pause d'une seconde pour une réponse plus rapide
        else:
            nouveau_mot_de_passe = input("Créez un nouveau mot de passe : ")
            enregistrer_mot_de_passe(nouveau_mot_de_passe)
            print("Mot de passe enregistré.")
            break

    # Pause pour empêcher la fermeture immédiate de la fenêtre
    time.sleep(5)  # Attendre 5 secondes (ajuste selon tes besoins)

if __name__ == "__main__":
    main()
