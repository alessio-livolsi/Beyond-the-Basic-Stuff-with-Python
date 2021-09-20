# Chapter 1 - abc_traceback.py


# def a():
#     print("Start of a()")
#     b()  # Call b().


# def b():
#     print("Start of b()")
#     c()  # Call c().


# def c():
#     print("Start of c()")
#     42 / 0  # This will cause a zero divide error.


# a()  # Call a().


# `zeroDivideTraceback.py`


def spam(number1, number2):
    return number1 / (number2 - 42)


spam(101, 42)
