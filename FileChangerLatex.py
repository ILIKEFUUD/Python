"""
Rahul Shah
FileChanger.py
"""

open('chap09.tex', 'w') as file:
    open('KLSadd.tex', 'r') as obj:
        for word in obj:
            if(
