class MoneyBox:
    def __init__(self, capacity):
	    # конструктор с аргументом – вместимость копилки
        self.capacity = capacity
        self.coins = 0

    def can_add(self, v):
        # True, если можно добавить v монет, False иначе
	    return (self.capacity - self.coins - v) >= 0

    def add(self, v):
        # положить v монет в копилку
        self.coins += v

x = MoneyBox(10)
print(x.can_add(11))