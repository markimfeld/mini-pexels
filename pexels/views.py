from django.shortcuts import render

import requests

def is_valid_queryparam(param):
    return param != '' and param is not None

def home(request):

    # api for dolar
    URL = 'https://www.dolarsi.com/api/api.php?type=valoresprincipales'

    json = requests.get(URL).json()


    compra_oficial = json[0]['casa']['compra']
    venta_oficial = json[0]['casa']['venta']

    compra_blue = json[1]['casa']['compra']
    venta_blue = json[1]['casa']['venta']


    category = request.GET.get('category')

    headers = {
        'Authorization': '563492ad6f91700001000001d27a49601b434ade90674bf3293a18d2',
    }

    url = "https://api.pexels.com/v1/search"
    per_page = 50

    params = (
        ('query', 'people'),
        ('per_page', per_page)
    )

    if is_valid_queryparam(category):
        params = (
            ('query', category),
            ('per_page', per_page)
        )

    response = requests.get(url, headers=headers, params=params)


    context = {
        'compra_oficial': compra_oficial,
        'venta_oficial': venta_oficial,
        'compra_blue': compra_blue,
        'venta_blue': venta_blue
    }

    if response.status_code == 200:
        data = response.json()

        total_results = data["total_results"]
        
        if total_results > 0:
            photos = data["photos"]
            next_page = data["next_page"]

            print(next_page)

            context = {
                'photos': photos,
                'compra_oficial': compra_oficial,
                'venta_oficial': venta_oficial,
                'compra_blue': compra_blue,
                'venta_blue': venta_blue
            }
        else: 
            context = {
                'compra_oficial': compra_oficial,
                'venta_oficial': venta_oficial,
                'compra_blue': compra_blue,
                'venta_blue': venta_blue
            }

    return render(request, 'pexels/home.html', context)