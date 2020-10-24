import time
import os

slide1 = '(^_^)'
slide2 = '(^_~)'
slide3 = '(^_^)'
slide4 = '(о_О)'
slide5 = '(O_O)'
slide6 = 'Hello, World!'

time.sleep(0.3)
print(slide1, end='\r')
time.sleep(0.3)
print(slide2, end='\r')


str1 = """
******Заметки лесника******

Погода была пасмурной.
...
...
"""

str2 = """
******Заметки лесника******

Погода была пасмурной.
Шел дождь.
...
"""

str3 = """
******Заметки лесника******

Погода была пасмурной.
Шел дождь.
Но настроение все равно хорошее!
"""

str4 = """
******Заметки лесника ..******

         КОНЕЦ

****************************
"""

os.system('cls')

print(str1, end='\r')
time.sleep(1)
os.system('cls')
print(str2, end='\r')
time.sleep(1)
os.system('cls')
print(str3, end='\r')
time.sleep(1)
os.system('cls')
print(str4, end='\r')
time.sleep(1)

