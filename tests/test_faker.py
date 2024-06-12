# pylint: disable=unnecessary-dunder-call, invalid-name, line-too-long, trailing-whitespace, missing-final-newline
''' This file tests the use of Faker library'''
from decimal import Decimal
from faker import Faker
fake = Faker()

#Calculator requires a pair of numbers from, picking decimals on purpose
numPair = (Decimal(f"{fake.random.uniform(0, 20):.2f}"),
           Decimal(f"{fake.random.uniform(0, 20):.2f}"))

# Define four options
options = ['Add', 'Subtract', 'Multiply', 'Divide']

# Select a random option
selected_option = fake.random_element(elements=options)

# Output the results
print(f"Number Pair: {numPair}")
print(f"Selected Option: {selected_option}")


# def test_print_num_records(num_records):
#     """Test function that prints the number of records."""
#     print(f"\nNumber of records: {num_records}")
#     # Assuming you want to assert something based on num_records
#     assert int(num_records) >= 0, "Number of records should be non-negative"