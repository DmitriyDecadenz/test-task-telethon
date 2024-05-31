# Test Task Telethon


# How to start app

1. 
```terminal
poetry shell
```
2.
```terminal
poetry install
 ```
3.
create .env file 

fill the fields

example:

```terminal
API_ID = 12345
```

```terminal
API_HASH = '0123456789abcdef0123456789abcdef'
```

4.
```terminal
uvicorn src.main:app --reload
```
