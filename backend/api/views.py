import json
from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    # request -> HttpRequest -> Django Request

    body = request.body
    print(body) # byte string of JSON data
    print(request.GET)
    data = {}

    try:
        data = json.loads(request.body)
    except:
        pass
    data['params'] = dict(request.GET)
    data["content_type"] = request.content_type
    data["headers"] = dict(request.headers)
    print(data)

    return JsonResponse(data)
