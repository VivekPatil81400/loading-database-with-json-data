from rest_framework import serializers

class WordDataSerializer(serializers.Serializer):
    name = serializers.CharField()
    sector = serializers.CharField()
    siren = serializers.IntegerField()
    results = serializers.ListField(child = serializers.DictField())

    def create(self, validated_date):
        for data in validated_date:
            name = data.get('name')
            sector = data.get('sector')
            siren = data.get('siren')
            results = data.get('results', [])

            processed_results = []
            for result in results:
                ca = result.get('ca')
                margin = result.get('margin')
                ebitda = result.get('ebitda')
                loss = result.get('loss')
                year = result.get('year')

                processed_result = {
                    'ca' : ca,
                    'margin' : margin,
                    'ebitda' : ebitda,
                    'loss' : loss,
                    'year' : year
                }

                processed_results.append(processed_result)

            word_data = {
                'name' : name,
                'sector' : sector,
                'siren' : siren,
                'results' : processed_results,

            }
            
            return word_data