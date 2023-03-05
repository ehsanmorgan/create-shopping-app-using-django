
import os,django
os.environ['DJANGO_SETTINGS_MODULE'] = 'center.settings'
django.setup()

from faker import Faker
import random
from shop.models import Fashion


def seed_fashion(n):
    flag_chois=['English','France']
    fake=Faker()
    images=['1.1.jpeg','1.2.jpeg','1.3.jpeg','1.4.jpeg','1.5.jpeg','1.6.jpeg','1.7.jpeg','1.jpeg','2.1.jpeg','2.2.jpeg','2.3.jpeg','2.4.jpeg','2.5.jpeg','2.6.jpeg','2.7.jpeg','13.jpeg','14.jpeg','15.jpeg','16.jpeg','17.jpeg','18.jpeg','19.jpeg','20.jpeg']
    for _ in range(n):
        image=f"shoping/{images[random.randint(0,22)]}"
        name=fake.name()
        description=fake.text(max_nb_chars=(1000))
        price=round(random.uniform(20.99,99.99),2)
        quantity=random.randint(2,30)
        flag=flag_chois[random.randint(0,1)]
        
        Fashion.objects.create(
            image=image,
            name=name,
            description=description,
            price=price,
            quantity=quantity,
            flag=flag,

        )
    print(f"seed{n} fashion ...")
    
seed_fashion(100)