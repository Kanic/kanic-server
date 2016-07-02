# Kanic


| Name |  Version |
| :--: | :---: |
| [Python][python] | 2.7.X |
| [Django][django] | 1.8.6 |
| [PostgreSQL][post] | 9.X |

REST APIs Guidance
==================
- http://104.236.60.23 is our server ip address, will be replaced by domain name soon. 
- Default admin user: `username=admin`, `password=123`, note: will be changed in the future.

##Authentication Token
###Fetch authentication token
This api is to get authentication for a user
- Method: POST
- Url: `http://104.236.60.23/api-beta/auth/token/`
- Parameters required: `username`, `password`
- Parameters optional: None
- Permissions: No extra permissions needed
- Instructions: Copy paste following commnad in your terminal to get your token for `username:admin` and `password:123`
- Command: `curl -X POST -d "username=admin&password=123" http://104.236.60.23/api-beta/auth/token/`
- Response example:
```javascript
{
  "active":true,
  "token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwidXNlcl9pZCI6MywiZW1haWwiOiJhZG1pbkBnbWFpbC5jb20iLCJleHAiOjE0NjYwNDU1NzZ9.l1g8yvsV03T9utGR6sZvpHUCgiEyNq3VhTm1G9zGRMk",
  "user":"admin"
}
```

##User
###List users
This api is to list out all registered users
- Method: GET
- Url: `http://104.236.60.23/api-beta/users`
- Parameters required: None
- Parameters optional: None
- Permissions: Must be a admin user
- Instructions: Copy paste following commnad in your terminal to get all users.
- Command: `curl -H "Authorization: JWT <admin_token>" http://104.236.60.23/api-beta/users`
- Response example:
```javascript
[
    {
        "url": "http://127.0.0.1:8000/api-beta/users/admin",
        "id": 3,
        "username": "admin",
        "email": "admin@gmail.com",
        "first_name": null,
        "last_name": null,
        "is_mechanic": false,
        "mechanic": null,
        "request_set": [
            {
                "id": 8,
                "car_owner": "http://127.0.0.1:8000/api/users/3/",
                "mechanic": "http://127.0.0.1:8000/api/mechanics/5/",
                "location": "asdasd",
                "scheduled_time": "2018-11-02T03:01:00Z",
                "service": "http://127.0.0.1:8000/api/services/2/",
                "status": 0,
                "extra_info": "aasd"
            }
        ]
    },
    {
        "url": "http://127.0.0.1:8000/api-beta/users/asda",
        "id": 4,
        "username": "asda",
        "email": "aasdad@gmail.com",
        "first_name": null,
        "last_name": null,
        "is_mechanic": false,
        "mechanic": null,
        "request_set": [
            {
                "id": 1,
                "car_owner": "http://127.0.0.1:8000/api/users/4/",
                "mechanic": null,
                "location": "city college",
                "scheduled_time": "2016-06-14T20:52:52Z",
                "service": "http://127.0.0.1:8000/api/services/1/",
                "status": 0,
                "extra_info": ""
            }
        ]
    }
]
```
###Create a user
This api is to create a user
- Method: POST
- Url: `http://104.236.60.23/api-beta/users/create/`
- Parameters required: `username`, `email`, `password`, `is_mechanic`
- Parameters optional: `first_name`, `last_name`
- Permissions: Must be a admin user
- Instructions: Copy paste following commnad in your terminal to create a user.
- Command: `curl -X POST -d "username=david&email=david@gmail.com&password=aaaaa&is_mechanic=False" -H "Authorization: JWT <admin_token>" http://104.236.60.23/api-beta/users/create/`
- Response example:
```javascript
{
  "email":"david@gmail.com",
  "username":"david",
  "is_mechanic":false
}
```
###Show a user's detail
This api is to show a user's detail
- Method: GET
- Url: `http://104.236.60.23/api-beta/api-beta/users/<username>`
- Parameters required: None
- Parameters optional: None
- Permissions: Must be the owner of the profile
- Instructions: Copy paste following commnad in your terminal to create a user.
- Command: `curl -H "Authorization: JWT <admin_token>" http://104.236.60.23/api-beta/users/<username>`
- Response example:
```javascript
{
  "url":"http://127.0.0.1:8000/api-beta/users/dongdong",
  "id":19,
  "username":"dongdong",
  "email":"dongdong@gmail.com",
  "first_name":null,
  "last_name":null,
  "is_mechanic":false,
  "mechanic":null,
  "request_set":[]
}
```
##Mechanic
Note that a mechanic is a User as well but with extra attributes.


##Service
We have a specific range of services
###List all Service
This api is to list all services
- Method: GET
- Url: `http://104.236.60.23/api-beta/services/`
- Parameters required: None
- Parameters optional: None
- Permissions: Must be a admin user
- Instructions: Copy paste following commnad in your terminal to create a user.
- Command: `curl -H "Authorization: JWT <admin_token>" http://104.236.60.23/api-beta/services/`
- Response example:
```javascript
[
    {
        "id": 1,
        "type": "oil change",
        "tools": "ipad",
        "car": "toyota"
    },
    {
        "id": 2,
        "type": "tire change",
        "tools": "Mac",
        "car": "honda"
    },
    {
        "id": 3,
        "type": "brake change",
        "tools": "screw driver",
        "car": "benz"
    }
  ]
```

##Service Request
A request has 4 status, 0(request was created by a car owner), 1(request was assigned to a mechanic by admin), 2(request was accepted by a mechanic), 3(request was completed).
###List all requests
This api is to list all requests
- Method: GET
- Url: `http://104.236.60.23/api-beta/requests/`
- Parameters required: None
- Parameters optional: None
- Permissions: Must be a admin user
- Instructions: Copy paste following commnad in your terminal to create a user.
- Command: `curl -H "Authorization: JWT <admin_token>" http://104.236.60.23/api-beta/requests/`
- Response example:
```javascript
[
    {
        "url": "http://127.0.0.1:8000/api-beta/users/admin",
        "id": 3,
        "username": "admin",
        "email": "admin@gmail.com",
        "first_name": null,
        "last_name": null,
        "is_mechanic": false,
        "mechanic": null,
        "request_set": [
            {
                "id": 8,
                "car_owner": "http://127.0.0.1:8000/api/users/3/",
                "mechanic": "http://127.0.0.1:8000/api/mechanics/5/",
                "location": "asdasd",
                "scheduled_time": "2018-11-02T03:01:00Z",
                "service": "http://127.0.0.1:8000/api/services/2/",
                "status": 0,
                "extra_info": "aasd"
            }
        ]
    },
    {
        "url": "http://127.0.0.1:8000/api-beta/users/asda",
        "id": 4,
        "username": "asda",
        "email": "aasdad@gmail.com",
        "first_name": null,
        "last_name": null,
        "is_mechanic": false,
        "mechanic": null,
        "request_set": [
            {
                "id": 1,
                "car_owner": "http://127.0.0.1:8000/api/users/4/",
                "mechanic": null,
                "location": "city college",
                "scheduled_time": "2016-06-14T20:52:52Z",
                "service": "http://127.0.0.1:8000/api/services/1/",
                "status": 0,
                "extra_info": ""
            }
        ]
    }
  ]
```
###Create a request
This api is to create a request
- Method: POST
- Url: `http://104.236.60.23/api-beta/requests/create/`
- Parameters required: `location`, `scheduled_time`(example: 2018-11-02T03:01:00Z), `car`(need car id), `service`(need service id), `status`
- Parameters optional: `extra_info`
- Permissions: Must be an authorized user(registered user)
- Instructions: Copy paste following commnad in your terminal to create a user.
- Command: `curl -X POST -d "car_owner=1&location=city college&scheduled_time=2018-11-02T03:01:00Z&car=audi&service=1&status=0" -H "Authorization: JWT <admin_token>" http://104.236.60.23/api-beta/requests/create/`
- Response example:
```javascript
{
    "id": 7,
    "car_owner": 9,
    "location": "brooklyn",
    "scheduled_time": "2016-06-29T11:11:00Z",
    "car": "BMW tw22 2013",
    "service": 3,
    "status": 0,
    "extra_info": ""
}
```
###List requests for currently authorized user
This api is to list all requests for currently authorized user
- Method: GET
- Url: `http://104.236.60.23/api-beta/requests/user/`
- Parameters required: None
- Parameters optional: None
- Permissions: Must be an authorized user(registered user)
- Instructions: Copy paste following commnad in your terminal to create a user.
- Command: `curl -H "Authorization: JWT <admin_token>" http://104.236.60.23/api-beta/requests/user/`
- Response example:
```javascript

[
    {
        "car_owner": 7,
        "location": "asdasda",
        "scheduled_time": "2016-06-15T01:01:00Z",
        "service": 3,
        "status": 2,
        "extra_info": "1"
    },
    {
        "car_owner": 7,
        "location": "bronx",
        "scheduled_time": "2016-06-18T21:31:07Z",
        "service": 3,
        "status": 3,
        "extra_info": "hurry up"
    },
    {
        "car_owner": 7,
        "location": "queens",
        "scheduled_time": "2016-06-18T21:24:48Z",
        "service": 3,
        "status": 2,
        "extra_info": "take it easy"
    }
]
```
##Cars
###List all makes in database
This api is to list all all makes in database
- Method: GET
- Url: `http://104.236.60.23/api-beta/makes`
- Parameters required: None
- Parameters optional: None
- Query String(multiple query strings can be used at the same time): 
  * `niceName`(string), example: `http://104.236.60.23/api-beta/makes?niceName=toyota`
  * `has_model_set`(boolean), example: `http://104.236.60.23/api-beta/makes?has_model_set=true`
- Permissions: Must be an authorized user(registered user)
- Instructions: Copy paste following commnad in your terminal to create a user.
- Command: `curl -H "Authorization: JWT <admin_token>" http://104.236.60.23/api-beta/makes?niceName=toyota`
- Response example:
```javascript
[
    {
        "id": 1,
        "name": "Acura",
        "niceName": "acura"
    }
]
```
[python]: https://www.python.org/
[django]: https://www.djangoproject.com/
[post]: https://www.postgresql.org/
