import PySimpleGUI as sg
import cv2

from misc import Layout, Face

layout = [
    [sg.Image(key=Layout.IMAGE_KEY)],
    [sg.Text(text=Layout.TEXT_TEXT,
             key=Layout.TEXT_KEY,
             expand_x=True,
             justification=Layout.TEXT_JUSTIFICATION,
             font=Layout.TEXT_FONT)]
]

window = sg.Window(title='Face detector', layout=layout)

# Получаем видео
video = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(Face.FACE_CASCADE)

while True:
    event, values = window.read(timeout=0)
    if event == sg.WIN_CLOSED:
        break

    _, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=Face.SCALE_FACTOR,
        minNeighbors=Face.MIN_NEIGHBORS,
        minSize=Face.MIN_SIZE,
    )

    # Отрисовываем прямоугольники
    for x, y, w, h in faces:
        cv2.rectangle(img=frame, pt1=(x, y), pt2=(x + w, y + h),
                      color=Face.RECTANGLE_COLOR, thickness=Face.RECTANGLE_THICKNESS)

    # Обновляем картинку
    img_bytes = cv2.imencode('.png', frame)[1].tobytes()
    window[Layout.IMAGE_KEY].update(data=img_bytes)

    # Обновляем текст
    window[Layout.TEXT_KEY].update(f'{Layout.TEXT_TEXT} {len(faces)}')

window.close()
