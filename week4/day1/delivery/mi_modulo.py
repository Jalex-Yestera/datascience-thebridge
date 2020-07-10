# FUNCION RANDOM NUMBER GENERATOR:
def Random_n_g ():
    """ Next line is not needed if you wrote it before. Consider deletion."""
    import numpy as np
    # Return list with random integers from low (inclusive) to high (exclusive).
    number = np.random.randint(0, high=10, size=4, dtype=int)
    # Group the four elements in the list to a str
    strings = [str(num) for num in number]
    a_string = "".join(strings)
    # In the lines below we can modify number value to int (= int(a_string))
    # but remember int removes the 'left sided' ceros.
    number = (a_string)
    print(number)




# Download data from url and print it
def pabajo (url):
    import requests 
    url= input("introduce una url")
        # n = input ("introduce un id para el paquete")
    paquete = requests.get(url).content     
    print(paquete)



# FUNCION QUE IMPORTA ARCHIVO TSV Y LO TRANSFORMA EN DATA FRAME
def tsv_df (x):
    # This line is not needed if you wrote before. Consider deletion.
    import pandas as pd
    import numpy as np

    # Import tsv file.
    import requests 
    # url=input("Instroduce una url valida:")
    url="https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv"

    # Read the file with panda read_csv and delete the delimiters. Create a variable wich is a list with all the data
    x = pd.read_csv(url, delimiter = "\t")
    print (x)

    # Set up the data in columns and rows with an index and so.. aka magic panda's DataFrame
    dfr = pd.DataFrame(data=x)
    dfr


    