from apps.management.models import report
from apps.record.models.education import Education
from apps.record.models.resume import Resume
from apps.sys_admin.models.employee import Employee
from apps.management.models.department import Department, Employee_Department
from apps.management.models import Department
from apps.management.models.role import Employee_Role
from rest_framework import serializers
from rest_framework.request import Request
from rest_framework.reverse import reverse
from apps.common.serializer import BaseSerializer
from apps.record.api.serializers import ResumeSerializer
from apps.management.api.serializers import *

resumes = Resume.objects.all()
class ResumeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Resume
        fields = '__all__'


class EmployeeReadSerializer(BaseSerializer):
    """
    --------------------------------------------
    Serialize Employee Model with all fields
    This work for Read Methods of request
    List and Detail 
    --------------------------------------------
    """


    # Custom Fields 
    full_name = serializers.SerializerMethodField()

    # Serialize relationships

    # Management
    roles = RoleSerializer(many=True)
    departments = DepartmentSerializer(many=True)
    teams = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name="team-detail",
        many=True
    )
    reports = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name="report-detail",
        many=True
    )

    # Record
    resume = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name="resume-detail"
        #context={'request': resumes}
    )
    education = serializers.HyperlinkedIdentityField(
        view_name="education-detail",
        read_only=True,
        many=True
    )
    experience = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name="experience-detail",
        many=True
    )

    # Legal
    salary = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name="salary-detail"
    )
    socialsecurity = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name="socialsecurity-detail",
        many=True
    )
    vacation = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name="vacation-detail",
        many=True
    )

    # Intermediate tables
    employee_role = serializers.SerializerMethodField()
    employee_department = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = '__all__' # Add all fields
        # depth=2
        #lookup_field = "indetifier"

    def get_full_name(self, obj):
        """
        -----------------------------------------
        Custom methos to add fiel in the response
        -----------------------------------------
        """
        return f'{obj.first_name} {obj.last_name}'

    def to_representation(self, instance):
        """
        --------------------------------------
        Method manage the json representation
        fields in the api
        -------------------------------------
        """
        representation = super().to_representation(instance)
        del representation["password"] # Don't show the password
        return representation
    
    def get_employee_role(self, obj):
        role_by_employee = Employee_Role.objects.filter(employee=obj.id).all()
        serializer = EmployeeRoleSerializer(role_by_employee, many=True)
        return serializer.data

    def get_employee_department(self, obj):
        department_by_employee = Employee_Department.objects.filter(employee=obj.id).all()
        serializer = EmployeeDepartmentSerializer(department_by_employee, many=True)
        return serializer.data
    

class EmployeeWriteSerializer(BaseSerializer):
    """
    ---------------------------------------
    Class to serializer only update method
    ---------------------------------------
    """
    class Meta:
        model = Employee
        # What fields are allowed to update? and for who?
        fields = [
            "first_name",
            "last_name",
            "password"]
        
class EmployeeLoginSerializer(BaseSerializer):
    """
    ---------------------------------------
    Class to serializer only update method
    ---------------------------------------
    """
    class Meta:
        model = Employee
        # What fields are allowed to update? and for who?
        fields = [
            "email",
            "password"]