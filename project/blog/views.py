from django.shortcuts import render


def index(request):
    return render(request, 'blog/day_list.html')
