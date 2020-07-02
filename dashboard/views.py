from django.shortcuts import render, redirect
from .models import MelghatHamlets23Apr, FeedbackModel
from django.core.serializers import serialize
from django.http import HttpResponse, HttpResponseRedirect
from .forms import feedbackForm
# Create your views here.

def Dashboard(request):
    obj = MelghatHamlets23Apr.objects.all()
    # raw  = MelghatHamlets23Apr.objects.raw('SELECT * FROM MelghatHamlets23Apr')
    ser_test = serialize('geojson', obj,)
    #print(ser_test)
    context = {'image_loc': ser_test} # Send data to front end
    return render(request,"dashboard/dashboard.html", context)

#def Dashboard(request):
#    return render(request,"dashboard/dashboard.html")
"""
def FeedbackForm(request, lat, lng):
    form = feedbackForm(initial={'lat':lat, 'lng':lng})
    return render(request, "dashboard/feedback.html", {'lat': lat, 'lng': lng, 'form': form})

"""
def FeedbackForm(request, lat, lng):
    print("Inside feedback")
    if request.method == "POST":
        print("Inside request.method")
        form = feedbackForm(initial={'lat':lat, 'lng':lng})
        if form.is_valid():
            # Process the form data
            obj = FeedbackModel()
            obj.lat = form.cleaned_data['lat']
            obj.lng = form.cleaned_data['lng']
            obj.pin = form.cleaned_data['pin']
            obj.address = form.cleaned_data['address']
            obj.state = form.cleaned_data['state']
            obj.city = form.cleaned_data['city']
            obj.domain = form.cleaned_data['domain']
            obj.date = form.cleaned_data['date']
            print("Form Data", form.cleaned_data)
            # Save the data
            obj.save()
            return HttpResponseRedirect('/')
    else:
        form = feedbackForm(initial={'lat':lat, 'lng':lng})
    return render(request, "dashboard/feedback.html", {'lat': lat, 'lng': lng, 'form': form})

    