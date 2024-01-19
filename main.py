board = [
    ["r", "n", "b", "q", "k", "b", "n", "r"],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    ["R", "N", "B", "Q", "K", "B", "N", "R"]
]


def print_board(current_board):
    for row in current_board:

        cellCount = 0
        rank = ""

        for cell in row:

            cellCount += 1

            if cellCount == len(row):
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


print_board(board)
