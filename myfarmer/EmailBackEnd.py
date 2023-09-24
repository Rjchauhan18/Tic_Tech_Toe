from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

class EmailBackEnd(ModelBackend):
    def authenticate(self, email=None, password=None, **kwargs):
        usermodel = get_user_model()
        try:
            user = usermodel.objects.get(email=email)
        except usermodel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
            return None
                
