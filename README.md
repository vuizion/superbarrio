# Super Barrio

Super Barrio est un jeu vidéo en 2D développé avec **pygame** dans le cadre de notre projet de fin d'année en NSI.

🚀 **Contrôles :**  
- **Joueur 1** : Z (saut), Q (gauche), S (bas), D (droite), Espace (saut alternatif)  
- **Joueur 2** *(si activé)* : Flèche haut (saut), Flèche gauche (gauche), Flèche bas (bas), Flèche droite (droite), Majuscule droite (saut alternatif)  

---

## Installation 🔧

1. **Cloner le projet** :
   ```bash
   git clone https://github.com/vuizion/superbarrio.git
   cd superbarrio
   ```

2. **Installer les dépendances** :
   ```bash
   pip install pygame
   ```

3. **Lancer le jeu** :
   ```bash
   python main.py
   ```

---

## Mode multijoueur 🎮

Le jeu propose un mode **multijoueur**, désactivé par défaut.  
Pour activer le mode 2 joueurs, il suffit de modifier la variable `multiplayer` dans `main.py` :

```python
multiplayer = True  # Mettre False pour jouer en solo
```

---

## Note sur le développement ⚠️

Le développement du projet s'est arrêté plus tôt que prévu, ce qui explique un certain manque de difficulté.  
Par exemple, il est possible d'effectuer **trois sauts d'affilée**, ce qui n'était pas initialement prévu.  

Malgré ces limitations, nous espérons que Super Barrio vous amusera ! 🎉
