
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets


from vision.serializers import SkillsSerializer
from vision.models import Skills


class SkillsViewSet(viewsets.ModelViewSet):
    queryset = Skills.objects.all()
    # d = 0
    # for i in queryset:
    #     d += float(i.price)
    # permission_classes = [
    #     permissions.AllowAny
    # ]
    serializer_class = SkillsSerializer