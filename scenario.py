#PLOUVIN Patrice
#21/11/2017
#Fonctions qu’initialise, met à jour et dessine le scénario dans ce module

#Import du pygame
import pygame

#Autre import
from couleur import NOIR, BLANC, BLEU_CIEL, VERT, VERT_FONCE, BEIGE, MARRON, ARDOISE, ROUGE_FEU, ORANGE, JAUNE_OR, JAUNE_CIT
import nuages
import perso

#3.1 Initialisation
def init():
    ''' La fonction initialise le dictionnaire des attributs du scénario
        Argument : None
        Retour : dict'''
    att = {}
    att['nuages'] = nuages.init(4)
    att['perso'] = perso.init(20, 440)
    return att


#3.2 Dessin
def dessine(att, surface):
    '''Fonction qui dessine le dessin
       Argument : att --- dict
                  surface
       Retour : None'''
    #3.3
    dessine_ciel(surface)
    #4.2
    nuages.dessine(att['nuages'], surface)
    #3.4
    dessine_soleil(surface)
    #3.5
    dessine_montagnes(surface)
    #3.6
    dessine_sol(surface)
    #3.7 deriere le perso
    dessine_arbre(150, 370, surface)
    dessine_arbre(325, 405, surface)
    dessine_arbre(500, 360, surface)
    dessine_arbre(745, 390, surface)
    #5.2
    if att['perso']['img']==0:
        perso.dessine_0(surface, att['perso']['pos'][0], att['perso']['pos'][1])
    if att['perso']['img']==1:
        perso.dessine_1(surface, att['perso']['pos'][0], att['perso']['pos'][1])
    if att['perso']['img']==2:
        perso.dessine_2(surface, att['perso']['pos'][0], att['perso']['pos'][1])
    #3.7 devant le perso
    dessine_arbre(650, 430, surface)
    dessine_arbre(900, 436, surface)

    
#3.3 Le ciel
def dessine_ciel(surface):
    '''La fonction dessine le ciel du scénario
       Argument : surface
       Retour : None '''
    surface.fill(BLEU_CIEL)



#3.4 Le soleil
def dessine_soleil(surface):
    '''Fonction qui dessine le soleil
       Argument : surface
       Retour : None'''
    pygame.draw.circle(surface, JAUNE_OR, [900, 75], 50)
    pygame.draw.circle(surface, JAUNE_CIT, [900, 75], 45)


#3.5 Les montagnes
def dessine_montagnes(surface):
    '''Fonction qui dessine les montagnes
       Argument : surface
       Retour : None'''
    pygame.draw.polygon(surface, MARRON, [[-200,500], [250,100], [600,500]])
    pygame.draw.polygon(surface, MARRON, [[200,500], [750,100], [1275,500]])
    pygame.draw.polygon(surface, BLANC, [[250,100], [136.15,201.19], [338.15,200.74]])
    pygame.draw.polygon(surface, BLANC, [[750,100], [610.86,201.19], [882.23,200.74]])



#3.6 Le sol
def dessine_sol(surface):
    '''Fonction qui dessine le sol
       Argument : surface
       Retour : None'''
    pygame.draw.rect(surface, BLANC, [0, 400, 1000, 100])

#3.7 Les arbres
def dessine_arbre(x, y, surface):
    '''Fonction qui dessine les arbres
       Argument : tuple
                  surface
       Retour : None'''
    
    for i in range(4):
        pygame.draw.polygon(surface, VERT, ((x, y+20), (x+20, y), (x+40, y+20)))
        y+=10

#3.8 Mise à jour
def update(att):
    '''Fontion qui met a jour les nuages et le personnage
       Argument : dict
       Retour : None'''
    
    nuages.update(att['nuages'])
    perso.update(att['perso'])



