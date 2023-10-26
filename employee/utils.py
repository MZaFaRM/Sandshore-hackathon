from rest_framework.response import Response

class CustomResponse:
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
