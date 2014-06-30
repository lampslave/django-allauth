# -*- coding: utf-8 -*-
from allauth.socialaccount import providers
from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider


class YandexAccount(ProviderAccount):
    def to_str(self):
        dflt = super(YandexAccount, self).to_str()
        return self.account.extra_data.get('display_name', dflt)


class YandexProvider(OAuth2Provider):
    id = 'yandex'
    name = 'Yandex'
    package = 'allauth.socialaccount.providers.yandex'
    account_class = YandexAccount

    def extract_uid(self, data):
        return data['id']

    def extract_common_fields(self, data):
        return dict(email=data.get('default_email'),
                    username=data.get('display_name'))


providers.registry.register(YandexProvider)
