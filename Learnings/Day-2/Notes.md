CRUD = what you want to do with the data
HTTP = how you say it

CRUD	  Meaning	       HTTP Method	    Endpoint Example
Create	  Add new data	    POST	            /users
Read	  Get data	        GET	                /users
Read-one  Get single item	GET	                /users/5
Update	  Replace data	    PUT	                /users/5
Update	  Partial update	PATCH	            /users/5
Delete	  Remove data	    DELETE	            /users/5


Status code usage(2##)

200     OK(GET/PUT/DELETE)
201     Resource created Successfully(POST)
204     Success but nothing to Return(no content)

Client Errors(4##)

400  Bad request    invalid input
401  Unauthorized   not logged in
403  Forbidden      no permission
404  Not found      resource missing

Server Error(5##)
500      internal server error
502/503  downstream server issue



