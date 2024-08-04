"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    lista = []
    i = 0
    while i < len(result):
        lista.append(result[i])
        lista.append('@')
        i += 1
    return lista 