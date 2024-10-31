from fltk import *
import random
import os

def quadrillage(i,j,largeur,hauteur):
    for k in range(i):
        for l in range(j):
            rectangle(l*largeur/j,k*hauteur/i,(l+1)*largeur/j,(k+1)*hauteur/i)

def affichage_jeu(taille_plat,lst_joueur,rectangles,lst_rectangles,superpo,tour=0):
    if superpo==0:
        rectangle(0,0,largeur_fenetre(),hauteur_fenetre(),"white",remplissage="white")
    a=taille_plat*2+taille_plat+1
    i,j=a,a
    dico_taille_pion={'5':fenetre/10,'7':fenetre/13,'9':fenetre/15,'11':fenetre/19}
    taille_case=largeur_fenetre()/i
    rectangle((lst_joueur[tour][1]+1)*taille_case+lst_joueur[tour][1]*(2*taille_case)-0.5*taille_case,(lst_joueur[tour][0]+1)*taille_case+lst_joueur[tour][0]*(2*taille_case)-0.5*taille_case,(lst_joueur[tour][1]+1)*taille_case+lst_joueur[tour][1]*(2*taille_case)+2.5*taille_case,(lst_joueur[tour][0]+1)*taille_case+lst_joueur[tour][0]*(2*taille_case)+2.5*taille_case,couleur="red",remplissage='red')
    nb_joueur=0
    for element in lst_joueur:
        if element!=None:
            nb_joueur+=1
    image(largeur_fenetre()/2,hauteur_fenetre()/2, 'plateau_'+str(taille_plat)+'_'+str(nb_joueur)+'.png',largeur=largeur_fenetre(), hauteur=hauteur_fenetre())
    image((lst_joueur[0][1]+1)*taille_case+lst_joueur[0][1]*(2*taille_case)+taille_case,(lst_joueur[0][0]+1)*taille_case+lst_joueur[0][0]*(2*taille_case)+taille_case, 'joueur_1.png',largeur=int(dico_taille_pion[str(taille_plat)]), hauteur=int(dico_taille_pion[str(taille_plat)]))
    image((lst_joueur[1][1]+1)*taille_case+lst_joueur[1][1]*(2*taille_case)+taille_case,(lst_joueur[1][0]+1)*taille_case+lst_joueur[1][0]*(2*taille_case)+taille_case, 'joueur_2.png',largeur=int(dico_taille_pion[str(taille_plat)]), hauteur=int(dico_taille_pion[str(taille_plat)]))
    image((lst_joueur[0][1]+1)*taille_case+lst_joueur[0][1]*(2*taille_case)+2*taille_case,(lst_joueur[0][0]+1)*taille_case+lst_joueur[0][0]*(2*taille_case),'carre.png',largeur=int(taille_case), hauteur=int(taille_case))
    image((lst_joueur[1][1]+1)*taille_case+lst_joueur[1][1]*(2*taille_case)+2*taille_case,(lst_joueur[1][0]+1)*taille_case+lst_joueur[1][0]*(2*taille_case),'carre.png',largeur=int(taille_case), hauteur=int(taille_case))
    texte((lst_joueur[0][1]+1)*taille_case+lst_joueur[0][1]*(2*taille_case)+2*taille_case,(lst_joueur[0][0]+1)*taille_case+lst_joueur[0][0]*(2*taille_case),lst_rectangles[0],couleur="black",taille=int(dico_taille_pion[str(taille_plat)]/3.5),ancrage='center')
    texte((lst_joueur[1][1]+1)*taille_case+lst_joueur[1][1]*(2*taille_case)+2*taille_case,(lst_joueur[1][0]+1)*taille_case+lst_joueur[1][0]*(2*taille_case),lst_rectangles[1],couleur="black",taille=int(dico_taille_pion[str(taille_plat)]/3.5),ancrage='center')
    if lst_joueur[2]!=None and lst_joueur[3]!=None:
        image((lst_joueur[2][1]+1)*taille_case+lst_joueur[2][1]*(2*taille_case)+taille_case,(lst_joueur[2][0]+1)*taille_case+lst_joueur[2][0]*(2*taille_case)+taille_case, 'joueur_3.png',largeur=int(dico_taille_pion[str(taille_plat)]), hauteur=int(dico_taille_pion[str(taille_plat)]))
        image((lst_joueur[3][1]+1)*taille_case+lst_joueur[3][1]*(2*taille_case)+taille_case,(lst_joueur[3][0]+1)*taille_case+lst_joueur[3][0]*(2*taille_case)+taille_case, 'joueur_4.png',largeur=int(dico_taille_pion[str(taille_plat)]), hauteur=int(dico_taille_pion[str(taille_plat)]))
        image((lst_joueur[2][1]+1)*taille_case+lst_joueur[2][1]*(2*taille_case)+2*taille_case,(lst_joueur[2][0]+1)*taille_case+lst_joueur[2][0]*(2*taille_case),'carre.png',largeur=int(taille_case), hauteur=int(taille_case))
        image((lst_joueur[3][1]+1)*taille_case+lst_joueur[3][1]*(2*taille_case)+2*taille_case,(lst_joueur[3][0]+1)*taille_case+lst_joueur[3][0]*(2*taille_case),'carre.png',largeur=int(taille_case), hauteur=int(taille_case))
        texte((lst_joueur[2][1]+1)*taille_case+lst_joueur[2][1]*(2*taille_case)+2*taille_case,(lst_joueur[2][0]+1)*taille_case+lst_joueur[2][0]*(2*taille_case),lst_rectangles[2],couleur="black",taille=int(dico_taille_pion[str(taille_plat)]/3.5),ancrage='center')
        texte((lst_joueur[3][1]+1)*taille_case+lst_joueur[3][1]*(2*taille_case)+2*taille_case,(lst_joueur[3][0]+1)*taille_case+lst_joueur[3][0]*(2*taille_case),lst_rectangles[3],couleur="black",taille=int(dico_taille_pion[str(taille_plat)]/3.5),ancrage='center')
    for rect in rectangles:
        if rect[2]-rect[0]==5:
            image(rect[1]*taille_case+0.5*taille_case,rect[2]*taille_case-2.5*taille_case, 'mur_1.png',largeur=int(taille_case), hauteur=5*int(taille_case))
        else:
            image(rect[3]*taille_case-2.5*taille_case,rect[0]*taille_case+0.5*taille_case, 'mur_2.png',largeur=5*int(taille_case), hauteur=int(taille_case))
    #quadrillage(i,j,largeur_fenetre(),hauteur_fenetre())

def clic_vers_case(x, y,i,j,structure,dico_clic,rectangles,lst_rectangles,tour):
    """permet de convertir les coordonnées d'un clic en coordonnées (ligne,colonne)"""
    larg_case,haut_case=largeur_fenetre()/j,hauteur_fenetre()/i
    clic=int(y / haut_case), int(x / larg_case)
    for element in dico_clic:
        if clic in dico_clic[element]:
            return element,structure,rectangles,None,clic
    if x>=larg_case and x<=largeur_fenetre()-3*larg_case and y>=haut_case and y<=hauteur_fenetre()-3*haut_case:
        if lst_rectangles[tour]!=0:
            return creation_mur(dico_clic,larg_case,haut_case,structure,clic,rectangles)
    return None,structure,rectangles,None,clic

def clic_vers_case2(x, y,i,j):
    """permet de convertir les coordonnées d'un clic en coordonnées (ligne,colonne)"""
    larg_case,haut_case=largeur_fenetre()/j,hauteur_fenetre()/i
    clic=int(y / haut_case), int(x / larg_case)
    return clic

def creation_mur(dico_clic,larg_case,haut_case,structure,clic,rectangles):
        for element in dico_clic:
            if (clic[0]-1,clic[1]) in dico_clic[element]:
                if structure[element[0]][element[1]][2]==True and structure[element[0]][element[1]+1][2]==True and structure[element[0]+1][element[1]+1][0]==True and structure[element[0]+1][element[1]][0]==True:
                    if (clic[0]-2,clic[1]+2,clic[0]+3,clic[1]+3) not in rectangles and (clic[0]-2,clic[1]+1,clic[0]+3,clic[1]+2) not in rectangles:
                        if (clic[0]-1,clic[1]+1) in dico_clic[element]:
                            rectangle(clic[1]*larg_case,clic[0]*haut_case,(clic[1]+5)*larg_case,(clic[0]+1)*haut_case,couleur="gray",remplissage="gray")
                            rectangles.append((3+element[0]*3,1+element[1]*3,4+element[0]*3,6+element[1]*3))
                            structure[element[0]][element[1]],structure[element[0]][element[1]+1],structure[element[0]+1][element[1]+1],structure[element[0]+1][element[1]]=(structure[element[0]][element[1]][0],structure[element[0]][element[1]][1],False,structure[element[0]][element[1]][3]),(structure[element[0]][element[1]+1][0],structure[element[0]][element[1]+1][1],False,structure[element[0]][element[1]+1][3]),(False,structure[element[0]+1][element[1]+1][1],structure[element[0]+1][element[1]+1][2],structure[element[0]+1][element[1]+1][3]),(False,structure[element[0]+1][element[1]][1],structure[element[0]+1][element[1]][2],structure[element[0]+1][element[1]][3])
                        else:
                            rectangle((clic[1]-1)*larg_case,clic[0]*haut_case,(clic[1]+4)*larg_case,(clic[0]+1)*haut_case,couleur="gray",remplissage="gray")
                            rectangles.append((3+element[0]*3,1+element[1]*3,4+element[0]*3,6+element[1]*3))
                            structure[element[0]][element[1]],structure[element[0]][element[1]+1],structure[element[0]+1][element[1]+1],structure[element[0]+1][element[1]]=(structure[element[0]][element[1]][0],structure[element[0]][element[1]][1],False,structure[element[0]][element[1]][3]),(structure[element[0]][element[1]+1][0],structure[element[0]][element[1]+1][1],False,structure[element[0]][element[1]+1][3]),(False,structure[element[0]+1][element[1]+1][1],structure[element[0]+1][element[1]+1][2],structure[element[0]+1][element[1]+1][3]),(False,structure[element[0]+1][element[1]][1],structure[element[0]+1][element[1]][2],structure[element[0]+1][element[1]][3])
                        return None,structure,rectangles,1,clic
            if (clic[0],clic[1]-1) in dico_clic[element]:
                if structure[element[0]][element[1]][1]==True and structure[element[0]][element[1]+1][3]==True and structure[element[0]+1][element[1]+1][3]==True and structure[element[0]+1][element[1]][1]==True:
                    if (clic[0]+2,clic[1]-2,clic[0]+3,clic[1]+3) not in rectangles and (clic[0]+1,clic[1]-2,clic[0]+2,clic[1]+3) not in rectangles:
                        if (clic[0]+1,clic[1]-1) in dico_clic[element]:
                            rectangle(clic[1]*larg_case,clic[0]*haut_case,(clic[1]+1)*larg_case,(clic[0]+5)*haut_case,couleur="gray",remplissage="gray")
                            rectangles.append((1+element[0]*3,3+element[1]*3,6+element[0]*3,4+element[1]*3))
                            structure[element[0]][element[1]],structure[element[0]][element[1]+1],structure[element[0]+1][element[1]+1],structure[element[0]+1][element[1]]=(structure[element[0]][element[1]][0],False,structure[element[0]][element[1]][2],structure[element[0]][element[1]][3]),(structure[element[0]][element[1]+1][0],structure[element[0]][element[1]+1][1],structure[element[0]][element[1]+1][2],False),(structure[element[0]+1][element[1]+1][0],structure[element[0]+1][element[1]+1][1],structure[element[0]+1][element[1]+1][2],False),(structure[element[0]+1][element[1]][0],False,structure[element[0]+1][element[1]][2],structure[element[0]+1][element[1]][3])
                        else:
                            rectangle((clic[1])*larg_case,(clic[0]-1)*haut_case,(clic[1]+1)*larg_case,(clic[0]+4)*haut_case,couleur="gray",remplissage="gray")
                            rectangles.append((1+element[0]*3,3+element[1]*3,6+element[0]*3,4+element[1]*3))
                            structure[element[0]][element[1]],structure[element[0]][element[1]+1],structure[element[0]+1][element[1]+1],structure[element[0]+1][element[1]]=(structure[element[0]][element[1]][0],False,structure[element[0]][element[1]][2],structure[element[0]][element[1]][3]),(structure[element[0]][element[1]+1][0],structure[element[0]][element[1]+1][1],structure[element[0]][element[1]+1][2],False),(structure[element[0]+1][element[1]+1][0],structure[element[0]+1][element[1]+1][1],structure[element[0]+1][element[1]+1][2],False),(structure[element[0]+1][element[1]][0],False,structure[element[0]+1][element[1]][2],structure[element[0]+1][element[1]][3])
                        return None,structure,rectangles,1,clic
        return None,structure,rectangles,None,clic

def verifie_impasse(structure,joueur,lst_joueur,lst_win,tour,visite):
    visite.add(joueur)
    cibles=[]
    cible=[]
    for element in lst_win[tour]:
        if joueur==element:
            return True
    cible=verif_voisin(structure,joueur,lst_joueur)
    for element in cible:
        if element not in visite:
            cibles.append(element)
    if len(cibles)>1:
        for element in cibles:
            result=verifie_impasse(structure,element,lst_joueur,lst_win,tour,visite)
            if result==True:
                return True
        return False
    if len(cibles)==0:
        return False
    return verifie_impasse(structure,cibles[0],lst_joueur,lst_win,tour,visite)

def structure_retour(structure,dico_clic,clic,rectangles):
    for element in dico_clic:
        if (clic[0]-1,clic[1]) in dico_clic[element]:
            structure[element[0]][element[1]],structure[element[0]][element[1]+1],structure[element[0]+1][element[1]+1],structure[element[0]+1][element[1]]=(structure[element[0]][element[1]][0],structure[element[0]][element[1]][1],True,structure[element[0]][element[1]][3]),(structure[element[0]][element[1]+1][0],structure[element[0]][element[1]+1][1],True,structure[element[0]][element[1]+1][3]),(True,structure[element[0]+1][element[1]+1][1],structure[element[0]+1][element[1]+1][2],structure[element[0]+1][element[1]+1][3]),(True,structure[element[0]+1][element[1]][1],structure[element[0]+1][element[1]][2],structure[element[0]+1][element[1]][3])
            rectangles.pop()
            return structure,rectangles
        if (clic[0],clic[1]-1) in dico_clic[element]:
            structure[element[0]][element[1]],structure[element[0]][element[1]+1],structure[element[0]+1][element[1]+1],structure[element[0]+1][element[1]]=(structure[element[0]][element[1]][0],True,structure[element[0]][element[1]][2],structure[element[0]][element[1]][3]),(structure[element[0]][element[1]+1][0],structure[element[0]][element[1]+1][1],structure[element[0]][element[1]+1][2],True),(structure[element[0]+1][element[1]+1][0],structure[element[0]+1][element[1]+1][1],structure[element[0]+1][element[1]+1][2],True),(structure[element[0]+1][element[1]][0],True,structure[element[0]+1][element[1]][2],structure[element[0]+1][element[1]][3])
            rectangles.pop()
            return structure,rectangles
    return structure,rectangles
    
def voisin(structure,joueur,lst_joueur):
    lst_valide=[]
    if joueur[0]!=0:
        if structure[joueur[0]][joueur[1]][0]==True:
            if (joueur[0]-1,joueur[1])!=lst_joueur[0] and (joueur[0]-1,joueur[1])!=lst_joueur[1] and (joueur[0]-1,joueur[1])!=lst_joueur[2] and (joueur[0]-1,joueur[1])!=lst_joueur[3]:
                lst_valide.append((joueur[0]-1,joueur[1]))
            else:
                if structure[joueur[0]-1][joueur[1]][0]==True:
                    if (joueur[0]-2,joueur[1])!=lst_joueur[0] and (joueur[0]-2,joueur[1])!=lst_joueur[1] and (joueur[0]-2,joueur[1])!=lst_joueur[2] and (joueur[0]-2,joueur[1])!=lst_joueur[3]:
                        lst_valide.append((joueur[0]-2,joueur[1]))
                if structure[joueur[0]-1][joueur[1]][1]==True:
                    if (joueur[0]-1,joueur[1]+1)!=lst_joueur[0] and (joueur[0]-1,joueur[1]+1)!=lst_joueur[1] and (joueur[0]-1,joueur[1]+1)!=lst_joueur[2] and (joueur[0]-1,joueur[1]+1)!=lst_joueur[3]:
                        lst_valide.append((joueur[0]-1,joueur[1]+1))
                if structure[joueur[0]-1][joueur[1]][3]==True:
                    if (joueur[0]-1,joueur[1]-1)!=lst_joueur[0] and (joueur[0]-1,joueur[1]-1)!=lst_joueur[1] and (joueur[0]-1,joueur[1]-1)!=lst_joueur[2] and (joueur[0]-1,joueur[1]-1)!=lst_joueur[3]:
                        lst_valide.append((joueur[0]-1,joueur[1]-1))
    if joueur[1]!=(len(structure[0])-1):
        if structure[joueur[0]][joueur[1]][1]==True:
            if (joueur[0],joueur[1]+1)!=lst_joueur[0] and (joueur[0],joueur[1]+1)!=lst_joueur[1] and (joueur[0],joueur[1]+1)!=lst_joueur[2] and (joueur[0],joueur[1]+1)!=lst_joueur[3]:
                lst_valide.append((joueur[0],joueur[1]+1))
            else:
                if structure[joueur[0]][joueur[1]+1][1]==True:
                    if (joueur[0],joueur[1]+2)!=lst_joueur[0] and (joueur[0],joueur[1]+2)!=lst_joueur[1] and (joueur[0],joueur[1]+2)!=lst_joueur[2] and (joueur[0],joueur[1]+2)!=lst_joueur[3]:
                        lst_valide.append((joueur[0],joueur[1]+2))
                if structure[joueur[0]][joueur[1]+1][0]==True:
                    if (joueur[0]-1,joueur[1]+1)!=lst_joueur[0] and (joueur[0]-1,joueur[1]+1)!=lst_joueur[1] and (joueur[0]-1,joueur[1]+1)!=lst_joueur[2] and (joueur[0]-1,joueur[1]+1)!=lst_joueur[3]:
                        lst_valide.append((joueur[0]-1,joueur[1]+1))
                if structure[joueur[0]][joueur[1]+1][2]==True:
                    if (joueur[0]+1,joueur[1]+1)!=lst_joueur[0] and (joueur[0]+1,joueur[1]+1)!=lst_joueur[1] and (joueur[0]+1,joueur[1]+1)!=lst_joueur[2] and (joueur[0]+1,joueur[1]+1)!=lst_joueur[3]:
                        lst_valide.append((joueur[0]+1,joueur[1]+1))
    if joueur[0]!=(len(structure)-1):
        if structure[joueur[0]][joueur[1]][2]==True:
            if (joueur[0]+1,joueur[1])!=lst_joueur[0] and (joueur[0]+1,joueur[1])!=lst_joueur[1] and (joueur[0]+1,joueur[1])!=lst_joueur[2] and (joueur[0]+1,joueur[1])!=lst_joueur[3]:
                lst_valide.append((joueur[0]+1,joueur[1]))
            else:
                if structure[joueur[0]+1][joueur[1]][2]==True:
                    if (joueur[0]+2,joueur[1])!=lst_joueur[0] and (joueur[0]+2,joueur[1])!=lst_joueur[1] and (joueur[0]+2,joueur[1])!=lst_joueur[2] and (joueur[0]+2,joueur[1])!=lst_joueur[3]:
                        lst_valide.append((joueur[0]+2,joueur[1]))
                if structure[joueur[0]+1][joueur[1]][1]==True:
                    if (joueur[0]+1,joueur[1]+1)!=lst_joueur[0] and (joueur[0]+1,joueur[1]+1)!=lst_joueur[1] and (joueur[0]+1,joueur[1]+1)!=lst_joueur[2] and (joueur[0]+1,joueur[1]+1)!=lst_joueur[3]:
                        lst_valide.append((joueur[0]+1,joueur[1]+1))
                if structure[joueur[0]+1][joueur[1]][3]==True:
                    if (joueur[0]+1,joueur[1]-1)!=lst_joueur[0] and (joueur[0]+1,joueur[1]-1)!=lst_joueur[1] and (joueur[0]+1,joueur[1]-1)!=lst_joueur[2] and (joueur[0]+1,joueur[1]-1)!=lst_joueur[3]:
                        lst_valide.append((joueur[0]+1,joueur[1]-1))
    if joueur[1]!=0:
        if structure[joueur[0]][joueur[1]][3]==True:
            if (joueur[0],joueur[1]-1)!=lst_joueur[0] and (joueur[0],joueur[1]-1)!=lst_joueur[1] and (joueur[0],joueur[1]-1)!=lst_joueur[2] and (joueur[0],joueur[1]-1)!=lst_joueur[3]:
                lst_valide.append((joueur[0],joueur[1]-1))
            else:
                if structure[joueur[0]][joueur[1]-1][3]==True:
                    if (joueur[0],joueur[1]-2)!=lst_joueur[0] and (joueur[0],joueur[1]-2)!=lst_joueur[1] and (joueur[0],joueur[1]-2)!=lst_joueur[2] and (joueur[0],joueur[1]-2)!=lst_joueur[3]:
                        lst_valide.append((joueur[0],joueur[1]-2))
                if structure[joueur[0]][joueur[1]-1][0]==True:
                    if (joueur[0]-1,joueur[1]-1)!=lst_joueur[0] and (joueur[0]-1,joueur[1]-1)!=lst_joueur[1] and (joueur[0]-1,joueur[1]-1)!=lst_joueur[2] and (joueur[0]-1,joueur[1]-1)!=lst_joueur[3]:
                        lst_valide.append((joueur[0]-1,joueur[1]-1))
                if structure[joueur[0]][joueur[1]-1][2]==True:
                    if (joueur[0]+1,joueur[1]-1)!=lst_joueur[0] and (joueur[0]+1,joueur[1]-1)!=lst_joueur[1] and (joueur[0]+1,joueur[1]-1)!=lst_joueur[2] and (joueur[0]+1,joueur[1]-1)!=lst_joueur[3]:
                        lst_valide.append((joueur[0]+1,joueur[1]-1))
    return lst_valide

def verif_voisin(structure,joueur,lst_joueur):
    lst_valide=[]
    if joueur[0]!=0:
        if structure[joueur[0]][joueur[1]][0]==True:
            lst_valide.append((joueur[0]-1,joueur[1]))
    if joueur[1]!=(len(structure[0])-1):
        if structure[joueur[0]][joueur[1]][1]==True:
            lst_valide.append((joueur[0],joueur[1]+1))
    if joueur[0]!=(len(structure)-1):
        if structure[joueur[0]][joueur[1]][2]==True:
                lst_valide.append((joueur[0]+1,joueur[1]))
    if joueur[1]!=0:
        if structure[joueur[0]][joueur[1]][3]==True:
                lst_valide.append((joueur[0],joueur[1]-1))
    return lst_valide

def affiche_valide(structure,lst_valide,lst_joueur,rectangles,lst_rectangles,tour=0):
    a=len(structure)*2+len(structure)+1
    i,j=a,a
    taille_case=largeur_fenetre()/i
    for element in lst_valide:
        rectangle(taille_case+element[1]*(taille_case*3)-taille_case/3,taille_case+element[0]*(taille_case*3)-taille_case/3,3*taille_case+element[1]*(taille_case*3)+taille_case/3,3*taille_case+element[0]*(taille_case*3)+taille_case/3,couleur=lst_couleur[tour],remplissage=lst_couleur[tour])
    affichage_jeu(len(structure),lst_joueur,rectangles,lst_rectangles,1,tour)

def evenement(i,j,structure,dico_clic,rectangles,lst_rectangles,tour):
    while True:
        ev = attend_ev()
        tev = type_ev(ev)
        if tev == "Quitte":
            ferme_fenetre()
            return 'quitte',None,None,None,None
        if tev == "ClicGauche":
            return clic_vers_case(abscisse(ev), ordonnee(ev),i,j,structure,dico_clic,rectangles,lst_rectangles,tour)

def evenement2(i,j):
    while True:
        ev = attend_ev()
        tev = type_ev(ev)
        if tev == "Quitte":
            ferme_fenetre()
            return 'quitte'
        if tev == "ClicGauche":
            return clic_vers_case2(abscisse(ev), ordonnee(ev),i,j)

def jeu(mur,structure,dico_clic,lst_joueur,rectangles,lst_rectangles,bot,tour=0):
    a=len(structure)*2+len(structure)+1
    larg_case,haut_case=largeur_fenetre()/a,hauteur_fenetre()/a
    lst_valide=[]
    nb_joueur=0
    for element in lst_joueur:
        if element!=None:
            nb_joueur+=1
    if lst_joueur[tour]==None:
        if tour==3:
            return jeu(mur,structure,dico_clic,lst_joueur,rectangles,lst_rectangles,bot,0)
        return jeu(mur,structure,dico_clic,lst_joueur,rectangles,lst_rectangles,bot,tour+1)
    bord=len(structure)-1
    if nb_joueur==2:
        lst_win=[[(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),(0,9),(0,10)],[(bord,0),(bord,1),(bord,2),(bord,3),(bord,4),(bord,5),(bord,6),(bord,7),(bord,8),(bord,9),(bord,10)]]
    else:
        lst_win=[[(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),(0,9),(0,10)],[(0,bord),(1,bord),(2,bord),(3,bord),(4,bord),(5,bord),(6,bord),(7,bord),(8,bord),(9,bord),(10,bord)],
                [(bord,0),(bord,1),(bord,2),(bord,3),(bord,4),(bord,5),(bord,6),(bord,7),(bord,8),(bord,9),(bord,10)],[(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0)]]
    if bot==True:
        if tour==0:
            for element in lst_win[nb_joueur-1]:
                if lst_joueur[nb_joueur-1]==element:
                    return menu_fin(len(structure),nb_joueur,mur,bot,int(nb_joueur))
        for element in lst_win[tour-1]:
            if lst_joueur[tour-1]==element:
                return menu_fin(len(structure),nb_joueur,mur,bot,int(tour))
        if tour!=0:
            t=random.choice([0.4,0.5,0.6,0.7])
            attente(t)
            if lst_rectangles[tour]!=0:
                choix=random.choice(['jouer','mur'])
            else:
                choix='jouer'
            if choix=='jouer':
                action=lst_joueur[tour]
                lst_valide=voisin(structure,action,lst_joueur)
                affiche_valide(structure,lst_valide,lst_joueur,rectangles,lst_rectangles,tour)
                t=random.choice([0.4,0.5,0.6,0.7,0.8,0.9,1])
                attente(t)
                action=random.choice(lst_valide)
                while action[0]<0 or action[0]>len(structure)-1 or action[1]<0 or action[1]>len(structure)-1:
                    action=random.choice(lst_valide)
                lst_joueur[tour]=action
                if tour==3:
                    affichage_jeu(len(structure),lst_joueur,rectangles,lst_rectangles,0,0)
                    return jeu(mur,structure,dico_clic,lst_joueur,rectangles,lst_rectangles,bot,0)
                else:
                    if nb_joueur==2:
                        if tour==0:
                            affichage_jeu(len(structure),lst_joueur,rectangles,lst_rectangles,0,tour+1)
                        else:
                            affichage_jeu(len(structure),lst_joueur,rectangles,lst_rectangles,0,0)
                    else:
                        affichage_jeu(len(structure),lst_joueur,rectangles,lst_rectangles,0,tour+1)
                return jeu(mur,structure,dico_clic,lst_joueur,rectangles,lst_rectangles,bot,tour+1)
            if choix=='mur':
                liste=[]
                initi=1
                for kk in range(len(structure)-1):
                    initi2=3
                    for ll in range(len(structure)-1):
                        liste.append((initi,initi2))
                        liste.append((initi+1,initi2))
                        initi2+=3
                    initi+=3
                initi=3
                for ii in range(len(structure)-1):
                    initi2=1
                    for jj in range(len(structure)-1):
                        liste.append((initi,initi2))
                        liste.append((initi,initi2+1))
                        initi2+=3
                    initi+=3
                rectangles3=rectangles.copy()
                while len(rectangles)==len(rectangles3):
                    clic=(random.randint(1,a-4),random.randint(1,a-4))
                    if clic in liste:
                        action,structure,rectangles,rect,clic=creation_mur(dico_clic,larg_case,haut_case,structure,clic,rectangles)
                lst_rectangles[tour]-=1
                Tour=0
                for joueur in lst_joueur:
                    if joueur!=None:
                        visite=set()
                        if verifie_impasse(structure,joueur,lst_joueur,lst_win,Tour,visite)==False:
                            structure,rectangles=structure_retour(structure,dico_clic,clic,rectangles)
                            lst_rectangles[tour]+=1
                            affichage_jeu(len(structure),lst_joueur,rectangles,lst_rectangles,0,tour)
                            return jeu(mur,structure,dico_clic,lst_joueur,rectangles,lst_rectangles,bot,tour)
                    Tour+=1
                if tour==3:
                    affichage_jeu(len(structure),lst_joueur,rectangles,lst_rectangles,0,0)
                    return jeu(mur,structure,dico_clic,lst_joueur,rectangles,lst_rectangles,bot,0)
                else:
                    if nb_joueur==2:
                        if tour==0:
                            affichage_jeu(len(structure),lst_joueur,rectangles,lst_rectangles,0,tour+1)
                        else:
                            affichage_jeu(len(structure),lst_joueur,rectangles,lst_rectangles,0,0)
                    else:
                        affichage_jeu(len(structure),lst_joueur,rectangles,lst_rectangles,0,tour+1)
                return jeu(mur,structure,dico_clic,lst_joueur,rectangles,lst_rectangles,bot,tour+1)
    while True:
        if tour==0:
            for element in lst_win[nb_joueur-1]:
                if lst_joueur[nb_joueur-1]==element:
                    return menu_fin(len(structure),nb_joueur,mur,bot,int(nb_joueur))
        for element in lst_win[tour-1]:
            if lst_joueur[tour-1]==element:
                return menu_fin(len(structure),nb_joueur,mur,bot,int(tour))
        rectangles2=rectangles.copy()
        action,structure,rectangles,rect,clic=evenement(a,a,structure,dico_clic,rectangles,lst_rectangles,tour)
        if action=='quitte':
            return 'quitte'
        if len(rectangles2)<len(rectangles):
            lst_rectangles[tour]-=1
        Tour=0
        for joueur in lst_joueur:
            if joueur!=None:
                visite=set()
                if verifie_impasse(structure,joueur,lst_joueur,lst_win,Tour,visite)==False:
                    structure,rectangles=structure_retour(structure,dico_clic,clic,rectangles)
                    lst_rectangles[tour]+=1
                    affichage_jeu(len(structure),lst_joueur,rectangles,lst_rectangles,0,tour)
                    return jeu(mur,structure,dico_clic,lst_joueur,rectangles,lst_rectangles,bot,tour)
            Tour+=1
        if action in lst_valide or rect==1:
            if rect!=1:
                lst_joueur[tour]=action
            if tour==3:
                affichage_jeu(len(structure),lst_joueur,rectangles,lst_rectangles,0,0)
                return jeu(mur,structure,dico_clic,lst_joueur,rectangles,lst_rectangles,bot,0)
            else:
                if nb_joueur==2:
                    if tour==0:
                        affichage_jeu(len(structure),lst_joueur,rectangles,lst_rectangles,0,tour+1)
                    else:
                        affichage_jeu(len(structure),lst_joueur,rectangles,lst_rectangles,0,0)
                else:
                    affichage_jeu(len(structure),lst_joueur,rectangles,lst_rectangles,0,tour+1)
            return jeu(mur,structure,dico_clic,lst_joueur,rectangles,lst_rectangles,bot,tour+1)
        if action==lst_joueur[tour]:
            lst_valide=voisin(structure,action,lst_joueur)
            affiche_valide(structure,lst_valide,lst_joueur,rectangles,lst_rectangles,tour)

def structure_donnée(taille_plat,joueur,mur):
    lst=[]
    for i in range(taille_plat):
        lst2=[]
        for j in range(taille_plat):
            lst2.append((True,True,True,True))
        lst.append(lst2)
    if joueur==2:
        joueur1,joueur2,joueur3,joueur4,lst_rectangles=(taille_plat-1,taille_plat//2),(0,taille_plat//2),None,None,[mur//2,mur//2,None,None]
    elif joueur==4:
        joueur1,joueur2,joueur3,joueur4,lst_rectangles=(taille_plat-1,taille_plat//2),(taille_plat//2,0),(0,taille_plat//2),(taille_plat//2,taille_plat-1),[mur//4,mur//4,mur//4,mur//4]
    return lst,lst_rectangles,joueur1,joueur2,joueur3,joueur4

def settings2(taille_plat,joueur=4,place=1,bot=True):
    i,j=16,16
    if taille_plat==5:
        murs=[4,8]
    elif taille_plat==7:
        murs=[8,12,16,20]
    elif taille_plat==9:
        murs=[16,20,24,28]
    elif taille_plat==11:
        murs=[28,32,36,40]
    rectangle(0,0,largeur_fenetre(),hauteur_fenetre(),"white",remplissage="white")
    image(largeur_fenetre()/2,hauteur_fenetre()/2, 'menu_settings2.png',largeur=largeur_fenetre(), hauteur=hauteur_fenetre())
    if bot==True:
        image(12*(largeur_fenetre()/16),8*(hauteur_fenetre()/16), 'vert.png',largeur=largeur_fenetre()//11, hauteur=hauteur_fenetre()//11)
    else:
        image(12*(largeur_fenetre()/16),8*(hauteur_fenetre()/16), 'rouge.png',largeur=largeur_fenetre()//11, hauteur=hauteur_fenetre()//11)
    texte(12*(largeur_fenetre()/16),2*(hauteur_fenetre()/16),str(joueur),couleur="black",taille=largeur_fenetre()//18,ancrage='center')
    texte(12*(largeur_fenetre()/16),5*(hauteur_fenetre()/16),str(murs[place]),couleur="black",taille=largeur_fenetre()//18,ancrage='center')
    while True:
        action=evenement2(i,j)
        if action=='quitte':
            return 'quitte'
        if action==(1,10) or action==(2,10) or action==(1,9) or action==(2,9):
            if joueur==4:
                return settings2(taille_plat,2,place,bot)
            return settings2(taille_plat,4,place,bot)
        if action==(1,13) or action==(2,13) or action==(1,14) or action==(2,14):
            if joueur==4:
                return settings2(taille_plat,2,place,bot)
            return settings2(taille_plat,4,place,bot)
        if action==(4,10) or action==(5,10) or action==(4,9) or action==(5,9):
            if place==0:
                return settings2(taille_plat,joueur,len(murs)-1,bot)
            return settings2(taille_plat,joueur,place-1,bot)
        if action==(4,13) or action==(5,13) or action==(4,14) or action==(5,14):
            if place==len(murs)-1:
                return settings2(taille_plat,joueur,0,bot)
            return settings2(taille_plat,joueur,place+1,bot)
        if action==(7,10) or action==(8,10) or action==(7,9) or action==(8,9):
            if bot==True:
                return settings2(taille_plat,joueur,place,False)
            return settings2(taille_plat,joueur,place,True)
        if action==(7,13) or action==(8,13) or action==(7,14) or action==(8,14):
            if bot==True:
                return settings2(taille_plat,joueur,place,False)
            return settings2(taille_plat,joueur,place,True)
        for k in range(11,14):
            for l in range(5,11):
                if action==(k,l):
                    return menu(taille_plat,joueur,murs[place],bot)

def menu_fin(taille_plat,joueur,mur,bot,gagnant):
    i,j=16,16
    structure,lst_rectangles,joueur1,joueur2,joueur3,joueur4=structure_donnée(taille_plat,joueur,mur)
    lst_joueur=[joueur1,joueur2,joueur3,joueur4]
    dico_clic,init={},1
    for o in range(len(structure)):
        init2=1
        for p in range(len(structure)):
            dico_clic[(o,p)]=[(init,init2),(init,init2+1),(init+1,init2),(init+1,init2+1)]
            init2+=3
        init+=3
    quadrillage(i,j,largeur_fenetre(),hauteur_fenetre())
    if bot==True and gagnant!=1:
        image(largeur_fenetre()/2,hauteur_fenetre()/2, 'over.png',largeur=largeur_fenetre(), hauteur=hauteur_fenetre())
    else:
        image(largeur_fenetre()/2,hauteur_fenetre()/2, 'win.png',largeur=largeur_fenetre(), hauteur=hauteur_fenetre())
        image(7*(largeur_fenetre()/16),8*(hauteur_fenetre()/16),'joueur_'+str(gagnant)+'.png',largeur=largeur_fenetre()//8, hauteur=hauteur_fenetre()//8)
    while True:
        action=evenement2(i,j)
        if action=='quitte':
            return 'quitte'
        for k in range(10,12):
            for l in range(5,11):
                if action==(k,l):
                    rectangles=[]
                    affichage_jeu(taille_plat,lst_joueur,rectangles,lst_rectangles,0)
                    return jeu(mur,structure,dico_clic,lst_joueur,rectangles,lst_rectangles,bot)
        for k in range(13,15):
            for l in range(5,11):
                if action==(k,l):
                    rectangles=[]
                    return menu(taille_plat,joueur,mur,bot)
    
    

def settings(taille_plat=5):
    i,j=6,6
    rectangle(0,0,largeur_fenetre(),hauteur_fenetre(),"white",remplissage="white")
    quadrillage(i,j,largeur_fenetre(),hauteur_fenetre())
    image(largeur_fenetre()/2,hauteur_fenetre()/2, 'menu_settings.png',largeur=largeur_fenetre(), hauteur=hauteur_fenetre())
    image(largeur_fenetre()/2,hauteur_fenetre()/2, 'plateau_'+str(taille_plat)+'_4.png',largeur=largeur_fenetre()//3, hauteur=hauteur_fenetre()//3)
    action=evenement2(i,j)
    if action=='quitte':
        return 'quitte'
    for k in range(2,4):
        for l in range(2,4):
            if action==(k,l):
                return settings2(taille_plat)
    if action==(2,1) or action==(3,1):
        if taille_plat==5:
            return settings(11)
        return settings(taille_plat-2)
    if action==(2,4) or action==(3,4):
        if taille_plat==11:
            return settings(5)
        return settings(taille_plat+2)

def menu(taille_plat=9,joueur=4,mur=20,bot=True):
    rectangles=[]
    i,j=16,16
    structure,lst_rectangles,joueur1,joueur2,joueur3,joueur4=structure_donnée(taille_plat,joueur,mur)
    lst_joueur=[joueur1,joueur2,joueur3,joueur4]
    dico_clic,init={},1
    for o in range(len(structure)):
        init2=1
        for p in range(len(structure)):
            dico_clic[(o,p)]=[(init,init2),(init,init2+1),(init+1,init2),(init+1,init2+1)]
            init2+=3
        init+=3
    image(largeur_fenetre()/2,hauteur_fenetre()/2, 'fond.png',largeur=largeur_fenetre(), hauteur=hauteur_fenetre())
    #quadrillage(i,j,largeur_fenetre(),hauteur_fenetre())
    while True:
        action=evenement2(i,j)
        if action=='quitte':
            return 'quitte'
        for k in range(9,11):
            for l in range(3,7):
                if action==(k,l):
                    affichage_jeu(taille_plat,lst_joueur,rectangles,lst_rectangles,0)
                    return jeu(mur,structure,dico_clic,lst_joueur,rectangles,lst_rectangles,bot)
        for k in range(9,11):
            for l in range(9,13):
                if action==(k,l):
                    print('online')
        for k in range(12,14):
            for l in range(6,10):
                if action==(k,l):
                    return settings()

if __name__ == "__main__":
    lst_couleur=["tan","gold","pink","silver"]
    rectangles=[]
    fenetre=800
    cree_fenetre(fenetre, fenetre)
    menu()