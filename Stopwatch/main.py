import PySimpleGUI as sg
from time import time


def create_window():
    sg.theme('purple')
    layout = [
        [sg.Push(), sg.Image('cross.png', pad=0, enable_events=True, key='-CLOSE-')],
        [sg.VPush()],
        [sg.Text('', font='Young 50', key='-TIME-')],
        [
            sg.Button('Start', button_color='#DFE6AC', border_width=0, key='-STARTSTOP-', font='Young'),
            sg.Button('Lap', button_color='#DFE6AC', border_width=0, key='-LAP-', visible=False, font='Young')
        ],
        [sg.Column([[]], key='-LAPS-')],
        [sg.VPush()],
    ]

    return sg.Window(
        title='Stopwatch',
        layout=layout,
        size=(300, 300),
        no_titlebar=True,
        element_justification='center'
    )


window = create_window()
start_time = 0
active = False
lap_amount = 1

while True:
    event, value = window.read(timeout=10)
    if event in (sg.WIN_CLOSED, '-CLOSE-'):
        break

    if event == '-STARTSTOP-':
        if active:
            # from active to stop
            active = False
            window['-STARTSTOP-'].update('Reset')
            window['-LAP-'].update(visible=False)
        else:
            # from stop to reset
            if start_time > 0:
                window.close()
                window = create_window()
                start_time = 0
                lap_amount = 1
            else:
                # from start to active
                start_time = time()
                active = True
                window['-STARTSTOP-'].update('Stop')
                window['-LAP-'].update(visible=True)

    if active:
        elapsed_time = round(time() - start_time, 1)
        window['-TIME-'].update(elapsed_time)

    if event == '-LAP-':
        window.extend_layout(
            window['-LAPS-'],
            [[sg.Text(lap_amount, font='16'), sg.VSeparator(), sg.Text(elapsed_time, font='16')]]
        )
        lap_amount += 1

window.close()
