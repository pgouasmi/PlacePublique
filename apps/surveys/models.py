from django.db import models
from django.utils.text import slugify

class Question(models.Model):
    text = models.TextField()
    slug = models.SlugField(unique=True)
    category = models.CharField(max_length=100)
    status = models.CharField(
        max_length=20,
        choices=[
            ('draft', 'Brouillon'),
            ('active', 'Actif'),
            ('closed', 'Terminé')
        ],
        default='draft'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    ends_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.text[:50])
        super().save(*args, **kwargs)

class Response(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    dm_id = models.CharField(max_length=100, unique=True)
    text = models.TextField()
    received_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('new', 'Nouveau'),
            ('analyzed', 'Analysé')
        ],
        default='new'
    )

    class Meta:
        ordering = ['-received_at']

class Theme(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    count = models.IntegerField(default=0)

    def increment_count(self):
        self.count += 1
        self.save()

class ResponseTheme(models.Model):
    response = models.ForeignKey(Response, on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    confidence = models.FloatField()

    class Meta:
        unique_together = ['response', 'theme']

class Analysis(models.Model):
    question = models.OneToOneField(Question, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    summary = models.TextField()
    response_count = models.IntegerField()
    main_themes = models.ManyToManyField(Theme, through='AnalysisTheme')

class AnalysisTheme(models.Model):
    analysis = models.ForeignKey(Analysis, on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    count = models.IntegerField()
    percentage = models.FloatField()

    class Meta:
        unique_together = ['analysis', 'theme']