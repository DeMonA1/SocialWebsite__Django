# test absolute url for User model via the ABSOLUTE_URL_OVERRIDES parameter
# python manage.py shell
from django.contrib.auth.models import User
user = User.objects.latest('id')
str(user.get_absolute_url())