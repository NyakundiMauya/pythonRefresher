def reg(name,age,gender):
    print(f"studename is: {name} Age:{age} Gender:{gender} ")
reg("John","18","Male")


def fullname(fname, lname):
    print(f"My name is {fname} {lname} ")
fullname("Ivan", "Nyakundi")

def arbitraryArgs(*names):
    print(f"The oldest child is {names}")
arbitraryArgs("Ivan", "Nyakundi", "Mary", "Vincent")

# def keyArgs(**):?