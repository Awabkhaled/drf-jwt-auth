# drf-jwt-auth
### Small Description
- A RESTful API designed to exercise JSON Web Tokens (JWT) using Django Rest Framework (DRF) with the SimpleJWT package.

# User
### User Model
- Simple Model with user name and password only
### User serializer
- simple serializer that ensure using the create_user I created
- Updating ensuring password secure and using the current user
### User Api View
#### Create View
- Used The Built in Create API View
#### Update and retrieve
- Used The Built in Retrieve Update API View, with overloading the get object (get the current user) method
### Authentication
- Did not implement it yet