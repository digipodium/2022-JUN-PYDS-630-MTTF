# contructor

class Paratha:

    def __init__(self,typ,price):
        self.type = typ # object variable
        self.price = price

    def display(self):
        print(f"{self.type} : ${self.price}")


if __name__ == "__main__":
    ap = Paratha("Aloo Paratha",30)    # object creation
    bp = Paratha("Paneer Paratha",50)
    pp = Paratha('Pyaaz Paratha',40)
    mp = Paratha('Muli Paratha',40)

    print("today menu")
    ap.display()
    bp.display()
    pp.display()
    mp.display()