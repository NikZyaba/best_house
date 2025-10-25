from django.db import models


class OurProjects(models.Model):
    project_image = models.ImageField(verbose_name="Image", help_text="Choose project image")
    project_description = models.CharField(max_length=1000, help_text="Describe project")

    def __str__(self):
        return f"Project {self.id}: {self.project_description[:50]}..."  # первые 50 символов

    class Meta:
        verbose_name = "Our Project"
        verbose_name_plural = "Our Projects"

