print(__name__)
def buy(item):
    cart = []
    cart.append(item)
    return cart

if __name__ == '__main__':
    print("this won't be printed, because this is not the main file")