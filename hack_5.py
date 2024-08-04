"""
text: "fooziman" output => "f00z1m@n"
"""

def fn_hack_5():
    result = "fooziman"
    diccionario = {'a':'@', 'i':'1', 'o':'0'}

    for i in result:
        if i in diccionario.keys():
            result = result.replace(i, diccionario[i])
    return result  
