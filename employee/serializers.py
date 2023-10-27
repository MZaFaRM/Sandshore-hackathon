import datetime
from rest_framework import serializers
from .models import Employee, Department


class EmployeeSerializer(serializers.ModelSerializer):
    """
    A serializer for Employee objects.
    """
    def validate_is_manager(self, value):
        """
        Needs at least 5 years of experience to be a manager.
        There should also be only one manager per department.
        """
        if (
            value
            and (datetime.date.today() - self.instance.date_of_joining).days < 1825
        ):
            raise serializers.ValidationError(
                "Needs at least 5 years of experience to be a manager"
            )
        elif (
            value
            and Employee.objects.filter(
                department=self.instance.department, is_manager=True
            ).exists()
        ):
            raise serializers.ValidationError("This department already has a manager")
        return value

    def to_representation(self, instance):
        values = super().to_representation(instance)
        values["department"] = DepartmentSerializer(instance.department).data
        return values

    class Meta:
        model = Employee
        fields = "__all__"


class DepartmentSerializer(serializers.ModelSerializer):
    """
    Serializer for Department objects.
    """
    def to_representation(self, instance):
        values = super().to_representation(instance)
        values["manager"] = instance.manager
        return values

    class Meta:
        model = Department
        fields = "__all__"
