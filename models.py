from pydantic import BaseModel,Field
from typing import Optional


class Model(BaseModel):
    #value : type
    id     : int
    name   : str = Field(...)        #required field
    price : float = Field(...)       #required field
    category:str
    is_available : bool = Field(default = True)    #default field
    discription : Optional[str]=None     #optional field
    
item = Model(id = 1,name = "orange",price = 34.5 , category = "orange",is_available=True,discription= "orange is sour fruit")

    
    