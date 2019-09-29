import random
import string
from django.utils.text import slugify


# def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
#     return ''.join(random.choice(chars) for _ in range(size))

def random_int_generator(size=5):
    return random.randint(1500,9600)

def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = random_int_generator(size=5)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    # if qs_exists:
    #     new_slug = "{slug}-{randstr}".format(
    #                 slug=slug,
    #                 randstr=random_string_generator(size=4)
    #             )
    if qs_exists:
        new_slug = "{randstr}".format(
                    randstr=random_int_generator(size=4)
                )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug