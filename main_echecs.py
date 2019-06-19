#code mail du jeu d'echecs
cadre=[]
for i in 1,2,3,4,5,6,7,8:
    for j in 1,2,3,4,5,6,7,8:
        cadre.append(int(f"{i}{j}"))

print("cadre : ", cadre)

bordDuCadre=[]
for i in 0,1,2,3,4,5,6,7,8,9:
    bordDuCadre.append(i)
    bordDuCadre.append(i*10)
    bordDuCadre.append(i+90)
    bordDuCadre.append(i*10+9)
print("bord du cadre :", bordDuCadre)

cadreEtBord=cadre+bordDuCadre
print("cadre et bord : ",cadreEtBord)


class piece():
    def __init__ (self, couleur, typePiece, position):
        self.couleur = couleur #'requete sql' #blanc ou noir
        self.typePiece= typePiece  # king queen fou cavalier tour pion
        self.position= position # coordonnées
        self.enjeu=True #enjeu ou pas (pris)
        self.moved=False # a bougé (True) ou non (False)
        self.controle=[] #liste des cases sur laquelle la pièce peut se déplacer ou prendre une pièce
        self.echec=False #pour le roi 
    def mouvement(arrivee):
        # TODO : vérifier que le mouvement appartient à la liste de self.controle
        if arrivee in self.controle:
            self.position=arrivee 
            self.moved=True # on change l'état du moved pour marquer que la pièce a bougé (pour le roc ou le pion)
    def casescontrolees():
        pass

#mvt du pion
def mvtPion(pieceActive):
    patern=[]
    if pieceActive.couleur=='blanc':
        patern.append(pieceActive.position+1)
        patern.append(pieceActive.position+11)
        patern.append(pieceActive.position-9)
        if pieceActive.moved==False:
            patern.append(pieceActive.position+2)
    if pieceActive.couleur=='noir':
        patern.append(pieceActive.position-1)
        patern.append(pieceActive.position-11)
        patern.append(pieceActive.position+9)
        if pieceActive.moved==False:
            patern.append(pieceActive.position-2)
    patern.sort()
    return patern

#mvt de la tour
def mvtTour(pieceActive):
    patern=[]
    for i in 1,2,3,4,5,6,7,8:
        patern.append(pieceActive.position+10*i)
        if pieceActive.position+10*i in bordDuCadre: break
    print(patern)
    for i in -1,-2,-3,-4,-5,-6,-7,-8:
        patern.append(pieceActive.position+10*i)
        if pieceActive.position+10*i in bordDuCadre: break
    print(patern)
    for i in range(10):
        dizaine=pieceActive.position//10
        dizaine=dizaine*10
        patern.append(dizaine+i) #la colonne c'est mauvais, il faudrait rester dans la dizaine
    print("patern de la Tour : ", patern)
    patern.sort()
    return patern
#mvt du fou
def mvtFou(pieceActive):
    patern=[]
    for i in 1,2,3,4,5,6,7:
        patern.append(pieceActive.position+11*i)
        if pieceActive.position+11*i in bordDuCadre: break
    for i in 1,2,3,4,5,6,7:
        patern.append(pieceActive.position+9*i)
        if pieceActive.position+9*i in bordDuCadre: break
    for i in 1,2,3,4,5,6,7:
        patern.append(pieceActive.position-11*i)
        if pieceActive.position-11*i in bordDuCadre: break
    for i in 1,2,3,4,5,6,7:
        patern.append(pieceActive.position-9*i)
        if pieceActive.position-9*i in bordDuCadre: break
    #patern.sort()
    print("patern du Fou : ", patern)
    return patern
#mvt de la reine
def mvtQueen(pieceActive):
    patern=[]
    patern=mvtFou(pieceActive)+mvtTour(pieceActive)
    # for i in -7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7:
    #     patern.append(pieceActive.position+11*i)
    #     patern.append(pieceActive.position+9*i)
    #     patern.append(pieceActive.position+10*i)
    # for i in range(10):
    #     dizaine=pieceActive.position//10
    #     dizaine=dizaine*10
    #     patern.append(dizaine+i) #la colonne c'est mauvais, il faudrait rester dans la dizaine
    # patern.sort()
    print("patern de la reine : ",patern)
    return patern
#mvt du cavalier
def mvtCavalier(pieceActive):
    global cadre
    patern=[]
    for i in -21,-19,-12,-8,8,12,19,21:
        if pieceActive.position+i in cadre:
            patern.append(pieceActive.position+i)
    patern.sort()
    return patern
#mvt du roi
def mvtKing(pieceActive):
    patern=[]
    for i in -1,1:
        patern.append(pieceActive.position+11*i)
        patern.append(pieceActive.position+9*i)
        patern.append(pieceActive.position+10*i)
        patern.append(pieceActive.position+1*i)
    patern.sort()
    return patern

#la fonction mvt calcule les trajectoires de la pièce
def mvt(pieceActive):
    if active.typePiece=='pion':
        print (mvtPion(pieceActive))
        return mvtPion(pieceActive)
    if active.typePiece=='tour':
        # print (mvtTour(pieceActive))
        return mvtTour(pieceActive)
    if active.typePiece=='fou':
        # print (mvtFou(pieceActive))
        return mvtFou(pieceActive)
    if active.typePiece=='queen':
        # print (mvtQueen(pieceActive))
        return mvtQueen(pieceActive)
    if active.typePiece=='king':
        #print (mvtKing(pieceActive))
        return mvtKing(pieceActive)
    if active.typePiece=='cavalier':
        #print (mvtCavalier(pieceActive))
        return mvtCavalier(pieceActive)

def mvtPlateau(pieceActive):
    global cadre
    patern=[]
    temp=mvt(pieceActive)
    for i in temp:
        if i in cadre:
            patern.append(i)
    print("les cases où on peut aller :", patern)
    return patern



#check mouvement vérifie que la caseArrivee est sur les trajectoire de la pièce
def checkmvt(pieceActive, caseArrivee):
    temp=mvtPlateau(pieceActive)
    if caseArrivee in temp:
        print ("mouvement correct")
        return True
    else:
        print("mouvement interdit")
        return False

def lesTrajectoires(pieceActive):
    # if not checkmvt(pieceActive,caseArrivee):
    #     return False
    if pieceActive.typePiece=='king' or pieceActive.typePiece=='cavalier' or pieceActive.typePiece=='pion':
        print("pas d'obstacle pour le roi ou le cavalier")
        chemin=[]
        chemin=mvtPlateau(pieceActive)
        return chemin
    mvtBordDuCadre=[]
    temp=mvt(pieceActive)
    for i in bordDuCadre:
        if i in temp and i not in mvtBordDuCadre:
                mvtBordDuCadre.append(i)
    print("les cases où la pièce sort du cadre : ", mvtBordDuCadre)
    tousChemins=[]
    for j in mvtBordDuCadre:
        difference=abs(pieceActive.position-j)
        print(difference)
        for i in 11,10,9:
            if difference%i==0:
                quotient=i
                print (quotient)
        if difference%11==0 or difference%10==0 or difference%9==0:
            pass
        else:
            quotient=1
        chemin=[]
        if pieceActive.position < j:
            temp=100
            i=1
            while temp!=j:
                temp=pieceActive.position+i*quotient
                chemin.append(temp)
                i+=1
                print(temp)
            chemin.sort()
        if pieceActive.position > j:
            temp=100
            i=1
            while temp!=j:
                temp=pieceActive.position-i*quotient
                chemin.append(temp)
                i+=1
                print(temp)
            chemin.sort(reverse=True)
        tousChemins.append(chemin)
    #on sort la desitination de la liste
    #chemin.pop()
    print("toutes les trajectoires de la pièce ", pieceActive.typePiece, " à partir de la position ",pieceActive.position," : ", tousChemins)
    return tousChemins

# lestrajectoires valides = les cases cliquables où notre pièce peut aller
# == aussi la zone de controle, qui sera utile pour la definition de l'echec
def lesTrajectoiresValides(pieceActive):
    # pour chaque liste, dans l'ordre :
    # vérifier dans la bdd si la case est libre
    # si elle n'est pas libre vérifier si la couleur est prenable
    # si elle est prenable, ajouter cette case dans les destinations et sortir de la boucle
    # ajouter la liste à la liste des trajectoires
    
    #sortir les listes de liste
    for i in lesTrajectoires(pieceActive):
        print("on va regarder la trajectoire ", i)
        for j in i:
            print("on regarde la case ",j)
            # pour savoir si il y a une pièce dessus on regarde avec rowcount
            # https://openclassrooms.com/forum/sujet/savoir-si-une-requete-sql-renvoie-des-informations-53841
            if j in cadre:
                print("la case est dans le cadre")
            else:
                print("la case n'est pas dans le cadre")
            
    
    pass





#la fonction chemin donne le chemin le plus direct pour aller à la destination
# inclut la destination
def leChemin(pieceActive, caseArrivee):
    if not checkmvt(pieceActive,caseArrivee):
        return False
    if pieceActive.typePiece=='king' or pieceActive.typePiece=='cavalier':
        print("pas d'obstacle pour le roi ou le cavalier")
        chemin=[]
        return chemin
    difference=abs(pieceActive.position-caseArrivee)
    print("difference : ",difference)
    for i in 11,10,9:
        if difference%i==0:
            quotient=i
            print ("quotient : ", quotient)
    if difference%11==0 or difference%10==0 or difference%9==0:
        pass
    else:
        quotient=1
    chemin=[]
    if pieceActive.position < caseArrivee:
        temp=0
        i=1
        while temp!=caseArrivee:
            temp=pieceActive.position+i*quotient
            chemin.append(temp)
            i+=1
            print("phase ascendante : ",temp)
        chemin.sort()
    if pieceActive.position > caseArrivee:
        temp=0
        i=1
        while temp!=caseArrivee:
            temp=pieceActive.position-i*quotient
            chemin.append(temp)
            i+=1
            print("phase descendante : ",temp)
        chemin.sort(reverse=True)
    #on sort la desitination de la liste
    #chemin.pop()
    print(chemin)
    return chemin

# la maintenant on va taper dans la bdd
# pour vérifier les positions du chemin et vérifier qu'il n'y a rien sur le chemin
# def verifObstacle(pieceActive, caseArrivee):


# si le mouvement est légal, qu'il n'y a pas d'obstacles sur le chemin 'leChemin'
# et que la case de destination n'est pas occupé par une pièce de la même couleur
# alors on bouge la pièce
# si il y a une pièce au bout, alors on la "mange" :
#   la pièce à destination passe de l'état "enJeu" 'True' à 'False' avec des coordonnées en 100 100 ou autre
def bougeLaPiece(active, destination):
    pass
    # regarder dans la BDD si la case de destination est occupée par une pièce adverse
    # si oui, retirer la valeur "enJeu" de cette pièce en False
    # 
    # bouger notre pièce vers la nouvelle case (changer la valeur des coordonnées dans la bdd)
    #  


#POUR TESTER AVANT D AVOIR TOUT FINI
active=piece('noir','tour',11)
# mvt(active)
# checkmvt(active, 55)
#leChemin(active,26)
lesTrajectoires(active)
lesTrajectoiresValides(active)
#leChemin(active, 23)
