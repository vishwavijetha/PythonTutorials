"""
================================================================================================================================
Author: Vishwa
Date Created: 03/04/2019
--------------------------
Topic: File IO
--------------------------

Declaration: {file_object = open(path, mode, buffering)}

Methods: --> {open(), close(), read(), tell(), seek(), os.rename(), os.remove()}

Access Modes: --> {r, rb, r+, rb+, w, wb, w+, wb+, a, ab, a+, ab+}

File Object Attributes: -- { file_object.closed, file_object.mode, file_object.name, file_object.softspace}
================================================================================================================================
"""
file_path = r'python.txt'
data = 'Hi, this data is written using python'

print('\n\nFile IO:')
print('--------------------------------------------------------------------------------------------')
print('''\n1) Write/Overwrite/Create using Access Mode --> 'w+' ''')
file_obj = open(file_path, 'w+')
print(file_obj.name, 'is opened using ', file_obj.mode)
file_obj.write(data)
print('Writing data: ', data)
file_obj.close()
print('Closing file: ', file_obj.closed)

print('''\n2) Read/Overwrite (pointer at the start of file) using Access Mode --> 'r+' ''')
file_obj = open(file_path, 'r+')
file_obj.write('Added this line using r+ mode\n')
print(file_obj.read())
print("Name of the file: ", file_obj.name)
print("Opening mode : ", file_obj.mode)
file_obj.close()
print('Closing file: ', file_obj.closed)


print('''\n3) Append/Overwrite (pointer at the end of file) using Access Mode --> 'a+' ''')
file_obj = open(file_path, 'a+')
file_obj.write('Appended this line using a+ mode')
print("Name of the file: ", file_obj.name)
print("Opening mode : ", file_obj.mode)
file_obj.close()
print('Closing file: ', file_obj.closed)

print('''\n4) Read only using Access Mode --> 'r' ''')
file_obj = open(file_path, 'r')
print('File content: ', file_obj.read())
print("Name of the file: ", file_obj.name)
print("Opening mode : ", file_obj.mode)
file_obj.close()
print('Closing file: ', file_obj.closed)

import shutil

shutil.copy(file_path, file_path.replace('python', 'python copy'))
