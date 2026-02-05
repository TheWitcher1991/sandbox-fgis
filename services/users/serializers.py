from packages.kernel.adapters import ModelSerializerAdapter
from users.models import Member, User


class UserSerializer(ModelSerializerAdapter):

    class Meta:
        model = User
        fields = "__all__"


class MemberSerializer(ModelSerializerAdapter):
    user = UserSerializer()

    class Meta:
        model = Member
        fields = "__all__"
