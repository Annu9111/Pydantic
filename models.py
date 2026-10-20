from pydantic import BaseModel


class Model:
    #value : type
    id     : int
    name   : str
    price : float 
    category:str
    is_available : bool
    discription : str
    
item = Model(id = 1,name = "orange",price = "34.5" , category = "orange",is_available=True,discription= "orange is sour fruit")

    
    