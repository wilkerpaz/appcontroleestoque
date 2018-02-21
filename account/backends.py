from django.contrib.auth.backends import ModelBackend as BaseModelBackend
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class ModelBackend(BaseModelBackend):
    def authenticate(self, request, username=None, password=None):
        if username is not None:
            try:
                user = UserModel.objects.get(email=username)
                if user.check_password(password):
                    return user
            except UserModel.DoesNotExist:
                pass
