from django.db import models
from django.utils.timezone import now

class Note(models.Model):
    """
    Represents a note with text and a completion status.
    """
    text = models.CharField(max_length=200, verbose_name="Note Text")
    is_completed = models.BooleanField(default=False, verbose_name="Completed")
    created_at = models.DateTimeField(default=now)
    def __str__(self):
        """
        Returns a string representation of the note.
        """
        return self.text[:50]

    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Notes"
        ordering = ["-id"]
