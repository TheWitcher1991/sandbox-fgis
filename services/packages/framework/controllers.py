from typing import Dict, List, Optional, Type, TypeVar

from rest_framework import generics, viewsets

TAuth = TypeVar("TAuth")
TPermission = TypeVar("TPermission")
TSerializer = TypeVar("TSerializer")


from .mixins import AllowAnyMixin


class Controller:
    authentication_classes_map: Dict[str, List[Type[TAuth]]] = {}
    permission_classes_map: Dict[str, List[Type[TPermission]]] = {}
    serializer_class_map: Dict[str, Type[TSerializer]] = {}

    action_map = None

    def _get_action_or_method(self) -> str:
        return getattr(self, "action", self.request.method).lower()

    def _initialize_authenticators(self, classes: Optional[List[Type[TAuth]]] = None) -> List[TAuth]:
        auth_classes = classes if classes is not None else getattr(self, "authentication_classes", [])
        return [auth() for auth in auth_classes]

    def _initialize_permissions(self, classes: Optional[List[Type[TPermission]]] = None) -> List[TPermission]:
        perm_classes = classes if classes is not None else getattr(self, "permission_classes", [])
        return [perm() for perm in perm_classes]

    def get_authenticators(self) -> list[TAuth]:
        assert self.authentication_classes or self.authentication_classes_map, (
            '"%s" должен либо включать `authentication_classes`, '
            "`authentication_classes_map`, атрибут, либо переопределять "
            "`get_authenticators()` метод." % self.__class__.__name__
        )

        if not self.authentication_classes_map:
            return self._initialize_authenticators()

        action_or_method = self._get_action_or_method()
        auth_classes = self.authentication_classes_map.get(action_or_method)
        return self._initialize_authenticators(auth_classes)

    def get_permissions(self) -> list[TPermission]:
        assert self.permission_classes or self.permission_classes_map, (
            '"%s" должен либо включать `permission_classes`, '
            "`permission_classes_map`, атрибут, либо переопределять "
            "`get_permissions()` метод." % self.__class__.__name__
        )

        if not self.permission_classes_map:
            return self._initialize_permissions()

        action_or_method = self._get_action_or_method()
        permission_classes = self.permission_classes_map.get(action_or_method)
        return self._initialize_permissions(permission_classes)

    def get_serializer_class(self) -> TSerializer:
        assert self.serializer_class or self.serializer_class_map, (
            '"%s" должен либо включать `serializer_class`, '
            "`serializer_class_map`, атрибут, либо переопределять "
            "`get_serializer_class()` метод." % self.__class__.__name__
        )

        if not self.serializer_class_map:
            return self.serializer_class

        action_or_method = self._get_action_or_method()
        return self.serializer_class_map.get(action_or_method) or self.serializer_class


class APIController(Controller, generics.GenericAPIView):
    pass


class APISetController(Controller, viewsets.ViewSetMixin, generics.GenericAPIView):
    pass


class AnonymousController(AllowAnyMixin, APIController):
    pass
