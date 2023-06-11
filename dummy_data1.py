
import os,django
os.environ['DJANGO_SETTINGS_MODULE'] = 'center.settings'
django.setup()

from faker import Faker
import random
from shop.models import Electronic


def seed_electronic(n):
    flag_chois=['English','France']
    fake=Faker()
    images=['b.jpeg','c.jpeg','d.jpeg','e.jpeg','f.jpeg','g.jpeg','h.jpeg','i.jpeg','j.jpeg','k.jpeg','m.jpeg','n.jpeg','x.jpeg','z.jpeg']
    for _ in range(n):
        image=f"electronic/{images[random.randint(0,13)]}"
        name=fake.name()
        description=fake.text(max_nb_chars=(1000))
        price=round(random.uniform(200.99,999.99),2)
        quantity=random.randint(2,30)
        flag=flag_chois[random.randint(0,1)]
        
        Electronic.objects.create(
            image=image,
            name=name,
            description=description,
            price=price,
            quantity=quantity,
            flag=flag,

        )
    print(f"seed{n} electronic ...")
    
seed_electronic(100)

