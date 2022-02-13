class FirstHundredGenerator:
    def __init__(self):
        self.number = 0


    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()

    # 🔃
    def __iter__(self):
        return self

# 🔃
# No longer need this
# class FirstHundredIterable:
#     def __iter__(self):
#         return FirstHundredGenerator()

print(sum(FirstHundredGenerator()))

for i in FirstHundredGenerator():
    print(i)


# Generator comprehension ()
my_numbers_gen = (x for x in [1,2,3,4,5])
print(next(my_numbers_gen))
