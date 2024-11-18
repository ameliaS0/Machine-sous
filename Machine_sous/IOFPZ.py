import pygame, sys # recupére les composant
import numpy
pygame.init()

# creer une classe qui va gérer la notion d'emplacement    
class Emplacement(pygame.sprite.Sprite):

    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load('P1/pomme_dore.png')
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

    def set_image(self,image):
        self.image = image
 
# definir une fonctions lancement
def lancement():

    global jetons

    # choix au hasard selon les probabilités
    hasard = numpy.random.choice(fruits, 3, p=proba_fruits)
    fruit_gauche = fruits_dict[hasard[0]]
    fruit_milieu = fruits_dict[hasard[1]]
    fruit_droite = fruits_dict[hasard[2]]

    # changement des images 
    emplacement_gauche.set_image(fruit_gauche)
    emplacement_milieu.set_image(fruit_milieu)
    emplacement_droite.set_image(fruit_droite)

    

   
    #afficher le tirage
    print(hasard)

    #faire la verification des lots
    if hasard[0] == hasard[1] == hasard [2]: #les 3 premiers fruits sont identique
        fruit =  hasard[0]
        jetons_gagnes = fruits_dict_gains[fruit]
        jetons += jetons_gagnes
        print(f"Une ligne de {fruit} a été completé ! + {jetons_gagnes} Jetons ")




# Création de la fenetre
largeur = 800
hauteur = 460
ecran = pygame.display.set_mode([800,460]) # Dimension de l'affichage de l'écrant
pygame.display.set_caption('Machine à sous')
white = [255, 255, 255]  #Couleur du fond (variable = white)
ecran.fill(white) #permet de remplir la surface de la variable = white

# argent du joueur
jetons = 1000


# Dictionnaire de fruits
fruits_dict = {
    "pomme_dore": pygame.image.load('P1/pomme_dore.png'),
    "7": pygame.image.load('P1/7.png'),
    "pasteque": pygame.image.load('P1/pasteque.png'),
    "cerise": pygame.image.load('P1/cerises.png'),
    "orange": pygame.image.load('P1/orange.png')

}

# Liste stokant le nom de chaque fruit

fruits = ["7", "cerise", "orange", "pasteque", "pomme_dore"]
proba_fruits = [0.2, 0.25, 0.4, 0.1, 0.05]

fruits_dict_gains = {
    'orange': 5,
    'cerise': 15,
    '7': 50,
    'pasteque': 150,
    'pomme_dore': 10000

}

# chargement des emplacements
hauteur_emplacement = hauteur / 3 + 30
emplacement_x_milieu = largeur / 2 - 27
emplacement_x_gauche = emplacement_x_milieu -150
emplacement_x_droite = emplacement_x_milieu + 150

emplacements = pygame.sprite.Group()
emplacement_gauche = Emplacement(emplacement_x_gauche, hauteur_emplacement)
emplacement_milieu = Emplacement(emplacement_x_milieu, hauteur_emplacement)
emplacement_droite = Emplacement(emplacement_x_droite, hauteur_emplacement)

# rangement des emplacements dans le groupe
emplacements.add(emplacement_gauche)
emplacements.add(emplacement_milieu)
emplacements.add(emplacement_droite)

# charger l'image de l'arriere plan
fond = pygame.image.load('P1/slot.png')
police = pygame.font.SysFont("comicsansms", 30)

# Boucle pour maintenir la fenetre pygame en eveil 
running =  True # par défauts la fêtre dois reste allumé 

while running:

    ecran. fill(white) #permet de le recharger 
    ecran.blit(fond,(100,0))
    emplacements.draw(ecran)
    
    #  afficher son nombre de jetons
    texte = police.render(str(jetons) + "jeton", True, (0,0,0))
    ecran.blit(texte, (10, 0))
    
    pygame.display.flip() #met à jours l'écrant

    for event in pygame.event.get():
        # verifier si le joueur ferme la fenetre
        if event.type == pygame.QUIT: 
            running = False  #Si le joueur à fermer l'application 
            quit()
        # verifier si le joueur appuie sur une touche
        if event.type == pygame.KEYDOWN:
            #    si la touche est la touche ESPACE
            if event.key == pygame.K_SPACE and jetons >= 10:
                lancement() #apelle la fonction
                jetons -= 10


