#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")
greet_programmer()

def greet(name):
    print(f"Hello, {name}!")
greet("Naureen")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")
greet_with_default()
greet_with_default("Sunny")

def add(num1, num2):
    return num1 + num2
sum1 = add(1,2)
print(sum1)

def halve(number):
    if not isinstance(number, (int, float)):
        return None
    return number / 2

result1 = halve(4)
result2 = halve("four")

print(result1)
print(result2)