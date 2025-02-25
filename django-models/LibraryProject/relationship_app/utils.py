from django.contrib.auth.decorators import user_passes_test

def role_required(role):
    def check_role(user):
        return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == role
    return user_passes_test(check_role)
