from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):

    """Custom User Model"""

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "other")
    )

    LANGUAGE_ENGLISH = "english"
    LANGUAGE_KOREAN = "korean"

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "English"),
        (LANGUAGE_KOREAN, "한국어")
    )

    
    CURRENCY_USD = "USD"
    CURRENCY_KRW = "KRW"


    CURRENCY_CHOICES = (
        (CURRENCY_USD, "USD"),
        (CURRENCY_KRW, "KRW")
    )

    avatar = models.ImageField(blank=True)
    gender = models.CharField(
        choices = GENDER_CHOICES, max_length=10, blank = True
    )
    bio = models.TextField(default="" , blank = True)
    birthday = models.DateField(null=True)
    language = models.CharField(
        choices = LANGUAGE_CHOICES, max_length=2, blank = True
    )
    currency = models.CharField(
        choices = CURRENCY_CHOICES, max_length=3, blank=True
    )
    superhost = models.BooleanField(default=False)
    pass
