default_board = [
    ["r", "n", "b", "q", "k", "b", "n", "r"],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    ["R", "N", "B", "Q", "K", "B", "N", "R"]
]


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


print_board(default_board)
