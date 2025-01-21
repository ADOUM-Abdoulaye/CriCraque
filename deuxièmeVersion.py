import pygame

pygame.init()

# Constantes
SCREENWIDTH = 844
SCREENHEIGHT = 597
FPS = 60

# Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Positions possibles
Postion = [
    (90, 125), (400, 125), (695, 125),
    (90, 305), (400, 305), (695, 305),
    (90, 480), (400, 480), (695, 480)
]

# Initialisation de la fenêtre
window = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption("Cricraque")

# Chargement des ressources
images = {
    "background": pygame.image.load("images/Arriere_plan.png"),
    "Balle_a": pygame.image.load("images/Balle_a.png"),
    "Balle_b": pygame.image.load("images/Balle_b.png"),
    "Balle_c": pygame.image.load("images/Balle_c.png"),
    "Balle_d": pygame.image.load("images/Balle_d.png"),
    "Balle_e": pygame.image.load("images/Balle_e.png"),
    "Ball_f": pygame.image.load("images/Ball_f.png")
}

sounds = {
    "goal": pygame.mixer.Sound("sounds/goal.mp3")
}

# Polices
font = pygame.font.Font(None, 100)

# Rectangles des balles
balle_rects = {
    "Balle_a": images["Balle_a"].get_rect(center=(SCREENWIDTH/2 - 370, SCREENHEIGHT/2 - 60)),
    "Balle_b": images["Balle_b"].get_rect(center=(SCREENWIDTH/2 - 370, SCREENHEIGHT/2 + 30)),
    "Balle_c": images["Balle_c"].get_rect(center=(SCREENWIDTH/2 - 370, SCREENHEIGHT/2 + 120)),
    "Balle_d": images["Balle_d"].get_rect(center=(SCREENWIDTH/2 + 370, SCREENHEIGHT/2 - 60)),
    "Balle_e": images["Balle_e"].get_rect(center=(SCREENWIDTH/2 + 370, SCREENHEIGHT/2 + 30)),
    "Ball_f": images["Ball_f"].get_rect(center=(SCREENWIDTH/2 + 370, SCREENHEIGHT/2 + 120))
}

# Variables de jeu
joueur_actif = 1
score = {1: 0, 2: 0}
clock = pygame.time.Clock()
game_running = True

def reset_positions():
    """Réinitialise les positions des balles."""
    balle_rects["Balle_a"].center = (SCREENWIDTH/2 - 370, SCREENHEIGHT/2 - 60)
    balle_rects["Balle_b"].center = (SCREENWIDTH/2 - 370, SCREENHEIGHT/2 + 30)
    balle_rects["Balle_c"].center = (SCREENWIDTH/2 - 370, SCREENHEIGHT/2 + 120)
    balle_rects["Balle_d"].center = (SCREENWIDTH/2 + 370, SCREENHEIGHT/2 - 60)
    balle_rects["Balle_e"].center = (SCREENWIDTH/2 + 370, SCREENHEIGHT/2 + 30)
    balle_rects["Ball_f"].center = (SCREENWIDTH/2 + 370, SCREENHEIGHT/2 + 120)

def check_score():
    """Vérifie si un joueur a marqué et met à jour les scores."""
    global joueur_actif
    if balle_rects["Balle_a"].center == Postion[0] and balle_rects["Balle_b"].center == Postion[1] and balle_rects["Balle_c"].center == Postion[2]:
        score[1] += 1
        sounds["goal"].play()
        reset_positions()
        joueur_actif = 2
    elif balle_rects["Balle_d"].center == Postion[0] and balle_rects["Balle_e"].center == Postion[1] and balle_rects["Ball_f"].center == Postion[2]:
        score[2] += 1
        sounds["goal"].play()
        reset_positions()
        joueur_actif = 1

def handle_input():
    """Gère les entrées utilisateur en fonction du joueur actif."""
    keys = pygame.key.get_pressed()
    active_keys = {
        1: {"A": "Balle_a", "B": "Balle_b", "C": "Balle_c"},
        2: {"D": "Balle_d", "E": "Balle_e", "F": "Ball_f"}
    }
    current_keys = active_keys[joueur_actif]
    for key, ball in current_keys.items():
        for i, position in enumerate(Postion, start=1):
            if keys[getattr(pygame, f"K_{i}")] and keys[getattr(pygame, f"K_{key.lower()}")]:
                balle_rects[ball].center = position

# Boucle principale du jeu
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    # Gérer les entrées
    handle_input()

    # Mettre à jour le score
    check_score()

    # Dessiner l'écran
    window.blit(images["background"], (0, 0))
    for ball, rect in balle_rects.items():
        window.blit(images[ball], rect)

    # Afficher les scores et le joueur actif
    score_text_1 = font.render(f"Joueur 1: {score[1]}", True, WHITE)
    score_text_2 = font.render(f"Joueur 2: {score[2]}", True, WHITE)
    player_text = font.render(f"Tour: Joueur {joueur_actif}", True, WHITE)

    window.blit(score_text_1, (50, 50))
    window.blit(score_text_2, (SCREENWIDTH - 300, 50))
    window.blit(player_text, (SCREENWIDTH/2 - 150, 10))

    # Rafraîchir l'écran
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()