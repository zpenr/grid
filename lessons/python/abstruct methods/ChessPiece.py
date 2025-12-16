import abc

class ChessPiece(abc.ABC):
    def __init__(self, horizontal, vertical):
        self.horizontal = horizontal
        self.vertical = vertical

    @abc.abstractmethod
    def can_move():
        pass