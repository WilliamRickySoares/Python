import cv2

# Carregar o classificador pré-treinado para detecção de rosto
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Inicializar a câmera
cap = cv2.VideoCapture(0)

while True:
    # Capturar frame por frame
    ret, frame = cap.read()

    # Converter a imagem para escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar rostos na imagem
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Desenhar retângulos ao redor dos rostos detectados
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Exibir o frame resultante
    cv2.imshow("Detector de Rostos [Pressione q para sair ]", frame)

    # Parar o loop se a tecla 'q' for pressionada
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar os recursos
cap.release()
cv2.destroyAllWindows()
