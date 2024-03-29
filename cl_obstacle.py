from random import randint

# Exemple de map :
    # 0 : case vide
    # 0.1 : spawn du joueur 1
    # 0.2 : spawn du joueur 2
    # 0.3 : point de respawn pendant le parcours
    # 1 : Élémént sol (1x2)
    # 1.1 : Élément sol plus grand (2x2)
    # 2 : Bloc solide
    # 2.2 : Mur de 2 blocs de hauteur
    # 2.3 : Mur de 3 blocs de hauteur
    # 2.4 : Mur de 4 blocs de hauteur
    # 3 : Plateforme d'un bloc de large
    # 4 : Élément décoratif : cactus
    # 4.1 : Déco : rocher
    # 4.2 : Déco : baril

class obstacle:
    def __init__(self) -> None:
        pass

    def randomChoice(self, difficultyMax:int=1) :
        l = self.difficulty_1()
        return l[randint(0,len(l)-1)]

    def difficulty_1(self) -> list:
        obs = []

        # Obstacle N°1
        obs.append([
            [0, 0, 0, 0, 0, 0, 0, 1.1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1.1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1.1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ])

        # Obstacle N°2
        obs.append([
            [0, 0, 0, 0, 0, 0, 0, 1.1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 1],
            [0, 0, 0, 0, 0, 1.1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 3, 0, 0, 0, 0],
            [0, 0, 0, 0, 3, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1.1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 1.1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ])

        # Obstacle N°3
        obs.append([
            [0, 0, 0, 0, 0, 0, 0, 1.1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 4.1, 1.1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1.1, 0],
            [0, 0, 0, 0, 0, 9, 4, 0, 0],
            [0, 0, 0, 0, 0, 9, 4, 1.1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1.1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ])

        return obs
