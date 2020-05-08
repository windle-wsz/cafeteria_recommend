# 添加和读取数据到数据库中
import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cafeteria.settings")
import random
import os
django.setup()

from user.models import Cafeteria, Tags

images = os.listdir('media/cafeteria')
Cafeteria.objects.all().delete()
Tags.objects.all().delete()
opener = open('cafeteria.csv', 'r')
lines = opener.readlines()
for line in lines[1:]:
    res = line.strip().split(',')
    type = res[0]
    id = res[1]
    name = res[2]
    address = res[3]
    info = res[26]
    image = random.choices(images)[0]
    cafeteria = Cafeteria.objects.create(name=name, intro=info, address=address, pic=image)
    tag_obj, created = Tags.objects.get_or_create(name=type)
    cafeteria.tags.add(tag_obj.id)

print('finished')
