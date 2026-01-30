"""
Documentation for the 'sys' module.

Introduction:
The 'sys' module in Python provides access to system-specific parameters and functions. It allows interaction with the Python interpreter, including command-line arguments, standard input/output streams, and system exit mechanisms.

When to use it:
- To access command-line arguments passed to a script.
- For reading from standard input or writing to standard output/error.
- To exit a program gracefully or handle system-level operations.
- In scripts that need to interact with the Python runtime environment.

Key Functions and Their Functionalities:
- sys.argv: A list containing the command-line arguments passed to the script.
- sys.stdin: Standard input stream (file-like object).
- sys.stdout: Standard output stream (file-like object).
- sys.stderr: Standard error stream (file-like object).
- sys.exit([arg]): Exits the program with an optional exit code.
- sys.path: A list of strings specifying the search path for modules.
- sys.version: A string containing the Python version.
- sys.platform: A string identifying the platform (e.g., 'win32', 'linux').
- sys.getsizeof(object): Returns the size of an object in bytes.
- sys.modules: A dictionary mapping module names to loaded modules.

Other Information:
- 'sys' is part of Python's standard library, no installation needed.
- Useful for command-line tools and scripts that process arguments.
- Be cautious with sys.exit() as it terminates the program immediately.
- sys.path can be modified to add custom module search paths.
"""
