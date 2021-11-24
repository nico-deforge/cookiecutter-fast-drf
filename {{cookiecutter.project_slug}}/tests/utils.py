import json
from datetime import date
from typing import Type

from rest_framework.exceptions import APIException
from rest_framework.renderers import JSONRenderer


def serializer_to_json(data):
    return json.loads(JSONRenderer().render(data))


def exception_to_json(exception_class: Type[APIException]):
    return json.loads(
        JSONRenderer().render(
            {
                "errors": [
                    {
                        "message": exception_class.default_detail,
                        "code": exception_class.default_code,
                    }
                ]
            }
        )
    )

def match_drf_date(date: date) -> str:
    return date.strftime("%Y-%m-%d")
