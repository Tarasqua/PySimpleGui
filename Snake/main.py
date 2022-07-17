from time import time
from random import randint
import PySimpleGUI as sg


def convert_position_to_pixel(cell):
    tl = cell[0] * CELL_SIZE, cell[1] * CELL_SIZE
    br = tl[0] + CELL_SIZE, tl[1] + CELL_SIZE
    return tl, br


def apple_place():
    apple_pos = randint(0, CELL_NUM - 1), randint(0, CELL_NUM - 1)
    while apple_pos in snake_body:
        apple_pos = randint(0, CELL_NUM - 1), randint(0, CELL_NUM - 1)
    return apple_pos


# game constants
FIELD_SIZE = 400
CELL_NUM = 10
CELL_SIZE = FIELD_SIZE / CELL_NUM

# snake
snake_body = [(4, 4), (3, 4), (2, 4)]
DIRECTIONS = {'left': (-1, 0), 'right': (1, 0), 'up': (0, 1), 'down': (0, -1)}
direction = DIRECTIONS['up']

# apple
apple_position = apple_place()
apple_eaten = False

sg.theme('Green')
field = sg.Graph(canvas_size=(FIELD_SIZE, FIELD_SIZE),
                 graph_bottom_left=(0, 0),
                 graph_top_right=(FIELD_SIZE, FIELD_SIZE),
                 background_color='black')

layout = [[field]]

window = sg.Window('Snake', layout=layout, return_keyboard_events=True)

start_time = time()
while True:
    event, values = window.read(timeout=10)
    if event == sg.WIN_CLOSED:
        break

    if event == 'Left:37':
        direction = DIRECTIONS['left']
    if event == 'Up:38':
        direction = DIRECTIONS['up']
    if event == 'Right:39':
        direction = DIRECTIONS['right']
    if event == 'Down:40':
        direction = DIRECTIONS['down']

    time_since_start = time() - start_time
    if time_since_start >= 0.3:
        start_time = time()

        # apple snake collision
        if snake_body[0] == apple_position:
            apple_position = apple_place()
            apple_eaten = True

        # snake update
        new_head = (snake_body[0][0] + direction[0],
                    snake_body[0][1] + direction[1])
        snake_body.insert(0, new_head)
        if not apple_eaten:
            snake_body.pop()
        apple_eaten = False

        field.DrawRectangle((0, 0), (FIELD_SIZE, FIELD_SIZE), 'black')

        # check death
        if not 0 <= snake_body[0][0] <= CELL_NUM - 1 or \
           not 0 <= snake_body[0][1] <= CELL_NUM - 1 or \
           snake_body[0] in snake_body[1:]:
            break

        # draw apple
        top_left, bottom_right = convert_position_to_pixel(apple_position)
        field.DrawRectangle(top_left, bottom_right, 'Red')

        # draw snake
        for index, part in enumerate(snake_body):
            top_left, bottom_right = convert_position_to_pixel(part)
            color = 'yellow' if index == 0 else 'green'
            field.DrawRectangle(top_left, bottom_right, color)

window.close()
