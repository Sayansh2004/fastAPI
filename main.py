from fastapi import FastAPI;
import json 
app=FastAPI();

def load_data():
    with open('dummy.json','r')as f:
        data=json.load(f)
    return data 


@app.get("/")
def hello():
    return {'message':"hello"}


@app.get("/about")
def about():
    return {'message':"This is the about page"}

@app.get("/users")
def view():
    data=load_data()
    return data.get("users")
