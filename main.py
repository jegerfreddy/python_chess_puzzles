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


def get_board_map(board):

    # This function takes a given board and maps out what pieces are on the board,
    # and which coordinates they have.

    # rank-/file_index tracks which file and rank we are indexing through the for-loops
    rank_index = 8

    # We use the i variable to specify where to store to data in the array,
    # we could use rank_index - 1 here, but it would look messy...
    i = 0

    board_map = [
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

        file_index = 1

        for cell in row:

            board_map[i].append((file_index, rank_index, cell))

            file_index += 1

        rank_index -= 1
        i += 1

    return board_map


current_board_map = get_board_map(default_piece_positions)

print(current_board_map)


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

