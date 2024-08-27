# When we talk about python, we mean two separate things that are closely related:

# 1- Python language: Python as a language is just a specification that defines a set of rules and grammar for writing python code.

# 2- Particular implementation: A python implementation is basically a program that understands those rules and can execute python code.

# Python implementation:
# - CPython: It's the default implementation of Python and It's written in C.
# - Jython: It written in Java.
# - IronPython: It written in C#.
# - PyPy: it written in a subset of Python itself.

# As new features are added to the Python language, they are first supported by CPython because that's the default implementation, and then they will gradually come to the other implementations. In theory if we give some python code to any of these implementations we should get the same result, but in practice that's not always the case. Certain features may be available in one implementation but not another, or they just behave a little bit differently in a particular implementation.

# Why do we have several implementations of Python? Wouldn't CPython be enough?
#  Well, it's for the same reason we have multiple operating systems, Or multiple operating systems, or multiple browsers, or multiple programming languages. After all these years, programmers haven't agreed on a single programming language, and that's the same story with Python implementation. However, there is one technical reason behind these implementations that you should be aware of. Since Jython is implemented in Java, it allows you to reuse some existing Java code in a Python program. So if you're a Java developer and you want to import some Java code into a Python program, you should use Jython instead of Cpython. Similarly IronPython is written in C#, so if you're a C# developer, and want to bring some C# code into a Python program, you will have to use IronPython. Next we will look at how exactly CPython executes Python Code.
