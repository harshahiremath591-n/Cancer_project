from django.db import models

class CancerPrediction(models.Model):
    image = models.ImageField(upload_to='scans/')
    result = models.CharField(max_length=100)
    confidence = models.FloatField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.result} - {self.confidence}%"