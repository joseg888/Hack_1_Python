"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    resultado = []
    diccionario = {'o': '0', 'i': '1', 'a': '@'}
    
    for i in result:
        if i in diccionario:
            resultado.append(diccionario[i])
        else:
            resultado.append(i.upper())
    return resultado  