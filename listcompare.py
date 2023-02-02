list1 = []
list2 = []

def listcheck(li1, li2):
    print("This is a list of removed songs:")
    print(list(set(list1) - set(list2)))
    print('----------------------------------------------------------------------')
    print("This is a list of added songs")
    print(list(set(list2) - set(list1)))

listcheck(list1, list2)