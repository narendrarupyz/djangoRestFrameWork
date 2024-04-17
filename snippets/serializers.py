from rest_framework import serializers # type: ignore
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


#Serializer class
"""class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')"""

#ModelSerializer class
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']

    def create(self, validateted_date):
        """Created and return a new 'Snippet' instance, give the validated date"""
        return Snippet.objects.create(**validateted_date)
    
    def update(self, instance, validateed_date):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validateed_date.get('title', instance.title)
        instance.code = validateed_date.get('code', instance.code)
        instance.linenos = validateed_date.get('linenos', instance.linenos)
        instance.language = validateed_date.get('language', instance.language)
        instance.style = validateed_date.get('style', instance.style)
        instance.save()
        return instance