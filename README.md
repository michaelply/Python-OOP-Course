# Python OOP Course
FreeCodeCamp.org:
https://www.youtube.com/watch?v=Ej_02ICOIgs&t=327s

## Object Oriented Programming:

### Encapsulation:
Hiding information and restricting direct access to some of the 
attributes.

## Python Syntax
Class method is used to create objects with similar attributes
to benefit from methods implemented within class.

### def \_\_init\_\_(self):
It is used as a constructor of an object instance. We define the 
attributes shared commonly within the class when creating new
instances. Note that self refer to the particular instance when
calling the method.

### @classmethod
It is used when there is a relationship with the class
(not individual unique instances) and data structures manipulation
is needed. For example, creating new object instances from a csv or 
json file.

### @staticmethod 
It is used where there is relationship with the class but
not common between instances. Therefore, self object is not needed
to pass on as an argument. It is like a regular function but defined
within the class itself.

### class child(parent):
The syntax to create a child class that builds upon the parent class

### super()
This method is used in the \_\_init\_\_ method to inherit attributes
from the parent class so we don't have to assign them repetitively.
Note that it will also inherit the methods from the parent class.

### @property
This decorator is used to declare read-only attribute.

### @name.setter
Decorator used to set read-only attribute specified by property
decorator.