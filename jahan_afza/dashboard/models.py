from django.db import models



class ProjectRequest(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30 , unique=True)
    message = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class ConsultingPage(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30 , unique=True)
    phone = models.CharField(max_length=11)
    message = models.CharField(max_length=150)

class NewsLetterForm(models.Model):

    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=30 , unique=True)

    def __str__(self):
        return self.email


# class ContactUs(models.Model):

#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=20)
#     email = models.EmailField(max_length=30 , null=True , blank=True)
#     phone = models.CharField(max_length=20)
#     message = models.CharField(max_length=30)