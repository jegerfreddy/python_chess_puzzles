from pieces.Piece import Piece


class King(Piece):

    def move(self):
        if self.color == "white" and self.pos[1] < 8:
            self.pos[1] += 1
