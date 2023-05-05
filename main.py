print("Random Number Generator\n")
def generate_random_numbers(seed, n):
    random_numbers = [seed]
    for i in range(n-1):
        new_number = (5 * random_numbers[i] + 1) % 8
        random_numbers.append(new_number)
    return random_numbers

random_numbers = generate_random_numbers(seed=0, n=10)
print(random_numbers)
