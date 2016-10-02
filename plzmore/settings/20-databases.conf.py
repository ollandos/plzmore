# flake8: noqa

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': "localhost",
        'PORT': "5432",
        'NAME': "plzmore",
        'USER': "uplzmore",
        'PASSWORD': "plzmore"
    }
}
