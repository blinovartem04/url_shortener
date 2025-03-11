from django.db import models
import string
import random

def generate_short_code():
    """Генерация случайного короткого кода."""
    length = 6
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

class URL(models.Model):
    original_url = models.URLField(max_length=500)
    short_code = models.CharField(max_length=10, unique=True, default=generate_short_code)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.original_url} -> {self.short_code}"