
import random

# =====================================================
# 1. random() - Generate a random decimal between 0 and 1
# =====================================================

number = random.random()

print("Random decimal:", number)


# =====================================================
# 2. randint() - Generate a random integer
# =====================================================

number = random.randint(1, 100)

print("Random integer:", number)


# =====================================================
# 3. randrange() - Generate a random number in a range
# =====================================================

number = random.randrange(0, 100, 5)

print("Random number with steps of 5:", number)


# =====================================================
# 4. uniform() - Generate a random floating-point number
# =====================================================

number = random.uniform(1, 10)

print("Random floating-point number:", number)


# =====================================================
# 5. choice() - Select one random item from a sequence
# =====================================================

fruits = ['Apple', 'Banana', 'Orange', 'Mango', 'Grapes']

random_fruit = random.choice(fruits)

print("Random fruit:", random_fruit)


# =====================================================
# 6. choices() - Select multiple random items
# =====================================================

random_fruits = random.choices(fruits, k=3)

print("Three random fruits:", random_fruits)


# =====================================================
# 7. sample() - Select unique random items
# =====================================================

random_fruits = random.sample(fruits, k=3)

print("Three unique fruits:", random_fruits)


# =====================================================
# 8. shuffle() - Randomly rearrange a list
# =====================================================

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

random.shuffle(numbers)

print("Shuffled numbers:", numbers)


# =====================================================
# 9. seed() - Make random results reproducible
# =====================================================

random.seed(10)

print("Seeded number 1:", random.randint(1, 100))
print("Seeded number 2:", random.randint(1, 100))

# Running this program again with the same seed
# produces the same sequence of numbers.


# =====================================================
# 10. getrandbits() - Generate random bits
# =====================================================

number = random.getrandbits(8)

print("Random 8-bit integer:", number)


# =====================================================
# 11. Random data generation
# =====================================================

# Generate random student marks

student_marks = []

for student in range(10):
    mark = random.randint(0, 100)
    student_marks.append(mark)

print("Student marks:", student_marks)


# Generate random names

names = ['Alex', 'John', 'Sarah', 'David', 'Emma']

for student in range(5):
    name = random.choice(names)
    print("Student:", name)


# =====================================================
# 12. Weighted random choices
# =====================================================

items = ['Common', 'Rare', 'Epic', 'Legendary']

# Each item's weight represents its relative probability.

result = random.choices(
    items,
    weights=[70, 20, 8, 2],
    k=1
)

print("Random reward:", result[0])


# =====================================================
# 13. Practical example - Dice simulator
# =====================================================

def roll_dice():
    dice = random.randint(1, 6)
    return dice


for roll in range(5):
    print("Dice roll:", roll_dice())


# =====================================================
# 14. Practical example - Random password generator
# =====================================================

import string

characters = string.ascii_letters + string.digits + string.punctuation

password = ''.join(random.choices(characters, k=12))

print("Generated password:", password)


# =====================================================
# 15. Practical example - Random lottery
# =====================================================

lottery_numbers = random.sample(range(1, 50), 6)

print("Lottery numbers:", sorted(lottery_numbers))
