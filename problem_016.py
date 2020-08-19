class OrderLog:
    def __init__(self, size):
        self.log = []
        self.size = size

    def  __repr__(self):
        return str(self.log)

    def record(self, order_id):
        self.log.append(order_id)
        if len(self.log) > self.size:
            self.log.pop(0)
    
    def get_last(self, i):
        return self.log[-i]

log = OrderLog(6)
log.record(1)
log.record(2)
log.record(3)
assert log.log == [1, 2, 3]
log.record(4)
log.record(5)
log.record(6)
assert log.log == [1, 2, 3, 4, 5, 6]
log.record(7)
log.record(8)
log.record(9)
assert log.log == [4, 5, 6, 7, 8, 9]
assert log.get_last(3) == 7
assert log.get_last(5) == 5
assert log.get_last(1) == 9


