from pydantic import BaseModel,Field,field_validator,model_validator,computed_field
from typing import Optional,Literal


class Category(BaseModel):
    Literal['starter','dessert','maincourse','beverage']
    
    
class Model(BaseModel):
    #value : type
    id     : int
    name   : str = Field(...,min_length=3,max_length=100,description="item core")        #required field
    price : float = Field(...,gt=0)        #required field
    category: Category = Field(...)  
    is_available : bool = Field(default = True)    #default field
    discription : Optional[str]=None     #optional field
    
    
    #field validators
    @field_validator('name') 
    @classmethod
    def title_name(cls,value):
        return value.title()
    
    
    #model validator
    @model_validator(mode='after')
    def check_available(self):
        if self.is_available and self.price<=0:
            raise('available element must have price')
        return self 
    
    #computed field
    @computed_field
    @property
    def price_tax(self)->float:
        return round(self.price*0.5,2)
        
        
    
    
    
item = Model(id = 1,name = "orange",price = 34.5 , category = Category(name="starter"),is_available=True,discription= "orange is sour fruit")

# model_dump ->