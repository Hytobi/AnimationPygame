#PLOUVIN Patrice
#21/11/2017
#Module principal Dessin
#Pygame sur python 3.6




# Import de pygame.
import pygame

# Autre import :
import scenario
import nuages


def main():
    ''' Fonction principale.
    Arguments:
        None.
    Retour:
        None.
    '''
    #1 Initialise Pygame.
    pygame.init()

    #2 Ouvre la fenêtre de l'application.
    surface = pygame.display.set_mode((1000, 500))
    pygame.display.set_caption('Promenade en montagne')

    #3 Initialise l'horloge.
    horloge = pygame.time.Clock()
    
    #3.1 Initialisation
    scen = scenario.init()

    #4 Tant que le programme n’est pas terminé :
    terminer = False
    while not terminer :
        
        #a) Evénement pygame.quit.
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                terminer = True
                
        #b) Efface l'écran.
        surface.fill((0, 0, 0))

        #3.8 Mise a jour
        scenario.update(scen)

        #3.2 Dessin
        scenario.dessine(scen, surface)
        
        #c) Met à jour l'écran.
        pygame.display.update()
        
        #d) Ajuste la vitesse de la boucle (1 FPS).
        horloge.tick(5)

    #5 Termine Pygame.
    pygame.quit()

# Appel à la fonction principale.
if __name__ == '__main__':
    main()



