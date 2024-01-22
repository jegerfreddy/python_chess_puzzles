from pieces.Piece import Piece


class Pawn(Piece):
    hasMoved: bool = False

    def move(self):
        if self.color == "white" and self.pos[1] < 8:
            self.pos[1] += 1

        elif self.color == "black" and self.pos[1] > 1:
            self.pos[1] -= 1

