from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    name=models.CharField(max_length=200,null=True)
    description=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name

# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    TYPE=(
        ('Sedan','Sedan'), 
        ('SUV','SUV'),
        ('WAGON','WAGON'),
        )
    carmake=models.ForeignKey(CarMake,null=True,on_delete=models.SET_NULL)
    dealer_id=models.IntegerField(null=True)
    name=models.CharField(max_length=200,null=True)
    model_type=models.CharField(max_length=200,null=True,choices=TYPE)
    year=models.DateField(auto_now_add=True,null=True)

    def __str__(self):
       return self.name
        

class CarDealer(models.Model):
    dealer_name=models.CharField(max_length=200,null=True)
    # carmake=models.ForeignKey(CarMake,null=True,on_delete=models.SET_NULL)
    # carmodel=models.ForeignKey(CarModel,null=True,on_delete=models.SET_NULL)
   
    def __str__(self):
       return self.dealer_name

# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
