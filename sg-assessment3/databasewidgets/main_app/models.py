from django.db import models
from django.forms import ModelForm
from django.urls import reverse


class Widget(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=250)
    quantity = models.IntegerField()

    def __str__(self):
        return self.description, self.quantity

    # def get_absolute_url(self):
    #     return reverse('index', kwargs={'widget_id': self.id})


# form for new widget
class WidgetsForm(ModelForm):
    class Meta:
        model = Widget
        fields = ['description', 'quantity']
