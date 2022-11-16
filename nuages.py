#PLOUVIN Patrice
#21/11/2017
#Module nuages


#Import pygame
import pygame
#Autre import
from random import randint
from couleur import BLANC



#4.1 Initialisation
def init(nombre):
    '''Fonction qui liste les attributs des nuages
       Argument : int
       Retour : dict'''
    #Dictionnaire
    att={}
    #La vitesse de déplacement d’un nuage (constante)
    att['vit'] = 5
    #Les coordonnées (x, y) limites pour un nuage à l’écran
    att['lim'] = [1000,100]
    #Une liste contenant nombre tuples de deux entiers (x, y)
    att['objs'] = []
    for i in range(nombre):
        x = int(randint(0, 975))
        y = int(randint(0, 100))
        att['objs'].append([x, y])
    return att
        

#4.2 Dessin
def dessine(att, surface):
    '''Fonction qui dessine les nuages
       Argument : dict
                  surface
       Retour : None'''
    for i in range(len(att['objs'])):
        pygame.draw.ellipse(surface, BLANC, [att['objs'][i][0], att['objs'][i][1], 100, 50])
        pygame.draw.ellipse(surface, BLANC, [(att['objs'][i][0])+25, (att['objs'][i][1])-25, 50, 100])


#4.3 Mise à jour
def update(att):
    '''Fonction qui fait bouger les nuages
       Argument : dict
       Retour : None'''
    for i in range(len(att['objs'])):
        att['objs'][i][0] += att['vit']
        if att['objs'][i][0] > att['lim'][0]:
            att['objs'][i][0] = 0
            att['objs'][i][1] = randint(0, 100)
            
    





        
        
