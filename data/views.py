from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response
from .serializers import WordDataSerializer
class WordDataAPIView(generics.GenericAPIView):
    serializer_class = WordDataSerializer

    def post(self, request):
        word_file = request.FILES.get('C:\Users\vivek\Desktop\task\tkt_mock_data (1)')

       

        # Serialize the processed data using the serializer
        serializer = self.get_serializer(data=processed_data)
        serializer.is_valid(raise_exception=True)
        serialized_data = serializer.data

        return Response(serialized_data)

