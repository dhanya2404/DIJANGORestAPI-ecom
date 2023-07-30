from django.db import models
from django.utils import timezone 


CATEGORY_CHOICES = [
    ('tv', 'TV'),
    ('washingmechine', 'WashingMechine'),
    ('hplaptop', 'HpLaptop'),
    ('phone', 'Phone'),
]

# Create your models here.
class doto(models.Model):
    customer = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    Price = models.PositiveIntegerField()
    Image = models.ImageField(upload_to='static/images')   
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=100)
    is_active = models.BooleanField(default=True)
    created_at =models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.name} -- {self.pk}'

    def is_registered_before_two_months(self):
        two_months_ago = timezone.now() - timezone.timedelta(days=60)
        if self.created_at == None:
            return False
        return self.created_at < two_months_ago

    def save(self, *args, **kwargs):
        # Check if the doto is registered before two months and make it inactive
        if self.is_registered_before_two_months():
            self.is_active = False
        super(doto, self).save(*args, **kwargs)