from django import forms
from predict_popularity.models import Popularity_Predictions
class Predict_Popularity_Form(forms.ModelForm):
    
    class Meta:
        model = Popularity_Predictions
        fields = ("Title","Artist","Year","bpm","Energy","Danceability","Loudness","Liveness","Valence","Duration","Acousticness","Speechiness")
        widgets = {
            "Title" : forms.TextInput(attrs={'class':'form-control '}),
            "Artist": forms.TextInput(attrs={'class':'form-control '}),
            "Year" : forms.TextInput(attrs={'class':'form-control'}),
            "bpm" : forms.TextInput(attrs={'class':'form-control'}),
            "Energy" : forms.TextInput(attrs={'class':'form-control'}),
            "Danceability" : forms.TextInput(attrs={'class':'form-control'}),
            "Loudness" :forms.TextInput(attrs={'class':'form-control'}),
            "Liveness" :forms.TextInput(attrs={'class':'form-control'}),
            "Valence" : forms.TextInput(attrs={'class':'form-control'}),
            "Duration" : forms.TextInput(attrs={'class':'form-control'}),
            "Acousticness" : forms.TextInput(attrs={'class':'form-control'}),
            "Speechiness" :forms.TextInput(attrs={'class':'form-control'})
            
        }
    
    

