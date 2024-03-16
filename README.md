# Simple Web App

## Overview

This project is a simple web application for sending scheduled emails. It follows the [Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html) pattern.

## Tech Stacks
- Python 3.11
- Flask Micro Framework
- PostgreSQL & SQLAlchemy (ORM)
- Redis
- Celery & Celery Beat

## How to Run It?

Copy .env.example:
```
cp .env.example .env
```

### Run with Docker Compose

**Requirements:** Docker and Docker Compose must be installed.


Start the project with the following command:
```
docker-compose up -d
```
The application can be accessed at: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

### Run Without Docker Compose
**Requirements:** Redis must be installed for Celery to work.

Setup virtual environment with the following command:



#### 1.  Run the app:
```
flask --app src/app run
```

#### 2. Run the Celery worker
```
celery -A src.celery_config.celery_app worker --loglevel=info
```

#### 3. Run the Celery Beat
```
celery -A src.celery_config.celery_app beat
```

The application can be accessed at: [https://127.0.0.1:5000/](https://127.0.0.1:5000/)

## Migrate db
With docker:
```
docker exec -it flask_app flask db upgrade
```

Without docker:
```
flask db upgrade
```

### Import Sample data
Import sample data using the SQL query below:

```
INSERT INTO events (id, name)
VALUES 
    (1, 'Event 1'),
    (2, 'Event 2'),
    (3, 'Event 3');

INSERT INTO users (id, email)
VALUES 
    (1, 'user1@example.com'),
    (2, 'user2@example.com'),
    (3, 'user3@example.com');

INSERT INTO event_user_association (event_id, user_id)
VALUES 
    (1, 1), -- Event 1 with User 1
    (1, 2), -- Event 1 with User 2
    (2, 2), -- Event 2 with User 2
    (3, 1), -- Event 3 with User 1
    (3, 3); -- Event 3 with User 3
```

## How to run the tests

```
python -m unittest discover -s tests
```

## User Interface
You can access http://localhost:5000 to use the user interface to create emails.

## Example request with curl command


```
curl -X POST \
  http://localhost:5000/email \
  -H 'Content-Type: application/json' \
  -d '{
  "event_id": 1,
  "email_subject": "Example subject 3",
  "email_content": "Example email content",
  "timestamp": "15 Dec 2015 23:12"
}'

```

Sample Response (200 OK):

```
*   Trying 127.0.0.1:5000...
* Connected to localhost (127.0.0.1) port 5000 (#0)
> POST /email HTTP/1.1
> Host: localhost:5000
> User-Agent: curl/7.88.1
> Accept: */*
> Content-Type: application/json
> Content-Length: 139
> 
< HTTP/1.1 200 OK
< Server: gunicorn
< Date: Sat, 16 Mar 2024 13:24:04 GMT
< Connection: close
< Content-Type: application/json
< Content-Length: 123
< 
{"email_content":"Example email content","email_subject":"Example subject 3","event_id":1,"timestamp":"15 Dec 2015 23:12"}
* Closing connection 0

```