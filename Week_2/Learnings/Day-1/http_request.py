#HTTP Request
POST /login HTTP/1.1
Host: api.example.com
content-Type: application/json
Authorization: Bearer token123
{
    "usernme" : "Ram",
    "password" : "secret"
}

#HTTP Response
HTTP/1.1 200 OK
content-Type: application/json

{
    "status" : "success",
    "user_id" : 42
}