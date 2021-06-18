from django.db import models
from twilio.rest import Client

# Create your models here.


class Message(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.score >= 70:
            account_sid = 'AC33b4e34a7e5c7ea0d6c9528b349d9cc8'
            auth_token = 'be23ba82eb617c3d17a3839ae0829c82'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body=f"Congratulations {self.name}, your score is {self.score}",
                from_='+12019924209',
                to='+233244895256'
            )
        else:
            account_sid = 'AC33b4e34a7e5c7ea0d6c9528b349d9cc8'
            auth_token = 'be23ba82eb617c3d17a3839ae0829c82'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body=f"Sorry {self.name}, your score is {self.score}. Try again",
                from_='+12019924209',
                to='+233244895256'
            )

        print(message.sid)
        return super().save(*args, **kwargs)
