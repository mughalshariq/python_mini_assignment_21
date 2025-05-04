class Countdown:
    def __init__(self, start):
        self.start = start + 1  # Initialize counter (we decrement first)
    
    def __iter__(self):
        return self  # Returns the iterator object
    
    def __next__(self):
        self.start -= 1
        if self.start < 0:
            raise StopIteration  # Signal iteration complete
        return self.start

# Test the iterable
print("Countdown from 5:")
for num in Countdown(5):
    print(num, end=" ")  # Prints: 5 4 3 2 1 0

print("\n\nCountdown from 3:")
for num in Countdown(3):
    print(num, end=" ")  # Prints: 3 2 1 0

# Manual iteration demonstration
print("\n\nManual iteration:")
counter = Countdown(2)
print(next(counter))  # 2
print(next(counter))  # 1
print(next(counter))  # 0
try:
    print(next(counter))  # Raises StopIteration
except StopIteration:
    print("Countdown finished!")