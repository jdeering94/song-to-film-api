from sys import maxsize
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from songs.models import Context
from jwt_auth.models import CustomUser
User = get_user_model()


class Review(models.Model):

    # text = models.TextField(max_length=300)
    owner = models.ForeignKey(CustomUser, related_name="reviews", on_delete=models.CASCADE)
    usage = models.ForeignKey(Context, related_name="reviews", on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(default=1, validators=[MaxValueValidator(10), MinValueValidator(1)])
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
      return f"Review written by {self.owner} is: {self.rating} written at {self.created_date}"
