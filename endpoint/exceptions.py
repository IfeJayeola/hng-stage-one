from rest_framework import status
from rest_framework.views import exceptions
from rest_framework.exceptions import APIException


class DuplicateValueError(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = "String already exists in the system"
    default_code = "409 Conlict"


class InvalidRequest(APIException):
    status_code=status.HTTP_400_BAD_REQUEST
    default_detail = "Invalid request body or missing value field"
    default_code="400 Bad Request"
    
class UnprocessableEntry(APIException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    default_detail = "Invalid data type for entry - must be string"
    default_code = "422 Unprocessable Entry"
