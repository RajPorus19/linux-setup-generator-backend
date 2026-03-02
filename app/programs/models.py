from django.db import models

    

class ProgramCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name = "Program Category"
        verbose_name_plural = "Program Categories"

class Program(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    git_path = models.CharField(max_length=255)
    is_daemon = models.BooleanField(default=False)
    categories = models.ManyToManyField(ProgramCategory, blank=True)

    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name = "Program"
        verbose_name_plural = "Programs"

class LinuxDistribution(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Linux Distribution"
        verbose_name_plural = "Linux Distributions"

class InitSystem(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Init System"
        verbose_name_plural = "Init Systems"

class DisplayServerProtocol(Program):
    pass