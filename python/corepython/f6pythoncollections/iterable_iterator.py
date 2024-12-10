'''

Iterable- eg: range, list, tuple, set, dic, string, files
is a python object that can return an 'iterator' (using __iter__() mtd) 
which means it can be used in the contexts where iteration is required.
so that it can be traversed through all elements(iterator aanu ith cheyyanath)

...................

iterator- 
is a python object that represents a stream of data & has ability to traversed through all elements
it holds the state & keeps track of current position of iteration
elements onnum emmory yil store cheyyilla. demand anusarich generate cheyyum(using next mtd)
have __iter__() and __next__()) mtd 

....................

eg:library. (iterable)
The library itself is not the book—you cant read the library directly—but you can go into it and get a book.
You can ask for a "reader" (an iterator) who will go through the books one by one.
The reader can fetch one book (using next()) and move on to the next until they reach the end.
but is one-time use only—once the reader has gone through the books, they are "done."

......................

eg: in list for loop use cheyyumbo,
python automatically handles iter next and stopiteration exception

so where iter next is used . it is used where we need more manual control
read below example


'''



log_lines = [
    "Start of log",
    "Meta Data: blah",
    "Error: Something went wrong",
    "Info: This is just a message",
    "Error: Another issue occurred",
    "End of log"
]

# Create an iterator for the log lines
iterator = iter(log_lines)

# Skip the first two lines (headers/meta data)
next(iterator)
next(iterator)

# Now process the lines and stop when we encounter an 'Error'
for line in iterator:
    print(f"Processing: {line}")
    if "Error" in line:
        print("Found an error! Stopping.")
        break
