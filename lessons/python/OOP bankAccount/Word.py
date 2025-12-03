def check_type(method):
        def wrapper(self, other):
            if not isinstance(other, Word):
                return NotImplemented
            return method(self, other)
        return wrapper

class Word():
    def __init__(self, word):
        self.word = word

    def __str__(self):
        return self.word.capitalize()
    
    def __repr__(self):
        return f"Word('{self.word}')"
    
    @check_type
    def __eq__(self, other):
        return len(self.word) == len(other.word)
    
    @check_type
    def __ne__(self, other):
        return len(self.word) != len(other.word)
    
    @check_type
    def __lt__(self, other):
        return len(self.word) < len(other.word)
    
    @check_type
    def __gt__(self, other):
        return len(self.word) > len(other.word)
    
    @check_type
    def __le__(self, other):
        return len(self.word) <= len(other.word)
    
    @check_type
    def __ge__(self, other):
        return len(self.word) >= len(other.word)