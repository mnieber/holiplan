from rest_framework.exceptions import ValidationError

from api.model_io import ModelIO


def validate_or_400(io: ModelIO, request_data):
    data, errors = io.validate(request_data)
    if data is None:
        raise ValidationError(errors)
    return data
