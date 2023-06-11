from django.db import models


class Condition(models.Model):
    KEYWORD_OPERATION = [
        ('and', 'And'),
        ('or', 'Or'),
    ]
    keywords = models.CharField(max_length=255)
    operation = models.CharField(max_length=5, choices=KEYWORD_OPERATION, default='and')

    def __str__(self):
        return f"[{self.keywords}] {self.operation} {self.response}"
    
    def get_keywords(self):
        return self.keywords.split(',')


class MessageResponse(models.Model):    
    response = models.TextField()
    or_condition = models.ManyToManyField(Condition, related_name="or_condition", help_text='At least one condition must be met to send the message.')
    and_condition = models.ManyToManyField(Condition, related_name="and_condition", help_text='All conditions must pass for the message to be sent.')

