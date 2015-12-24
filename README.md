# python-shorturl

python implementation of a simple URL shortener service to shorten a long URL. Example, input  an  "http://www.yahoo.com/" output "http://myshorten/1". The short url can be any other string with six characters containing a-z, A-Z and 0-9. 

The approach:

For the shorten request:
- Each shorten request has an unique id, which auto-increment each time
- Convert the id to shortURL by encoding it on base 62
- Insert the shortURL to longURL in redis

For the redirect request:
- Return the longURL from redis
