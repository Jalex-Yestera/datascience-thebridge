# Funcion protected
import pandas as pd
import numpy as np
import requests
from functools import wraps


def _f_protected(x):
    l1 = [ x for x in range(16)]
    filtrada = list(filter(lambda x : x > 5, l1))
    print (fv)

# Decorador prepost
def prepost(*args , **kwargs ):
    print("args =",args,'\n',"kwargs =", kwargs)
    print(kwargs.keys())
    print(kwargs.values())
    url = kwargs['url']
    readed = pd.read_csv(url, sep=",")
    df = pd.DataFrame(readed)
    print (df)
    df.hist()

prepost(url = 'http://winterolympicsmedals.com/medals.csv' )


@prepost(url=key_url)
_f_protected(x)



def prepost_2(*arg, **kwargs):
    def inner(function):
        l1 = [ x for x in range(16)]
        filtrada = list(filter(lambda x : x > 5, l1))
        print (fv)
        @wraps(_f_protected)
        def prepost(*args_function, **kwargs_function):
            print("args =",args,'\n',"kwargs =", kwargs)
            print(kwargs.keys())
            print(kwargs.values())
            url = kwargs['url']
            readed = pd.read_csv(url, sep=",")
            df = pd.DataFrame(readed)
            print (df)
            df.hist()
        return result
    return wrapper
return inner

@prepost(url='http://winterolympicsmedals.com/medals.csv')