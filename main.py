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

white_pieces = []
black_pieces = []


# This function takes a given board and maps out what pieces are on the board,
# and which coordinates they have.
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

            if cell == "P":
                pawn = Pawn.Pawn("white", (file_index, rank_index))

                white_pieces.append(pawn)

            elif cell == "p":
                pawn = Pawn.Pawn("black", (file_index, rank_index))

                black_pieces.append(pawn)

            elif cell == "R":
                rook = Rook.Rook("white", (file_index, rank_index))

                white_pieces.append(rook)

            elif cell == "r":
                rook = Rook.Rook("black", (file_index, rank_index))

                black_pieces.append(rook)

            elif cell == "B":
                bishop = Bishop.Bishop("white", (file_index, rank_index))

                white_pieces.append(bishop)

            elif cell == "b":
                bishop = Bishop.Bishop("black", (file_index, rank_index))

                black_pieces.append(bishop)

            elif cell == "N":
                knight = Knight.Knight("white", (file_index, rank_index))

                white_pieces.append(knight)

            elif cell == "n":
                knight = Knight.Knight("black", (file_index, rank_index))

                black_pieces.append(knight)

            elif cell == "Q":
                queen = Queen.Queen("white", (file_index, rank_index))

                white_pieces.append(queen)

            elif cell == "q":
                queen = Queen.Queen("black", (file_index, rank_index))

                black_pieces.append(queen)

            elif cell == "K":
                king = King.King("white", (file_index, rank_index))

                white_pieces.append(king)

            elif cell == "k":
                king = King.King("black", (file_index, rank_index))

                black_pieces.append(king)

            file_index += 1

        rank_index -= 1
        i += 1

    return board_map


current_board_map = get_board_map(default_piece_positions)


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
