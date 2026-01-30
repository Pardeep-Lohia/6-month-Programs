"""
Python Concepts: Comprehensive Guide and Cheatsheet

This file serves as an in-depth reference and learning resource for Python programming concepts, ranging from fundamental basics to advanced topics. It combines theoretical explanations with practical code examples to demonstrate how each concept works in real-world scenarios.

Key Features:
- Structured sections covering all major Python concepts
- Detailed explanations with code demonstrations
- Covers syntax, data types, control flow, OOP, and more
- Suitable for beginners to advanced learners
- Run this script to execute all examples and see outputs
- Expanded with additional modules, best practices, and edge cases

Usage:
- Read the comments and docstrings for explanations
- Execute the code to observe behavior
- Modify examples to experiment and learn

Note: This guide assumes Python 3.x. Some features (like match statements) require Python 3.10+.
"""

# 1. Python Basics & Syntax
"""
Python Basics & Syntax: This section covers the fundamental building blocks of Python programming.

What is Python:
- Python is a high-level, interpreted programming language created by Guido van Rossum in 1991.
- It's known for its simplicity, readability, and versatility.
- Python emphasizes code readability with its clean syntax and extensive use of whitespace.
- Python follows the philosophy "There should be one—and preferably only one—obvious way to do it" (The Zen of Python).

Key Features:
- Easy to learn: Simple syntax similar to English, making it beginner-friendly.
- Cross-platform: Runs on Windows, macOS, Linux, and more.
- Extensive libraries: Rich ecosystem of modules for various tasks (web development, data science, AI, etc.).
- Dynamic typing: Variables can change types during execution.
- Automatic memory management: Garbage collection handles memory allocation/deallocation.
- Interpreted language: Code is executed line by line, allowing for interactive development.
- Batteries included: Extensive standard library for common tasks.

Python Versions:
- Python 2.x: Legacy version, reached end-of-life on January 1, 2020. Not recommended for new projects.
- Python 3.x: Current major version, with significant improvements over 2.x.
- Major versions: 3.6 (f-strings), 3.7 (dataclasses), 3.8 (walrus operator), 3.9 (dict union), 3.10 (match statement), 3.11 (performance improvements), 3.12 (per-interpreter GIL).
- Use python --version or python3 --version to check installed version.

Installation:
- Official website: python.org - Download and install the latest stable version.
- Package managers: apt (Ubuntu), brew (macOS), chocolatey (Windows).
- Virtual environments: venv or conda for isolated project environments.
- IDEs: VS Code, PyCharm, Jupyter Notebook for development.

Python Interpreter:
- The Python interpreter reads and executes Python code.
- It translates high-level Python code into machine-readable bytecode.
- The interpreter includes the Python Virtual Machine (PVM) that executes the bytecode.
- CPython: Standard implementation in C.
- Alternatives: PyPy (JIT compiler), Jython (JVM), IronPython (.NET), MicroPython (embedded).

Execution Modes:
- Interactive mode: Type commands directly in the Python shell (python or python3 in terminal).
  - Useful for testing small code snippets, learning, and debugging.
  - Commands are executed immediately, results displayed.
  - Exit with Ctrl+D (Unix) or Ctrl+Z (Windows).
- Script mode: Write code in .py files and run with 'python filename.py'.
  - Used for larger programs and automation scripts.
  - Code is compiled to bytecode (.pyc files in __pycache__) on first run.
  - Command-line arguments accessible via sys.argv.
- IDE execution: Run scripts directly from editors like VS Code, PyCharm.
- Jupyter notebooks: Interactive execution in browser-based environment.

Indentation Rules:
- Python uses indentation to define code blocks instead of curly braces {} like many other languages.
- Consistent indentation is crucial - mixing spaces and tabs can cause IndentationError.
- Standard practice: Use 4 spaces per indentation level (PEP 8 style guide).
- All statements in a block must have the same indentation level.
- Indentation defines scope: functions, classes, loops, conditionals.

Comments:
- Single-line comments: Start with #, everything after is ignored until end of line.
- Multi-line comments/docstrings: Use triple quotes for multi-line strings.
- Docstrings: Special multi-line strings at the start of functions/classes/modules that document their purpose.
- Comments improve code readability and maintainability.
- PEP 257 defines docstring conventions.

Keywords: Reserved words like if, for, class, etc. Full list: and, as, assert, break, class, continue, def, del, elif, else, except, False, finally, for, from, global, if, import, in, is, lambda, None, nonlocal, not, or, pass, raise, return, True, try, while, with, yield
Identifiers: Names for variables, functions, etc. (letters, digits, underscore, not starting with digit, not keyword).
Statements vs Expressions: Statements perform actions, expressions evaluate to values.
Line continuation: Use \\ or implicit in brackets/parentheses.
Code blocks & scope: Defined by indentation.

Best Practices:
- Use meaningful variable names following snake_case convention.
- Add comments for complex logic, not obvious code.
- Follow PEP 8 style guidelines for consistent formatting.
- Use docstrings for all public functions, classes, and modules.
- Keep lines under 79 characters (PEP 8).
- Use spaces around operators and after commas.
"""
# Example: Indentation and comments
if True:  # This is a single-line comment
    print("Hello, Python!")  # Indented block

"""
Keywords: Reserved words like if, for, class, etc. Full list: and, as, assert, break, class, continue, def, del, elif, else, except, False, finally, for, from, global, if, import, in, is, lambda, None, nonlocal, not, or, pass, raise, return, True, try, while, with, yield
Identifiers: Names for variables, functions, etc. (letters, digits, underscore, not starting with digit).
Statements vs Expressions: Statements perform actions, expressions evaluate to values.
Line continuation: Use \\ or implicit in brackets.
Code blocks & scope: Defined by indentation.
"""

# 2. Variables & Assignment
"""
Variables & Assignment: This section explores how Python handles variables, assignment, and memory management.

Variable Naming Rules:
- Must start with a letter (a-z, A-Z) or underscore (_)
- Can contain letters, digits (0-9), and underscores
- Cannot contain spaces or special characters
- Case-sensitive: 'var', 'Var', and 'VAR' are different variables
- Cannot use Python keywords as variable names
- Convention: Use snake_case for variables (e.g., my_variable)

Dynamic Typing:
- Variables don't have fixed types; they can hold any data type
- Type is determined at runtime based on assigned value
- Same variable can hold different types during execution
- No need to declare variable types explicitly

Reassignment:
- Variables can be reassigned to new values
- Can change both value and type in the process
- Previous value is discarded (unless referenced elsewhere)

Multiple Assignment:
- Assign same value to multiple variables: a = b = c = 10
- Unpack sequences: a, b = 1, 2 (tuple unpacking)
- Extended unpacking: a, *rest = [1, 2, 3, 4] (Python 3+)

Swapping Variables:
- Traditional way: temp = a; a = b; b = temp
- Python way: a, b = b, a (tuple packing/unpacking)

Reference vs Value Semantics:
- Immutable objects (int, str, tuple): Assignment copies the value
- Mutable objects (list, dict, set): Assignment creates a reference
- Changes to mutable objects affect all references

Object Identity:
- Every object has a unique identity (memory address)
- id() function returns the identity as an integer
- 'is' operator compares identity, '==' compares values
- Small integers and strings may share identities (interning)

Garbage Collection:
- Automatic memory management system
- Reference counting: Objects deleted when reference count reaches zero
- Cyclic garbage collector handles circular references
- No need for manual memory management

Del Keyword:
- Removes variable name from namespace
- Decrements reference count of the object
- Object may still exist if other references exist
- Can delete list elements, dict keys, etc.

Reference Counting:
- Python uses reference counting to track how many references point to an object
- When reference count reaches zero, object is deallocated
- sys.getrefcount(obj) returns current reference count
- Reference counting is automatic but can be observed

Weak References:
- weakref module provides weak references that don't increase reference count
- Useful for caches, circular references, and avoiding memory leaks
- weakref.ref() creates a weak reference
- weakref.WeakValueDictionary, WeakKeyDictionary for weak collections

del vs None:
- del removes variable name from namespace, potentially decreasing reference count
- Setting to None keeps the name but allows garbage collection of the object
- del is more explicit about removing the reference
- Use del for cleanup, None for optional attributes

Best Practices:
- Use descriptive variable names
- Avoid single-character names except for loops/counters
- Don't use built-in names as variables (shadowing)
- Use constants for values that shouldn't change
- Understand reference counting for memory management
- Use weak references for caches to prevent memory leaks
"""
import sys
import weakref

a = b = c = 10
print(f"Multiple assignment: a={a}, b={b}, c={c}")
print(f"Reference count of 10: {sys.getrefcount(10)}")

x, y = 1, 2
print(f"Unpacking: x={x}, y={y}")

x, y = y, x  # Swapping
print(f"Swapped: x={x}, y={y}")

print(f"ID of x: {id(x)}")

# Weak reference example
class MyClass:
    def __init__(self, value):
        self.value = value

obj = MyClass(42)
weak_ref = weakref.ref(obj)
print(f"Weak ref: {weak_ref()}")
del obj
print(f"After del obj: {weak_ref()}")  # None

# del vs None
lst = [1, 2, 3]
lst_ref = lst  # Another reference
lst = None  # Object still exists via lst_ref
print(f"After None: {lst_ref}")

del lst_ref  # Now object can be garbage collected
# print(lst_ref)  # NameError

# 3. Data Types (Built-in)
"""
Data Types in Python: Python provides several built-in data types that are fundamental to programming. They are categorized into immutable and mutable types, which affects how they behave in memory and operations.

Immutable Types (cannot be modified after creation):
- int: Integer numbers (arbitrary precision, no overflow)
- float: Floating-point numbers (IEEE 754 double precision)
- complex: Complex numbers with real and imaginary parts
- bool: Boolean values (True/False, subclasses of int)
- str: Unicode strings (immutable sequences of characters)
- tuple: Immutable sequences of objects
- frozenset: Immutable sets (unordered collections of unique elements)
- bytes: Immutable sequences of bytes

Mutable Types (can be modified in place):
- list: Ordered, mutable sequences of objects
- set: Mutable, unordered collections of unique elements
- dict: Mutable mappings of key-value pairs
- bytearray: Mutable sequences of bytes

Special Types:
- NoneType: Represents the absence of a value (None object)

Type Conversion Functions:
- int(x, base=10): Convert to integer (with optional base for strings)
- float(x): Convert to floating-point number
- str(x): Convert to string representation
- bool(x): Convert to boolean (truthy/falsy evaluation)
- complex(real, imag): Create complex number
- list(iterable): Convert iterable to list
- tuple(iterable): Convert iterable to tuple
- set(iterable): Convert iterable to set
- dict(iterable): Create dictionary from key-value pairs
- frozenset(iterable): Convert iterable to immutable set
- bytes(iterable): Convert to immutable bytes
- bytearray(iterable): Convert to mutable byte array

Type Inspection:
- type(obj): Returns the type object of the given object
- isinstance(obj, classinfo): Checks if obj is an instance of classinfo or its subclasses
- issubclass(class, classinfo): Checks if class is a subclass of classinfo

Mutability Concepts:
- Immutable objects: Once created, their value cannot be changed. Operations that appear to modify them actually create new objects.
- Mutable objects: Can be modified in place, which affects all references to the same object.
- This distinction is crucial for understanding reference semantics and avoiding bugs.

Type Hints (Python 3.5+):
- Type hints provide static type checking and better IDE support
- Use typing module for complex types
- Optional[T] is equivalent to Union[T, None]
- Any represents any type (disables type checking)

Union Types:
- Union[X, Y] represents a value that can be either X or Y
- Can be written as X | Y in Python 3.10+
- Useful for function parameters that accept multiple types

Optional Types:
- Optional[T] = Union[T, None]
- Commonly used for parameters that can be None
- Example: def func(param: Optional[str] = None)

Any Type:
- Any accepts any type
- Used when you don't know the type or want to disable checking
- Import from typing: from typing import Any

Best Practices:
- Choose the appropriate data type for your use case (list vs tuple, set vs list)
- Be aware of mutability when passing objects to functions
- Use isinstance() for type checking rather than direct type comparison
- Understand that bool is a subclass of int (True == 1, False == 0)
- Use type hints for better code documentation and IDE support
- Import typing constructs: from typing import Optional, Union, Any, List, Dict, etc.

Cross-references:
- See Section 2 (Variables & Assignment) for mutability concepts and reference semantics
- See Section 11 (Data Structures) for detailed data structure usage
- See Section 24 (Advanced Core Concepts) for hashability and truthy/falsy values
- See Section 29 (Collections Module) for specialized container types
"""
# Type hints examples (Python 3.5+)
from typing import Optional, Union, Any, List, Dict

def greet(name: str) -> str:
    return f"Hello, {name}!"

def process_data(data: Union[List[int], Dict[str, int]], flag: Optional[bool] = None) -> Any:
    if isinstance(data, list):
        return sum(data)
    else:
        return sum(data.values())

print(f"Type hinted function: {greet('Alice')}")
print(f"Union/Optional example: {process_data([1,2,3])}")
print(f"Union/Optional example: {process_data({'a':1, 'b':2})}")
# Examples
num = 42  # int
pi = 3.14  # float
comp = 1 + 2j  # complex
flag = True  # bool
text = "Hello"  # str
tup = (1, 2, 3)  # tuple
frozen = frozenset([1, 2, 3])  # frozenset
byts = b"bytes"  # bytes

lst = [1, 2, 3]  # list
st = {1, 2, 3}  # set
dct = {"key": "value"}  # dict
bytearr = bytearray(b"mutable")  # bytearray

nothing = None  # NoneType

print(f"Type of num: {type(num)}")
print(f"Is num int? {isinstance(num, int)}")

# Type conversion
str_num = str(num)
print(f"Converted to str: {str_num}, type: {type(str_num)}")

# Mutability demo
lst.append(4)  # Mutable
print(f"List after append: {lst}")

# tup.append(4)  # Would raise AttributeError, immutable

# 4. Numeric Concepts
"""
Numeric Types in Python: Python provides three built-in numeric types for mathematical operations. Understanding their characteristics and operations is crucial for numerical programming.

Integer Type (int):
- Arbitrary precision: No fixed size limit (unlike C/Java int types)
- Can represent arbitrarily large integers
- Operations: +, -, *, //, %, **, etc.
- No overflow: Numbers grow as needed
- Memory efficient for small integers (interning)

Floating-Point Type (float):
- IEEE 754 double precision (64-bit)
- Approximate decimal numbers
- Range: ~1.8 × 10^308 to ~1.8 × 10^-308
- Precision: About 15 decimal digits
- Special values: float('inf'), float('-inf'), float('nan')
- Limitations: Floating-point arithmetic can have precision errors

Complex Type (complex):
- Form: real + imaginary*j (where j is the imaginary unit)
- Real and imaginary parts are floats
- Operations: +, -, *, /, ** supported
- Access parts: .real, .imag attributes
- Useful for mathematical computations, signal processing

Arithmetic Operations:
- Addition: a + b
- Subtraction: a - b
- Multiplication: a * - b
- Division: a / b (always produces float)
- Floor Division: a // b (integer division, truncates toward negative infinity)
- Modulo: a % b (sign follows divisor)
- Power: a ** b (or pow(a, b))

Division Behavior:
- / always returns float, even for integer operands
- // performs floor division, returns integer type
- % modulo operation follows the sign of the divisor
- divmod(a, b) returns (a//b, a%b) as a tuple

Operator Precedence (PEMDAS):
1. Parentheses: ()
2. Exponentiation: **
3. Unary: +x, -x
4. Multiplication/Division: *, /, //, %
5. Addition/Subtraction: +, -

Augmented Assignment:
- Shorthand for: x = x + 1 becomes x += 1
- Available for: +=, -=, *=, /=, //=, %=, **=
- More efficient, modifies in-place when possible

Numeric Built-in Functions:
- abs(x): Absolute value
- round(x, ndigits): Round to specified decimal places
- pow(base, exp, mod): Power with optional modulo
- divmod(a, b): Division and modulo as tuple
- bin(x), hex(x), oct(x): Convert to different bases

Best Practices:
- Use integers for counting, indexing, exact arithmetic
- Be aware of floating-point precision limitations
- Use decimal module for financial calculations requiring exact decimal representation
- Check for division by zero
- Use // for integer division when needed
"""
a = 10
b = 3
print(f"Addition: {a + b}")
print(f"Float division: {a / b}")
print(f"Integer division: {a // b}")
print(f"Modulo: {a % b}")
print(f"Power: {a ** b}")

a += 5  # Augmented
print(f"Augmented: {a}")

# Complex
c = 2 + 3j
print(f"Complex: {c}, real: {c.real}, imag: {c.imag}")

# 5. Strings (Complete)
"""
Strings in Python: Immutable sequences of Unicode characters with extensive built-in methods for manipulation.

String Creation:
- Single quotes: 'Hello'
- Double quotes: "Hello"
- Triple quotes:  (for multi-line strings)
String Operations:
- Indexing: s[0] (first character), s[-1] (last character)
- Slicing: s[start:end:step] (extract substrings)
- Concatenation: s + t (join strings)
- Repetition: s * 3 (repeat string)
- Membership: 'a' in s (check if character/substring exists)
- Comparison: s < t (lexicographical comparison)

String Properties:
- Immutability: Strings cannot be modified in place (operations create new strings)
- Unicode Support: Full UTF-8 support for international characters
- Escape Sequences: \n (newline), \t (tab), \\ (backslash), \" (quote)
- Raw Strings: r"string" (treat backslashes literally, useful for regex/file paths)

String Methods (Comprehensive):
Case Conversion:
- upper(): Convert to uppercase
- lower(): Convert to lowercase
- title(): Capitalize first letter of each word
- capitalize(): Capitalize first letter only
- swapcase(): Swap case of all characters

Whitespace Handling:
- strip(): Remove leading/trailing whitespace
- lstrip(): Remove leading whitespace
- rstrip(): Remove trailing whitespace
- expandtabs(): Expand tab characters to spaces

Searching and Finding:
- find(sub): Find first occurrence index (-1 if not found)
- rfind(sub): Find last occurrence index
- index(sub): Find first occurrence (raises ValueError if not found)
- rindex(sub): Find last occurrence (raises ValueError if not found)
- count(sub): Count occurrences of substring

String Splitting and Joining:
- split(sep): Split into list (default: whitespace)
- rsplit(sep): Split from right
- splitlines(): Split on line breaks
- join(iterable): Join strings with separator
- partition(sep): Split into 3 parts around first separator
- rpartition(sep): Split into 3 parts around last separator

String Checking/Validation:
- startswith(prefix): Check if starts with prefix
- endswith(suffix): Check if ends with suffix
- isupper(): Check if all uppercase
- islower(): Check if all lowercase
- isalpha(): Check if all alphabetic
- isdigit(): Check if all digits
- isalnum(): Check if all alphanumeric
- isspace(): Check if all whitespace
- isnumeric(): Check if all numeric characters
- isdecimal(): Check if all decimal characters
- isidentifier(): Check if valid Python identifier
- isprintable(): Check if all printable characters

String Formatting and Padding:
- center(width): Center string in width
- ljust(width): Left justify in width
- rjust(width): Right justify in width
- zfill(width): Pad with zeros on left
- format(*args, **kwargs): Format string with placeholders
- format_map(mapping): Format with mapping object

Advanced String Operations:
- replace(old, new): Replace substring
- translate(table): Translate characters using translation table
- maketrans(): Create translation table
- encode(encoding): Encode to bytes
- decode(encoding): Decode from bytes

Best Practices:
- Use f-strings for string formatting (Python 3.6+)
- Prefer raw strings for regex patterns and file paths
- Use join() for concatenating multiple strings (more efficient)
- Be aware of immutability when performing many operations
- Use appropriate string methods instead of manual character checking
"""
s = "Hello, World!"
print(f"String: {s}")
print(f"Indexing: s[0]={s[0]}, s[-1]={s[-1]}")
print(f"Slicing: s[0:5]={s[0:5]}")
print(f"Step slicing: s[::2]={s[::2]}")

# Immutability
# s[0] = 'h'  # TypeError

print(f"Escape: {'Hello\nWorld'}")
print(f"Raw: {r'Hello\nWorld'}")
print(f"Repetition: {s * 2}")
print(f"Concatenation: {s + ' Again'}")
print(f"Membership: {'World' in s}")
print(f"Comparison: {'apple' < 'banana'}")

# Unicode
uni = "Hello, 世界!"
print(f"Unicode: {uni}")

# Encoding
encoded = uni.encode('utf-8')
print(f"Encoded: {encoded}")
decoded = encoded.decode('utf-8')
print(f"Decoded: {decoded}")

# String methods examples
text = "  hello world  "
print(f"Original: '{text}'")
print(f"upper(): '{text.upper()}'")
print(f"lower(): '{text.lower()}'")
print(f"title(): '{text.title()}'")
print(f"capitalize(): '{text.capitalize()}'")
print(f"strip(): '{text.strip()}'")
print(f"lstrip(): '{text.lstrip()}'")
print(f"rstrip(): '{text.rstrip()}'")

words = "apple,banana,cherry"
print(f"split(','): {words.split(',')}")
print(f"join(['a','b','c']): {','.join(['a','b','c'])}")
print(f"replace('l','x'): {'hello'.replace('l','x')}")
print(f"find('lo'): {'hello'.find('lo')}")
print(f"count('l'): {'hello'.count('l')}")
print(f"startswith('He'): {'Hello'.startswith('He')}")
print(f"endswith('!'): {'Hello!'.endswith('!')}")
print(f"isupper(): {'HELLO'.isupper()}")
print(f"islower(): {'hello'.islower()}")
print(f"isalpha(): {'hello'.isalpha()}")
print(f"isdigit(): {'123'.isdigit()}")
print(f"isalnum(): {'hello123'.isalnum()}")
print(f"isspace(): {'   '.isspace()}")
print(f"center(20): '{s.center(20)}'")
print(f"zfill(10): {'42'.zfill(10)}")
print(f"format: {'{} {}'.format('Hello', 'World')}")
print(f"partition(','): {'a,b,c'.partition(',')}")
print(f"expandtabs(): {'a\tb'.expandtabs()}")

# 6. Operators
"""
Operators in Python: Operators are special symbols that perform operations on variables and values. Python supports various types of operators that allow for mathematical calculations, comparisons, logical operations, and more.

Arithmetic Operators:
- Addition (+): Adds two operands (e.g., a + b)
- Subtraction (-): Subtracts right operand from left (e.g., a - b)
- Multiplication (*): Multiplies two operands (e.g., a * b)
- Division (/): Divides left operand by right, always returns float (e.g., a / b)
- Floor Division (//): Divides and returns floor value (integer part) (e.g., a // b)
- Modulo (%): Returns remainder of division (e.g., a % b)
- Exponentiation (**): Raises left operand to power of right (e.g., a ** b)

Comparison Operators (return boolean):
- Equal to (==): Checks if two values are equal
- Not equal to (!=): Checks if two values are not equal
- Greater than (>): Checks if left is greater than right
- Less than (<): Checks if left is less than right
- Greater than or equal (>=): Checks if left is greater or equal
- Less than or equal (<=): Checks if left is less or equal

Logical Operators:
- and: Returns True if both operands are True
- or: Returns True if at least one operand is True
- not: Reverses the boolean value (unary operator)

Bitwise Operators (work on binary representations):
- AND (&): Sets each bit to 1 if both bits are 1
- OR (|): Sets each bit to 1 if at least one bit is 1
- XOR (^): Sets each bit to 1 if bits are different
- NOT (~): Inverts all bits (unary)
- Left Shift (<<): Shifts bits left by specified positions
- Right Shift (>>): Shifts bits right by specified positions

Assignment Operators:
- Simple assignment (=): Assigns value to variable
- Augmented assignments: Combine operation with assignment
  - +=, -=, *=, /=, //=, %=, **=, &=, |=, ^=, <<=, >>=

Identity Operators:
- is: Returns True if both variables point to same object
- is not: Returns True if variables point to different objects
- Different from == (equality) which compares values

Membership Operators:
- in: Returns True if value found in sequence
- not in: Returns True if value not found in sequence

Ternary Operator (Conditional Expression):
- Syntax: value_if_true if condition else value_if_false
- Short form of if-else statement
- Evaluates condition and returns appropriate value

Operator Precedence (order of evaluation):
1. Parentheses ()
2. Exponentiation **
3. Unary +x, -x, ~x
4. Multiplication *, /, //, %
5. Addition +, -
6. Bitwise shifts <<, >>
7. Bitwise AND &
8. Bitwise XOR ^
9. Bitwise OR |
10. Comparisons ==, !=, >, <, >=, <=
11. Identity is, is not
12. Membership in, not in
13. Logical not
14. Logical and
15. Logical or
16. Ternary conditional

Best Practices:
- Use parentheses for clarity when operator precedence is unclear
- Be careful with floating-point comparisons (use math.isclose for floats)
- Understand short-circuiting in logical operators (and/or stop at first decisive result)
- Use identity operators (is) for None checks and singleton comparisons
- Avoid complex expressions; break them into multiple statements for readability
"""
a, b = 10, 5
print(f"Arithmetic: {a} + {b} = {a + b}")
print(f"Comparison: {a} > {b} = {a > b}")
print(f"Logical: {a > 0 and b > 0} = {a > 0 and b > 0}")
print(f"Bitwise: {a} & {b} = {a & b}")
print(f"Identity: {a is b} = {a is b}")
print(f"Membership: {5 in [1,2,3,4,5]} = {5 in [1,2,3,4,5]}")
print(f"Ternary: {'even' if a % 2 == 0 else 'odd'}")

# 7. Input & Output
"""
input(): Reads string from stdin.
Type conversion: int(input())
print(): Outputs to stdout.
sep: Separator between args.
end: End character.
Formatting: % , .format(), f-strings
"""
# Input example (commented to avoid blocking)
# name = input("Enter name: ")
# age = int(input("Enter age: "))
# print(f"Hello {name}, you are {age} years old.")

print("Hello", "World", sep=", ", end="!\n")
print("Formatted: %s is %d" % ("Alice", 25))
print("Formatted: {} is {}".format("Bob", 30))
print(f"Formatted: {'Charlie'} is {35}")

# 8. Control Flow
"""
if: if condition
if-else: if cond else
if-elif-else: Multiple conditions
Nested if: if inside if
Match (3.10+): match value: case pattern
"""
x = 10
if x > 5:
    print("x > 5")
elif x == 5:
    print("x == 5")
else:
    print("x < 5")

# Nested
if x > 0:
    if x % 2 == 0:
        print("Positive even")

# Match (Python 3.10+)
def match_example(value):
    match value:
        case 1:
            return "One"
        case 2 | 3:
            return "Two or Three"
        case _:
            return "Other"

print(f"Match 1: {match_example(1)}")
print(f"Match 4: {match_example(4)}")

# 9. Loops
"""
While: while cond: break, continue, else
For: for item in iterable: range(), nested, else
"""
# While
i = 0
while i < 3:
    print(f"While: {i}")
    i += 1
else:
    print("While else")

# For
for j in range(3):
    print(f"For: {j}")
else:
    print("For else")

# Break/continue
for k in range(5):
    if k == 2:
        continue
    if k == 4:
        break
    print(f"Loop: {k}")

# 10. Iteration Concepts
"""
Iterable: Object with __iter__
Iterator: Object with __next__
iter(): Get iterator
next(): Get next item
StopIteration: When exhausted
"""
lst = [1, 2, 3]
it = iter(lst)
print(f"Next: {next(it)}")
print(f"Next: {next(it)}")
print(f"Next: {next(it)}")
# print(next(it))  # StopIteration

# Manual iteration
it2 = iter(lst)
try:
    while True:
        print(f"Manual: {next(it2)}")
except StopIteration:
    print("Iteration complete")

# 11. Data Structures — Detailed
"""
Lists: Mutable, ordered, []
Tuples: Immutable, ordered, ()
Sets: Mutable, unordered, unique, {}
Dictionaries: Mutable, key-value, {}
"""

# Lists - Methods
lst = [1, 2, 3]
print(f"List: {lst}")
print(f"Indexing: {lst[1]}")
print(f"Slicing: {lst[1:3]}")
nested = [[1,2], [3,4]]
print(f"Nested: {nested}")
lst_copy = lst.copy()  # Shallow copy
lst.append(4)
print(f"Append: {lst}")
lst.insert(1, 99)
print(f"Insert: {lst}")
lst.extend([5, 6])
print(f"Extend: {lst}")
lst.remove(99)
print(f"Remove: {lst}")
popped = lst.pop()
print(f"Pop: {popped}, List: {lst}")
lst.reverse()
print(f"Reverse: {lst}")
lst.sort()
print(f"Sort: {lst}")
print(f"Index of 2: {lst.index(2)}")
print(f"Count of 1: {lst.count(1)}")
lst.clear()
print(f"Clear: {lst}")

# Tuples - Limited methods
tup = (1, 2, 3)
print(f"Tuple: {tup}")
single = (1,)  # Single element
packed = 1, 2, 3  # Packing
a, b, c = packed  # Unpacking
print(f"Unpacked: {a}, {b}, {c}")
print(f"Index of 2: {tup.index(2)}")
print(f"Count of 1: {tup.count(1)}")

# Sets - Methods
st = {1, 2, 3, 3}  # Unique
print(f"Set: {st}")
st2 = {2, 3, 4}
print(f"Union: {st | st2}")
print(f"Intersection: {st & st2}")
print(f"Difference: {st - st2}")
print(f"Symmetric diff: {st ^ st2}")
st.add(5)
print(f"Add: {st}")
st.remove(5)
print(f"Remove: {st}")
st.discard(10)  # No error if not present
print(f"Discard: {st}")
popped = st.pop()
print(f"Pop: {popped}, Set: {st}")
st.clear()
print(f"Clear: {st}")

# Dicts - Methods
dct = {"a": 1, "b": 2}
print(f"Dict: {dct}")
print(f"Key: {dct['a']}")
nested_dct = {"inner": {"key": "value"}}
print(f"Nested: {nested_dct}")
for k, v in dct.items():
    print(f"Item: {k}={v}")
dct.update({"c": 3, "d": 4})
print(f"Update: {dct}")
dct["e"] = 5  # Set item
print(f"Setitem: {dct}")
popped = dct.pop("e")
print(f"Pop: {popped}, Dict: {dct}")
popped = dct.popitem()
print(f"Popitem: {popped}, Dict: {dct}")
print(f"Get 'a': {dct.get('a')}")
print(f"Keys: {list(dct.keys())}")
print(f"Values: {list(dct.values())}")
print(f"Items: {list(dct.items())}")
dct.clear()
print(f"Clear: {dct}")

# 12. Comprehensions
"""
List: [expr for item in iterable if cond]
Set: {expr for item in iterable if cond}
Dict: {key: value for item in iterable if cond}
Nested: Comprehensions inside comprehensions
Conditional: if in comprehension

Cross-references:
- See Section 26 for generator expressions (similar to list comprehensions but lazy)
- See Section 11 for data structures that comprehensions can create
- See Section 15 for functional programming alternatives (map/filter)
"""
# List
squares = [x**2 for x in range(5)]
print(f"List comp: {squares}")

# Set
even_squares = {x**2 for x in range(10) if x % 2 == 0}
print(f"Set comp: {even_squares}")

# Dict
square_dict = {x: x**2 for x in range(5)}
print(f"Dict comp: {square_dict}")

# Nested
matrix = [[i*j for j in range(3)] for i in range(3)]
print(f"Nested: {matrix}")

# 13. Functions (Very Important)
"""
Definition: def func(params):
Calling: func(args)
Return: return value(s)
Default args: def func(a=1)
Keyword args: func(a=1, b=2)
Positional: func(1, 2)
*args: Variable positional
**kwargs: Variable keyword
Keyword-only: After *args or *
Docstrings: """ """
Annotations: def func(a: int) -> int:
Local/global: Scope
global/nonlocal: Access outer scopes
"""
def greet(name="World"):
    """Greets someone."""
    return f"Hello, {name}!"

print(greet())
print(greet("Alice"))

def add(a, b=0):
    return a + b

print(f"Add: {add(5, 3)}")

def var_args(*args, **kwargs):
    print(f"Args: {args}, Kwargs: {kwargs}")

var_args(1, 2, x=3, y=4)

def keyword_only(a, *, b):
    return a + b

print(f"Keyword only: {keyword_only(1, b=2)}")

# Annotations
def annotated(a: int, b: int) -> int:
    return a + b

print(f"Annotated: {annotated(2, 3)}")

# Scope
x = 10  # Global
def scope_test():
    x = 5  # Local
    print(f"Local x: {x}")

scope_test()
print(f"Global x: {x}")

def global_test():
    global x
    x = 20

global_test()
print(f"Global after: {x}")

# 14. Scope & Namespace (LEGB Rule)
"""
Local: Inside function
Enclosing: Nested functions
Global: Module level
Built-in: Python built-ins
Name resolution: LEGB order
Shadowing: Local hides global
"""
# LEGB Example
global_var = "Global"

def outer():
    enclosing_var = "Enclosing"
    def inner():
        local_var = "Local"
        print(f"Local: {local_var}")
        print(f"Enclosing: {enclosing_var}")
        print(f"Global: {global_var}")
        print(f"Built-in: {len}")  # len is built-in
    inner()

outer()

# 15. Lambda & Functional Concepts
"""
Lambda: lambda params: expr
First-class: Functions as objects
Higher-order: Functions taking/returning functions
Closures: Function remembering enclosing scope
"""
# Lambda
square = lambda x: x**2
print(f"Lambda: {square(4)}")

# First-class
funcs = [lambda x: x+1, lambda x: x*2]
print(f"First-class: {funcs[0](5)}")

# Higher-order
def apply_func(func, value):
    return func(value)

print(f"Higher-order: {apply_func(square, 3)}")

# Closure
def outer(x):
    def inner(y):
        return x + y
    return inner

closure = outer(10)
print(f"Closure: {closure(5)}")

# 16. Recursion
"""
Base case: Stops recursion
Recursive case: Calls itself
Stack: Call stack
Tail recursion: Last call is recursive
Recursion vs iteration: Recursion uses stack, iteration loop
"""
def factorial(n):
    if n == 0:  # Base
        return 1
    return n * factorial(n-1)  # Recursive

print(f"Factorial 5: {factorial(5)}")

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print(f"Fib 6: {fib(6)}")

# 17. Object-Oriented Programming (Core Python)
"""
Classes: class ClassName:
Objects: instance = Class()
__init__: Constructor
Instance vars: self.var
Class vars: Class.var
Methods: def method(self):
Instance: self
Class: @classmethod
Static: @staticmethod
Encapsulation: Public, _protected, __private
Inheritance: class Sub(Super):
Multiple: class Sub(A, B)
Overriding: Same method name
super(): Call parent
Polymorphism: Same interface, different behavior
Duck typing: If it quacks like duck
Operator overloading: __add__, etc.
Special methods: __str__, __repr__, etc.
"""
class Animal:
    species = "Animal"  # Class var

    def __init__(self, name):
        self.name = name  # Instance var

    def speak(self):
        return "Some sound"

    @classmethod
    def get_species(cls):
        return cls.species

    @staticmethod
    def info():
        return "Animals are living beings"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):  # Override
        return "Woof"

    def __str__(self):
        return f"Dog: {self.name}, {self.breed}"

    def __add__(self, other):  # Overload +
        return f"{self.name} and {other.name}"

dog1 = Dog("Buddy", "Golden")
dog2 = Dog("Max", "Lab")
print(f"Speak: {dog1.speak()}")
print(f"Str: {str(dog1)}")
print(f"Add: {dog1 + dog2}")
print(f"Class method: {Dog.get_species()}")
print(f"Static: {Dog.info()}")

# 18. Exception Handling
"""
Exception: Runtime error
Syntax vs runtime: Syntax at compile, runtime at execution
try-except: Catch exceptions
Multiple except: Different types
else: If no exception
finally: Always execute
Nested try: Try inside try
Raising: raise Exception
Custom: class MyError(Exception)
"""
try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(f"Caught: {e}")
except:
    print("Other error")
else:
    print("No error")
finally:
    print("Always")

# Raising
def check_positive(n):
    if n < 0:
        raise ValueError("Must be positive")
    return n

try:
    check_positive(-1)
except ValueError as e:
    print(f"Raised: {e}")

# Custom
class MyError(Exception):
    pass

try:
    raise MyError("Custom error")
except MyError as e:
    print(f"Custom: {e}")

# 19. File Handling (Built-in Only)
"""
Opening: open(filename, mode)
Modes: 'r', 'w', 'a', 'rb', etc.
Reading: read(), readline(), readlines()
Writing: write(), writelines()
Closing: close()
with: Automatic closing
Pointer: seek(), tell()
Text vs binary: str vs bytes
"""
# Writing
with open("temp.txt", "w") as f:
    f.write("Hello\nWorld")

# Reading
with open("temp.txt", "r") as f:
    content = f.read()
    print(f"Read: {content}")

    f.seek(0)  # Reset pointer
    lines = f.readlines()
    print(f"Lines: {lines}")

# Binary
with open("temp.txt", "rb") as f:
    binary = f.read()
    print(f"Binary: {binary}")

# Clean up
import os
os.remove("temp.txt")

# 29. Collections Module
"""
Collections module provides specialized container datatypes beyond built-in types.

namedtuple: Factory function for creating tuple subclasses with named fields
deque: Double-ended queue for efficient appends/pops from both ends
Counter: Dictionary subclass for counting hashable objects
OrderedDict: Dictionary that remembers insertion order (Python 3.7+ dicts maintain order)
defaultdict: Dictionary that provides default values for missing keys
ChainMap: Single view of multiple mappings
UserDict, UserList, UserString: Wrappers for easier subclassing
"""

import collections

# namedtuple
Point = collections.namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(f"namedtuple: {p}, x={p.x}, y={p.y}")

# deque
dq = collections.deque([1, 2, 3])
dq.append(4)  # Right append
dq.appendleft(0)  # Left append
print(f"deque: {dq}")
print(f"pop: {dq.pop()}, popleft: {dq.popleft()}")

# Counter
cnt = collections.Counter(['a', 'b', 'c', 'a', 'b', 'a'])
print(f"Counter: {cnt}")
print(f"Most common: {cnt.most_common(2)}")

# OrderedDict (Python 3.7+ maintains insertion order by default)
od = collections.OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(f"OrderedDict: {od}")

# defaultdict
dd = collections.defaultdict(int)
dd['a'] += 1  # No KeyError, defaults to 0
dd['b'] += 2
print(f"defaultdict: {dict(dd)}")

# ChainMap
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
cm = collections.ChainMap(dict1, dict2)
print(f"ChainMap: {dict(cm)}, b={cm['b']}")  # b from first dict

# 30. Itertools Module
"""
Itertools provides functions creating iterators for efficient looping.

Infinite iterators: count(), cycle(), repeat()
Terminating iterators: accumulate(), chain(), compress(), dropwhile(), filterfalse(), groupby(), islice(), pairwise(), starmap(), takewhile(), tee(), zip_longest()
Combinatoric iterators: product(), permutations(), combinations(), combinations_with_replacement()
"""

import itertools

# Infinite iterators
print(f"count(10, 2): {list(itertools.islice(itertools.count(10, 2), 5))}")
print(f"cycle('AB'): {list(itertools.islice(itertools.cycle('AB'), 6))}")
print(f"repeat(5, 3): {list(itertools.repeat(5, 3))}")

# Terminating iterators
print(f"accumulate([1,2,3,4]): {list(itertools.accumulate([1,2,3,4]))}")
print(f"chain('ABC', 'DEF'): {list(itertools.chain('ABC', 'DEF'))}")
print(f"compress('ABCDEF', [1,0,1,0,1,1]): {list(itertools.compress('ABCDEF', [1,0,1,0,1,1]))}")
print(f"dropwhile(lambda x: x<3, [1,2,3,4]): {list(itertools.dropwhile(lambda x: x<3, [1,2,3,4]))}")
print(f"takewhile(lambda x: x<3, [1,2,3,4]): {list(itertools.takewhile(lambda x: x<3, [1,2,3,4]))}")

# Groupby
data = [('A', 1), ('A', 2), ('B', 3), ('B', 4)]
for key, group in itertools.groupby(data, lambda x: x[0]):
    print(f"groupby {key}: {list(group)}")

# Combinatoric
print(f"product('AB', '12'): {list(itertools.product('AB', '12'))}")
print(f"permutations('ABC', 2): {list(itertools.permutations('ABC', 2))}")
print(f"combinations('ABC', 2): {list(itertools.combinations('ABC', 2))}")

# 31. Functools Module
"""
Functools provides higher-order functions and operations on callable objects.

partial: Create partial function with fixed arguments
partialmethod: Method version of partial
lru_cache: Memoization decorator for functions
cached_property: Property that caches its value
total_ordering: Fill in missing comparison methods
reduce: Apply function cumulatively to iterable
singledispatch: Single dispatch generic functions
singledispatchmethod: Method version of singledispatch
wraps: Update wrapper function for decorators
"""

import functools

# partial
def multiply(x, y, z):
    return x * y * z

double = functools.partial(multiply, 2)
print(f"partial multiply(2, 3, 4): {double(3, 4)}")

# lru_cache
@functools.lru_cache(maxsize=128)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(f"fib(10) with cache: {fib(10)}")

# reduce
print(f"reduce(lambda x,y: x+y, [1,2,3,4]): {functools.reduce(lambda x,y: x+y, [1,2,3,4])}")

# total_ordering
@functools.total_ordering
class Number:
    def __init__(self, value):
        self.value = value
    def __eq__(self, other):
        return self.value == other.value
    def __lt__(self, other):
        return self.value < other.value

n1, n2 = Number(1), Number(2)
print(f"total_ordering: {n1 < n2}, {n1 <= n2}, {n1 > n2}")

# 32. OS Module
"""
OS module provides functions for interacting with the operating system.

File operations: os.path, os.listdir, os.mkdir, os.remove, os.rename
Path operations: os.path.join, os.path.split, os.path.exists, os.path.isfile, os.path.isdir
Environment: os.environ, os.getenv, os.putenv
Process: os.system, os.execv, os.fork (Unix), os.spawnv
Current directory: os.getcwd, os.chdir
Permissions: os.chmod, os.chown
"""

import os

# Current directory
print(f"Current dir: {os.getcwd()}")

# Path operations
path = os.path.join('folder', 'file.txt')
print(f"Joined path: {path}")
print(f"Split path: {os.path.split(path)}")
print(f"File exists: {os.path.exists(__file__)}")
print(f"Is file: {os.path.isfile(__file__)}")

# Environment
print(f"PATH env: {os.getenv('PATH')[:50]}...")

# List directory
print(f"Files in current dir: {os.listdir('.')[:5]}")

# 33. Sys Module
"""
Sys module provides access to some variables used or maintained by the interpreter.

Command line args: sys.argv
Exit: sys.exit()
Modules: sys.modules
Path: sys.path
Platform: sys.platform
Version: sys.version
Stdin/stdout/stderr: sys.stdin, sys.stdout, sys.stderr
Recursion limit: sys.getrecursionlimit(), sys.setrecursionlimit()
"""

import sys

print(f"Python version: {sys.version}")
print(f"Platform: {sys.platform}")
print(f"Command line args: {sys.argv}")
print(f"Recursion limit: {sys.getrecursionlimit()}")

# Path manipulation
print(f"Python path: {sys.path[0]}")

# 34. Datetime Module
"""
Datetime module supplies classes for manipulating dates and times.

Classes: date, time, datetime, timedelta, tzinfo
Formatting: strftime(), strptime()
Timezones: timezone, utc
Operations: Addition, subtraction with timedelta
"""

import datetime

# Current datetime
now = datetime.datetime.now()
print(f"Current datetime: {now}")

# Date and time components
print(f"Date: {now.date()}, Time: {now.time()}")

# Formatting
print(f"Formatted: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# Parsing
parsed = datetime.datetime.strptime('2023-01-01 12:00:00', '%Y-%m-%d %H:%M:%S')
print(f"Parsed: {parsed}")

# Timedelta
tomorrow = now + datetime.timedelta(days=1)
print(f"Tomorrow: {tomorrow}")

# Timezone
utc = datetime.timezone.utc
utc_time = now.replace(tzinfo=utc)
print(f"UTC time: {utc_time}")

# 35. Advanced OOP - Metaclasses, Descriptors, __slots__
"""
Advanced OOP concepts in Python.

Metaclasses: Classes that create classes
Descriptors: Objects that control attribute access
__slots__: Memory optimization by restricting instance attributes
Method Resolution Order (MRO): super() and multiple inheritance
Abstract Base Classes: abc module
"""

# Metaclass example
class Meta(type):
    def __new__(cls, name, bases, dct):
        dct['created_by_meta'] = True
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    pass

print(f"Metaclass attribute: {hasattr(MyClass, 'created_by_meta')}")

# Descriptor
class Descriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, f'_{self.name}', None)

    def __set__(self, instance, value):
        setattr(instance, f'_{self.name}', value)

class Person:
    name = Descriptor('name')
    age = Descriptor('age')

p = Person()
p.name = 'Alice'
p.age = 30
print(f"Descriptor: {p.name}, {p.age}")

# __slots__
class SlottedClass:
    __slots__ = ['x', 'y']  # Only these attributes allowed

    def __init__(self, x, y):
        self.x = x
        self.y = y

sc = SlottedClass(1, 2)
print(f"__slots__: x={sc.x}, y={sc.y}")
# sc.z = 3  # AttributeError

# MRO
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass

print(f"MRO: {D.__mro__}")

# 36. Best Practices and Common Pitfalls
"""
Common Python best practices and pitfalls to avoid.

Mutable defaults: Use None and create inside function
String concatenation: Use join() instead of +
Exception handling: Catch specific exceptions
Import placement: At top of file
Naming conventions: PEP8
List comprehensions: Prefer over map/filter when simple
Context managers: Use with for file operations
Type hints: Use for better code documentation
Docstrings: Write for all public functions/classes
Testing: Write unit tests
Code organization: Keep functions small, single responsibility
"""

# Mutable default fix
def safe_append(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(f"Safe append: {safe_append(1)}, {safe_append(2)}")

# String concatenation
words = ['Hello', 'World', 'Python']
# Bad: result = ''
# for word in words:
#     result += word + ' '
# Good:
result = ' '.join(words)
print(f"String join: {result}")

# Specific exception handling
try:
    int('not_a_number')
except ValueError as e:
    print(f"Specific exception: {e}")

# 37. Regular Expressions - re Module
"""
Regular expressions for pattern matching in strings.

Functions: re.match(), re.search(), re.findall(), re.finditer(), re.sub(), re.split()
Patterns: Literals, character classes, quantifiers, anchors, groups
Flags: re.IGNORECASE, re.MULTILINE, re.DOTALL
"""

import re

# Basic matching
pattern = r'hello'
text = 'hello world'
match = re.search(pattern, text)
print(f"Regex match: {match.group() if match else 'No match'}")

# Find all
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', 'test@example.com and user@domain.org')
print(f"Emails found: {emails}")

# Substitution
result = re.sub(r'\d+', 'NUMBER', 'I have 42 apples and 7 oranges')
print(f"Substitution: {result}")

# Groups
match = re.search(r'(\w+) (\w+)', 'John Doe')
if match:
    print(f"Groups: {match.groups()}")

# 38. JSON Handling - json Module
"""
JSON (JavaScript Object Notation) for data interchange.

Functions: json.dumps(), json.loads(), json.dump(), json.load()
Custom encoders: json.JSONEncoder subclass
Custom decoders: object_hook parameter
"""

import json

# Basic usage
data = {'name': 'Alice', 'age': 30, 'city': 'NYC'}
json_str = json.dumps(data)
print(f"JSON string: {json_str}")

parsed = json.loads(json_str)
print(f"Parsed back: {parsed}")

# Custom object
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def person_encoder(obj):
    if isinstance(obj, Person):
        return {'name': obj.name, 'age': obj.age, '__type__': 'Person'}
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")

person = Person('Bob', 25)
json_str = json.dumps(person, default=person_encoder)
print(f"Custom JSON: {json_str}")

# 39. Multithreading Basics - threading Module
"""
Multithreading for concurrent execution.

Classes: Thread, Lock, RLock, Condition, Event, Semaphore
Functions: active_count(), current_thread(), enumerate()
GIL: Global Interpreter Lock limits true parallelism for CPU-bound tasks
Use cases: I/O-bound tasks, GUI responsiveness
"""

import threading
import time

# Simple thread
def worker(name):
    print(f"Worker {name} starting")
    time.sleep(1)
    print(f"Worker {name} finished")

# Create and start threads
threads = []
for i in range(3):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

# Wait for all to complete
for t in threads:
    t.join()

print("All threads completed")

# Lock example
lock = threading.Lock()
counter = 0

def increment():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1

threads = [threading.Thread(target=increment) for _ in range(2)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"Counter with lock: {counter}")

# 40. Async/Await Basics - asyncio Module
"""
Asynchronous programming with coroutines.

Keywords: async, await
Functions: asyncio.run(), asyncio.create_task(), asyncio.gather()
Use cases: I/O-bound operations, network requests, concurrent tasks
"""

import asyncio

# Simple async function
async def say_hello(name, delay):
    await asyncio.sleep(delay)
    print(f"Hello {name}")
    return f"Done {name}"

# Main coroutine
async def main():
    # Create tasks
    task1 = asyncio.create_task(say_hello("Alice", 1))
    task2 = asyncio.create_task(say_hello("Bob", 2))

    # Wait for completion
    results = await asyncio.gather(task1, task2)
    print(f"Results: {results}")

# Run the event loop
# asyncio.run(main())  # Commented to avoid blocking in script

print("Async/Await basics demonstrated (run commented to avoid blocking)")

# 20. Memory Management Concepts
"""
Stack vs heap: Stack for calls, heap for objects
Reference counting: Count of references
Garbage collection: Automatic cleanup
Mutability impact: Mutable can change, affecting refs
Interning: Reusing immutable objects
"""
a = 42  # Interned
b = 42
print(f"Interned: {a is b}")  # True for small ints

s1 = "hello"
s2 = "hello"
print(f"String interning: {s1 is s2}")

# 21. Modules & Packages (Core Concepts)
"""
Module: .py file
Import: import mod, from mod import func
__name__: "__main__" if run directly
Python path: sys.path
Package: Directory with __init__.py
"""
# This file is a module
print(f"__name__: {__name__}")

# Import example (built-in)
import math
print(f"Math pi: {math.pi}")

# 22. Built-in Functions (Comprehensive)
"""
Built-in functions are always available without import.

Type conversion:
int(x, base=10): Convert to int
float(x): Convert to float
str(x): Convert to string
bool(x): Convert to bool
complex(real, imag): Create complex
list(iterable): Create list
tuple(iterable): Create tuple
set(iterable): Create set
dict(iterable): Create dict
frozenset(iterable): Create frozenset
bytes(iterable): Create bytes
bytearray(iterable): Create bytearray
slice(start, stop, step): Create slice object

Numeric:
abs(x): Absolute value
round(number, ndigits): Round to ndigits
pow(base, exp, mod): Power with optional modulo
divmod(a, b): Division and modulo as tuple
bin(x): Binary string
hex(x): Hexadecimal string
oct(x): Octal string
chr(i): Character from Unicode code
ord(c): Unicode code from character

String and representation:
repr(obj): String representation
ascii(obj): ASCII representation
format(value, format_spec): Format string

Sequence and iteration:
len(s): Length
range(start, stop, step): Range object
enumerate(iterable, start=0): Index-value pairs
zip(*iterables): Parallel iteration
reversed(seq): Reverse iterator
sorted(iterable, key, reverse): Sorted list
sum(iterable, start=0): Sum
min(iterable, key, default): Minimum
max(iterable, key, default): Maximum
any(iterable): Any true
all(iterable): All true
map(func, *iterables): Map function
filter(func, iterable): Filter
iter(object, sentinel): Iterator
next(iterator, default): Next item

Functional:
eval(expression, globals, locals): Evaluate expression
exec(object, globals, locals): Execute code
compile(source, filename, mode): Compile code

Reflection and introspection:
type(obj): Type of object
id(obj): Identity
hash(obj): Hash value
isinstance(obj, classinfo): Instance check
issubclass(class, classinfo): Subclass check
callable(obj): Callable check
hasattr(obj, name): Has attribute
getattr(obj, name, default): Get attribute
setattr(obj, name, value): Set attribute
delattr(obj, name): Delete attribute
dir(obj): Attributes list
vars(obj): __dict__ of object
globals(): Global namespace dict
locals(): Local namespace dict
help(obj): Help on object

Import and I/O:
__import__(name, globals, locals, fromlist, level): Import module
open(file, mode, buffering, encoding, errors, newline, closefd, opener): Open file
input(prompt): Read input
print(*objects, sep, end, file, flush): Print
"""

# Examples

# Type conversion
print(f"int('42'): {int('42')}")
print(f"float('3.14'): {float('3.14')}")
print(f"str(42): {str(42)}")
print(f"bool(0): {bool(0)}")
print(f"complex(1,2): {complex(1,2)}")
print(f"list('abc'): {list('abc')}")
print(f"tuple([1,2]): {tuple([1,2])}")
print(f"set([1,2,2]): {set([1,2,2])}")
print(f"dict([('a',1)]): {dict([('a',1)])}")
print(f"frozenset([1,2]): {frozenset([1,2])}")
print(f"bytes([65,66]): {bytes([65,66])}")
print(f"bytearray([65,66]): {bytearray([65,66])}")
print(f"slice(1,10,2): {slice(1,10,2)}")

# Numeric
print(f"abs(-5): {abs(-5)}")
print(f"round(3.14159, 2): {round(3.14159, 2)}")
print(f"pow(2,3): {pow(2,3)}")
print(f"divmod(10,3): {divmod(10,3)}")
print(f"bin(10): {bin(10)}")
print(f"hex(10): {hex(10)}")
print(f"oct(10): {oct(10)}")
print(f"chr(65): {chr(65)}")
print(f"ord('A'): {ord('A')}")

# String and representation
print(f"repr('hello'): {repr('hello')}")
print(f"ascii('héllo'): {ascii('héllo')}")
print(f"format(42, '04d'): {format(42, '04d')}")

# Sequence and iteration
lst = [1, 2, 3, 4]
print(f"len(lst): {len(lst)}")
print(f"list(range(5)): {list(range(5))}")
print(f"list(enumerate(lst)): {list(enumerate(lst))}")
print(f"list(zip([1,2], ['a','b'])): {list(zip([1,2], ['a','b']))}")
print(f"list(reversed(lst)): {list(reversed(lst))}")
print(f"sorted([3,1,4,1,5]): {sorted([3,1,4,1,5])}")
print(f"sum(lst): {sum(lst)}")
print(f"min(lst): {min(lst)}, max(lst): {max(lst)}")
print(f"any([True, False]): {any([True, False])}, all([True, True]): {all([True, True])}")

def square(x): return x**2
mapped = list(map(square, lst))
print(f"list(map(square, lst)): {mapped}")

filtered = list(filter(lambda x: x % 2 == 0, lst))
print(f"list(filter(lambda x: x % 2 == 0, lst)): {filtered}")

it = iter(lst)
print(f"next(it): {next(it)}")

# Functional
print(f"eval('1+2'): {eval('1+2')}")
# exec example (commented to avoid execution)
# exec('print("Hello")')
# compile example
code = compile('1+2', '<string>', 'eval')
print(f"eval(code): {eval(code)}")

# Reflection
print(f"type(lst): {type(lst)}")
print(f"id(lst): {id(lst)}")
print(f"hash(42): {hash(42)}")
print(f"isinstance(42, int): {isinstance(42, int)}")
print(f"issubclass(int, object): {issubclass(int, object)}")
print(f"callable(square): {callable(square)}")
print(f"hasattr(lst, 'append'): {hasattr(lst, 'append')}")
print(f"getattr(lst, 'append'): {getattr(lst, 'append')}")
# setattr example
class Temp:
    pass
temp_obj = Temp()
setattr(temp_obj, 'new_attr', 'value')
print(f"temp_obj.new_attr: {temp_obj.new_attr}")
# dir example
print(f"dir(lst)[:5]: {dir(lst)[:5]}")  # First 5
print(f"globals() keys: {list(globals().keys())[:5]}")
print(f"locals() keys: {list(locals().keys())[:5]}")
# help example (commented as it opens interactive)
# help(len)

# Import
import math
print(f"math.pi: {math.pi}")

# open example (already in file handling)
# input example (commented)
# print example
print("Hello", "World", sep=", ")

# 23. Python Execution Model
"""
Compilation: To bytecode (.pyc)
PVM: Python Virtual Machine executes bytecode
Interpreted: Executes line by line, but compiles to bytecode first
"""
# .pyc files are created in __pycache__

# 24. Advanced Core Concepts
"""
Shallow copy: copy.copy() - nested refs shared
Deep copy: copy.deepcopy() - full copy
Mutable default: def func(lst=[]): - shared list
Late binding: Closures capture variables at call time
Name mangling: __var becomes _Class__var
Equality vs identity: == vs is
Hashability: Immutable if hashable
Truthy/falsy: Non-zero, non-empty true
"""
import copy

original = [[1,2], [3,4]]
shallow = copy.copy(original)
deep = copy.deepcopy(original)

original[0][0] = 99
print(f"Shallow: {shallow}")  # Changed
print(f"Deep: {deep}")  # Unchanged

# Mutable default pitfall
def append_to_list(item, lst=[]):
    lst.append(item)
    return lst

print(append_to_list(1))  # [1]
print(append_to_list(2))  # [1,2] - shared!

# Name mangling
class Test:
    def __init__(self):
        self.__private = "hidden"

t = Test()
# print(t.__private)  # AttributeError
print(t._Test__private)  # Mangled

# Equality/Identity
a = [1,2]
b = [1,2]
print(f"Equal: {a == b}, Same: {a is b}")

# Hashability
print(f"Hashable: {hash(42)}")
# print(hash([1,2]))  # TypeError, mutable

# Truthy/Falsy
print(f"Truthy: {bool(1)}, {bool('')}, {bool([])}")

# 25. Coding Practices (Language Level)
"""
PEP8: Style guide - 4 spaces, naming, etc.
Readability: Clear names, comments
Docstrings: Function/class docs
Clean functions: Single responsibility, short
"""
# Example of clean function
def calculate_area(radius: float) -> float:
    """
    Calculate the area of a circle.

    Args:
        radius: The radius of the circle.

    Returns:
        The area of the circle.
    """
    import math
    return math.pi * radius ** 2

print(f"Area: {calculate_area(5)}")

# PEP8: Use snake_case for functions/vars, CamelCase for classes

# 26. Generators
"""
Generators: Functions that yield values lazily, saving memory.
yield: Pauses function, returns value, resumes on next call.
Generator expressions: (expr for item in iterable)
Built-in functions: next(), iter()
Advantages: Memory efficient for large sequences.
"""
def countdown(n):
    while n > 0:
        yield n
        n -= 1

gen = countdown(5)
print(f"Generator: {next(gen)}")
print(f"Generator: {next(gen)}")

# Generator expression
squares_gen = (x**2 for x in range(5))
print(f"Gen expr: {list(squares_gen)}")

# 27. Decorators
"""
Decorators: Functions that modify other functions.
@decorator: Syntactic sugar for func = decorator(func)
Function decorators: Modify function behavior.
Class decorators: Modify class behavior.
Built-in: @staticmethod, @classmethod, @property
"""
def timer(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_func():
    import time
    time.sleep(0.1)
    return "Done"

print(f"Decorated: {slow_func()}")

# Class decorator
def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class MyClass:
    pass

obj1 = MyClass()
obj2 = MyClass()
print(f"Singleton: {obj1 is obj2}")

# 28. Context Managers
"""
Context managers: Manage resources with with statement.
__enter__: Setup, returns resource
__exit__: Cleanup, handles exceptions
Built-in: with open(), contextlib
"""
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

with FileManager("temp.txt", "w") as f:
    f.write("Hello from context manager")

with open("temp.txt", "r") as f:
    print(f"Context read: {f.read()}")

import contextlib

@contextlib.contextmanager
def my_context():
    print("Entering")
    yield "resource"
    print("Exiting")

with my_context() as res:
    print(f"Using: {res}")

# Clean up
import os
os.remove("temp.txt")
