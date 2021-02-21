import turtle
import math


# Constants
STEP_SIZE = 30
DIAGONAL_STEP_SIZE = math.sqrt(2) * STEP_SIZE


def draw_symbol(symbol, coords):
    """
    :param symbol: symbol to draw
    :param coords: left upper corner coords
    """
    turtle.penup()
    if symbol == '0':
        turtle.goto(coords[0], coords[1])
        turtle.pendown()
        turtle.forward(STEP_SIZE)
        turtle.right(90)
        turtle.forward(STEP_SIZE * 2)
        turtle.right(90)
        turtle.forward(STEP_SIZE)
        turtle.right(90)
        turtle.forward(STEP_SIZE * 2)
        turtle.right(90)
    elif symbol == '1':
        turtle.goto(coords[0], coords[1] - STEP_SIZE)
        turtle.pendown()
        turtle.left(45)
        turtle.forward(DIAGONAL_STEP_SIZE)
        turtle.right(135)
        turtle.forward(STEP_SIZE * 2)
        turtle.left(90)
    elif symbol == '2':
        turtle.goto(coords[0], coords[1])
        turtle.pendown()
        turtle.forward(STEP_SIZE)
        turtle.right(90)
        turtle.forward(STEP_SIZE)
        turtle.right(45)
        turtle.forward(DIAGONAL_STEP_SIZE)
        turtle.left(135)
        turtle.forward(STEP_SIZE)
    elif symbol == '3':
        turtle.goto(coords[0], coords[1])
        turtle.pendown()
        turtle.forward(STEP_SIZE)
        turtle.right(135)
        turtle.forward(DIAGONAL_STEP_SIZE)
        turtle.left(135)
        turtle.forward(STEP_SIZE)
        turtle.right(135)
        turtle.forward(DIAGONAL_STEP_SIZE)
        turtle.left(135)
    elif symbol == '4':
        turtle.goto(coords[0], coords[1])
        turtle.pendown()
        turtle.right(90)
        turtle.forward(STEP_SIZE)
        turtle.left(90)
        turtle.forward(STEP_SIZE)
        turtle.left(90)
        turtle.forward(STEP_SIZE)
        turtle.left(180)
        turtle.forward(2 * STEP_SIZE)
        turtle.left(90)
    elif symbol == '5':
        turtle.goto(coords[0] + STEP_SIZE, coords[1])
        turtle.pendown()
        turtle.right(180)
        turtle.forward(STEP_SIZE)
        turtle.left(90)
        turtle.forward(STEP_SIZE)
        turtle.left(90)
        turtle.forward(STEP_SIZE)
        turtle.right(90)
        turtle.forward(STEP_SIZE)
        turtle.right(90)
        turtle.forward(STEP_SIZE)
        turtle.right(180)
    elif symbol == '6':
        turtle.goto(coords[0] + STEP_SIZE, coords[1])
        turtle.pendown()
        turtle.right(135)
        turtle.forward(DIAGONAL_STEP_SIZE)
        turtle.left(45)
        turtle.forward(STEP_SIZE)
        turtle.left(90)
        turtle.forward(STEP_SIZE)
        turtle.left(90)
        turtle.forward(STEP_SIZE)
        turtle.left(90)
        turtle.forward(STEP_SIZE)
        turtle.left(180)
    elif symbol == '7':
        turtle.goto(coords[0], coords[1])
        turtle.pendown()
        turtle.forward(STEP_SIZE)
        turtle.right(135)
        turtle.forward(DIAGONAL_STEP_SIZE)
        turtle.left(45)
        turtle.forward(STEP_SIZE)
        turtle.left(90)
    elif symbol == '8':
        turtle.goto(coords[0], coords[1])
        turtle.pendown()
        turtle.forward(STEP_SIZE)
        turtle.right(90)
        turtle.forward(STEP_SIZE * 2)
        turtle.right(90)
        turtle.forward(STEP_SIZE)
        turtle.right(90)
        turtle.forward(STEP_SIZE * 2)
        turtle.right(180)
        turtle.forward(STEP_SIZE)
        turtle.left(90)
        turtle.forward(STEP_SIZE)
    elif symbol == '9':
        turtle.goto(coords[0] + STEP_SIZE, coords[1] - STEP_SIZE)
        turtle.pendown()
        turtle.right(180)
        turtle.forward(STEP_SIZE)
        turtle.right(90)
        turtle.forward(STEP_SIZE)
        turtle.right(90)
        turtle.forward(STEP_SIZE)
        turtle.right(90)
        turtle.forward(STEP_SIZE)
        turtle.right(45)
        turtle.forward(DIAGONAL_STEP_SIZE)
        turtle.left(135)
    else:
        print(f'Unknown symbol "{symbol}"')


if __name__ == "__main__":
    screensize = turtle.screensize()
    current_x = int(-screensize[0] / 2) + 10
    current_y = int(screensize[1] / 2) - 10

    turtle.shape('turtle')
    turtle.color('blue')
    turtle.width(5)

    input_seq = input('Please input sequence to draw: ')
    for symbol in input_seq:
        draw_symbol(symbol, [current_x, current_y])
        current_x += 2 * STEP_SIZE

input('Press any key...')
