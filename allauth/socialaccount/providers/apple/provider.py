from allauth.account.models import EmailAddress
from allauth.socialaccount.app_settings import QUERY_EMAIL
from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider


class AppleProvider(OAuth2Provider):
    id = 'apple'
    name = 'Apple'
    account_class = ProviderAccount

    def extract_uid(self, data):
        return str(data['sub'])

    # def extract_common_fields(self, data):
    #     fields = {
    #         "email": data.get("email")
    #     }
    #     name = data.get("name")
    #     if name:
    #         fields["first_name"] = name.get("firstName", "")
    #         fields["last_name"] = name.get("lastName", "")

    #     return fields

    # def extract_email_addresses(self, data):
    #     ret = []
    #     email = data.get('email')
    #     verified = data.get('email_verified')
    #     if not isinstance(verified, bool):
    #         verified = verified.lower() == 'true'
    #     if email:
    #         ret.append(
    #             EmailAddress(
    #                 email=email,
    #                 verified=verified,
    #                 primary=True,
    #             )
    #         )
    #     return ret

    def get_default_scope(self):
        scopes = ["name"]
        if QUERY_EMAIL:
            scopes.append("email")
        return scopes

    def extract_common_fields(self, data):
        return dict(email=data['user']['email'],
                    last_name=data['user']['name']['firstName'],
                    first_name=data['user']['name']['lastName'])


    def extract_email_addresses(self, data):
        ret = []
        email = data['user']['email']
        if email:
            ret.append(EmailAddress(email=email,
                       verified=True,
                       primary=True))
        return ret


provider_classes = [AppleProvider]