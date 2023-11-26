import random 


# Generate random numbers
random_numbers = []
for i in range (0,10000):
    number = random.randint(0,10)
    random_numbers.append(number)

writer = open('random_numbers.txt', 'w')
for number in random_numbers:
    writer.write(str(number) + '\n')
writer.close()


