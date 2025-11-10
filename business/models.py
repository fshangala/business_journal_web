from django.db import models

# Create your models here.
class Business(models.Model):
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
ENTRY_TYPE_CHOICES=[
	('CAPITAL','Capital'),
	('SALE','Sale'),
	('EXPENSE','Expense'),
]
class BusinessEntry(models.Model):
    business=models.ForeignKey(Business,on_delete=models.CASCADE)
    entry_type=models.CharField(max_length=100,choices=ENTRY_TYPE_CHOICES)
    description=models.TextField()
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    date=models.DateField()
    
    def __str__(self):
        return f"{self.business.name} - {self.entry_type}"
    
    class Meta:
        ordering=['-date']