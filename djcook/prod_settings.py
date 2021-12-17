from djcook.settings import *

DEBUG = False
ALLOWED_HOSTS = ['*']
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_PRELOAD = True

SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = 3600

MIDDLEWARE.append('core.middleware.UserBasedExceptionMiddleware')

