from rest_framework import serializers
from .models import Blog

class BlogSerializers(serializers.ModelSerializer):

    class Meta:
        fields = ['title','post','category']  #__all__ share all columns of your table
        model = Blog