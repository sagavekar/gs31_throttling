from rest_framework.throttling import UserRateThrottle

#create own throttle class

class OmkarThrottle(UserRateThrottle):
    scope = "Omkar" # use this scope in setting.py