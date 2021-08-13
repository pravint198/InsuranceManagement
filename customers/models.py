from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customers(models.Model):
	SELECT=''
	MALE='M'
	FEMALE='F'
	OTHERS='O'

	YES='Y'
	NO='N'

	gender_choices=[(SELECT,'Gender'),(MALE,'Male'),(FEMALE,'Female'),(OTHERS,'Others')]
	is_married_choices=[(SELECT,'Is Married'),(YES,'Yes'),(NO,'No')]

	name=models.CharField(max_length=50)
	father_name=models.CharField(max_length=50)
	mother_name=models.CharField(max_length=50)
	last_name=models.CharField(max_length=50)
	spouse_name=models.CharField(max_length=50,blank=True)
	gender=models.CharField(max_length=1,choices=gender_choices)
	is_married=models.CharField(max_length=1,choices=is_married_choices)
	dob=models.DateField()
	place_of_birth=models.CharField(max_length=25)
	correspondence_address=models.TextField(max_length=100)
	is_perm_same=models.BooleanField()
	permanent_address=models.TextField(max_length=100)	
	pan=models.CharField(max_length=10,unique=True,error_messages={'unique':'Customer with this pan already exists'})
	aadhar=models.CharField(max_length=12, unique=True,error_messages={'unique':'Customer with this aadhar already exists'})
	education=models.CharField(max_length=20)
	mobile=models.CharField(max_length=10)
	height=models.FloatField()
	weight=models.FloatField()
	username=models.CharField(max_length=150)

	def __str__(self):
		return str(self.id)


class Policies(models.Model):
	cid=models.ForeignKey('Customers',on_delete=models.CASCADE)
	policy_no=models.CharField(max_length=15,unique=True,null=False)
	term_plan=models.CharField(max_length=8)
	sum_assured=models.IntegerField()
