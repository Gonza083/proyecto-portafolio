from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=3000)
    image = models.ImageField(upload_to="projects")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    link= models.URLField(null=True, blank=True)

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural= "proyectos"
        ordering = ["-created"]

    def __str__(self):
        return self.title

