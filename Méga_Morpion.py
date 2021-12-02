from tkinter import *#On importe le module Tkinter, utilisé tout au long du programme
import webbrowser
from random import randint

def menu():
    global fen1
    fen1 = Tk()
    fen1.title('Projet ISN')

    label=Label(fen1,text="Bienvenue sur le projet d'ISN de terminale de"+'\n'+"Florence Danan, David Goblot et Clément Dauvois !",font=('Arial',16,'bold'))
    label.pack(side=TOP,padx=15,pady=15)#On crée une étiquette (un texte) de presentation

    bou1 = Button(fen1,text='Règles',font=('Arial',15,'normal'),padx=65,pady=5,command=regle)
    bou1.pack(side=LEFT,padx=5,pady=4)#On crée un bouton pour afficher les règles

    bou2 = Button(fen1,text='Joueur VS Joueur',font=('Arial',15,'normal'),padx=25,pady=5,command=debut_jeu)
    bou2.pack(side=LEFT,padx=5,pady=4)#On crée un bouton pour lancer une partie Joueur contre Joueur

    bou3 = Button(fen1,text='Joueur VS Ordinateur',font=('Arial',15,'normal'),padx=10,pady=5,command=debut_jeu_ordi)
    bou3.pack(side=LEFT,padx=5,pady=4)
    

def regle():
    webbrowser.open_new(r"https://docs.google.com/document/d/1abnEAK6QaIkvd2Q7Xer-49_Y94nfqv56sc-CjpgoWsU/edit?usp=sharing")#On affiche une page web avec les règles

def debut_jeu():
    fen1.destroy()
    terrain_m()
    global tour
    tour = 0
    global symbole
    symbole=[["*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*"],
             ["*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*"],
             ["*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*"]]

    #Variable regardant le symbole sur chaque case sous forme de liste afin d'être maniable plus facilement
    global terr_cible
    terr_cible=9 #Si le terrain cible est 9, alors touts les terrains sont utilisables (ils vont de 0 à 8)
    global partie_ordi
    partie_ordi="non"

def debut_jeu_ordi():
    fen1.destroy()
    terrain_m()
    global tour
    tour = 0
    global symbole
    symbole=[["*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*"],
             ["*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*"],
             ["*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*"],["*","*","*","*","*","*","*","*","*"]]
    #Variable regardant le symbole sur chaque case sous forme de liste afin d'être maniable plus facilement
    global terr_cible
    terr_cible=9 #Si le terrain cible est 9, alors touts les terrains sont utilisables (ils vont de 0 à 8)
    global partie_ordi
    partie_ordi="oui"
    global can1
    can1.config(cursor="X_cursor")
    global vic
    vic=0
    

def terrain_m():#Fonction créant le grand terrain de morpion
    global fen2
    fen2=Tk()
    fen2.title('Méga-Morpion')#On crée une fenétre qu'on nomme Méga-morpion
    global can1
    can1 = Canvas(fen2,bg='#CACACA',height=600,width=600,cursor="circle")
    can1.focus_set()
    can1.bind('<Button-1>',clique)
    can1.pack()#On crée un canevas appelant la fonction 'clique' lors du clique gauche de la souris
    can1.create_line(200,10,200,590,width=7,fill='#FE4E50')
    can1.create_line(400,10,400,590,width=7,fill='#FE4E50')
    can1.create_line(10,200,590,200,width=7,fill='#FE4E50')
    can1.create_line(10,400,590,400,width=7,fill='#FE4E50')#On crée les 4 grandes lignes rouges
    terrain_mega_m()



def terrain_mega_m():#Fonction créant le terrain du méga morpion
    x1=70
    x2=10
    for i in list(range(3)):
        y1=10
        y2=70
        for i in list(range(3)):
            coord_mega_m(x1,y1,x2,y2,'black')
            y1=y1+200
            y2=y2+200
        x1=x1+200
        x2=x2+200
        

def coord_mega_m(x1,y1,x2,y2,coul):#Fonction créant un petit terrain de morpion à partir de 2 points
    can1.create_line(x1,y1,x1,y1+180,width=3,fill=coul)
    can1.create_line(x1+60,y1,x1+60,y1+180,width=3,fill=coul)
    can1.create_line(x2,y2,x2+180,y2,width=3,fill=coul)
    can1.create_line(x2,y2+60,x2+180,y2+60,width=3,fill=coul)


def clique(event):#Fonction détectant sur quelle petit terrain l'utilisateur a cliqué, appelé lors d'un clique gauche
    global x1,y1,x2,y2
    global n_terr
    if event.y>=10 and event.y<=190:#On verifie d'abord la ligne
        if event.x>=10 and event.x<=190:#Puis la colonne
            x1,y1,x2,y2=20,20,60,60
            n_terr=0#Le numéro du terrain est enregistré
            p_terr(event,10,10)#On lance la fonction suivante
        if event.x>=210 and event.x<=390:
            x1,y1,x2,y2=220,20,260,60
            n_terr=1
            p_terr(event,210,10)
        if event.x>=410 and event.x<=590:
            x1,y1,x2,y2=420,20,460,60
            n_terr=2
            p_terr(event,410,10)
    if event.y>=210 and event.y<=390:
        if event.x>=10 and event.x<=190:
            x1,y1,x2,y2=20,220,60,260
            n_terr=3
            p_terr(event,10,210)
        if event.x>=210 and event.x<=390:
            x1,y1,x2,y2=220,220,260,260
            n_terr=4
            p_terr(event,210,210)
        if event.x>=410 and event.x<=590:
            x1,y1,x2,y2=420,220,460,260
            n_terr=5
            p_terr(event,410,210)
    if event.y>=410 and event.y<=590:
        if event.x>=10 and event.x<=190:
            x1,y1,x2,y2=20,420,60,460
            n_terr=6
            p_terr(event,10,410)
        if event.x>=210 and event.x<=390:
            x1,y1,x2,y2=220,420,260,460
            n_terr=7
            p_terr(event,210,410)
        if event.x>=410 and event.x<=590:
            x1,y1,x2,y2=420,420,460,460
            n_terr=8
            p_terr(event,410,410)
            

def p_terr(event,a,b):#Fonction détéctant sur quelle case du petit terrain l'utilisateur a cliqué
    if terr_cible==9 or terr_cible==n_terr:#Le terrain doit être celui déigné par le joueur précédent
        if event.y>=b and event.y<=b+55:#On verifie d'abord la ligne
            if event.x>=a and event.x<=a+55:#Puis la colonne
                case(0)#On lance la fonction suivante
            if event.x>=a+65 and event.x<=a+115:
                case(1)
            if event.x>=a+125 and event.x<=a+175:
                case(2)
        if event.y>=b+65 and event.y<=b+115:
            if event.x>=a and event.x<=a+55:
                case(3)
            if event.x>=a+65 and event.x<=a+115:
                case(4)
            if event.x>=a+125 and event.x<=a+175:
                case(5)
        if event.y>=b+125 and event.y<=b+175:
            if event.x>=a and event.x<=a+55:
                case(6)
            if event.x>=a+65 and event.x<=a+115:
                case(7)
            if event.x>=a+125 and event.x<=a+175:
                case(8)
           


def case(n_case):#Fonction mettant un symbole dans la case cliqué
    global terr_cible
    global can1
    global symbole
    global tour
    if partie_ordi=="non":
        if symbole[n_terr][n_case]=="*":#La case doit être libre
            terrain_mega_m()
            if tour%2 == 0:#On voit quel joueur joue
                if n_case == 0:#On crée le symbole en fonction de la case et du joueur
                    can1.create_oval(x1,y1,x2,y2,outline='blue',width=5)
                    coord_mega_m(70,10,10,70,'green')#On change la couleur du terrain ciblé
                if n_case == 1:
                    can1.create_oval(x1+60,y1,x2+60,y2,outline='blue',width=5)
                    coord_mega_m(270,10,210,70,'green')
                if n_case == 2:
                    can1.create_oval(x1+120,y1,x2+120,y2,outline='blue',width=5)
                    coord_mega_m(470,10,410,70,'green')
                if n_case == 3:
                    can1.create_oval(x1,y1+60,x2,y2+60,outline='blue',width=5)
                    coord_mega_m(70,210,10,270,'green')
                if n_case == 4:
                    can1.create_oval(x1+60,y1+60,x2+60,y2+60,outline='blue',width=5)
                    coord_mega_m(270,210,210,270,'green')
                if n_case == 5:
                    can1.create_oval(x1+120,y1+60,x2+120,y2+60,outline='blue',width=5)
                    coord_mega_m(470,210,410,270,'green')
                if n_case == 6:
                    can1.create_oval(x1,y1+120,x2,y2+120,outline='blue',width=5)
                    coord_mega_m(70,410,10,470,'green')
                if n_case == 7:
                    can1.create_oval(x1+60,y1+120,x2+60,y2+120,outline='blue',width=5)
                    coord_mega_m(270,410,210,470,'green')
                if n_case == 8:
                    can1.create_oval(x1+120,y1+120,x2+120,y2+120,outline='blue',width=5)
                    coord_mega_m(470,410,410,470,'green')
                symbole[n_terr][n_case]="O"#On change dans la liste l'étoile par le symbole du joueur
                can1.config(cursor="X_cursor")#on change le curseur
            else:
                if n_case == 0:
                    can1.create_line(x1,y1,x2,y2,fill='red',width=5,capstyle='round')
                    can1.create_line(x1,y1+40,x2,y2-40,fill='red',width=5,capstyle='round')
                    coord_mega_m(70,10,10,70,'green')
                if n_case == 1:
                    can1.create_line(x1+60,y1,x2+60,y2,fill='red',width=5,capstyle='round')
                    can1.create_line(x1+60,y1+40,x2+60,y2-40,fill='red',width=5,capstyle='round')
                    coord_mega_m(270,10,210,70,'green')
                if n_case == 2:
                    can1.create_line(x1+120,y1,x2+120,y2,fill='red',width=5,capstyle='round')
                    can1.create_line(x1+120,y1+40,x2+120,y2-40,fill='red',width=5,capstyle='round')
                    coord_mega_m(470,10,410,70,'green')
                if n_case == 3:
                    can1.create_line(x1,y1+60,x2,y2+60,fill='red',width=5,capstyle='round')
                    can1.create_line(x1,y1+100,x2,y2+20,fill='red',width=5,capstyle='round')
                    coord_mega_m(70,210,10,270,'green')
                if n_case == 4:
                    can1.create_line(x1+60,y1+60,x2+60,y2+60,fill='red',width=5,capstyle='round')
                    can1.create_line(x1+60,y1+100,x2+60,y2+20,fill='red',width=5,capstyle='round')
                    coord_mega_m(270,210,210,270,'green')
                if n_case == 5:
                    can1.create_line(x1+120,y1+60,x2+120,y2+60,fill='red',width=5,capstyle='round')
                    can1.create_line(x1+120,y1+100,x2+120,y2+20,fill='red',width=5,capstyle='round')
                    coord_mega_m(470,210,410,270,'green')
                if n_case == 6:
                    can1.create_line(x1,y1+120,x2,y2+120,fill='red',width=5,capstyle='round')
                    can1.create_line(x1,y1+160,x2,y2+80,fill='red',width=5,capstyle='round')
                    coord_mega_m(70,410,10,470,'green')
                if n_case == 7:
                    can1.create_line(x1+60,y1+120,x2+60,y2+120,fill='red',width=5,capstyle='round')
                    can1.create_line(x1+60,y1+160,x2+60,y2+80,fill='red',width=5,capstyle='round')
                    coord_mega_m(270,410,210,470,'green')
                if n_case == 8:
                    can1.create_line(x1+120,y1+120,x2+120,y2+120,fill='red',width=5,capstyle='round')
                    can1.create_line(x1+120,y1+160,x2+120,y2+80,fill='red',width=5,capstyle='round')
                    coord_mega_m(470,410,410,470,'green')
                symbole[n_terr][n_case]="X"
                can1.config(cursor="circle")
            terr_cible=n_case#On définit le terrain où le joueur prochain devra jouer
            complet()#On voit si le terrain est complet
            if symbole[terr_cible]=="terr_complet_O" or symbole[terr_cible]=="terr_complet_X" or symbole[terr_cible]=="Egalité":
                terr_cible=9#Si le terrain cible est complet, le joueur suivant peut jouer partout
                terrain_mega_m()
            tour=tour+1#On change de joueur
            victoire_test()#On voit si un joueur a gagner
    else:
        if symbole[n_terr][n_case]=="*":
            terrain_mega_m()
            if n_case == 0:
                can1.create_line(x1,y1,x2,y2,fill='red',width=5,capstyle='round')
                can1.create_line(x1,y1+40,x2,y2-40,fill='red',width=5,capstyle='round')
            if n_case == 1:
                can1.create_line(x1+60,y1,x2+60,y2,fill='red',width=5,capstyle='round')
                can1.create_line(x1+60,y1+40,x2+60,y2-40,fill='red',width=5,capstyle='round')
            if n_case == 2:
                can1.create_line(x1+120,y1,x2+120,y2,fill='red',width=5,capstyle='round')
                can1.create_line(x1+120,y1+40,x2+120,y2-40,fill='red',width=5,capstyle='round')
            if n_case == 3:
                can1.create_line(x1,y1+60,x2,y2+60,fill='red',width=5,capstyle='round')
                can1.create_line(x1,y1+100,x2,y2+20,fill='red',width=5,capstyle='round')
            if n_case == 4:
                can1.create_line(x1+60,y1+60,x2+60,y2+60,fill='red',width=5,capstyle='round')
                can1.create_line(x1+60,y1+100,x2+60,y2+20,fill='red',width=5,capstyle='round')
            if n_case == 5:
                can1.create_line(x1+120,y1+60,x2+120,y2+60,fill='red',width=5,capstyle='round')
                can1.create_line(x1+120,y1+100,x2+120,y2+20,fill='red',width=5,capstyle='round')
            if n_case == 6:
                can1.create_line(x1,y1+120,x2,y2+120,fill='red',width=5,capstyle='round')
                can1.create_line(x1,y1+160,x2,y2+80,fill='red',width=5,capstyle='round')
            if n_case == 7:
                can1.create_line(x1+60,y1+120,x2+60,y2+120,fill='red',width=5,capstyle='round')
                can1.create_line(x1+60,y1+160,x2+60,y2+80,fill='red',width=5,capstyle='round')
            if n_case == 8:
                can1.create_line(x1+120,y1+120,x2+120,y2+120,fill='red',width=5,capstyle='round')
                can1.create_line(x1+120,y1+160,x2+120,y2+80,fill='red',width=5,capstyle='round')
            terr_cible=n_case
            symbole[n_terr][n_case]="X"
            complet()#On voit si le terrain est complet
            if symbole[terr_cible]=="terr_complet_O" or symbole[terr_cible]=="terr_complet_X" or symbole[terr_cible]=="Egalité":
                terr_cible=9#Si le terrain cible est complet, l'ordinateur peut jouer partout
                terrain_mega_m()
            victoire_test()#On voit si le joueur a gagner
            coord_ordi()
        
    

def coord_ordi():
    global x1,y1,x2,y2
    global terr_cible
    if terr_cible==9:
        terr_cible=randint(0,8)
    while symbole[terr_cible]=="terr_complet_O" or symbole[terr_cible]=="terr_complet_X" or symbole[terr_cible]=="Egalité":
        terr_cible=randint(0,8)
    if terr_cible==0:
        x1,y1,x2,y2=20,20,60,60
    if terr_cible==1:
        x1,y1,x2,y2=220,20,260,60
    if terr_cible==2:
        x1,y1,x2,y2=420,20,460,60
    if terr_cible==3:
        x1,y1,x2,y2=20,220,60,260
    if terr_cible==4:
        x1,y1,x2,y2=220,220,260,260
    if terr_cible==5:
        x1,y1,x2,y2=420,220,460,260
    if terr_cible==6:
        x1,y1,x2,y2=20,420,60,460
    if terr_cible==7:
        x1,y1,x2,y2=220,420,260,460
    if terr_cible==8:
        x1,y1,x2,y2=420,420,460,460
    case_ordi(randint(0,8))
        
    
def case_ordi(o_case):
    global terr_cible
    global canl
    global symbole
    global tour
    global n_terr
    n_terr=terr_cible
    if vic==0:
        while symbole[terr_cible][o_case]!="*":
            o_case=randint(0,8)
        if o_case == 0:
            can1.create_oval(x1,y1,x2,y2,outline='blue',width=5)#On crée le symbole en fonction de la case et du joueur
            coord_mega_m(70,10,10,70,'green')#On change la couleur du terrain ciblé
        if o_case == 1:
            can1.create_oval(x1+60,y1,x2+60,y2,outline='blue',width=5)
            coord_mega_m(270,10,210,70,'green')
        if o_case == 2:
            can1.create_oval(x1+120,y1,x2+120,y2,outline='blue',width=5)
            coord_mega_m(470,10,410,70,'green')
        if o_case == 3:
            can1.create_oval(x1,y1+60,x2,y2+60,outline='blue',width=5)
            coord_mega_m(70,210,10,270,'green')
        if o_case == 4:
            can1.create_oval(x1+60,y1+60,x2+60,y2+60,outline='blue',width=5)
            coord_mega_m(270,210,210,270,'green')
        if o_case == 5:
            can1.create_oval(x1+120,y1+60,x2+120,y2+60,outline='blue',width=5)
            coord_mega_m(470,210,410,270,'green')
        if o_case == 6:
            can1.create_oval(x1,y1+120,x2,y2+120,outline='blue',width=5)
            coord_mega_m(70,410,10,470,'green')
        if o_case == 7:
            can1.create_oval(x1+60,y1+120,x2+60,y2+120,outline='blue',width=5)
            coord_mega_m(270,410,210,470,'green')
        if o_case == 8:
            can1.create_oval(x1+120,y1+120,x2+120,y2+120,outline='blue',width=5)
            coord_mega_m(470,410,410,470,'green')
        symbole[terr_cible][o_case]="O"
        terr_cible=o_case#On définit le terrain où le joueur humain devra jouer
        complet()#On voit si le terrain est complet
        if symbole[terr_cible]=="terr_complet_O" or symbole[terr_cible]=="terr_complet_X" or symbole[terr_cible]=="Egalité":
            terr_cible=9#Si le terrain cible est complet, le joueur suivant peut jouer partout
            terrain_mega_m()
        victoire_test()#On voit si un joueur a gagner

def complet():#On voit si le terrain est complet
    global symbole
    if symbole[n_terr][0]==symbole[n_terr][1]==symbole[n_terr][2] and symbole[n_terr][0] !="*":#On teste toutes les possibilitées qu'un terrain soit complet
        symbole[n_terr]="terr_complet_"+symbole[n_terr][0]#On change dans la liste pour indiquer que le terrain est complet et on précise le symbole
        grand_symb()#On place un grand symbole
    elif symbole[n_terr][3]==symbole[n_terr][4]==symbole[n_terr][5] and symbole[n_terr][3] !="*":
        symbole[n_terr]="terr_complet_"+symbole[n_terr][3]
        grand_symb()
    elif symbole[n_terr][6]==symbole[n_terr][7]==symbole[n_terr][8] and symbole[n_terr][6] !="*":
        symbole[n_terr]="terr_complet_"+symbole[n_terr][6]
        grand_symb()
    elif symbole[n_terr][0]==symbole[n_terr][3]==symbole[n_terr][6] and symbole[n_terr][0] !="*":
        symbole[n_terr]="terr_complet_"+symbole[n_terr][0]
        grand_symb()
    elif symbole[n_terr][1]==symbole[n_terr][4]==symbole[n_terr][7] and symbole[n_terr][1] !="*":
        symbole[n_terr]="terr_complet_"+symbole[n_terr][1]
        grand_symb()
    elif symbole[n_terr][2]==symbole[n_terr][5]==symbole[n_terr][8] and symbole[n_terr][2] !="*":
        symbole[n_terr]="terr_complet_"+symbole[n_terr][2]
        grand_symb()
    elif symbole[n_terr][0]==symbole[n_terr][4]==symbole[n_terr][8] and symbole[n_terr][0] !="*":
        symbole[n_terr]="terr_complet_"+symbole[n_terr][0]
        grand_symb()
    elif symbole[n_terr][2]==symbole[n_terr][4]==symbole[n_terr][6] and symbole[n_terr][2] !="*":
        symbole[n_terr]="terr_complet_"+symbole[n_terr][2]
        grand_symb()
    elif symbole[n_terr].count('*')==0:#On verifie si il y a une égalité sur le terrain 
        symbole[n_terr]='Egalité'
        
    
def grand_symb():#Fonction plaçant le grand symbole correspondant
    if symbole[n_terr]=="terr_complet_O":
        can1.create_oval(x1,y1,x2+120,y2+120,outline='blue',width=15)
    if symbole[n_terr]=="terr_complet_X":
        can1.create_line(x1,y1,x2+120,y2+120,fill='red',width=15,capstyle='round')
        can1.create_line(x1,y1+160,x2+120,y2-40,fill='red',width=15,capstyle='round')
        

def victoire_test():#Fonction regardant si un joueur a gagné
    global fen2
    if symbole[0]==symbole[1]==symbole[2] and symbole[1][0] =="t":#Même principe qu'avec la fonction complet()
        victoire()#On lance la victoire
    elif symbole[3]==symbole[4]==symbole[5] and symbole[3][0] =="t":#On utilise "elife" car la dernière condition ne doit être appliqué que si aucune autre ne l'est
        victoire()
    elif symbole[6]==symbole[7]==symbole[8] and symbole[6][0] =="t":
        victoire()
    elif symbole[0]==symbole[3]==symbole[6] and symbole[3][0] =="t":
        victoire()
    elif symbole[1]==symbole[4]==symbole[7] and symbole[1][0] =="t":
        victoire()
    elif symbole[2]==symbole[5]==symbole[8] and symbole[2][0] =="t":
        victoire()
    elif symbole[0]==symbole[4]==symbole[8] and symbole[4][0] =="t":
        victoire()
    elif symbole[2]==symbole[4]==symbole[6] and symbole[2][0] =="t":
        victoire()
    elif symbole.count('terr_complet_O')+symbole.count('terr_complet_X')+symbole.count('Egalité')==9:
        égalité()
         

def victoire():#Fonction lancée si un joueur a gagner
    global vic
    vic=1
    fen2.destroy()#On détruit la fenètre du méga-morpion
    global fen3
    fen3=Tk()#On crée une nouvelle fenètre qu'on nomme victoire
    fen3.title('Victoire')
    msg=Label(fen3,text="Victoire des "+symbole[n_terr][13]+" ! Félicitations !",font=('Arial',60,'bold'),fg='red',padx=10,pady=10)
    msg.pack()#On affiche un texte désignant le vainqueur
    menu = Button(fen3,text='Revenir au menu principal',font=('Arial',15,'normal'),padx=5,pady=5,command=re)
    menu.pack(padx=5,pady=10)#On affiche un bouton pour revenir au menu du début
    

def re():
    fen3.destroy()
    menu()


def égalité():
    fen2.destroy()#On détruit la fenètre du méga-morpion
    global fen3
    fen3=Tk()#On crée une nouvelle fenètre qu'on nomme victoire
    fen3.title('Egalité')
    msg=Label(fen3,text="Egalité ! C'est balo !",font=('Arial',60,'bold'),fg='red',padx=10,pady=10)
    msg.pack()#On affiche un texte désignant le vainqueur
    menu = Button(fen3,text='Revenir au menu principal',font=('Arial',15,'normal'),padx=5,pady=5,command=re)
    menu.pack(padx=5,pady=10)#On affiche un bouton pour revenir au menu du début

menu()
