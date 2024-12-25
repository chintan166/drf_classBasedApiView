from rest_framework import serializers
from watchlist_app.models import Movie

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description  = serializers.CharField()
    active = serializers.BooleanField()
    
    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
    
    def update(self,instance,validate_data):
        instance.name = validate_data.get('name',instance.name)
        instance.description = validate_data.get('description',instance.description)
        instance.active = validate_data.get('active',instance.active)
        instance.save()
        return instance
        
    def validate_name(self,value):
        if len(value) < 2:
            raise serializers.ValidationError("name is too short")
        else:
            return value
        
    def validate(self,data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("title and dscription not same")
        return data