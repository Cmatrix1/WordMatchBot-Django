from django.db import models


class OrCondition(models.Model):
    KEYWORD_OPERATION = [
        ('and', 'And'),
        ('or', 'Or'),
    ]
    keywords = models.CharField(max_length=255)
    response = models.ForeignKey("matcher.MessageResponse", verbose_name="", on_delete=models.CASCADE, related_name="or_conditions")
    operation = models.CharField(max_length=5, choices=KEYWORD_OPERATION, default='and', related_name="operation", help_text='At least one condition must be met to send the message.')

    def __str__(self):
        return f"[{self.keywords}] {self.operation} {self.response}"
    
    def get_keywords(self):
        return self.keywords.split(',')


class AndCondition(models.Model):
    KEYWORD_OPERATION = [
        ('and', 'And'),
        ('or', 'Or'),
    ]
    keywords = models.CharField(max_length=255)
    response = models.ForeignKey("matcher.MessageResponse", verbose_name="", on_delete=models.CASCADE, related_name="and_conditions", help_text='All conditions must pass for the message to be sent.')
    operation = models.CharField(max_length=5, choices=KEYWORD_OPERATION, default='and', related_name="operation")
    
    def __str__(self):
        return f"[{self.keywords}] {self.operation} {self.response}"
    
    def get_keywords(self):
        return self.keywords.split(',')


class MessageResponse(models.Model):    
    response = models.TextField()

