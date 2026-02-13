## Schema Design Case Studies

* selecting wrong schema can lead to cost and using more joins and also performance wise.

### Most popular schemas 

* Flat model
* Hierrachial model
* Network model
* Relational model
* star model
* snowflake maodel

* Database schemas are blue prints which helps developers visualize how databases should be build.

## One to Many and Many to one

* One-to-many 
* Ex: customers and orders , customers can have multiple orders and one order belong to one customer.

* Many-to-one
* Ex: one student can take many classes and one class has many students

# Handling Large Tables

* follwing set of process like when a table reach more than 1 million entries or larger than 100 mb.
* we need to split or move tables or data therewill be set of rules to follow how to hanlde these. storing them somewhere and moving to another databases.


## soft deletes and hard deletes

* soft delete allows data to be marked as deleted but still keeps it in database. 
* while hard delete delete removes the data completly.

## Audit tables and History tracking

* who changed what and when and where these kind of activites comes and history tracking and maintaining chronological record of all data.

## Naming conventions 

* Not using reserved keywords
* Avoiding special characters and spaces.
* Avoiding abbrevations.