import PySimpleGUI as sg
from PIL import Image, ImageFilter, ImageOps
from io import BytesIO


def update_image(original, blur, contrast, emboss, contour, flipx, flipy):
    """Function management."""
    global image
    image = original.filter(ImageFilter.GaussianBlur(blur))
    image = image.filter(ImageFilter.UnsharpMask(contrast))

    if emboss:
        image = image.filter(ImageFilter.EMBOSS)
    if contour:
        image = image.filter(ImageFilter.CONTOUR)

    if flipx:
        image = ImageOps.mirror(image)
    if flipy:
        image = ImageOps.flip(image)

    bio = BytesIO()
    image.save(bio, format='PNG')

    window['-IMAGE-'].update(data=bio.getvalue())


image_path = sg.popup_get_file('Open', no_window=True)

sg.theme('DarkTeal4')
control_column = sg.Column([
    [sg.Frame('Blur', layout=[[sg.Slider(range=(0, 50), resolution=0.5, orientation='h', key='-BLUR-')]])],
    [sg.Frame('Contrast', layout=[[sg.Slider(range=(0, 50), resolution=0.5, orientation='h', key='-CONTRAST-')]])],
    [sg.Checkbox('Emboss', key='-EMBOSS-'), sg.Checkbox('Contour', key='-CONTOUR-')],
    [sg.Checkbox('Flip x', key='-FLIPX-'), sg.Checkbox('Flip y', key='-FLIPY-')],
    [sg.Button('Save Image', key='-SAVE-')],
])
image_column = sg.Column([[sg.Image(image_path, key='-IMAGE-')]])
layout = [[control_column, image_column]]

original = Image.open(image_path)
window = sg.Window(title='Image Editor', layout=layout)

while True:
    event, values = window.read(timeout=50)
    if event == sg.WIN_CLOSED:
        break

    update_image(original=original,
                 blur=values['-BLUR-'],
                 contrast=values['-CONTRAST-'],
                 emboss=values['-EMBOSS-'],
                 contour=values['-CONTOUR-'],
                 flipx=values['-FLIPX-'],
                 flipy=values['-FLIPY-'])

    if event == '-SAVE-':
        save_path = sg.popup_get_file('Save', save_as=True, no_window=True) + '.png'
        image.save(save_path, 'PNG')

window.close()
