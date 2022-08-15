from django.http import JsonResponse


def homepage(request):
    elements = [
        {
            'name': 'Ivan',
            'surname': 'Ivanov',
            'age': '24',
        },
        {
            'name': 'Danil',
            'surname': 'Ivanov',
            'age': '19',
        },
    ]

    if (request.method == 'GET'):
        return JsonResponse(elements, safe=False)

    return JsonResponse(status=400)