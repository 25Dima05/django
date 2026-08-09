from django.db import models

class Match(models.Model):
    location = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)
    team_1 = models.CharField(max_length=100)
    team_2 = models.CharField(max_length=100)
    score_team_1 = models.PositiveIntegerField(default=0)
    score_team_2 = models.PositiveIntegerField(default=0)
    winner = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text="Оставьте поле пустым, если матч не сыгран или ничья"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.team_1} vs {self.team_2} ({self.location})"