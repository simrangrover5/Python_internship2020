from django.db import models

# Create your models here.
class Adduser(models.Model):
    fname = models.CharField(max_length=200) #null = True
    lname = models.CharField(max_length=200)
    email = models.EmailField(unique=True)  #unique key, primary=True --> primary key
    password = models.CharField(max_length=200)
    image = models.ImageField(upload_to="static/images")


    def __str__(self):
        return f"{self.email}"

#create table user(column datatype(range))
#fname,lname --> column name
#charfield ---> data type
#max_length --> range
#models.py(table)      +      internship_batch
#do migrations every time you change in models.py file
#1. python manage.py makemigrations (this command will create a file in migration folder)
#use this file for later processing
#2. python manage.py sqlmigrate app_name file_name
#  python manage.py sqlmigrate users 0001
# python manage.py sqlmigrate users 0002
#this command will create a table into sql query format
#3. python manage.py migrate
#this command will add all your tables/models in models.py file into database