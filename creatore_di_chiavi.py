import string
import pyperclip
from random import *
characters = string.ascii_letters + string.punctuation  + string.digits
password =  "".join(choice(characters) for x in range(randint(8, 8192)))
print (password)
pyperclip.copy(password)
input()