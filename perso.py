#PLOUVIN Patrice
#25/11/2017
#Module avec les fonctions init, dessine et update du perso.

#Import pygame
import pygame

#Autre import

from couleur import VERT, ORANGE, NOIR, ROUGE_FEU

#5.1 Initialisation
def init(x, y):
    '''Fonction qui initialise les attribu du perso
       Argument : tuple
       Retour : dict'''
    att={}
    att['pos']=[x, y]
    att['lim']=[0, 1000]
    att['vit']=10
    att['img']=0  #varie entre 0 et 2
    return att



#5.2 Dessin
def dessine_0(surface, x, y):
    '''Fonction qui dessine l'homme baton avec les jambes ouvertes.
       Argument : surface, tuple
       Retourn : None'''
    pygame.draw.line(surface, ROUGE_FEU, [x, y], [x+10, y+10])
    pygame.draw.line(surface, ROUGE_FEU, [x, y], [x-10, y+10])
    pygame.draw.line(surface, ROUGE_FEU, [x, y], [x, y+20])
    pygame.draw.line(surface, VERT, [x, y+20], [x+10,y+30])
    pygame.draw.line(surface, VERT, [x, y+20], [x-10, y+30])
    pygame.draw.circle(surface, NOIR, [x, y-10], 10)


def dessine_1(surface, x, y):
    '''Fonction qui dessine l'homme baton avec les jambes demi-ouvertes.
       Argument : surface, tuple
       Retourn : None'''
    pygame.draw.line(surface, ROUGE_FEU, [x, y], [x+10, y+10])
    pygame.draw.line(surface, ROUGE_FEU, [x, y], [x-10, y+10])
    pygame.draw.line(surface, ROUGE_FEU, [x, y], [x, y+20])
    pygame.draw.line(surface, VERT, [x, y+20], [x+5,y+30])
    pygame.draw.line(surface, VERT, [x, y+20], [x-5, y+30])
    pygame.draw.circle(surface, NOIR, [x, y-10], 10)

def dessine_2(surface, x, y):
    '''Fonction qui dessine l'homme baton avec les jambes fermées.
       Argument : surface, tuple
       Retourn : None'''
    pygame.draw.line(surface, ROUGE_FEU, [x, y], [x+10, y+10])
    pygame.draw.line(surface, ROUGE_FEU, [x, y], [x-10, y+10])
    pygame.draw.line(surface, ROUGE_FEU, [x, y], [x, y+20])
    pygame.draw.line(surface, VERT, [x, y+20], [x+2,y+30])
    pygame.draw.line(surface, VERT, [x, y+20], [x-2, y+30])
    pygame.draw.circle(surface, NOIR, [x, y-10], 10)


#5.3
def update(att):
    '''Fonction qui met a jour le perso
       Argument : dict
       Retour : None'''
    att['img']+=1
    if att['img']==3 :
        att['img']=0
    att['pos'][0]+=att['vit']
    if att['pos'][0]-10<=att['lim'][0]:
        att['vit']=-att['vit']
    if att['pos'][0]+10>=att['lim'][1]:
        att['vit']=-att['vit']
    




    
    
