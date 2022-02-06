from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse
import datetime

zodiac_dict = {
    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': 'Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
}

zodiac_days_dict = {
    'aries': [datetime.date(2021, 3, 21) + datetime.timedelta(days=x) for x in range((datetime.date(2021, 4, 20) - datetime.date(2021, 3, 21)).days + 1)],
    'taurus': [datetime.date(2021, 4, 21) + datetime.timedelta(days=x) for x in range((datetime.date(2021, 5, 21) - datetime.date(2021, 4, 21)).days + 1)],
    'gemini': [datetime.date(2021, 5, 22) + datetime.timedelta(days=x) for x in range((datetime.date(2021, 6, 21) - datetime.date(2021, 5, 22)).days + 1)],
    'cancer': [datetime.date(2021, 6, 22) + datetime.timedelta(days=x) for x in range((datetime.date(2021, 7, 22) - datetime.date(2021, 6, 22)).days + 1)],
    'leo': [datetime.date(2021, 7, 23) + datetime.timedelta(days=x) for x in range((datetime.date(2021, 8, 21) - datetime.date(2021, 7, 23)).days + 1)],
    'virgo': [datetime.date(2021, 8, 22) + datetime.timedelta(days=x) for x in range((datetime.date(2021, 9, 23) - datetime.date(2021, 8, 22)).days + 1)],
    'libra': [datetime.date(2021, 9, 24) + datetime.timedelta(days=x) for x in range((datetime.date(2021, 10, 23) - datetime.date(2021, 9, 24)).days + 1)],
    'scorpio': [datetime.date(2021, 10, 24) + datetime.timedelta(days=x) for x in range((datetime.date(2021, 11, 22) - datetime.date(2021, 10, 24)).days + 1)],
    'sagittarius': [datetime.date(2021, 11, 23) + datetime.timedelta(days=x) for x in range((datetime.date(2021, 12, 22) - datetime.date(2021, 11, 23)).days + 1)],
    'capricorn': [datetime.date(2021, 12, 23) + datetime.timedelta(days=x) for x in range((datetime.date(2022, 1, 20) - datetime.date(2021, 12, 23)).days + 1)],
    'aquarius': [datetime.date(2021, 1, 21) + datetime.timedelta(days=x) for x in range((datetime.date(2021, 2, 19) - datetime.date(2021, 1, 21)).days + 1)],
    'pisces': [datetime.date(2021, 2, 20) + datetime.timedelta(days=x) for x in range((datetime.date(2021, 3, 20) - datetime.date(2021, 2, 20)).days + 1)],
}

type_dict = {
    'fire': ["aries", "leo", "sagittarius"],
    'earth': ["taurus", "virgo", "capricorn"],
    'air': ["gemini", "libra", "aquarius"],
    'water': ["cancer", "scorpio", "pisces"],
}




def type(request):
    types = list(type_dict)
    """
    <ol>
        <li>aries</li>
        <li>taurus</li>
        <li>gemini</li>
        ...
    </ol>    
    """
    li_elements = ''
    for type in types:
        redirect_path = reverse('horoscope-type', args=[type])
        li_elements += f"<li> <a href='{redirect_path}'>{type.title()} </a> </li>"
    response = f"<ul>{li_elements}</ul>"
    return HttpResponse(response)

def get_info_about_type_zodiac(request, type_zodiac: str):
    list_signs = type_dict.get(type_zodiac)
    if list_signs:
        li_elements = ''
        for type in list_signs:
            redirect_path = reverse('horoscope-name', args=[type])
            li_elements += f"<li> <a href='{redirect_path}'>{type.title()} </a> </li>"
        response = f"<ul>{li_elements}</ul>"
        return HttpResponse(response)
    else:
        return HttpResponseNotFound(f'Неизвестная стихия - {type_zodiac}')

def index(request):
    zodiacs = list(zodiac_dict)
    #f"<li> <a href='{redirect_path}'>{sign.title()} </a> </li>"
    context = {
        'zodiacs': zodiacs,
    'zodiac_dict': {},
    }
    return render(request, 'horoscope/index.html', context=context)

def get_info_about_sign_zodiac(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac)
    data = {
        'description': description,
        'sign': sign_zodiac,
        'zodiacs': zodiac_dict,
    }
    return render(request, 'horoscope/info_zodiac.html', context=data)

def get_info_about_sign_zodiac_by_number(request, sign_zodiac: int):
    zodiacs = list(zodiac_dict)
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound(f'Неправильный порядковый номер зодиака - {sign_zodiac}')
    name_zodiac = zodiacs[sign_zodiac-1]
    redirect_url = reverse('horoscope-name', args=(name_zodiac, ))
    return HttpResponseRedirect(redirect_url)


def get_info_by_date(request, month, day):
    sign_date = ''
    if month == 1 and day in range(21):
        sign_date = datetime.date(2022, month, day)
    elif month == 2 and day == 29:
        sign_date = datetime.date(2021, month, 28)
    else:
        try:
            sign_date = datetime.date(2021, month, day)
        except ValueError:
            return HttpResponse('<h1>Вы ввели неправильную дату</h1>')
    for key, value in zodiac_days_dict.items():
        if sign_date in value:
            redirect_path = reverse('horoscope-name', args=[key])
            return HttpResponse(f"Ваш знак зодиака - <a href='{redirect_path}'>{key.title()} </a>")