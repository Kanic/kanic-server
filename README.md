# Kanic


| Name |  Version |
| :--: | :---: |
| [Python][python] | 2.7.X |
| [Django][django] | 1.8.6 |
| [PostgreSQL][post] | 9.X |

REST APIs Guidance
==================
http://104.236.60.23 is our server ip address, will be replaced by domain name soon.
##Authentication Token
Fetch token url: http://104.236.60.23/api/auth/token/, copy paste following commnad in your terminal to get your token for `username:admin` and `password:123`. Command: `curl -X POST -d "username=admin&password=123" http://104.236.60.23/api/auth/token/`

Response example:
```javascript
{
  "active":true,
  "token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwidXNlcl9pZCI6MywiZW1haWwiOiJhZG1pbkBnbWFpbC5jb20iLCJleHAiOjE0NjYwNDU1NzZ9.l1g8yvsV03T9utGR6sZvpHUCgiEyNq3VhTm1G9zGRMk",
  "user":"admin"
}
```

##User

##Mechanic(**Note that a mechanic is a User as well but with extra attributes**)

##Request



[python]: https://www.python.org/
[django]: https://www.djangoproject.com/
[post]: https://www.postgresql.org/
