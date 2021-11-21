import os
from datetime import datetime

import requests
from social_core.exceptions import AuthForbidden
from authapp.models import ShopUserProfile
from geekshop.settings import MEDIA_URL, BASE_DIR


def save_user_profile(backend, user, response, *args, **kwargs):
    if backend.name != 'vk-oauth2':
        return
    url_method = 'https://api.vk.com/method/'
    access_token = response.get('access_token')
    fields = ','.join(['bdate', 'sex', 'about', 'crop_photo'])

    api_url = f"{url_method}users.get?fields={fields}&access_token={access_token}&v={os.getenv('API_VERSION')}"
    response = requests.get(api_url)
    if response.status_code != 200:
        return

    print(response.json())
    data_json = response.json()['response'][0]

    if 'sex' in data_json:
        if data_json['sex'] == 1:
            user.shopuserprofile.gender = ShopUserProfile.FEMALE
        elif data_json['sex'] == 2:
            user.shopuserprofile.gender = ShopUserProfile.MALE
        else:
            user.shopuserprofile.gender = ShopUserProfile.OTHERS

    if 'bdate' is data_json:
        birthday = datetime.strptime(data_json['bdate'], '%d.%m.%Y')

        age = datetime.now().year - birthday.year
        if age < 18:
            user.delete()
            raise AuthForbidden('social_core.backends.vk.VKOAuth2')

        user.age = age

    if 'about' in data_json:
        user.shopuserprofile.about = data_json['about']

    if 'crop_photo' in data_json:
        photo = data_json['crop_photo']['photo']['sizes'][-1]['url']
        name_photo = user
        get_photo = requests.get(photo)
        open(f"{BASE_DIR}/{MEDIA_URL}user_avatar/{name_photo}.jpg", "wb").write(get_photo.content)
        user.avatar = f'user_avatar/{name_photo}.jpg'

    user.save()

