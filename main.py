from pieces import Pawn, Rook, Bishop, Knight, Queen, King

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


# This function takes a given board and maps out what pieces are on the board,
# and which coordinates(file/rank) they are standing on.
def get_board_map(board):

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
                if cell[2] == " ":

                    rank += "| _ |"

                else:
                    rank += "| {piece} |".format(piece=cell[2])

            else:
                if cell[2] == " ":

                    rank += "| _ "

                else:
                    rank += "| {piece} ".format(piece=cell[2])

        print(rank)

    print("   __________________________________")
    print("      A   B   C   D   E   F   G   H")


print_board(current_board_map)