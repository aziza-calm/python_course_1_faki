n = int(input())
plane = []
for _ in range(n):
    plane.append(input())

# d = {"num": 2, "side": "left", "position": "aisle"}
groups = []
m = int(input())
for _ in range(m):
    # Здесь происходит считывание с клавиатуры, в raw_input пишется, например ["2", "left", "aisle"]
    raw_input = input().split()
    # Здесь нужно создать словарь из обработанного raw_input
    current_group = {
        "num": int(raw_input[0]),
        "side": raw_input[1],
        "position": raw_input[2]
    }
    # Здесь обработанный словарь добавляется в лист groups
    groups.append(current_group)


def check_side(plane_row, group):
    """
    :param plane_row: Информация о ряде самолета.
    :param group: Информация о группе и ее пожеланиях.
    :return: Флаг, подходит ли ряд самолета под пожелания о стороне.
    """
    pass


def check_position(plane_row, group):
    """
    :param plane_row: Информация о ряде самолета.
    :param group: Информация о группе и ее пожеланиях.
    :return: Флаг, подходит ли ряд самолета под пожелания о месте.
    """
    pass


def find_seats(plane, group):
    """
    :param plane: Информация о местах в самолете.
    :param group: Информация о группе и ее пожеланиях.
    :return: Информация о подходящих местах (номер ряда, левое место).
    """
    pass


def print_plane(plane):
    pass


def add_xx_to_plane(plane, row_num, seat_num, num):
    pass


def book_xx(plane):
    pass


def parse_seats(coord):
    pass


if __name__ == "__main__":
    for group in groups:
        coord = find_seats(plane, group)
        if coord[0] == -1:
            print("Cannot fulfill passengers requirements")
        else:
            print("Passengers can take seats: " + parse_seats(coord))
            plane = add_xx_to_plane(plane, row_num, seat_num, num)
            print_plane(plane)
            plane = book_xx(plane)
