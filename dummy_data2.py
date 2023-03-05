
import os,django
os.environ['DJANGO_SETTINGS_MODULE'] = 'center.settings'
django.setup()

from faker import Faker
import random
from shop.models import Jewellery


def seed_jewellery(n):
    flag_chois=['English','France']
    fake=Faker()
    images=['30.jpeg','31.jpeg','32.jpeg','33.jpeg','34.jpeg','35.jpeg','36.jpeg','37.jpeg','38.jpeg','39.jpeg','40.jpeg','41.jpeg','42.jpeg','43.jpeg','44.jpeg','45.jpeg','46.jpeg','47.jpeg','48.jpeg','49.jpeg','50.jpeg']
    for _ in range(n):
        image=f"jewellery/{images[random.randint(0,20)]}"
        name=fake.name()
        description=fake.text(max_nb_chars=(1000))
        price=round(random.uniform(1000.99,5000.99),2)
        quantity=random.randint(2,30)
        flag=flag_chois[random.randint(0,1)]
        
        Jewellery.objects.create(
            image=image,
            name=name,
            description=description,
            price=price,
            quantity=quantity,
            flag=flag,

        )
    print(f"seed{n} jewellery ...")
    
seed_jewellery(100)