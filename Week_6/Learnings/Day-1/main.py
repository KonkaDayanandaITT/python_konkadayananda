from fastapi import FastAPI

app = FastAPI()

users = [
    {
        "id": 1,
        "user_name": "ajack",
    },
    {
        "id": 2,
        "user_name": "mamba",
    },
    {
        "id": 3,
        "user_name": "okoye",
    },
    {
        "id": 4,
        "user_name": "tchalaa",
    },
    
]

@app.get("/")
def home():
    return {"message": "Hello, FastAPI!"}

@app.get("/users")
def about():
    return users

@app.get("/users/{user_id}")
def get_user(user_id:int):
    for user in users:
        if user["id"] == user_id:
            return user
    return {"message":"user not found"}

@app.post("/users")
def create_user():
    new_user = {"id": 5, "name":"mbaku"}
    users.append(new_user)
    return {"message": "user created", "users":users}

@app.put("/users")
def update_user():
    users[0]["User_name"] = "Updated_name"
    return {"message": "user Updated","users":users}

@app.delete("/users")
def delete_user():
    users.pop()
    return {"message": "user deleted", "users":users}


