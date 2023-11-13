from django.shortcuts import render
from datetime import datetime
import os


def current_time(request):
    time_ = f'{datetime.now().hour} ч. {datetime.now().hour} мин.'
    my_dict = {
        'title': 'Страница со временем',
        'time': time_
    }
    return render(request, 'first_app/current_time.html', my_dict)


def first_page(request):

    my_dict = {
        'title': 'Страница со временем',

    }
    return render(request, 'first_app/index.html', my_dict)


def work_dir(request):
    list_elem = [i for i in os.listdir(os.getcwd())]
    print(list_elem)
    my_dict = {
        'title': 'Список элементов директории',
        'list_': list_elem
    }

    return render(request, 'first_app/list_dir.html', my_dict)