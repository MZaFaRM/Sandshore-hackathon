from django.db import models
import uuid


class Department(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=100, unique=True, null=False)
    location = models.CharField(max_length=100, blank=True)

    @property
    def manager(self):
        try:
            return Employee.objects.get(department=self, is_manager=True).full_name
        except Employee.DoesNotExist:
            return None

    def __str__(self):
        return self.name


class Employee(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=15, blank=True)
    date_of_joining = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    is_manager = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.full_name} (Employee ID: {self.employee_id})"

