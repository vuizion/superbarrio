# -*- coding: utf-8 -*-
class Rectangle() :
    """
    Définition d'une classe représentant des rectangles
    """
    def __init__(self,x,y,longueur,hauteur) :
        """
        Le constructeur

        Parameters
        ----------
        x : float
            abscisse du coin supérieur gauche.
        y : float
            ordonnée du coin supérieure gauche.
        longueur : int >= 0
            longueur du rectangle.
        hauteur : int >= 0
            hauteur du rectangle.

        Returns
        -------
        Une instance de Rectangle.

        """

        self.x = float(x)
        self.y = float(y)

        if longueur > 0:
            self.longueur = int(longueur)
        else: self.longueur = 0
        
        if hauteur > 0:
            self.hauteur = int(hauteur)
        else: self.hauteur = 0


    def donne_x(self) :
        """
        Donne l'attribut x de l'instance

        Returns
        -------
        x de l'instance.

        """

        return self.x

    def donne_y(self) :
        """
        Donne l'attribut y de l'instance

        Returns
        -------
        y de l'instance.

        """
        
        return self.y

    def donne_longueur(self) :
        """
        Donne la longueur de l'instance

        Returns
        -------
        La longueur de l'instance.

        """

        return self.longueur

    def donne_hauteur(self) :
        """
        Donne la hauteur de l'isntance

        Returns
        -------
        La hauteur de l'instance.

        """

        return self.hauteur

    def change_x(self,x) :
        """
        change x

        Parameters
        ----------
        x : float
            valeur à ajouter.

        Returns
        -------
        None.

        """
        self.x = float(x)

    def change_y(self,y) :
        """
        change y

        Parameters
        ----------
        y : float
            valeur à ajouter.

        Returns
        -------
        None.

        """

        self.y = float(y)

    def ajoute_x(self,dx) :
        """
        Ajoute dx à l'attribut x de l'instance

        Parameters
        ----------
        dx : float
            valeur à ajouter.

        Returns
        -------
        None.

        """

        self.x += float(x)

    def ajoute_y(self,dy) :
        """
        Ajoute dy à l'attribut y de l'instance

        Parameters
        ----------
        dy : float
            valeur à ajouter.

        Returns
        -------
        None.

        """

        self.y += float(y)

    def verifie_colision(self,rectangle,dx = 0,dy = 0) :
        """
        Test si le rectangle croisse une autre instance de rectangle

        Parameters
        ----------
        rectangle : Rectangle
            instance d'un rectangle, on veut savoir si il y a contact.'

        dx : float
            ajout eventuel d'une valeur en abscisse.
        dy : float
            ajout eventuelle d'une valeur en ordonnee

        Returns
        -------
        Bool True si il y a intersection et false sinon.

        """
        A1 = (self.x, self.y)
        A2 = (self.x + self.longueur, self.y)
        A3 = (self.x + self.longueur, self.y + self.hauteur)
        A4 = (self.x, self.y + self.hauteur)

        B1 = (rectangle.donne_x(), rectangle.donne_y())
        B2 = (rectangle.donne_x() + rectangle.donne_longueur(), rectangle.donne_y())
        B3 = (rectangle.donne_x() + rectangle.donne_longueur(), rectangle.donne_y() + rectangle.donne_hauteur())
        B4 = (rectangle.donne_x(), rectangle.donne_y() + rectangle.donne_hauteur())

def test_verifie_colision() :
    r1 = Rectangle(0,100,200,100)
    r2 = Rectangle(50,20,50,20)
    r3 = Rectangle(50,20,200,100)
    r4 = Rectangle(0,300,200,100)
    r5 = Rectangle(300,100,200,100)

    assert r1.verifie_colision(r2) == False
    assert r2.verifie_colision(r1) == False
    assert r1.verifie_colision(r3) == True
    assert r3.verifie_colision(r1) == True
    assert r1.verifie_colision(r4) == False
    assert r4.verifie_colision(r1) == False
    assert r1.verifie_colision(r5) == False
    assert r5.verifie_colision(r1) == False