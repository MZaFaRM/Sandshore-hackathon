from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Employee, Department
from .serializers import EmployeeSerializer, DepartmentSerializer
from .utils import CustomResponse


class EmployeeAPI(APIView):
    """
    A view for performing CRUD operations on Employee objects.

    Methods:
        - get(request, pk=None): Retrieves a single employee or all employees.
        - post(request): Creates a new employee.
        - put(request, pk): Updates an existing employee.
        - delete(request, pk): Deletes an existing employee.
    """

    def get(self, request, pk=None):
        try:
            if pk:
                employee = Employee.objects.get(pk=pk)
                serializer = EmployeeSerializer(employee)
            else:
                employees = Employee.objects.all()
                serializer = EmployeeSerializer(employees, many=True)

            return CustomResponse.success(data=serializer.data).send(request)
        except Employee.DoesNotExist as e:
            return CustomResponse.error(error=str(e), status=404).send(request)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return CustomResponse.success(data=serializer.data).send(request)
        return CustomResponse.error(error=serializer.errors, status=400).send(request)

    def put(self, request, pk):
        try:
            employee = Employee.objects.get(pk=pk)
            serializer = EmployeeSerializer(employee, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return CustomResponse.success(data=serializer.data).send(request)
            return CustomResponse.error(error=serializer.errors, status=400).send(
                request
            )
        except Employee.DoesNotExist as e:
            return CustomResponse.error(error=str(e), status=404).send(request)

    def delete(self, request, pk):
        try:
            employee = Employee.objects.get(pk=pk)
            employee.delete()
            return CustomResponse.success(data="Successfully deleted").send(request)
        except Employee.DoesNotExist as e:
            return CustomResponse.error(error=str(e), status=404).send(request)


class DepartmentAPI(APIView):
    """
    A view for performing CRUD operations on Department objects.

    Methods:
        - get(request, pk=None): Retrieves a single department or all departments.
        - post(request): Creates a new department.
        - put(request, pk): Updates an existing department.
        - delete(request, pk): Deletes an existing department.
    """

    def get(self, request, pk=None):
        try:
            if pk:
                department = Department.objects.get(pk=pk)
                serializer = DepartmentSerializer(department)
            else:
                departments = Department.objects.all()
                serializer = DepartmentSerializer(departments, many=True)

            return CustomResponse.success(data=serializer.data).send(request)
        except Department.DoesNotExist as e:
            return CustomResponse.error(error=str(e), status=404).send(request)

    def post(self, request):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return CustomResponse.success(data=serializer.data).send(request)
        return CustomResponse.error(error=serializer.errors, status=400).send(request)

    def put(self, request, pk):
        try:
            department = Department.objects.get(pk=pk)
            serializer = DepartmentSerializer(
                department, data=request.data, partial=True
            )
            if serializer.is_valid():
                serializer.save()
                return CustomResponse.success(data=serializer.data).send(request)
            return CustomResponse.error(error=serializer.errors, status=400).send(
                request
            )
        except Department.DoesNotExist as e:
            return CustomResponse.error(error=str(e), status=404).send(request)

    def delete(self, request, pk):
        try:
            department = Department.objects.get(pk=pk)
            department.delete()
            return CustomResponse.success(data="Successfully deleted").send(request)
        except Department.DoesNotExist as e:
            return CustomResponse.error(error=str(e), status=404).send(request)
