from rest_framework.routers import SimpleRouter

from packages.framework.controllers import Controller


def auto_router(*controllers: Controller):
    router = SimpleRouter()

    for ctrl in controllers:
        router.register(
            ctrl.prefix,
            ctrl,
            basename=getattr(ctrl, "basename", ctrl.prefix),
        )

    return router
