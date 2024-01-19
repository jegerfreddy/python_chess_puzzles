import Player

default_piece_positions = [
    ["r", "n", "b", "q", "k", "b", "n", "r"],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    ["R", "N", "B", "Q", "K", "B", "N", "R"]
]

board_coordinates = [
    [(1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8)],
    [(1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7)],
    [(1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6), (8, 6)],
    [(1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (8, 5)],
    [(1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4)],
    [(1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (8, 3)],
    [(1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2)],
    [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1)]
]

rook_moves = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1)
]

knight_moves = [
    (2, 1),
    (2, -1),
    (1, 2),
    (-1, 2),
    (-2, 1),
    (-2, -1),
    (-2, -1),
    (-1, -2),
    (1, -2)
]

bishop_moves = [
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1)
]

king_moves = [
    (1, 0),
    (1, 1),
    (0, 1),
    (-1, 1),
    (-1, 0),
    (-1, -1),
    (0, -1),
    (1, -1)
]

queen_moves = king_moves

pawn_moves = [
    (1, 0),
    (1, 1),
    (1, -1)
]


def calculate_piece_positions(board):

    rank_index = 0
    file_index = 0
    piece_positions = [
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        []
    ]
    piece_coordinates = [
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        []
    ]

    for row in board:

        for cell in row:

            piece_positions[rank_index].append(cell)
            piece_coordinates[rank_index].append((rank_index + 1, file_index + 1))

            file_index += 1

        rank_index += 1

    return [piece_positions, piece_coordinates]


calculation = calculate_piece_positions(default_piece_positions)

print(calculation)

white = Player.Player()
black = Player.Player()


def print_board(board):
    # This variable is used to track which rank is being handled.
    rank_num = 8

    for row in board:

        rank = "{rankNum}.  ".format(rankNum=rank_num)
        rank_num -= 1

        # Similar to the variable rank_num, this is used to keep track of which cell in the rank
        # is being handled.
        cell_count = 0

        for cell in row:

            cell_count += 1

            if cell_count == len(row):
                if cell == " ":

                    rank += "| _ |"

                else:
                    rank += "| {piece} |".format(piece=cell)

            else:
                if cell == " ":

                    rank += "| _ "

                else:
                    rank += "| {piece} ".format(piece=cell)

        print(rank)

    print("   __________________________________")
    print("      A   B   C   D   E   F   G   H")

