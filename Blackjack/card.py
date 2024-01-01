class Card:

    def __init__(self, type) -> None:
        self.type = type
        if isinstance(type, int):
            self.value = type
        elif type == "King" or type == "Queen" or type == "Jack":
            self.value = 10
        else:
            self.value = 11
        

        def __str__(self):
            return "is this working?"
