'''
### Key Points:
- An object is an **iterable** if it implements the `__iter__()` method, which returns an iterator.
- Lists, dictionaries, sets, tuples, and other collections are iterables, but they do not implement the `__next__()` method directly, meaning they are not iterators.
- An **iterator** is an object that implements both `__iter__()` and `__next__()` methods.
- `__iter__()` initializes the iterator and `__next__()` retrieves the next item.

- When you use an iterable (like a list or dictionary) in a `for` loop, Python automatically calls `iter(iterable)` (or `__iter__()`), which returns an iterator.
- If you use an iterator directly in a `for` loop, Python does not call `iter(iterator)` again. It simply uses the iterator as-is.
- Behind the scenes, Python calls `next()` repeatedly on the iterator to get the next item until all items have been retrieved. When all items have been iterated over, Python raises a `StopIteration` exception to stop the loop.

### Analogy:
# Consider a library (an iterable):
- The library itself is not the book—you can't read the library directly—but you can go into it and get a book.
- You can ask for a "reader" (an iterator) who will go through the books one by one.
- The reader can fetch one book (using `next()`) and move on to the next until they reach the end.
- However, the reader is one-time use only—once they have gone through all the books, they are "done."
'''
### Example:

# Iterator Class Example
class MyIterator:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self  # The iterator object itself

    def __next__(self):
        if self.start <= self.end:
            current_value = self.start
            self.start += 1  # Update the start value
            return current_value
        else:
            raise StopIteration  # No more items to iterate over

# Create an instance of MyIterator
values = MyIterator(1, 10)

# Call __next__() manually
print(values.__next__())  # Output: 1
print(values.__next__())  # Output: 2

# Using a for loop, which automatically calls __iter__() and __next__()
for i in values:
    print(i)  # Output: 3, 4, 5, 6, 7, 8, 9, 10


### What happens with list, tuple, etc.:
# A custom class representing a List that is iterable

class List:
    def __init__(self, data):
        self.data = data  # List data
    def __iter__(self):
        return ListIterator(self.data)  # Create and return a new ListIterator

class ListIterator:
    def __init__(self, list_obj):
        self.list = list_obj  
        self.index = 0  

    def __next__(self):
        if self.index < len(self.list):  
            value = self.list[self.index]
            self.index += 1  
            return value
        else:
            raise StopIteration  

# Example Usage:
my_list = List([1, 2, 3, 4, 5])
list_iterator = iter(my_list)  # Create an iterator from the list

print(next(list_iterator))  # Output: 1
print(next(list_iterator))  # Output: 2

# Using a for loop with a custom iterable
for item in my_list:
    print(item)  # Output: 3, 4, 5
