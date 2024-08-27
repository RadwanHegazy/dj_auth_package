# Django Auth Package Explaination

Package for handle and create simple authentication system for your django resst full APIs project, with JWT for tokenization

## Package Installation

```
git clone https://github.com/RadwanHegazy/dj_auth_package
```

```
pip install -r dj_auth_package/requirments.txt
```

```python
# your_project/settings.py

INSTALLED_APPS = [
    ...
    'dj_auth_package',
    'rest_framework',
    ...
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES' : [
        # use JWT for authentication 
        'rest_framework_simplejwt.authentication.JWTAuthentication'
    ]
}

# NOTE: you will use this options for send the OTP code for users in forget password endpoint.
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "EMAIL_HOST"
EMAIL_HOST_USER = "YOUR_EMAIL"
EMAIL_HOST_PASSWORD = "YOUR_PASSWORD"
EMAIL_PORT = 587
EMAIL_USE_TLS = True

```

```python
# your_project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dj-auth/',include('dj_auth_package.urls')),
]

```

## Endpoints for this package :
- login
- register
- change password
- forget password
- re-type frogeted password

### 1. Now you can run server then the package endpoint
### 2. The package is compatible for any type of users.


# NOTE: This package made for fun 