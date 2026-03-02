from rest_framework.routers import DefaultRouter

from .views import (
    ProgramCategoryViewSet,
    ProgramViewSet,
    LinuxDistributionViewSet,
    InitSystemViewSet,
    DisplayServerProtocolViewSet,
)

router = DefaultRouter()
router.register(
    "program-categories",
    ProgramCategoryViewSet,
    basename="program-category",
)
router.register("programs", ProgramViewSet, basename="program")
router.register(
    "linux-distributions",
    LinuxDistributionViewSet,
    basename="linux-distribution",
)
router.register("init-systems", InitSystemViewSet, basename="init-system")
router.register(
    "display-server-protocols",
    DisplayServerProtocolViewSet,
    basename="display-server-protocol",
)

urlpatterns = router.urls
