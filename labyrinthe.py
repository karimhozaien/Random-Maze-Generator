# Auteur: Karim Hozaien
# Date : 23 Octobre 2023




# Fonction qui prend un nombre entier  comme parametre et retourne une séquence 
# de nombres de 0 à 'nombre - 1' et la stocke dans une liste.

def sequence(nombre):
    tab = []
# On ajoute la sequence de nombre au tableau.
    for i in range(nombre):
        tab.append(i)
    return tab



# Fonction qui prend pour parametre un tableau et un nombre et retourne True
# si le nombre ce trouve dans le tableau. Sinon la fonction retourne False.
def contient(tab,x):   
# On verifie si l'element actuel tab[i] est égal à 'x'.
    for i in range(len(tab)):
        if tab[i] == x:
            return True
            break
# Si tab[i] n'est pas egale a 'x' on recommence pour la porochaine iteration
# de tab
        else :
            i+=1
# Si on ne retrouve pas 'x' dans tab on retourne Faux
    return False



# Fonction qui prend pour parametre un tableau et un nombre. Si le nombre 
# donnee n'est pas dans le tableau on ajoute le nombre et la fonction retourne
# le tableau avec l'ajout du nombre. Si le nombre est compris dans le tableau
# la fonction retourne simplement le tableau. 

def ajouter(tab,x):
# On verifie si x est deja dans tab grace a la fonction contient. 
    if contient(tab,x) == True:
        return tab
    else:
        tab.append(x)
        return tab
    
    
    
    
# Fonction qui prend pour parametre un tableau et un nombre. Si le nombre 
# donnee est dans le tableau le nombre est retirer et la fonction retourne
# le tableau avec le retrait du nombre. Si le nombre n'est pas compris dans
# le tableau la fonction retourne simplement le tableau. 
    
def retirer(tab,x):
# On verifie si x est deja dans tab grace a la fonction contient.
    if contient(tab,x) == True:
        tab.remove(x)
        return tab
    else:
        return tab
    
    
    
    
# Fonction qui prend pour parametre 2 entier nx et ny, qui represente la 
# longeur et la largeur et cree un tableau de 2 dimensions de longeur nx et de
# largeur ny numerotee de 0 a nx*ny-1.

def creerTab(nx,ny):
# Le code suivant est inspiree de la fonction creerMatrice de la page 28 du
# chapitre 8 du cours.
    tab = [None]*nx
    compteur = 0
# On cree les colonne et les range de notre tableau en 2 dimensions. On le
# rempli de 0 temporairement.
    for i in range(nx):
        tab[i] = [0]*(ny)
# On numerote chaque case de notre tableau de 0 a nx*ny-1.
    for m in range(ny):
        for i in range(nx):
            tab[i][m] = compteur
            compteur+=1
    return tab

# Fonction qui prend pour parametre 4 entier x et y les coordonnee un point
# dans un tableau et nx ny la longeur et la largeur de ce dernier et retourne 
# un tableau. Cette fonction a pour but de donner toute les cellules adjacentes
# a la cellule voulu.

def voisins(x,y,nx,ny):
# On cree un tableau qu'on numerote de taille nx*ny, pour nous aider a reperer
# les voisins d'une cellule
    banqueDeCellules = creerTab(nx,ny)
# Boucle tant que qui verifie si la cellule est dans le tableau
    while x <= nx-1 and y <= ny-1:
        tabVoisins=[]
# 4 enonce if qui on pour but d'eliminer des voisins qui sont hors des
# limites du tableau
        if y-1 >= 0:
            tabVoisins.append(banqueDeCellules[x][y-1])
        if x-1 >=0:
            tabVoisins.append(banqueDeCellules[x-1][y])
        if y+1 <= ny-1:
            tabVoisins.append(banqueDeCellules[x][y+1])
        if x+1 <= nx-1:
            tabVoisins.append(banqueDeCellules[x+1][y])
        return tabVoisins

    
    
# Fonction qui prend pour parametres 3 entier, nx ny la longeur et la largeur
# du labyrinthe, et la dimension de la fenetre ou est-ce qu'on va construire
# notre labyrinthe. Cette fonction cree la fenetre ou le labyrinthe va etre
#trace et elle etablit la couleure de fond de cette derniere.

def creerFenetre(nx,ny,dimension):
# on etablit les dimensions de la fenetre
    setScreenMode(nx*dimension+1,ny*dimension+1)
    couleurFond = '#FFF'
# on etablit la couleure de fond
    for x in range(nx*dimension):
        for y in range(ny*dimension):
                setPixel(x,y,couleurFond)

                
                
                
# Fonction qui prend pour parametres 3 entier, nx ny la longeur et la largeur
# du labyrinthe, et la dimension de la fenetre ou est-ce qu'on va construire
# notre labyrinthe. Cette fonction cree une grille qui sert de base pour la
# construction du labyrinthe

def creerGrille(nx,ny,dimension):
    couleurGrille = '#000'
# On trace les ligne horizontale et verticale de la grille
    for x in range(nx*dimension):
        for y in range(ny*dimension):
            if x % dimension == 0:
                setPixel(x,y,couleurGrille)
            elif y % dimension == 0:
                setPixel(x,y,couleurGrille) 

# Fonction qui prend pour parametres  3 entiers, le numero d'une cellule et
# nx et ny qui sont la longeur et la largeur de notre labyrinthe. Cette 
# fonction trouve la coordonnee x de la cellule qu'on recherche

def trouverCooX(cellule,nx,ny):
# On determine la valeur de la coordonne x de la cellule
    xCellule = cellule % nx
    return xCellule




# Fonction qui prend pour parametres  3 entiers, le numero d'une cellule et
# nx et ny qui sont la longeur et la largeur de notre labyrinthe. Cette 
# fonction trouve la coordonnee y de la cellule qu'on recherche.

def trouverCooY(cellule,nx,ny):
    xCellule = trouverCooX(cellule,nx,ny)
# Si la cellule est dans le premier rang alors sa coordonnee y = 0.
    if cellule < nx:
        yCellule = 0
# On determine la valeur de la coordonne y de la cellule avec l'aide de x.
    elif cellule >= nx:
        yCellule = int((cellule-xCellule)/nx)
    return yCellule



# Fonction qui prend pour parametres  4 entiers, le numero d'une cellule,
# nx et ny qui sont la longeur et la largeur de notre labyrinthe et la 
# dimension de la fenetre ou est-ce qu'on va construire notre labyrinthe. Cette
# fonction efface un mur horizontale dans la grille au coordonnee fournie.

def effacerMursHoriz(cellule,nx,ny,dimension):
# On determine les coordonnees x et y de la cellule.
    yCelluleHoriz = trouverCooY(cellule,nx,ny+1)
    xCelluleHoriz = trouverCooX(cellule,nx,ny+1)
    couleurMur = '#FFF'
# on efface le mur avec l'aide des coordonnes x et y.
    for i in range(1,dimension):
                setPixel((xCelluleHoriz*dimension)+i,
                         yCelluleHoriz*dimension,couleurMur)

            
            
# Fonction qui prend pour parametres  4 entiers, le numero d'une cellule,
# nx et ny qui sont la longeur et la largeur de notre labyrinthe et la 
# dimension de la fenetre ou est-ce qu'on va construire notre labyrinthe. Cette
# fonction efface un mur horizontale dans la grille au coordonnee fournie.            
            
def effacerMursVerti(cellule,nx,ny,dimension):
# On determine les coordonnees x et y de la cellule.
    yCelluleVerti = trouverCooY(cellule,nx+1,ny)
    xCelluleVerti = trouverCooX(cellule,nx+1,ny)
    couleurMur = '#FFF'
# on efface le mur avec l'aide des coordonnes x et y.
    for i in range(1,dimension):
                setPixel((xCelluleVerti)*dimension,
                         (yCelluleVerti*dimension)+i,couleurMur)

            

# Fonction qui prend pour parametres  4 entiers, le numero d'une cellule,
# nx et ny qui sont la longeur et la largeur de notre labyrinthe et la 
# dimension de la fenetre ou est-ce qu'on va construire notre labyrinth. Et 2
# tableau qui sont cave et front. Cette fonction efface les murs de la grille
# d'une tel facon qu'il y a toujours un seul chemin pour sortir du labyrinthe.

def algoEffacer(cellule,cave,front,nx,ny,dimension):
    xCellule = trouverCooX(cellule,nx,ny)
    yCellule = trouverCooY(cellule,nx,ny)
    voisinsCellule = voisins(xCellule,yCellule,nx,ny)
    valeurDeTrop = []
# Si front ne contient pas un element de voisinsCellule on l'ajoute.
    for i in range(len(voisinsCellule)):
        if contient(front,voisinsCellule[i]) == False:
            ajouter(front,voisinsCellule[i])
# Si front contient une valeure dans cave on la stocke dans un variable 
# temporaire valeurDeTrop.
    for i in range(len(front)):
        if contient(cave,front[i]):
            ajouter(valeurDeTrop,front[i])
# Si valeur de trop n'est pas vide et contient une valeure dans front on la
# retire
    if len(valeurDeTrop) > 0:     
        for i in range(len(valeurDeTrop)):
            retirer(front,valeurDeTrop[i])
# Si voisinsCellule contient une valeure dans cave, alors cette valeure est
# prise comme la valeurs d'on on va effacer un mur.Ceci est fait pour que tout
# les murs qu'on efface reste dans la cavite.
    for i in range(len(cave)):
        if contient(voisinsCellule,cave[i]):
            xCelluleCav = trouverCooX(cave[i],nx,ny)
            yCelluleCav = trouverCooY(cave[i],nx,ny)
            break
# On etablit les murs de chaque cote par rapport a notre cellule choisit.
    murNord = xCelluleCav + yCelluleCav * nx
    murEst = 1 + xCelluleCav + yCelluleCav * (nx+1)
    murOuest = xCelluleCav + yCelluleCav * (nx+1)
    murSud = xCelluleCav + (yCelluleCav+1) * nx
# serie d'enonce if pour determiner quel mur de la cellule il faut effacer. On
# verifie aussi qu'on efface pas les bordures.
    if xCelluleCav == xCellule and yCellule == yCelluleCav-1:
        if yCelluleCav >= 1 and murNord < nx*(ny+1):
            effacerMursHoriz(murNord,nx,ny,dimension)
    if xCelluleCav == xCellule-1 and yCellule == yCelluleCav:
        if murEst <= (nx+1)*ny and xCelluleCav <nx-1:
            effacerMursVerti(murEst,nx,ny,dimension)
    if xCelluleCav == xCellule and yCellule == yCelluleCav+1:
        if yCelluleCav < ny-1 and murSud <= nx*(ny+1):
            effacerMursHoriz(murSud,nx,ny,dimension)
    if xCelluleCav == xCellule+1 and yCellule == yCelluleCav:
        if 0 < xCelluleCav and murOuest < (nx+1)*ny:
            effacerMursVerti(murOuest,nx,ny,dimension)

            
# Fonction qui prend pour parametres 3 entier, nx ny la longeur et la largeur
# du labyrinthe, et la dimension de la fenetre ou est-ce qu'on va construire
# notre labyrinthe.Cette fonction cree l'algorithme qui permet de tracer le
# labyrinthe.

def algorithme(nx,ny,dimension):
    cave = []
    front = []
    banqueDeCellules = creerTab(nx,ny)
    repeter = True
# boucle qui s'arrete quand la cavite est pleine. 
    while len(cave) != nx*ny:
# boucle pour  la premiere iteration de l'algorithme, qui initialise les 
# variables necessaire pour continuer
        if repeter == True:
# on commence par une cellule au hasard.
            xCellule = math.floor(random()*nx)
            yCellule = math.floor(random()*ny)
            cellule = banqueDeCellules[xCellule][yCellule]
            ajouter(cave,cellule)
            retirer(banqueDeCellules,cellule)
            voisinsCellule = voisins(xCellule,yCellule,nx,ny)
            front = voisinsCellule
            repeter = False
# enoce qui represente toute les etapes sauf la derniere.
        if len(cave) < nx*ny-1:
# on choisit une cellule au hasard dans front.
            cellule = front[math.floor(random()*len(front))]
            ajouter(cave,cellule)
            retirer(front,cellule)
            algoEffacer(cellule,cave,front,nx,ny,dimension)
# enonce qui represente la derniere etape de l'algorithme, quand il ne reste
# qu'une seule valeure dans front
        if len(front) == 1:
# la cellule restante est le dernier voisin.
            cellule = front[0]
            xCellule = trouverCooX(cellule,nx,ny)
            yCellule = trouverCooY(cellule,nx,ny)
            algoEffacer(cellule,cave,front,nx,ny,dimension)
            ajouter(cave,front[0])
            retirer(front,front[0])



# Fonction qui prend pour parametres 3 entier, nx ny la longeur et la largeur
# du labyrinthe, et la dimension de la fenetre ou est-ce qu'on va construire
# notre labyrinthe. Cette fonction Trace les ouverture a chaque extremite du
# labyrinthe.

def creerOuvertures(nx,ny,dimension):
    couleurMur = '#FFF'
# boucle qui trace les extremite du labyrinthe
    for i in range(dimension):
        setPixel(0+i,0,couleurMur)
        setPixel((nx-1)*dimension+i,ny*dimension,couleurMur)
            

            
def laby(nx,ny,dimension):
    creerFenetre(nx,ny,dimension)
    creerGrille(nx,ny,dimension)
    algorithme(nx,ny,dimension)
    creerOuvertures(nx,ny,dimension)
       
    
            
def testSequence():
    assert sequence(5) == [0, 1, 2, 3, 4]
    assert sequence(0) == []
    assert sequence(-3) == []
    assert sequence(1000) == list(range(1000))            
        
def testContient():
    assert contient([1, 2, 3, 4, 5], 3) == True
    assert contient([1, 2, 3, 4, 5], 6) == False
    assert contient([], 1) == False
    assert contient([1, 2, 3, 4, 5], 5) == True
    assert contient([1, 2, 3, 4, 5], 0) == False    
    
def testAjouter():
    assert ajouter([1, 2, 3, 4, 5], 3) == [1, 2, 3, 4, 5]  
    assert ajouter([1, 2, 3, 4, 5], 6) == [1, 2, 3, 4, 5, 6] 
    assert ajouter([], 1) == [1]  
    assert ajouter([1, 2, 3, 4, 5], 5) == [1, 2, 3, 4, 5]  
    assert ajouter([1, 2, 3, 4, 5], 0) == [1, 2, 3, 4, 5, 0]        
        
def testCreerTab():
    assert creerTab(2, 3) == [[0, 1, 2], [3, 4, 5]] 
    assert creerTab(3, 2) == [[0, 1], [2, 3], [4, 5]]  
    assert creerTab(1, 1) == [[0]] 
    assert creerTab(0, 3) == []  
    assert creerTab(4, 0) == [[],[],[],[],[]]        
         
def testTrouverCooX():
    assert trouverCooX(0, 3, 2) == 0            # nx = 3, ny = 2
    assert trouverCooX(5, 3, 2) == 2            # nx = 3, ny = 2
    assert trouverCooX(8, 4, 3) == 0            # nx = 4, ny = 3
    assert trouverCooX(10, 4, 3) == 2           # nx = 4, ny = 3
    assert trouverCooX(15, 5, 4) == 0           # nx = 5, ny = 4        
        
def testRetirer():
    assert retirer([1, 2, 3, 4, 5], 3) == [1, 2, 4, 5]  
    assert retirer([1, 2, 3, 4, 5], 6) == [1, 2, 3, 4, 5]  
    assert retirer([], 1) == []
    assert retirer([1, 2, 3, 4, 5], 5) == [1, 2, 3, 4]  
    assert retirer([1, 2, 3, 4, 5], 0) == [1, 2, 3, 4, 5] 
    
def testTrouverCooY():
    assert trouverCooY(0, 3, 2) == 0   # nx = 3, ny = 2
    assert trouverCooY(5, 3, 2) == 1   # nx = 3, ny = 2
    assert trouverCooY(8, 4, 3) == 2   # nx = 4, ny = 3
    assert trouverCooY(10, 4, 3) == 2  # nx = 4, ny = 3
    assert trouverCooY(15, 5, 4) == 3  # nx = 5, ny = 4
    
testSequence()   
testContient()
testAjouter()
testRetirer()
testTrouverCooX()
testTrouverCooY()
            
     
            
            
        
        
        
        
        
    
    
     
        
        
    
   
    
    
        

        
    
    
    
    
    
       
        
    
    
    

        

