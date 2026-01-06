from rest_framework.decorators import action

from packages.framework.controllers import BaseSetController
from packages.kernel.types import ExtendedRequest
from packages.usecases.serializer import SerializerUseCase
from users.serializers import UserSerializer
from users.usecases.user import UserUseCase


class UserSetController(BaseSetController):
    prefix = "users"

    use_case = UserUseCase()
    serializer_use_case = SerializerUseCase()
    serializer_class = UserSerializer

    @action(detail=False, methods=["get"], url_path="obtain")
    def obtain(self, request: ExtendedRequest, *args, **kwargs):
        serializer = self.get_serializer(self.use_case.obtain(request))
        return self.get_response(serializer.data)

    @action(detail=False, methods=["put"], url_path="obtain")
    def obtain(self, request: ExtendedRequest, *args, **kwargs):
        serializer = self.serializer_use_case.is_valid(serializer_class=self.get_serializer_class(), data=request.data)
        result = self.use_case.edit(id=self.request.user.id, data=serializer.validated_data)
        return self.get_response(result)
