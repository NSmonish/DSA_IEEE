class StockSpanner(object):

    def __init__(self):
        self.arr = []

    def next(self, price):
        span=1 #initializing span as 1 (itself)
        while self.arr and price>=self.arr[-1][0]:  #checking if any previous elements has higher price
            span = span + self.arr[-1][1] #if not add to span count
            self.arr.pop()      #removing the element
        self.arr.append((price, span))    #adding price and the respective span into array
        return span
