class Fruits:
    # constructor method
    def __init__(self, price,shape,name):
        self.price = price
        self.shape = shape
        self.name = name
    def display(self):
        print(f"My favorite fruits are {self.shape} and {self.name} and it costs {self.price}")

# create instance of a class(object)

myobj=Fruits(10,"oval","apple")
myobj.display()
