import pygame.camera
import pygame.surfarray
import numpy as np

cont_frame = 0

# Inicializar o módulo da câmera do pygame
pygame.camera.init()

# Lista as câmeras disponíveis
cam_list = pygame.camera.list_cameras()

if not cam_list:
    print("Nenhuma câmera encontrada.")
    quit()

# Inicializar a câmera
camera = pygame.camera.Camera(cam_list[0], (640, 480))

# Iniciar a câmera
camera.start()

# Loop principal
running = True
previous_frame = None

while running:
    cont_frame += 1

    # Capturar um frame da câmera
    frame = camera.get_image()

    # Converter o frame para uma matriz NumPy
    frame_array = pygame.surfarray.array3d(frame)

    # Converter para escala de cinza
    gray_frame = np.dot(frame_array[..., :3], [0.299, 0.587, 0.114])

    # Normalizar a imagem
    normalized_frame = gray_frame / 255.0

    if previous_frame is not None:
        # Calcular a diferença absoluta entre os frames atual e anterior
        diff_frame = np.abs(normalized_frame - previous_frame)

        # Calcular a média dos valores de diferença
        mean_diff = np.mean(diff_frame)

        # Definir um limite para o movimento
        motion_threshold = 0.01

        if mean_diff > motion_threshold:
            print(f"Movimento detectado! {cont_frame}")

    # Armazenar o frame atual para uso no próximo loop
    previous_frame = normalized_frame

    # Exibir o frame capturado
    screen = pygame.display.set_mode((640, 480))
    screen.blit(frame, (0, 0))
    pygame.display.flip()

    # Verificar eventos de saída
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Parar a câmera e finalizar o módulo
camera.stop()
pygame.camera.quit()
