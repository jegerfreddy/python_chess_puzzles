from pieces.Piece import Piece


class Rook(Piece):

    def move(self):
        if self.color == "white" and self.pos[1] < 8:
            self.pos[1] += 1
