from packages.kernel.adapters import ModelSerializerAdapter
from users.models import User


class UserSerializer(ModelSerializerAdapter):

    class Meta:
        model = User
        fields = "__all__"
