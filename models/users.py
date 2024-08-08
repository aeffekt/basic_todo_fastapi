from pydantic import BaseModel

class User(BaseModel):
    name: str
    surname: str
    url: str
    age: int

users = [User("Agustin", "Turko", "www.arnaiz.com.ar", 43)]
