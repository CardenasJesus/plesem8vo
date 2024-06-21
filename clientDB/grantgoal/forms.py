from django import forms

class CreateGrantGoalClientForm(forms.Form):

            ggname = forms.CharField(max_length=32, widget= forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe el grantgoal name!"}))
            description= forms.CharField(max_length=32, widget= forms.Textarea(attrs={"type":"text", "class":"form-control", "row": 3, "placeholder":"Escribe el grantgoal description!"}))
            days_duration =forms.IntegerField(widget=forms.NumberInput(attrs={"type":"number", "class":"form-control"}))
            status =  forms.BooleanField(initial= True ,widget=forms.CheckboxInput(attrs={"type":"checkbox"}))
            slug = forms.SlugField (widget= forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe el grantgoal slug!"}))