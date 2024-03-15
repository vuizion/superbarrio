import random
class Avocado:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y 
        self.vivant = True
        
    
       

    def deplacer(self, direction, plateau):
        # Vérifie si le AVOCADO est vivant avant de le déplacer
        if self.vivant == True:
            return
        # Génère une direction aléatoire : -1 pour gauche, 1 pour droite
        direction = random.choice([-1, 1])
        # Calcule la nouvelle position en se déplaçant de 5 cases
        nouvelle_position = self.x + (direction * 5)

        # Vérifie les limites du plateau pour s'assurer que le AVOCADO reste dans le jeu
        nouvelle_position = max(0, nouvelle_position)  # Pas moins que 0
        nouvelle_position = min(nouvelle_position, len(plateau[0]) - 1)  # Pas plus que la largeur du plateau

        # Met à jour la position du AVOCADO
        self.x = nouvelle_position
        plateau[self.y][self.x] = 'avocat'






    


      









        







def ecraser(self) :
    
        self.vivant = False







    

