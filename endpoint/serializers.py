from rest_framework import serializers
from .models import PropertyModel, StringModel
from .utils import hash_string, character_map, is_palindrome_check, word_counter
from .exceptions import DuplicateValueError, InvalidRequest, UnprocessableEntry
 


    
class PropertySerializers(serializers.ModelSerializer):
    class Meta:
        model = PropertyModel
        fields = '__all__'


class StringSerializers(serializers.ModelSerializer):
    property = PropertySerializers(read_only=True)
    class Meta:
        model = StringModel
        fields = '__all__'
        read_only_fields = ['length', 'unique_characters', 'word_count', 'is_palindrome', 'character_frequency_map', 'sha256_hash']

    def validate(self, data):
        value = data.get('value')
        if StringModel.objects.filter(value=value):
            raise DuplicateValueError()
        return data
    


    def create(self, validated_data):
        value = validated_data.get('value')
        length = len(value)
        is_palindrome = is_palindrome_check(value)
        unique_characters = len(character_map(value))
        word_count = word_counter(value)
        sha256_hash = hash_string(value)
        character_frequency_map = character_map(value)

        property_instance = PropertyModel.objects.create(
            length=length,
            is_palindrome=is_palindrome,
            unique_characters=unique_characters,
            word_count=word_count,
            sha256_hash=sha256_hash,
            character_frequency_map=character_frequency_map
        )
        string_instance, _ = StringModel.objects.get_or_create(
            id=sha256_hash,
            value=value,
            property=property_instance
        )
        return string_instance

        
