import pygame
import sys
import time

# Inicializar Pygame
pygame.init()

# Definir colores
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Configuración de la ventana
ANCHO = 800
ALTO = 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("BodyBuilder App")

# Fuente para el texto
fuente = pygame.font.SysFont("Arial", 30)

# Clase para los ejercicios
class Ejercicio:
    def __init__(self, nombre, repeticiones, series):
        self.nombre = nombre
        self.repeticiones = repeticiones
        self.series = series


# Lista de ejercicios
ejercicios = [
    Ejercicio("Flexiones", 10, 3),
    Ejercicio("Sentadillas", 15, 3),
    Ejercicio("plancha", 12, 3),
    Ejercicio("abdominal", 12, 3),
jjjjjjjjjjj
]

# Función para mostrar el menú principal
def mostrar_menu_principal():
    ventana.fill(BLUE)
    texto = fuente.render("Selnecciona una parte del cuerpo:", True, BLACK)
    ventana.blit(texto, (50, 50))
    texto2 = fuente.render("Hola soy tu entrenador personalizado", True, BLACK)
    ventana.blit(texto2, (50, 20))

    botones = ["1.Brazos", "2.Piernas", "3.Torso"]
    for i, boton in enumerate(botones):
        texto_boton = fuente.render(boton, True, WHITE)
        ventana.blit(texto_boton, (50, 100 + i * 50))

    pygame.display.flip()

# Función para mostrar ejercicios
def mostrar_ejercicios(parte):
    ventana.fill(BLUE)
    texto = fuente.render(f"Ejercicios para {parte}:", True, BLACK)
    ventana.blit(texto, (50, 50))

    for i, ejercicio in enumerate(ejercicios):
        texto_ejercicio = fuente.render(ejercicio.nombre, True, WHITE)
        ventana.blit(texto_ejercicio, (50, 100 + i * 50))

    pygame.display.flip()

# Función para iniciar el ejercicio
def iniciar_ejercicio(ejercicio):
    repeticiones_realizadas = 0
    serie_actual = 1
    tiempo_inicio = time.time()
    pausado = False

    while True:
        ventana.fill(BLUE)

        # Mostrar información del ejercicio
        elapsed_time = int(time.time() - tiempo_inicio) if not pausado else int(time.time() - tiempo_inicio - pausa_tiempo)
        display_text = f"Ejercicio: {ejercicio.nombre}\n"
        display_text += f"Repeticiones: {repeticiones_realizadas}/{ejercicio.repeticiones}\n"
        display_text += f"Serie: {serie_actual}/{ejercicio.series}\n"
        display_text += f"Tiempo transcurrido: {elapsed_time} segundos\n"
        
        # Mostrar el texto en la ventana
        for i, line in enumerate(display_text.split('\n')):
            texto_linea = fuente.render(line.strip(), True, BLACK)
            ventana.blit(texto_linea, (50, 50 + i * 40))

        # Botón de pausa
        boton_pausa = pygame.Rect(510, 50, 240, 40)
        pygame.draw.rect(ventana, WHITE if not pausado else BLACK, boton_pausa)
        texto_pausa = fuente.render("Pausar/Continuar", True, BLUE)
        ventana.blit(texto_pausa, (510, 55))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if boton_pausa.collidepoint(event.pos):
                    pausado = not pausado
                    if pausado:
                        pausa_tiempo = time.time() - tiempo_inicio

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:   # Presionar ESC para salir del ejercicio.
                    return

        # Solo incrementar repeticiones si no está pausado
        if not pausado:
            time.sleep(1)  
            repeticiones_realizadas += 1

            if repeticiones_realizadas >= ejercicio.repeticiones:
                if serie_actual < ejercicio.series:
                    serie_actual += 1
                    repeticiones_realizadas = 0

# Bucle principal de la aplicación
def main():
    while True:
        mostrar_menu_principal()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    mostrar_ejercicios("Brazos")
                    iniciar_ejercicio(ejercicios[0]) # Flexiones
                elif event.key == pygame.K_2:
                    mostrar_ejercicios("Piernas")
                    iniciar_ejercicio(ejercicios[1]) # Sentadillas
                elif event.key == pygame.K_3:
                    mostrar_ejercicios("Torso")
                    iniciar_ejercicio(ejercicios[2]) # Plancha

if __name__ == "__main__":
    main()