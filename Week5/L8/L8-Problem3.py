class Item(object):
    def __init__(self, name, value, weight, density):
        self.name = name
        self.value = float(value)
        self.weight = float(weight)
        self.density = float(density)

    def getName(self):
        return self.name

    def getValue(self):
        return self.value

    def getWeight(self):
        return self.weight

    def getDensity(self):
        return self.density

    def __str__(self):
        objectName = '<' + self.getName() + \
                     ', v:' + str(self.getValue()) + \
                     ', w:' + str(self.getWeight()) + \
                     ', d:' + str(self.getDensity())
        return objectName


def itemBuilder():
    names = ['clock', 'picture', 'radio', 'vase', 'book', 'computer']
    prices = [175.0, 90.0, 20.0, 50.0, 10.0, 200.0]
    weight = [10.0, 9.0, 4.0, 2.0, 1.0, 20.0]
    pricePerKg = [prices[i]/weight[i] for i in range(len(names))]
    itemList = [Item(names[i], prices[i], weight[i], pricePerKg[i])
                for i in range(len(names))]
    return itemList


def printList(lista):
    print 'len: ', len(lista)
    for l in lista:
        print l


def metric1(listItems=itemBuilder(), carry=20):
    listItemsCopy = sorted(listItems, key=lambda Item: -Item.getValue())
    carried = []
    for i in listItemsCopy:
        if not i.getWeight() > carry:
            carried.append(i)
            carry -= i.getWeight()
    return carried


def metric2(listItems=itemBuilder(), carry=20):
    itemCopy = sorted(listItems, key=lambda Item: Item.getWeight())
    carried = []
    for i in itemCopy:
        if not i.getWeight() > carry:
            carried.append(i)
            carry -= i.getWeight()
    return carried


def metric3(listItems=itemBuilder(), carry=20):
    printList(listItems)
    itemCopy = sorted(listItems, key=lambda Item: -Item.getDensity())
    printList(itemCopy)
    carried = []
    for i in itemCopy:
        if not i.getWeight() > carry:
            carried.append(i)
            carry -= i.getWeight()
    printList(carried)
    return carried

metric3()
