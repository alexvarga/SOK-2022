from django import forms

class SearchForm(forms.Form):
    search_node = forms.CharField(help_text="Enter label or part of text or id of a node.", label="Search nodes")
    #TODO clean