from rest_framework import viewsets

from api.models.Transfer import Transfer
from api.serializers.TransferSerializer import TransferSerializer


class TransferViewSet(viewsets.ModelViewSet):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer
