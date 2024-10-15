import re
from extract_features import extract_features
file_name = "rockyou.txt"

def clean_data(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        passwords = file.readlines()

    original_count = len(passwords)#Compte le nombre original de mots de passe
    passwords = [pwd.strip() for pwd in passwords]  # Enlève les espaces
    spaces_removed = sum(len(pwd) - len(pwd.strip()) for pwd in passwords)  # Compte les espaces superflus
    passwords = list(set(passwords))  #Supprime les doublons
    duplicates_removed = original_count - len(passwords)  # Compte le nombre de doublons enlevés

    #Affiche-les-informations
    print(f"Nombre de mots de passe originaux : {original_count}")
    print(f"Nombre de doublons enlevés : {duplicates_removed}")
    print(f"Nombre d'espaces superflus enlevés : {spaces_removed}")
    #Nettoyage-et-normalisation des mots de passe
    passwords = [pwd.strip() for pwd in passwords]  #Enlève-les-espaces-superflus
    passwords = list(set(passwords))  #Supprime-les-doublons

    return passwords
  #Comptage_des_espaces_superflus
    original_length = len(passwords)
    passwords = [pwd.strip() for pwd in passwords]
    spaces_removed = sum(len(pwd) - len(pwd.strip()) for pwd in passwords)

    #Suppression_des_doublons
    unique_passwords = list(set(passwords))
    duplicates_count = original_length - len(unique_passwords)

    return unique_passwords, duplicates_count, spaces_removed

def categorize_passwords(passwords):
    weak = []
    medium = []
    strong = []

    for password in passwords:
        #Vérifie_si_le_mot_de_passe_est_faible
        if len(password) < 6 :
            weak.append(password)
        #Vérifie_si_le_mot_de_passe_est_moyen
        elif (6 <= len(password) <= 10 and
              re.search("[0-9]", password) and
              re.search("[a-z]", password)):
            medium.append(password)
        #Vérifie si le mot de passe est fort
        elif (len(password) > 10 and
              re.search("[0-9]", password) and
              re.search("[a-z]", password) and
              re.search("[A-Z]", password) and
              re.search("[^a-zA-Z0-9]", password)):
            strong.append(password)
        else:
            medium.append(password)  # Par défaut dans la catégorie moyenne

    return weak, medium, strong



def save_categories(weak, medium, strong):
    with open('weak_passwords.txt', 'w', encoding='utf-8') as weak_file:
        weak_file.write("\n".join(weak))

    with open('medium_passwords.txt', 'w', encoding='utf-8') as medium_file:
        medium_file.write("\n".join(medium))

    with open('strong_passwords.txt', 'w', encoding='utf-8') as strong_file:
        strong_file.write("\n".join(strong))


def main():
    file_name = 'rockyou.txt'
    passwords = clean_data(file_name)
    #print(f"Nombre de mots de passe après nettoyage : {len(passwords)}")

    weak, medium, strong = categorize_passwords(passwords)

    #print(f"Mots de passe faibles : {len(weak)}")
    #print(f"Mots de passe moyens : {len(medium)}")
    #print(f"Mots de passe forts : {len(strong)}")

    save_categories(weak, medium, strong)
    #print("Les mots de passe ont été classés et enregistrés dans des fichiers séparés.")


password = "Passw0rd!123"
features = extract_features(password)
print(features)
if __name__ == "__main__":
    main()
