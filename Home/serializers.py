from rest_framework.serializers import ModelSerializer
from .models import MenuCard

class MenuCardSerializer(ModelSerializer):
    class Meta:
        model = MenuCard
        fields = "__all__"