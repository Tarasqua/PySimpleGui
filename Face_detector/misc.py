class Layout:
    IMAGE_KEY = '-IMAGE-'

    TEXT_TEXT = 'People in picture:'
    TEXT_KEY = '-TEXT-'
    TEXT_JUSTIFICATION = 'center'
    TEXT_FONT = 'Young 20'


class Face:
    FACE_CASCADE = 'haarcascade_frontalface_default.xml'

    SCALE_FACTOR = 1.3
    MIN_NEIGHBORS = 7
    MIN_SIZE = (50, 50)

    RECTANGLE_COLOR = (0, 255, 0)
    RECTANGLE_THICKNESS = 2
