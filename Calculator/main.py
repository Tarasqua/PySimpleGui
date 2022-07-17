import PySimpleGUI as sg

from misc import WindowCreation, Buttons


def create_window(theme):
    sg.theme(theme)
    sg.set_options(font=WindowCreation.MAIN_FONT, button_element_size=WindowCreation.MAIN_BUTTON_SIZE)
    layout = [
        [sg.Text('',
                 font=WindowCreation.MAIN_FONT,
                 justification=WindowCreation.LAYOUT_TEXT_JUSTIFICATION,
                 expand_x=True,
                 pad=WindowCreation.LAYOUT_TEXT_PAD,
                 right_click_menu=WindowCreation.THEME_MENU,
                 key=WindowCreation.LAYOUT_TEXT_KEY,
                 )
         ],
        [sg.Button(Buttons.CLEAR_BUTTON, expand_x=True), sg.Button(Buttons.ENTER_BUTTON, expand_x=True)],
        [sg.Button(int(Buttons.FIGURES[7]), size=WindowCreation.MAIN_BUTTON_SIZE),
         sg.Button(int(Buttons.FIGURES[8]), size=WindowCreation.MAIN_BUTTON_SIZE),
         sg.Button(int(Buttons.FIGURES[9]), size=WindowCreation.MAIN_BUTTON_SIZE),
         sg.Button(Buttons.ARITHMETIC_OPERATIONS[3], size=WindowCreation.MAIN_BUTTON_SIZE)
         ],
        [sg.Button(int(Buttons.FIGURES[4]), size=WindowCreation.MAIN_BUTTON_SIZE),
         sg.Button(int(Buttons.FIGURES[5]), size=WindowCreation.MAIN_BUTTON_SIZE),
         sg.Button(int(Buttons.FIGURES[6]), size=WindowCreation.MAIN_BUTTON_SIZE),
         sg.Button(Buttons.ARITHMETIC_OPERATIONS[2], size=WindowCreation.MAIN_BUTTON_SIZE)
         ],
        [sg.Button(int(Buttons.FIGURES[1]), size=WindowCreation.MAIN_BUTTON_SIZE),
         sg.Button(int(Buttons.FIGURES[2]), size=WindowCreation.MAIN_BUTTON_SIZE),
         sg.Button(int(Buttons.FIGURES[3]), size=WindowCreation.MAIN_BUTTON_SIZE),
         sg.Button(Buttons.ARITHMETIC_OPERATIONS[1], size=WindowCreation.MAIN_BUTTON_SIZE)
         ],
        [sg.Button(int(Buttons.FIGURES[0]), expand_x=True),
         sg.Button(Buttons.FIGURES[10], size=WindowCreation.MAIN_BUTTON_SIZE),
         sg.Button(Buttons.ARITHMETIC_OPERATIONS[0], size=WindowCreation.MAIN_BUTTON_SIZE)],
    ]
    return sg.Window(title=WindowCreation.TITLE, layout=layout)


window = create_window(WindowCreation.START_THEME)
current_number = []
full_operation = []

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event in WindowCreation.THEME_MENU[1]:
        window.close()
        window = create_window(event)

    if event in Buttons.FIGURES:
        current_number.append(event)
        number_str = ''.join(current_number)
        window[WindowCreation.LAYOUT_TEXT_KEY].update(number_str)

    if event in Buttons.ARITHMETIC_OPERATIONS:
        full_operation.append(''.join(current_number))
        current_number = []
        full_operation.append(event)
        window[WindowCreation.LAYOUT_TEXT_KEY].update('')

    if event == Buttons.ENTER_BUTTON:
        full_operation.append(''.join(current_number))
        result = round(eval(' '.join(full_operation)), 8)
        window[WindowCreation.LAYOUT_TEXT_KEY].update(result)
        full_operation = []

    if event == Buttons.CLEAR_BUTTON:
        current_number = []
        full_operation = []
        window[WindowCreation.LAYOUT_TEXT_KEY].update('')

window.close()
