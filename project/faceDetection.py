import cv2

arqCasc = 'haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(arqCasc)

webcam = cv2.VideoCapture(0)  # instancia o uso da webcam

while True:
    s, imagem = webcam.read() # pega a imagem da webcam
    imagem = cv2.flip(imagem,180) # espelha a imagem

    faces = faceCascade.detectMultiScale(imagem, minNeighbors=5, minSize=(50, 50), maxSize=(300,300))

    # Desenha um retangulo nas faces detectadas e salva a ultima face detectada
    for (x, y, w, h) in faces:
        cv2.rectangle(imagem, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imwrite('person_identificated.png', imagem)
        print 'hi there'

    cv2.imshow('Video', imagem) # mostra a imagem capturada na janela

    # o trecho seguinte a apenas para parar o codigo e fechar a janela
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release() # dispensa o uso da webcam
cv2.destroyAllWindows() # fecha todas a janelas aberta
