from django_filters import FilterSet
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.reverse import reverse

from spacejam import models, serializers


class SpaceViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.SpaceSerializer
    queryset = models.Space.objects.all()
    template_name = 'space-list.jinja'

    class filterset_class(FilterSet):
        pass

    def search(self, request, format=None):
        filter_ = self.filterset_class(self.request.GET, queryset=self.queryset)
        data = {
            "form": filter_.form,
            "results": filter_.qs,
            "form_url": reverse("space-list", format="html"),
        }
        return Response(data, template_name="space-search.jinja")
