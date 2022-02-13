class FirstHundredGenerator:
    def __init__(self):
        self.number = 0

# 🖇
    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()


my_gen = FirstHundredGenerator()
print(my_gen.number)
# 🖇
next(my_gen)
print(my_gen.number)
