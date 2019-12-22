from django.db import models
# Create your models here.
class Register_details(models.Model):
	Enter_Name           = models.CharField(max_length=50)  #max length=required length
	Enter_Email_address  = models.EmailField(max_length=30)
	Enter_Username       = models.CharField(max_length=30)
	Enter_Phone    		 = models.IntegerField(default=0)
	Enter_Password       = models.CharField(max_length=32)
	def __str__(self):
		return str((self.Enter_Name,self.Enter_Email_address,self.Enter_Username,self.Enter_Phone,self.Enter_Password))


class Personal(models.Model):
	Aadhar_Number  = models.IntegerField(default=0)
	DOB =models.DateField()
	TYPE = (
		('Hindu', 'Hindu'),
		('Muslim', 'Muslim'),
		('Christian','Christian'),
		('Sikh','Sikh'),
		('Others','Others'),
	)
	Religion = models.CharField(max_length=10, choices=TYPE)
	Address =models.CharField(max_length=50)
	Annual_income =models.IntegerField(default=0)
	Occupation =models.CharField(max_length=20)

	def __str__(self):
		return str((self.Aadhar_Number,self.DOB,self.Religion,self.Address,self.Annual_income,self.Occupation))



class Child(models.Model):
	Gender =(
		('Male','Male'),
		('Female','Female'),
		)
	Child_Gender =models.CharField(max_length=10,choices=Gender)
	Age_Group =(
		('Between 2 to 5','Between 2 to 5'),
		('Between 5 to 10','Between 5 to 10'),
		('Between 10 to 15','Between 10 to 15'),
		('Between 15 to 20','Between 15 to 20'),

		)

	Group =models.CharField(max_length=30,choices=Age_Group)
	Religion=models.CharField(max_length=30)
	def __str__(self):
		return str((self.Child_Gender,self.Group,self.Religion))	


