class Mom:
    def __init__(self):
        self.eyes = "blue"


class Dad:
    def __init__(self):
        self.hair = "black"


class Kid(Mom, Dad):
    def __init__(self):
        Mom.__init__(self)   # get Mom's data
        Dad.__init__(self)   # get Dad's data
        self.name = "Tom"

    def __str__(self):
        return f"Kid(name={self.name}, eyes={self.eyes}, hair={self.hair})"


k = Kid()
print(k)