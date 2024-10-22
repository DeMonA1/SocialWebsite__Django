# test absolute url for User model via the ABSOLUTE_URL_OVERRIDES parameter
# python manage.py shell
from django.contrib.auth.models import User
user = User.objects.latest('id')
str(user.get_absolute_url())


# interact with ContentType objects
from django.contrib.contenttypes.models import ContentType
image_type = ContentType.objects.get(app_label='images', model='image')
image_type
image_type.model_class()
from images.models import Image
ContentType.objects.get_for_model(Image)

# test ORM queries with Django Debug Toolbar
# python manage.py debugsqlshell
from images.models import Image
Image.objects.get(id=1)


## redis commands in the container shell
# > SET name "Peter"
# GET name
# EXISTS name
# EXPIRE name 2
# SET total 1
# DEL total


# Python with Redis
import redis
r = redis.Redis(host='localhost', port=6379, db=0)
r.set('foo', 'bar')
r.get('foo')