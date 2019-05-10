# Birthday paradox (birthday probability)
import random

class_size = random.randint(23, 100)  # Generate a class of random size

num_trials = 1000

dupe_count = 0
found_dupe = False

for trials in range(num_trials):
    # Generate birthdays
    birthdays = []
    for i in range(class_size):
        new_bd = random.randrange(365)
        birthdays.append(new_bd)

    # Find duplicates
    found_dupe = False
    for n in birthdays:
        if birthdays.count(n) > 1:
            found_dupe = True

    # Count the no of duplicates
    if found_dupe:
        dupe_count += 1

prob = dupe_count/num_trials
print("Probability of shared birthday in a class of", class_size, "is:", prob)
