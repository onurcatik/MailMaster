# MailMaster

## Step 1
```
python manage.py runserver
```
## Step 2 

```
redis-server
```


## Step 3 
```
celery -A MailMaster  worker --loglevel=info
```