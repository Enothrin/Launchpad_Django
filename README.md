# Launchpad_Django

In der setting.py folgende Punkte vervollständigen:

SECRET_KEY = '1'

AWS_ACCESS_KEY_ID = '[AWS_ACCESS_KEY_ID]'
AWS_SECRET_ACCESS_KEY = '[AWS_SECRET_ACCESS_KEY]'
AWS_STORAGE_BUCKET_NAME = '[AWS_STORAGE_BUCKET_NAME}'

In der home.html folgende Punkte vervollständigen:

const url = "http://[AWS_STORAGE_BUCKET_NAME].s3.amazonaws.com/media/"


Bucket policy

```bash

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Test3",
            "Effect": "Allow",
            "Principal": {
                "AWS": "[AWS_USER_ARN]"
            },
            "Action": [
                "s3:GetObject",
                "s3:PutObject",
                "s3:PutObjectAcl",
                "s3:ListMultipartUploadParts",
                "s3:AbortMultipartUpload",
                "s3:DeleteObject"
            ],
            "Resource": "[AWS_BUCKET_ARN]/*"
        }
    ]
}

```

CORS configuration 

```bash

<?xml version="1.0" encoding="UTF-8"?>
<CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
<CORSRule>
    <AllowedOrigin>*</AllowedOrigin>
    <AllowedMethod>GET</AllowedMethod>
    <AllowedMethod>HEAD</AllowedMethod>
    <AllowedMethod>PUT</AllowedMethod>
    <AllowedMethod>POST</AllowedMethod>
    <MaxAgeSeconds>5000</MaxAgeSeconds>
    <AllowedHeader>*</AllowedHeader>
</CORSRule>
</CORSConfiguration>

```


```bash

pip install -r requirements.txt

python manage.py makemigrations accounts

python manage.py migrate

python manage.py createsuperuser

python manage.py collectstatic

python manage.py runserver

```


