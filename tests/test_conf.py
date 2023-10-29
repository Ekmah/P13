from django.contrib.auth.models import User

from profiles.models import Profile
from lettings.models import Letting, Address


def populate_test_db():
    user = User.objects.create(username='test', first_name='test1_first_name',
                               last_name='test_last_name', email='t@t.t')
    Profile.objects.create(user=user, favorite_city='favorite_city')
    address = Address.objects.create(number=10, street='street', city='city',
                                     state='ST', zip_code=10,
                                     country_iso_code=100)
    Letting.objects.create(title='title', address=address)
