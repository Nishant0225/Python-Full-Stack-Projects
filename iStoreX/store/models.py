from django.db import models

class CategoryModelClass(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class ProductModelCLass(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="uploads/", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category=models.ForeignKey(CategoryModelClass, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name