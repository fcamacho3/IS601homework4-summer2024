from faker import Faker
from decimal import Decimal
fake = Faker()

#Calculator requires a pair of numbers from, picking decimals on purpose
numPair = (Decimal(fake.random.uniform(0, 20), 2),Decimal(fake.random.uniform(0, 20), 2))

# Define four options
options = ['Add', 'Subtract', 'Multiply', 'Divide']

# Select a random option
selected_option = fake.random_element(elements=options)

# Output the results
print(f"Number Pair: {numPair}")
print(f"Selected Option: {selected_option}")