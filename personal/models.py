from django.db import models

PRIORITY = [("L", "Low"), ("M", "Medium"), ("H", "high")]

# Create your models here.
class Question(models.Model):
    """Model definition for Question."""

    # TODO: Define fields here
    title = models.CharField(max_length=50)
    question = models.CharField(max_length=200)
    priority = models.CharField(max_length=1, choices=PRIORITY)

    class Meta:
        """Meta definition for Question."""

        verbose_name = "Question Itself"
        verbose_name_plural = "List of Questions"

    def __str__(self):
        """Unicode representation of Question."""
        return self.title

