class ReverseIteration:
    def __init__(self, numbers):
        self.nums = numbers
        self.index = len(numbers) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        value = self.nums[self.index]
        self.index -= 1
        return value


numbers = [10, 20, 30, 40, 50]
result = ReverseIteration(numbers)

for num in result:
    print(num)
