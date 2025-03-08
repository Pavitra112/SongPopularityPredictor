from django.shortcuts import render,HttpResponse,redirect
from .forms import Predict_Popularity_Form
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from sklearn.linear_model import LinearRegression
import numpy as np

from django.contrib.auth.models import User
# Create your views here.
@login_required
def PredictPopularity(request,pk):
    predicted = False
    prediction=0
    if request.session.has_key('user_id'):
        u_id = request.session['user_id']
        profile = get_object_or_404(User, pk=u_id)
    if request.method == 'POST':
        form = Predict_Popularity_Form(data=request.POST)
        profile = get_object_or_404(User, pk=u_id)
        Title = form['Title']
        Artist = form['Artist']
        Year = form['Year']
        bpm = int(form['bpm'].value())
        Energy = int(form['Energy'].value())
        Danceability= int(form['Danceability'].value())
        Loudness = int(form['Loudness'].value())
        Liveness = int(form['Liveness'].value())
        Valence = int(form['Valence'].value())
        Duration = int(form['Duration'].value())
        Acousticness = int(form['Acousticness'].value())
        Speechiness = int(form['Speechiness'].value())
        f = [[bpm,Energy,Danceability,Loudness,Liveness,Valence,Duration,Acousticness,Speechiness]]
        lr = LinearRegression()
        lr.coef_ = np.array([ 0.01926977 ,-0.09110784,  0.16452147 , 1.0174426,  -0.020846,   -0.10480276, 0.04093382, -0.15302508,  0.16218767])
        lr.intercept_ = 65.53187410230969
        prediction = np.round(lr.predict(f)[0]+10)
        predicted = True
        pred = form.save(commit=False)
        pred.profile = profile
        pred.result = prediction
        pred.save()
        
        if predicted:
            return redirect('/predict/'+ str(pk))

    else:
        form = Predict_Popularity_Form()

        return render(request, 'predict.html',
                      {'form': form,'predicted': predicted,'user_id':u_id,'prediction':prediction,'profile':profile})
