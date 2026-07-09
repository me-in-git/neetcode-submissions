class StockSpanner:

    def __init__(self):
        self.s=[]
        
    def next(self, price: int) -> int:
        if not self.s:
            self.s.append((price,1))
            return 1
        if price < self.s[-1][0]:
            self.s.append((price,1))
            return 1
        else:
            c=1
            while self.s and price >= self.s[-1][0]:
                c+=self.s[-1][1]
                self.s.pop()
            self.s.append((price,c))
            return c

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)