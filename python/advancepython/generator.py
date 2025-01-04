# Iterator: An object that allows iterating over a sequence (e.g., list, tuple) and fetching one value at a time.
# Issue: To create an iterator, we need to define two methods: __iter__() and __next__()

# However, we often want Python to handle this process for us automatically.
# This is where generators come in.

# Generator: A function that produces an iterator. It uses the 'yield' keyword to return values one at a time.
# When a function contains 'yield', it becomes a generator, meaning it doesn't run all at once, but yields a value each time it is called.

# Key Difference between 'yield' and 'return':
# - 'yield' returns a value like 'return', but it doesn't terminate the function. 
# - Each time 'yield' is encountered, the function state is saved and can resume from where it left off.
# - In contrast, 'return' ends the function execution immediately after returning a value.

# Why Use Generators?
# - Generators are memory-efficient: Instead of loading all records into memory at once, they generate values on-the-fly.
# - Ideal when dealing with large datasets or streams of data.


# Example of Generator function using 'yield':
def my_generator(start, end):
    while start <= end:
        yield start
        start += 1

# Using the generator
for number in my_generator(1, 5):
    print(number)


'''

import sqlite3

def fetch_data_from_db():
    connection = connect_to_database()  # Assuming this is a function that connects to your database
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM large_table")
    
    # Fetch all rows at once (this may use a lot of memory for large datasets)
    records = cursor.fetchall()  # This retrieves all rows into memory
    
    for record in records:
        print(record)  # Process each record from the fetched data
# .......................
# Hypothetical database query function that returns data in chunks
def fetch_data_from_db():
    connection = connect_to_database()  # Some database connection
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM large_table")
    
    for row in cursor:
        yield row  # Yield one row at a time

# Using the generator
for record in fetch_data_from_db():
    print(record)  # Process each record as it's fetched
'''