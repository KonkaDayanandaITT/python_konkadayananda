## Resource Modeling 
 * it means Representing real word objects or business concepts as structured python objects(modes)
   and treating them as resources in our applications.
 * A resource can be anything that your system manages.
 * ex : user, product, file etc.

 """
    class User:
        def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

 """
 * Here user is resource model 
 * we call it as resource because it has state, behaviour, identity, we can perform CRUD on it.

 ### why do we need it 
 * because we have to map real world concepts neatly.
 * To keep code oraginized and scalable.

## URI Desinging 

* URIs distinguish from one resource from another, That's matters most on the World Wibe Web.
* A URI is a character sequence that identifies a logical (abstract) or physical resource.




