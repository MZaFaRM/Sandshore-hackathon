from rest_framework.response import Response

class CustomResponse:
    """
    Represents a custom response object.

    This class provides a convenient way to create and send custom responses in Django REST Framework.

    Args:
        success (bool): Indicates whether the response is successful or not.
        data (Any, optional): The data to be included in the response. Defaults to None.
        error (Any, optional): The error message to be included in the response. Defaults to None.
        status (int, optional): The HTTP status code of the response. Defaults to None.

    Methods:
        send(request): Sends the custom response as a Django REST Framework Response object.
        success(data=None, status=None): Creates a successful custom response object.
        error(error=None, status=None): Creates an error custom response object.

    Example Usage:
        response = CustomResponse.success(data={"message": "Success"})
        return response.send(request)
    """
    def __init__(self, success, data=None, error=None, status=None):
        self.success = success
        self.data = data
        self.error = error
        self.status = status

    def send(self, request):
        if self.status:
            return Response(
                {
                    "success": self.success,
                    "error": self.error,
                    "data": self.data,
                },
                status=self.status,
            )
        return Response(
            {
                "success": self.success,
                "error": self.error,
                "data": self.data,
            }
        )

    @classmethod
    def success(cls, data=None, status=None):
        return cls(success=True, data=data, status=status)

    @classmethod
    def error(cls, error=None, status=None):
        return cls(success=False, error=error, status=status)
