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