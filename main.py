from PIL import Image


def reduire_taille_image(input_path, output_path, max_size):
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

        # Enregistrer l'image redimensionnée
        image_redimensionnee.save(output_path)

        print("Image réduite avec succès !")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")


# Exemple d'utilisation
input_path = r"C:\Users\username\Downloads\photo\DSC02.JPG"
output_path = r"C:\Users\username\Downloads\photo\Compress\DSC_compressed.JPG"
max_size = 800  # Définissez la taille maximale souhaitée ici

reduire_taille_image(input_path, output_path, max_size)
