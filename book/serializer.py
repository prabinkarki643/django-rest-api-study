import re
from rest_framework import serializers
from .models import Book, BookCompany
from django.template.defaultfilters import slugify

class BookSerializer(serializers.ModelSerializer):
    #Adding extra fileds in response data, slug will be added to each response
    #We need to create a function named get_slug as belows,
    slug = serializers.SerializerMethodField()
    
    class Meta:
        model = Book
        fields = '__all__'  # for all fields to return
        # fields = ["title","description","id"] # for only selected fields to return

    def get_slug(self,obj):
        return  slugify(obj.title)
    
    # Individual validation validate_<field_name>
    def validate_title(self,data):
        if(data):
            book_title = data
            regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
            
            if len(book_title)<3:
                raise serializers.ValidationError('title must be more than 3 chars')
            
            if not regex.search(book_title) == None:
                raise serializers.ValidationError('title can not contains special character')

        return data

    # Used for validating the request body works for all fileds
    # But for individual use individual validation
    # def validate(self, validated_data):
            
    #     if(validated_data.get("title")):
    #         book_title = validated_data["title"]
    #         regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
            
    #         if len(book_title)<3:
    #             raise serializers.ValidationError('title must be more than 3 chars')
            
    #         if not regex.search(book_title) == None:
    #             raise serializers.ValidationError('title can not contains special character')

    #     return validated_data

class BookCompanySerializer(serializers.ModelSerializer):
    book = BookSerializer()
    class Meta:
        model = BookCompany
        fields = '__all__'  # for all fields to return
        # depth=1