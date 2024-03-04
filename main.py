# Importation du module pygame
import pygame

# Initialisation de pygame et ses fonctionalites
pygame.init()

# Dimensions de l'ecran
WIDTH = 800
HEIGTH = 600

# Cree la surface de l'ecran
gameScreen =  pygame.display.set_mode((WIDTH,HEIGTH))

# Titre de l'ecran
pygame.display.set_caption('Pygame HDI handling')

# font = pygame.font.Font('freesansbold.ttf', 32)
# # Les clicks
# droit = font.render('droit',True,)
# gauche = font.render('gauche')



running = True

while running:
    # Rempli le fond de l'ecran par la couleur blanche
    gameScreen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed()[0]:
                print(f"Vous avez fait un click gauche à la position (X: {x},Y: {y}).")
                # text = gauche
            elif pygame.mouse.get_pressed()[2]:
                print(f"Vous avez fait un click droit à la position (X: {x},Y: {y}).")
                # text = droit
        # # Cree un rectangle 
        # textRect = text.get_rect()
        # # Defini le centre du rectangle
        # textRect.center = (WIDTH // 2, HEIGTH // 2)

pygame.quit()