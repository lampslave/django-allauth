# -*- coding: utf-8 -*-
from allauth.socialaccount.tests import create_oauth2_tests
from allauth.tests import MockedResponse
from allauth.socialaccount.providers import registry

from .provider import YandexProvider

class YandexTests(create_oauth2_tests(registry.by_id(YandexProvider.id))):
    def get_mocked_response(self):
        # FIXME this is fake data from docs
        # see http://api.yandex.ru/login/doc/dg/reference/response.xml
        return MockedResponse(200, """
        {
            "birthday": "1987-03-12",
            "display_name": "Vasya",
            "id": "1000034426",
            "sex": "male",
            "emails":
            [
            "test@yandex.ru"
            ],
            "default_email": "test@yandex.ru",
            "real_name": "\u041F\u0443\u043F\u043A\u0438\u043D \u0412\u0430\u0441\u044F"
        }""")
