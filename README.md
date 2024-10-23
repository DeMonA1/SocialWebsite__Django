# SocialWebsite__Django

For access to social feature from python-social-auth and
access for other social service except Google, you have to
add this line into /etc/hosts file:
    127.0.0.1   mysite.com
This domain name will be use for our website.

To run server with https protocol:
    python manage.py runserver_plus --cert-file cert.crt

After creating your app in GooleAPI add these constants
to the .env file is in the root project directory:
    GOOGLE_OAUTH2_KEY (in Goole API page has the name as 'Client ID')
    GOOGLE_OAUTH2_SECRET

To create Redis docker container:
    docker pull redis
    docker run --it --name redis -p 6379:6379 redis

In another shell:
    docker exec -it redis sh

    redis-cli
    
TO RUN the bookmark project:

- You should install docker;
- Run following command:
    docker compose up
