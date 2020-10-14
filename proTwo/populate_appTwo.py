import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','proTwo.settings')
import django
django.setup()
from appTwo.models import AccessRecord,Topic,Webpage,User
import random
from faker import Faker
topics = ['search','social','marketplace','news','games']
fakegen=Faker()

def add_topic():
    t=Topic.objects.get_or_create(top_name= random.choice(topics))[0]
    t.save()
    return t 

def populate(n=5):
    for entry in range(n):
        top=add_topic()
        fake_url=fakegen.url()
        fake_date=fakegen.date()
        fake_name=fakegen.company()
        webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]
        acc_rec=AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]
def populater(n=5):
    for entry in range(n):
        fake_fname=fakegen.first_name()
        fake_lname=fakegen.last_name()
        fake_email=fakegen.ascii_email()
        use=User.objects.get_or_create(fname=fake_fname,lname=fake_lname,email=fake_email)[0]


if __name__=='__main__':
    print("populating script!")
    populater(10)
    print("population Completed!")