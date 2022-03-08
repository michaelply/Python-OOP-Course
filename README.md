# Python OOP Course
FreeCodeCamp.org:
https://www.youtube.com/watch?v=Ej_02ICOIgs&t=327s

## Object Oriented Programming:

### Encapsulation:
Hiding data and restricting direct access to some of the object
attributes. The idea is to protect information by applying 
indirect changes to data attributes using methods if necessary.

### Abstraction:
Hiding internal implementation details and unnecessary information
from the instances by making methods private. This can be done by
adding double underscores \_\_ in front of a variable name.

### Inheritance:
The procedure in which one class inherits the attributes and methods
of another class. This allow us to reuse codes across all classes.

### Polymorphism:
Refers to the use of a single type entity to represent different types
in different scenarios. For example, the len() function in python 
behaves differently when given different data types (objects).
This is polymorphism in action.

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

### self.\_\_class\_\_.\_\_name\_\_
Access the class name from an object instance.