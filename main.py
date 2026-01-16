from fastapi import FastAPI
from data import product
from database import getData,add_data,update_data,delete_data

from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()
app.add_middleware(CORSMiddleware,allow_origins=["http://localhost:3000"],allow_methods=['*'])

# products=[
#     product(id=1,name='Laptop',description='Lenovo Ideapad Gaming 3',price=70000,quantity=10),
#     product(id=2,name='Laptop',description='Apple Mac M4',price=170000,quantity=12),
#     product(id=3,name='Laptop',description='HP ',price=40000,quantity=90),
#     product(id=4,name='Laptop',description='Dell',price=45000,quantity=100)
#     ]

# @app.get('/')
# def getData():
#     return "welcome to Code...."

# @app.get('/newPage')
# def getData():
#     return "welcome to new Page...."

@app.get("/products/")
def get_ListofProducts():
    return getData()

@app.get('/products/{id}')
def get_Products(id:int):
    products=getData()
    for i in products:
        if i.id==id:
            return i
    return "404 Product not found"

@app.post('/products/')
def add_product(product:product):
    return add_data(product)
    

@app.put('/products/{id}')
def update_product(id:int,product:product):
    return update_data(id,product)

@app.delete('/products/{id}')
def delete_product(id:int):
    return delete_data(id)
