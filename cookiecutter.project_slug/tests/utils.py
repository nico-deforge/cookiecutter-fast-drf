import json

from rest_framework.renderers import JSONRenderer


def serializer_to_json(data):
    return json.loads(JSONRenderer().render(data))
