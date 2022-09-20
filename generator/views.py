from django.shortcuts import render, get_object_or_404
import string, random

def generator(request):
    return render(request, 'generator/generator.html')

def password(request):
    thepassord = ''
    char = string.ascii_lowercase
    length = int(request.GET.get('length')) if 6 <= int(request.GET.get('length')) <= 12 else 9
    if request.GET.get('uppercase'):
        char += string.ascii_uppercase
    if request.GET.get('numbers'):
        char += string.digits
    if request.GET.get('special'):
        char += string.punctuation

    while length >= 0:
        thepassord += random.choice(char)
        length -= 1

    return render(request, 'generator/password.html', {'password':thepassord})
