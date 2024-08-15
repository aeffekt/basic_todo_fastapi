def serializer(todo) -> dict:
    return{
        "id": str(todo["_id"]), # _id: mongodb form to access the table id
        "name":todo["name"],
        "description":todo["description"],
        "complete":todo["complete"]
    }

def list_serial(todos) -> list:
    return(serializer(todo) for todo in todos)
    