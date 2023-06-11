from django.db import models


class Condition(models.Model):
    KEYWORD_OPERATION = [
        ('and', 'And'),
        ('or', 'Or'),
    ]
    keywords = models.CharField(max_length=255)
    response = models.ForeignKey("matcher.MessageResponse", verbose_name="", on_delete=models.CASCADE, related_name="conditions")
    operation = models.CharField(max_length=5, choices=KEYWORD_OPERATION, default='and')

    def __str__(self):
        return f"[{self.keywords}] {self.operation} {self.response}"
    
    def get_keywords(self):
        return self.keywords.split(',')


class MessageResponse(models.Model):    
    response = models.TextField()

