
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#-------------------------------------------------------------------
from django.db.models.signals import post_save				#signals import from django
from django.dispatch import receiver
#-------------------------------------------------------------------

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)     # this line creating one to one relation with existing User model of django 
    bio = models.TextField(max_length=500, blank=True)				# these three lines extending user model 
    location = models.CharField(max_length=30, blank=True)			# on_delete means when user is deleted its new objects also get deleted 
    birth_date = models.DateField(null=True, blank=True)
    profile_image=models.ImageField(default='avtar.png',upload_to='users/',null=True,blank=True)
	
    def __str__(self):                       
        return '%s' % (self.user.username)							#this function returning name of user in profile model(on django profile option)


# here reciever used to recieve signal from user by the server when he POST(send the data)
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile.objects.create(user=instance)			#profile is created using user sign in info 

@receiver(post_save, sender=User)						#profile is saved after collecting data in db permanently
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()													# use these two functions always with each other

#always make admin account after userprofile (recievers) are created otherwise error will occure or make new admin after