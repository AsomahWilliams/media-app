from typing import Tuple
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class supplier(BaseModel):
 supplierID:int
 supplierName:str
class product(BaseModel):
 productID:int
 prodname:str
 price:int
 supp:supplier
class customer(BaseModel):
 custID:int
 custname:str
 prod:Tuple[product]

@app.post('/invoice')
async def getInvoice(c1:customer):
    return c1
