"""
Python3 has 5 sequence types built in:
The string type
List
Tuple
Range
Bytes and byteArray

sequence:
In Python, a sequence is a generic term for an ordered set of elements.
There are several types of sequences, with the most common ones being lists, tuples, and strings, range, byte and byte array.
 Here are some important things to remember about sequences in Python, along with tips and tricks to understand and
 differentiate among them:

1. Common Characteristics:
Indexing: Elements in a sequence are accessed using indices, starting from 0.
Slicing: You can extract sub-sequences using slicing notation (sequence[start:stop:step]).
Iteration: Sequences support iteration using loops.
2. Types of Sequences:
Lists (list): Mutable, can be modified after creation. Defined using square brackets [].
Tuples (tuple): Immutable, cannot be modified after creation. Defined using parentheses ().
Strings (str): Immutable sequences of characters. Defined using single or double quotes.
3. Differences and Use Cases:
Mutability: Lists are mutable, meaning you can modify, add, or remove elements. Tuples and strings are immutable.
Syntax: Lists use square brackets [], tuples use parentheses (), and strings use quotes ('' or "").
Performance: Because of immutability, tuples and strings can be more efficient in certain situations than lists.
4. Memory and Performance Tips:
Memory Efficiency: Tuples and strings, being immutable, generally require less memory than lists.

List Methods: Lists have more built-in methods for manipulation
(e.g., append(), extend(), pop()).

String Methods: Strings have methods specifically designed for string manipulation
(e.g., upper(), lower(), replace()).


5. Remembering Methods:

Use dir(): To see all available methods for a particular sequence, use the dir() function.
"""
my_list = [1, 2, 3]
print(dir(my_list)) #prints all inbuilt available methods of a List

#Use help(): For more detailed information on a method, use the help() function.
help(my_list.append)
#output - Help on built-in function append:
#append(object, /) method of builtins.list instance
 #   Append object to the end of the list.

"""
6. Sequences and Iteration:
Common Looping: Sequences can be easily looped through using for loops.
"""
for element in my_list:
    print(element)
#output - 1 2 3 in y axis
"""
7. Built-in Functions:
len(): Returns the length of a sequence.
max() and min(): Find the maximum and minimum values in a sequence.
sum(): Sum all elements in a numerical

range:
In Python, range is a built-in function that generates a sequence of numbers. 
It is commonly used in for loops to iterate a specific number of times. it cannot be concatenated

Syntax:

range(stop)
range(start, stop, step)
stop: The end value of the range (exclusive).
start: The starting value of the range (default is 0).
step: The step size (default is 1).
Examples:
"""
# Example 1:
for i in range(5):
    print(i)
# Output: 0 1 2 3 4

# Example 2:
for i in range(1, 10, 2):
    print(i)
# Output: 1 3 5 7 9
"""
bytes and bytearray:
Both bytes and bytearray are used to represent sequences of bytes (8-bit values) in Python. 
However, they have some key differences:

bytes:
Immutable: Once created, the content cannot be changed.
Created using the bytes() constructor or by using the b prefix before a literal.
Example:
"""
byte_sequence = bytes([65, 66, 67, 68])  # ASCII values for 'A', 'B', 'C', 'D'
print(byte_sequence)
# Output: b'ABCD'

"""
bytearray:
Mutable: You can modify the elements after creation.
Created using the bytearray() constructor.
Example:
"""

byte_array = bytearray([65, 66, 67, 68])
print(byte_array)
# Output: bytearray(b'ABCD')

byte_array[0] = 69  # Change the first element to the ASCII value of 'E'
print(byte_array)
# Output: bytearray(b'EDCD')
"""
Use Cases:
bytes is often used for immutable sequences of bytes, such as representing fixed data.
bytearray is used when you need a mutable sequence of bytes, like when you want to modify individual elements.
Summary:
range: Generates a sequence of numbers used in iteration.
bytes: Immutable sequence of bytes.
bytearray: Mutable sequence of bytes.
Remember that bytes represent binary data, and operations on them are different from operations on strings or other sequences of characters.
"""
