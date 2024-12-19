# drf-jwt-auth
### Small Description
- A RESTful API designed to exercise JSON Web Tokens (JWT) using Django Rest Framework (DRF) with the SimpleJWT package.
### JWT related features applied
- Main JWT configurations
- Applied Authentication using `Access Token` and `Refresh Token`
- Used `Blacklisting`
- Used `Sliding Token` in authentication
---

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
- Used JWT for login and login refresh and set its configurations in the setting file

---

# JWT Authentication
## First Try (Basic JWT auth)
### Configurations
- in the settings.py file I configured some information like:
    - ACCESS_TOKEN_LIFETIME: one minute for testing
    - REFRESH_TOKEN_LIFETIME: 3 days
    - UPDATE_LAST_LOGIN: Yes
    - SIGNING_KEY: (Using a shared secret key algorithm)
### Urls
- Defined the two enpoints to
    - create a token
    - refresh a token with a refresh token
### in views
- Used in the update and retrieve endpoint
## Second Try (Black List)
- Used the **Blacklist** feature and the rotate and the refresh token black list
- Unsolved problem: That thw access token is not deleted after logout, it will to wait untill expire, not like the refresh one
## Third Try (Sliding Token)
- Applied the sliding token through adding the Comment model
    - I though at first that the view can only had one way, but then understood that sliding is just the type of token not the type of authentication
