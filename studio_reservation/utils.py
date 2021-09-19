import random
import string
import time
import os
from django.utils.text import slugify


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_store_image_path(instance, filename):
    new_filename = "{datetime}".format(
        datetime=time.strftime("%Y%m%d-%H%M%S")
    )
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(
        new_filename=new_filename, ext=ext
    )
    return "Stores/{store}/Images/{final_filename}".format(
        store=slugify(instance.name[:50]),
        final_filename=final_filename
    )

def random_string_generator(size=4, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def random_number_generator(size=4, chars='1234567890'):
    return ''.join(random.choice(chars) for _ in range(size))


def simple_random_string():
    timestamp_m = time.strftime("%Y")
    timestamp_d = time.strftime("%m")
    timestamp_y = time.strftime("%d")
    timestamp_now = time.strftime("%H%M%S")
    random_str = random_string_generator()
    random_num = random_number_generator()
    bindings = (
        random_str + timestamp_d + random_num + timestamp_now +
        timestamp_y + random_num + timestamp_m
    )
    return bindings


def simple_random_string_with_timestamp(size=None):
    timestamp_m = time.strftime("%Y")
    timestamp_d = time.strftime("%m")
    timestamp_y = time.strftime("%d")
    random_str = random_string_generator()
    random_num = random_number_generator()
    bindings = (
        random_str + timestamp_d + timestamp_m + timestamp_y + random_num
    )
    if not size == None:
        return bindings[0:size]
    return bindings


def unique_slug_generator(instance=None, field=None, new_slug=None):
    if field == None:
        field = instance.title
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(field[:50])

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug,
            randstr=random_string_generator(size=4)
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug
