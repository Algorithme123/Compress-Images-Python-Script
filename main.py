import os
from PIL import Image

def reduire_taille_image(input_path, output_path, max_size, quality=95):
    try:
        # Ouvrir l'image
        image = Image.open(input_path)

        # Obtenir les dimensions actuelles de l'image
        largeur_actuelle, hauteur_actuelle = image.size

        # Calculer la nouvelle taille proportionnelle
        if largeur_actuelle > hauteur_actuelle:
            nouvelle_largeur = max_size
            nouvelle_hauteur = int((hauteur_actuelle / largeur_actuelle) * max_size)
        else:
            nouvelle_hauteur = max_size
            nouvelle_largeur = int((largeur_actuelle / hauteur_actuelle) * max_size)

        # Redimensionner l'image
        image_redimensionnee = image.resize((nouvelle_largeur, nouvelle_hauteur), Image.LANCZOS)

        # Enregistrer l'image redimensionnée avec compression
        image_redimensionnee.save(output_path, quality=quality)

        print(f"Image réduite et enregistrée sous {output_path}")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")

def reduire_taille_images_dossier(input_folder, output_folder, extension, max_size, quality=95):
    try:
        # Vérifier si le dossier de sortie existe, sinon le créer
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Parcourir tous les fichiers du dossier d'entrée avec l'extension spécifiée
        for file_name in os.listdir(input_folder):
            if file_name.lower().endswith(extension.lower()):
                # Chemin complet du fichier d'entrée
                input_path = os.path.join(input_folder, file_name)

                # Nouveau nom de fichier pour la sortie basé sur l'ancien nom
                output_name = f"{os.path.splitext(file_name)[0]}_compressed.{extension}"

                # Chemin complet du fichier de sortie
                output_path = os.path.join(output_folder, output_name)

                # Appeler la fonction de compression pour chaque fichier
                reduire_taille_image(input_path, output_path, max_size, quality)

        print("Compression des images terminée !")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")

# Exemple d'utilisation
input_folder = r"C:\Users\username\Downloads\photo"  # Chemin du dossier contenant les images
output_folder = r"C:\Users\username\Downloads\photo\Compress"  # Chemin du dossier de sortie
extension = "jpg"  # L'extension des fichiers à compresser (en minuscules)
max_size = 800     # Définissez la taille maximale souhaitée ici
quality = 80       # Définissez le niveau de qualité (entre 0 et 100, 100 étant la meilleure qualité)

reduire_taille_images_dossier(input_folder, output_folder, extension, max_size, quality)
