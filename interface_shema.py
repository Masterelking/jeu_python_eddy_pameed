import pygame

# Initialisation de Pygame et de la fenêtre de jeu
pygame.init()
fenetre = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Schéma du Circuit")

# Couleurs
noir = (0, 0, 0)
blanc = (255, 255, 255)

def dessiner_circuit(surface, couleur):
    largeur_horizontale = 600
    hauteur_verticale = 200
    x_initial = 100
    y_initial = 300
    epaisseur = 10

    pygame.draw.line(surface, couleur, (x_initial, y_initial), (x_initial + largeur_horizontale, y_initial), epaisseur)
    pygame.draw.line(surface, couleur, (x_initial, y_initial - hauteur_verticale), (x_initial, y_initial + hauteur_verticale), epaisseur)
    pygame.draw.line(surface, couleur, (x_initial + largeur_horizontale, y_initial - hauteur_verticale), (x_initial + largeur_horizontale, y_initial + hauteur_verticale), epaisseur)
    x_1_3 = x_initial + largeur_horizontale // 3
    pygame.draw.line(surface, couleur, (x_1_3, y_initial), (x_1_3, y_initial + hauteur_verticale), epaisseur)
    x_2_3 = x_initial + 2 * (largeur_horizontale // 3)
    pygame.draw.line(surface, couleur, (x_2_3, y_initial), (x_2_3, y_initial - hauteur_verticale), epaisseur)

# Boucle principale
horloge = pygame.time.Clock()
en_cours = True
while en_cours:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False

    fenetre.fill(blanc)  # Effacer l'écran

    # Dessiner le circuit
    dessiner_circuit(fenetre, noir)

    pygame.display.flip()  # Mettre à jour l'écran
    horloge.tick(30)

pygame.quit()
