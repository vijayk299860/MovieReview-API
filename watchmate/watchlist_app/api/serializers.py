from watchlist_app.models import *
from rest_framework import serializers



#model serializers
class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review
        # fields = '__all__'
        exclude = ('watchlist',)

class WatchListSerializer(serializers.ModelSerializer):
    # review_set = ReviewSerializer(many=True,read_only=True)
    # length = serializers.SerializerMethodField()
    platform = serializers.CharField(source='stream.name')
    class Meta:
        model = WatchList
        fields = '__all__'
    
    # def get_length(self, obj):
    #     return len(obj.name)
    # def validate_name(self, value):
    #     if len(value)<2:
    #         raise serializers.ValidationError("Name should be at least 2 characters long.")
    #     return value
    
class StreamPlatFromSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(read_only=True,many=True)
    # watchlist = serializers.StringRelatedField(many=True)
    class Meta:
        model = StreamPlatform
        fields = '__all__'
        
# traditional serializers

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     director = serializers.CharField()
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self,instance,validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.director = validated_data.get('director', instance.director)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance