import pygame
import random
import math
import sys
import os

#Inicializar pygame
pygame.get_init()

# Inicializar el mezclador de sonido
pygame.mixer.init()

pygame.font.init()
    
def restart_game():
    global playerX, playerx_change, bulletX, bulletY, bullet_state, score

    # Restablecer variables del jugador
    playerX = 370
    playerx_change = 0

    # Restablecer variables de la bala
    bulletX = 0
    bulletY = 480
    bullet_state = "ready"

    # Restablecer puntuación
    score = 0

    # Restablecer posiciones de los enemigos
    for i in range(no_of_enemies):
        enemyX[i] = random.randint(0, 736)
        enemyY[i] = random.randint(0, 150)

    gameloop()

#Establece el tamaño de la pantalla
screen_weidth = 800
screen_height = 600
screen = pygame.display.set_mode((screen_weidth, screen_height))

#Funcion para obtener la ruta de los recursos
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)
    
def restart_game():
    global playerX, playerx_change, bulletX, bulletY, bullet_state, score

    # Restablecer variables del jugador
    playerX = 370
    playerx_change = 0

    # Restablecer variables de la bala
    bulletX = 0
    bulletY = 480
    bullet_state = "ready"

    # Restablecer puntuación
    score = 0

    # Restablecer posiciones de los enemigos
    for i in range(no_of_enemies):
        enemyX[i] = random.randint(0, 736)
        enemyY[i] = random.randint(0, 150)

    gameloop()  
     
#Cargar imagen de fondo
asset_background = resource_path("background.png")
background = pygame.image.load(asset_background)  

#Cargar icono de ventana
asset_icon = resource_path("ufo.png")
icon = pygame.image.load(asset_icon) 

#Cargar de sonido de fondo
asset_sound = resource_path("naruto.mp3")
background_sound = pygame.mixer.music.load(asset_sound) 

#Cargar imagen del jugador
asset_playering = resource_path("space-invaders.png")
playerimg = pygame.image.load(asset_playering) 

#Cargar imagen de bala
asset_bulletimg = resource_path("bullet.png")
bulletimg = pygame.image.load(asset_bulletimg) 

# Inicializar fuente de texto de game over 
asset_over_font = resource_path("RAVIE.TTF")
over_font = pygame.font.Font(asset_over_font, 60) 

# Inicializar fuente de texto del puntaje
asset_font = resource_path("comicbd.ttf")
font = pygame.font.Font(asset_font, 32) 

# Establecer titulo de ventana
pygame.display.set_caption("<<La Navecita>>")

# Estableder icono de ventana
pygame.display.set_icon(icon)

# Reproducir sonido de fondo en loop
pygame.mixer.music.play(-1)

#Reloj para controlar la velocidad del juego 
clock = pygame.time.Clock()

#Posicion inicial del jugador 
playerX = 370
playerY = 470
playerx_change = 0
playery_change = 0

# Listas para almacenar posiciones de los enemigos
enemyimg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
no_of_enemies = 10

#Se inicializan las variables para guardar las posiciones de los enemigos 
for i in range(no_of_enemies):
    #se carga la imagen del enemigo 1
    enemy1 = resource_path("enemy1.png")
    enemyimg.append(pygame.image.load(enemy1)) 
    #se carga la imagen del enemigo 2
    enemy2 = resource_path("enemy2.png")
    enemyimg.append(pygame.image.load(enemy2)) 


    #se asigna una posicion aleatoria en X e Y para el enemigo 
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(0,150))

    #se establece la velocidadad de movimiento del enemigo en X e Y
    enemyX_change.append(5)
    enemyY_change.append(20)

    #Se inicializan las variables para guardar la posicion de la bala
    bulletX = 0
    bulletY = 480
    bulletX_change = 0
    bulletY_change = 10
    bullet_state = "ready"

    #Se inicia la puntuacion en 0
    score = 0

    #funcion para mostrar la puntuacion en la pantalla
    def show_score():
        score_value = font.render("SCORE " + str(score), True, (255, 255, 255))
        screen.blit(score_value,(10, 10))

    #funcion para dibujar al jugador en la pantalla
    def player(x, y,):
        screen.blit(playerimg,(x, y))

    #Funcion para dibujar al enemigo en la pantalla
    def enemy(x, y, i):
        screen.blit(enemyimg[i], (x, y))

    #Funcion para disparar la bala
    def fire_bullet(x, y):
        global bullet_state

        bullet_state = "fire"
        screen.blit(bulletimg,(x + 16, y + 10))

    #Funcion para comprobar la colision entre la bala y el enemigo
    def isCollision(enemyX, enemyY, bulletX, bulletY):
        distance = math.sqrt((math.pow(enemyX - bulletX, 2)) +                                                         
                             (math.pow(enemyY - bulletY, 2))) 
        if distance < 27:
            return True
        else:
            return False
    
    #Funcion para el texto de Game Over en pantalla
    def game_over_text():
        over_text = over_font.render("GAME OVER", True, (255, 255, 255))
        text_rect = over_text.get_rect(center=(int(screen_weidth/2), int(screen_height/2)))
        screen.blit(over_text, text_rect)

        # Mostrar instrucción para reiniciar el juego
        restart_text = font.render("Presiona F para reiniciar", True, (255, 255, 255))
        restart_rect = restart_text.get_rect(center=(int(screen_weidth/2), int(screen_height/2) + 50))
        screen.blit(restart_text, restart_rect)

    pygame.display.update()

    #Funcion principal o Bucle del juego
    def gameloop():

        #Declarar variables globales
        global score
        global playerX
        global playerx_change
        global bulletX
        global bulletY
        global bullet_state

        in_game = True
        while in_game:
            #Manejar eventos, actualizar y renderizar el juego
            #Limpia la pantalla
            screen.fill((0, 0, 0))
            screen.blit(background, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   in_game = False
                   pygame.quit()
                   sys.exit()

                if event.type == pygame.KEYDOWN:
                    #Movientos del jugador y el disparo
                    if event.key == pygame.K_LEFT:
                        playerx_change = -5

                    if event.key == pygame.K_RIGHT:
                        playerx_change = 5

                    if event.key == pygame.K_SPACE:
                        if bullet_state == "ready":
                            bulletX = playerX
                            fire_bullet(bulletX, bulletY)

                if event.type == pygame.KEYUP:
                    playerx_change = 0

                # Verificar si el usuario presiona la tecla para reiniciar el juego
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_f:
                        restart_game()
                
             #Aqui se actualiza la posicion del jugador
            playerX += playerx_change

            if playerX <= 0:
                playerX = 0
            elif playerX >= 736:
                playerX = 736   

            #Bucle para el enemigo
            for i in range(no_of_enemies):
                if enemyY[i] > 440:
                    for j in range(no_of_enemies):
                        enemyY[j] = 2000
                    game_over_text()

                enemyX[i] += enemyX_change[i] 
                if enemyX[i] <= 0:
                    enemyX_change[i] = 8
                    enemyY[i] += enemyY_change[i]
                elif enemyX[i] >= 736:
                    enemyX_change[i] = -8
                    enemyY[i] += enemyY_change[i]
        
                #Aqui se comprueba la colicion entre la bala y el enemigo
                collison = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
                if collison:
                    bulletY = 454
                    bullet_state = "ready"
                    score += 1
                    enemyX[i] = random.randint(0, 736)
                    enemyY[i] = random.randint(0, 150)
                enemy(enemyX[i], enemyY[i], i)
        
            if bulletY < 0:
                    bulletY = 480
                    bullet_state = "ready"
            if bullet_state == "fire":
                    fire_bullet(bulletX, bulletY)
                    bulletY -= bulletY_change

            player(playerX, playerY)
            
            show_score()

            pygame.display.update()

            clock.tick(120)

gameloop()
