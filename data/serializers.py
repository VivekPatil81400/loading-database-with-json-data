from rest_framework import serializers
from .models import Company

class ResultSerializer(serializers.Serializer):
    ca = serializers.IntegerField(allow_null = True)
    margin = serializers.IntegerField(allow_null = True)
    ebitda = serializers.IntegerField(allow_null = True)
    loss = serializers.IntegerField(allow_null = True)
    year = serializers.IntegerField(allow_null = True)

class CompanySerializer(serializers.Serializer):
    name = serializers.CharField()
    sector = serializers.CharField()
    siren = serializers.IntegerField()
    results = ResultSerializer(many=True)

    def create(self, validated_data):
        results_data = validated_data.pop('results')
        company_data = validated_data
        for result in results_data:
            ca = result['ca']
            margin = result['margin']
            ebitda = result['ebitda']
            loss = result['loss']
            year = result['year']
        
            company = Company.objects.create(
                ca = ca,
                margin = margin,
                ebitda = ebitda,
                loss = loss,
                year = year,
                **company_data
            )
        return company