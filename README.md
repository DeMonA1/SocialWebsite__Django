# SocialWebsite

> [!TIP]
> [Main Django commands](https://github.com/DeMonA1/MyBlog__Django/blob/main/README.md#diamonds-basic-django-commands)
## :hammer_and_pick: Launch service
To run server with https protocol:
```
python manage.py runserver_plus --cert-file cert.crt
```
The simple launch:
```
python manage.py runserver
```
In order to launch SocialWebsite docker container:
- [x] [Install docker-desktop](https://docs.docker.com/desktop/setup/install/linux/)
- [x] Run following command:
```
    docker compose up
```
> [!WARNING]
> Be carefull with http and https!!
> If you wanna run server in http, use the simple runserver command,
> otherwise use cert.
> While using this app, you have to turn off adblocker.

## :people_hugging: Social authentication via Google
For access to social feature from python-social-auth and
access for other social service except Google, you have to
add this line into /etc/hosts file:
- ***127.0.0.1   mysite.com***
This domain name will be use for our website.

After creating your app in the GooleAPI add these constants
to the .env file, which is located in the root project directory:
- <ins>GOOGLE_OAUTH2_KEY (in Goole API page has the name as 'Client ID')</ins>
- <ins>GOOGLE_OAUTH2_SECRET</ins>

## :magnet: Redis
To create Redis docker container:
```
    docker pull redis;
    docker run --it --name redis -p 6379:6379 redis;
```
In another shell:
```
    docker exec -it redis sh;
    redis-cli;
```

