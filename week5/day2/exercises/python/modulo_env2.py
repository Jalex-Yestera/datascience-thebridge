import pandas as pd
import numpy as np
import requests
from functools import wraps

def prepost (*args,**kwargs):
    url = kwargs['url']
    df = pd.read_csv(url)
    def inner (function):
        @wraps(function)
        def wrapper(*a, **k):
            if url:
                retval = function(*a, **k)
                df.hist()
            return retval
        return wrapper
    return inner
@prepost(url="http://winterolympicsmedals.com/medals.csv")
def _f_protected ():
    l1 = [j for j in range(16)]
    fv= list(filter(lambda x : x > 5,l1)) 
    print(fv)
_f_protected()