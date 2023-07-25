from django.db import models

class Register(models.Model):
    Id = models.AutoField
    First_Name = models.CharField(max_length=60)
    Last_Name = models.CharField(max_length=60)
    E_mail = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    Re_password = models.CharField(max_length=50)

    def __str__(self):
        return self.First_Name

class Rooms(models.Model):
    Id = models.AutoField
    Room_ID = models.CharField(max_length=50)
    Room_Type = models.CharField(max_length=30)
    Room_Capacity = models.CharField(max_length=40)
    Fee = models.IntegerField(default=0)
    # img = models.ImageField(upload_to="website1/images")

    def __str__(self):
        return self.Room_ID


class Booking(models.Model):
    B_Id = models.AutoField
    Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=30)
    Contact_No = models.IntegerField()
    Check_In = models.DateField()

    def __str__(self):
        return self.Name

class FeedBack(models.Model):
    c_id=models.AutoField
    e_mail = models.CharField(max_length=40)
    comments =  models.CharField(max_length=100)

    def __str__(self):
        return self.e_mail

