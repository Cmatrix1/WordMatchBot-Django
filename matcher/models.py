from django.db import models


class Condition(models.Model):
    KEYWORD_OPERATION = [
        ('and', 'And'),
        ('or', 'Or'),
    ]
    keywords = models.CharField(max_length=255, verbose_name="کلید واژه ها")
    operation = models.CharField(max_length=5, choices=KEYWORD_OPERATION, default='and', verbose_name="عملگر بین کلیدواژه")

    ruleset = models.ForeignKey("matcher.RuleSet", related_name="conditions", on_delete=models.CASCADE, null=True, blank=True, verbose_name="مجموعه‌ی قوانین")

    def __str__(self):
        return f"[{self.keywords}] {self.operation}"
    
    def get_keywords(self):
        return list(map(lambda x: x.strip(), self.keywords.split(','))) 
    
    def check_condition(self, message:str) -> bool:
        keywords = self.get_keywords()
        and_operation = (self.operation == 'and' and all(keyword in message for keyword in keywords))
        or_operation = (self.operation == 'or' and any(keyword in message for keyword in keywords))
        return or_operation or and_operation
    
    class Meta:
        verbose_name = "شرط"
        verbose_name_plural = "شروط"


class RuleSet(models.Model):
    KEYWORD_OPERATION = [
        ('and', 'And'),
        ('or', 'Or'),
    ]
    operation = models.CharField(max_length=5, choices=KEYWORD_OPERATION, default='and', verbose_name="عملگر بین شروط")
    response = models.ForeignKey("matcher.MessageResponse", related_name="conditions", on_delete=models.CASCADE, verbose_name="پاسخ")

    class Meta:
        verbose_name = "مجموعه‌ی قوانین"
        verbose_name_plural = "مجموعه‌های قوانین"

    def __str__(self):
        return f"مجموعه قوانین {self.pk}"
    

class MessageResponse(models.Model):    
    response = models.TextField(verbose_name="پاسخ")

    class Meta:
        verbose_name = "پاسخ پیام"
        verbose_name_plural = "پاسخ‌های پیام"

    def __str__(self):
        return f"{self.pk} - {self.response[:60]}..."
    