from packages.framework.usecases import UseCaseAdapter
from users.models import Employee
from users.types import EmployeeId


class EmployeeUseCase(UseCaseAdapter[Employee, EmployeeId]):
    def __init__(self):
        super().__init__(Employee)


employee_use_case = EmployeeUseCase()
