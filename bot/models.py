from datetime import date
from django.db import models
from django.utils.timezone import now
from core.models import TimeStampedModel


class BotUser(TimeStampedModel):
    """
    The bot user
    """

    # Basic data
    chat_id = models.BigIntegerField()
    username = models.CharField(max_length=64, null=True, blank=True)
    first_name = models.CharField(max_length=64, null=True, blank=True)
    last_name = models.CharField(max_length=64, null=True, blank=True)
    joined = models.DateField(default=date.today)
    language_code = models.CharField(max_length=8, null=True, blank=True)

    # Permissions

    is_admin = models.BooleanField(default=False)

    # State
    is_blocked_bot = models.BooleanField(default=False)

    last_action_datetime = models.DateTimeField(null=True, blank=True)

    language = models.CharField(max_length=2, choices=(
        # define your bot languages here
        ('FR', 'fr'),
        ('EN', 'en'),
    ), default=None, null=True, blank=True)

    def __str__(self):
        name = self.first_name
        if self.last_name is not None:
            name += f' {self.last_name}'
        if self.username is not None:
            name += f' (@{self.username})'

        return name

    def report_last_action(self):
        self.last_action_datetime = now()
