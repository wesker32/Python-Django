from django.http import  HttpResponse

import random

def hello_world(request):
    return HttpResponse("HelloWorld")

def root_page(request):
    return HttpResponse("Root Home page")

def random_number(request, max_rand=100):
    random_num = random.randrange(0, int(max_rand))

    msg = ("Random Number Between 0 and %s : %d" % (max_rand, random_num))

    return HttpResponse(msg)