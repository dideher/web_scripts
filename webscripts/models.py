from django.db import models
from markdownx.utils import markdownify
from markdownx.models import MarkdownxField

# Create your models here.

class MyMainMenu(models.Model):
    Label = MarkdownxField()
    application_list = MarkdownxField()
    
    # Create a property that returns the markdown 
    @property
    def formatted_markdown(self):
        return markdownify(self.Label)

    @property
    def formatted_markdown_application_list(self):
        return markdownify(self.application_list)
    # def get_absolute_url(self):
    #     return reverse('markdown-detail', kwargs={'pk': self.pk})
    def __str__(self):
        return self.Label