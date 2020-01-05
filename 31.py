#importing functions from a file (modules)
#assuming hello.py is already a file
import hello
from hello import *

user = input("Enter user's name: ")
sayHello(user)
