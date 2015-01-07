from django.dispatch import Signal

# A new user has registered.
user_registered = Signal(providing_args=["user", "request"])

# A user has activated his/her account.
user_activated = Signal(providing_args=["user", "request"])

# A new password has registered.
password_registered = Signal(providing_args=["user", "request"])

# A new password has activated his/her account.
password_activated = Signal(providing_args=["user", "request"])