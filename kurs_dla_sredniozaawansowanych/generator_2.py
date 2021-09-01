import random

def cooking_artificial_intelligence(number_of_values,asserted_sum):
        trial = 0
        numbers = list(range(number_of_values))
        while True:
            trial += 1
            for i in range(number_of_values):
                numbers[i] = random.randint(1, 101)
            if sum(numbers) == asserted_sum:
                yield(trial,numbers)
                trial = 0


for i in range(10):
    (number_of_trials, numbers) = next(cooking_artificial_intelligence(3, 100))
    print(number_of_trials, numbers)


