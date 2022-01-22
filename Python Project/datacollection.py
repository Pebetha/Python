cart = []
#cart = [['Test',15,1],["Test",15,1]]

def countitem():
    count = 0
    for i in cart:
        count = count + i[2]

    return count

def Confirm():
    total = 0
    for i in cart:
        total = total + i[1] * i[2]
    return total