from rest_framework import viewsets, filters

from .models import (
    ProgramCategory,
    Program,
    LinuxDistribution,
    InitSystem,
    DisplayServerProtocol,
)
from .serializers import (
    ProgramCategorySerializer,
    ProgramSerializer,
    LinuxDistributionSerializer,
    InitSystemSerializer,
    DisplayServerProtocolSerializer,
)


class ProgramCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ProgramCategory.objects.all()
    serializer_class = ProgramCategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "slug", "description"]


class ProgramViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "slug", "description"]


class LinuxDistributionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = LinuxDistribution.objects.all()
    serializer_class = LinuxDistributionSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "slug", "description"]


class InitSystemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = InitSystem.objects.all()
    serializer_class = InitSystemSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "slug", "description"]


class DisplayServerProtocolViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DisplayServerProtocol.objects.all()
    serializer_class = DisplayServerProtocolSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "slug", "description"]
