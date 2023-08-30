# from django.shortcuts import render

# from rest_framework import generics
# from rest_framework.response import Response
# from .serializers import WordDataSerializer
# class WordDataAPIView(generics.GenericAPIView):
#     serializer_class = WordDataSerializer

#     def post(self, request):
#         word_file = request.FILES.get('C:\Users\vivek\Desktop\task\tkt_mock_data (1)')
        
       

#         # Serialize the processed data using the serializer
#         # serializer = self.get_serializer(data=processed_data)
#         # serializer.is_valid(raise_exception=True)
#         # serialized_data = serializer.data

#         return Response(serialized_data)
import os
from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Company
from .serializers import CompanySerializer
import json
from django.http import JsonResponse

@api_view(['POST'])
def create_instance_view(request):
    if request.method == 'POST':
        json_file_name = 'tkt_mock_data (1).json' 
        json_file_path = os.path.join(settings.BASE_DIR, json_file_name)
        print("BASE_DIR:", settings.BASE_DIR)
        print("JSON file path:", json_file_path)
        try:
            with open(json_file_path, 'r') as file:
                json_data_list = json.load(file)
        except FileNotFoundError:
            return JsonResponse({'message': 'JSON file not found'}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({'message': 'Invalid JSON format'}, status=400)
        
        for json_data in json_data_list:
            serializer = CompanySerializer(data=json_data)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=400)
        return Response({'message': 'Instance created successfully'})
    else:
        return Response({'message': 'Invalid request method'}, status=405)