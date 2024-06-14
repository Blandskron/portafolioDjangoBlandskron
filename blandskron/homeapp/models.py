from django.db import models

class HardSkill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='skill_images/', blank=True, null=True)
    project_url = models.URLField()

    def __str__(self):
        return self.name