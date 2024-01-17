# Postman, REST Client (vscode extensions) required!!!

Part 1 - Make a Provider in a Minute
# make your own Authorization Server to issue access tokens to client applications for a certain API.

client_id=id
client_secret=secret
redirect_uri=https://www.getpostman.com/oauth2/callback

code=pvXGXibuO8Vsc9OU6jhubszBJ2E1ei
access_token=Db2pgTeYoSmRvV0RIilQ0LuKgXK0Qc

Part 2 - protect your APIs
# we have an authorization server and we want it to provide an API to access some kind of resources. 
# We don’t need an actual resource, so we will simply expose an endpoint protected with OAuth2

For a quick test, try accessing your app at the url /api/hello with your browser and verify that it responds with a 403 (in fact no HTTP_AUTHORIZATION header was provided). 

Try performing a request and check that your Resource Server aka Authorization Server correctly responds with an HTTP 200.


Part 3 - OAuth2 token authentication
# Use an Access Token to authenticate users against Django’s authentication system.
To enable OAuth2 token authentication you need a middleware that checks for tokens inside requests and a custom authentication backend which takes care of token verification