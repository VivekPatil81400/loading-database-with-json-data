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

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Company
from .serializers import CompanySerializer
import json
from django.http import JsonResponse

@api_view(['POST'])
def create_instance_view(request):
    if request.method == 'POST':
        json_file_path = 'C:\Users\vivek\Desktop\task\tkt_mock_data (1).json'
        try:
            with open(json_file_path) as file:
                json_data = json.load(file)
        except FileNotFoundError:
            return JsonResponse({'message': 'JSON file not found'}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({'message': 'Invalid JSON format'}, status=400)
        data = json.loads(json_data) 
        serializer = CompanySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Instance created successfully'})
        else:
            return Response(serializer.errors, status=400)
    else:
        return Response({'message': 'Invalid request method'}, status=405)