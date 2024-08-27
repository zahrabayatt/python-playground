# The programming languages we use, like C, C#, Java, Python, these are all simple text based languages that we humans understand; computers don't understand them, they only understand machine code.

#  So if you have some code written in C, we should convert it to machine code, and that's the job of a C Compiler. So a C compiler is a program that knows how to convert or compile C code into machine code.

# However, this machine code is specific to the type of CPU of a computer so if you compile a C program on a Windows machine we can't execute it on a Mac, because Windows and Mac have different machine code just like how people from different countries speak different languages.

# Java came to solve this problem. Java compiler doesn't compile Java code into machine code, instead it compiles it into a portable language called JavaBytecode, Which is not specific to a hardware platform like Windows or Mac. Now, we still need to convert Java Bytecode to machine code. So Java also comes with a program called Java virtual machine or JVM for doing this. When we run a Java program, JVM kicks in , it loads our Java Bytecode and then at run time, it will convert each instruction to machine code. With this model, we can run Java Bytecode on any platforms that have a JVM. We have JVM implementations for Windows, Mac, and so on. C# and Python have also taken the same route, so they are platform independent.

# When we run a python program using CPython first it will compile our Python code into Python Bytecode, then it will pass that Bytecode to Python Virtual Machine which will in turn convert it into machine code and execute it.This is how C Python works.

# if you wanna reuse some Java code in a Python program we should use Jython. how Jython makes this possible?
# When you use Jython to run a python program, instead of compiling your  Python code into Python Bytecode, it will compile it to Java Bytecode, so we can take this Java Byte code and run it using Java virtual machine. And that's why we can import some Java code into a Python program when using Jython, because the end result is Java Bytecode which will eventually be executed by Java Virtual Machine.
