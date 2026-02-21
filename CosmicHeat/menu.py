import os
import sys
import random
import pygame
from .classes.constants import WIDTH, HEIGHT, BLACK, WHITE, RED

BASE_DIR = os.path.dirname(__file__)


def animate_screen(screen, mainmenu_img):
    for _ in range(20):
        screen.blit(mainmenu_img, (0, 0))
        pygame.display.flip()
        pygame.time.wait(10)
        screen.blit(mainmenu_img, (random.randint(-5, 5), random.randint(-5, 5)))
        pygame.display.flip()
        pygame.time.wait(10)


def show_menu():
    pygame.init()
    pygame.mixer.init()

    music_path = os.path.join(BASE_DIR, "game_sounds", "menu.mp3")
    pygame.mixer.music.load(music_path)
    pygame.mixer.music.set_volume(0.25)
    pygame.mixer.music.play(-1)

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Main Menu")
    clock = pygame.time.Clock()

    mainmenu_path = os.path.join(BASE_DIR, "images", "mainmenu.jpg")
    mainmenu_img = pygame.image.load(mainmenu_path).convert()
    mainmenu_img = pygame.transform.scale(mainmenu_img, (WIDTH, HEIGHT))

    logo_path = os.path.join(BASE_DIR, "images", "ch.png")
    logo_img = pygame.image.load(logo_path).convert_alpha()
    logo_x = (WIDTH - logo_img.get_width()) // 2
    logo_y = 50

    play_button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 25, 205, 50)
    quit_button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 50, 205, 50)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if play_button_rect.collidepoint(x, y):
                    running = False
                elif quit_button_rect.collidepoint(x, y):
                    pygame.quit()
                    sys.exit()

        screen.blit(mainmenu_img, (0, 0))
        screen.blit(logo_img, (logo_x, logo_y))
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    show_menu()

