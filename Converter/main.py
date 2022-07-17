import PySimpleGUI as sg

from misc import Layout

layout = [
    [
        sg.Input(key=Layout.INPUT_KEY),
        sg.Spin(Layout.SPIN_VALUES, key=Layout.SPIN_KEY),
        sg.Button(button_text=Layout.CONVERT_BUTTON_TEXT, key=Layout.CONVERT_BUTTON_KEY)
    ],
    [sg.Text('', key=Layout.OUTPUT_KEY)]
]
window = sg.Window(title='Converter', layout=layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == Layout.CONVERT_BUTTON_KEY:
        input_value = values[Layout.INPUT_KEY]
        output_string = ''
        if input_value.isnumeric():
            match values[Layout.SPIN_KEY]:
                case 'km to mile':
                    output = round(float(input_value) * 0.6214, 2)
                    output_string = f'{input_value} km are {output} miles.'
                case 'kg to pound':
                    output = round(float(input_value) * 2.20462, 2)
                    output_string = f'{input_value} kg are {output} pounds.'
                case 'sec to min':
                    output = round(float(input_value) / 60, 2)
                    output_string = f'{input_value} seconds are {output} minutes.'

            window[Layout.OUTPUT_KEY].update(output_string)
        else:
            window[Layout.OUTPUT_KEY].update('Please, enter a number.')

window.close()
