from django.shortcuts import render, redirect
import requests
import json
import random
from django.contrib import messages
from django.contrib.messages import get_messages
api_key = 'sRguZutdBDXqX7qS6_kPp4xgVacIyBzzmhHAeogaN2pSFgSzBsO8PtU3GCCsXzWTVqFqBvv7Hso7C20g2o_6o_6hZyyEnHq1kb6PoF5EE6w_qCBM-39I1rnA0V6KXXYx'


headers = {'Authorization': 'Bearer %s' % api_key}
# Create your views here.


def index(request):

    return render(request, 'ya_yeat_app/index.html')


def rng(request):
    url = 'https://api.yelp.com/v3/businesses/search'
    params = {'term': 'food',
              'location': request.POST['location'], 'is_closed': False, 'limit': 50, 'radius': 8000}
    req = requests.get(url, params=params, headers=headers)
    parsed = json.loads(req.text)
    if not req:
        messages.error(
            request,  request.POST['location'] + " " + 'not in search')
        return redirect('/')
    else:
        businesses = parsed["businesses"]
    request.session['location'] = request.POST['location']
    result = random.choice(businesses)
    print('id:', result['id'])
    print('Name:', result['name'])
    print("Address:", " ".join(result["location"]["display_address"]))
    print('Phone', result['phone'])
    print('Rating', result['rating'])
    print('Link', result['url'])
    print('image_url', result['image_url'])
    request.session['result'] = result
    return redirect('/result')


def result(request):
    return render(request, 'ya_yeat_app/random_result.html')


def reset(request):
    url = 'https://api.yelp.com/v3/businesses/search'
    params = {'term': 'food',
              'location': request.session['location'], 'is_closed': False, 'limit': 50, 'radius': 8000, }
    req = requests.get(url, params=params, headers=headers)
    parsed = json.loads(req.text)
    if not req:
        messages.error(
            request,  request.POST['location'] + " " + 'not in search')
        return redirect('/')
    else:
        businesses = parsed["businesses"]

    result = random.choice(businesses)
    print('id:', result['id'])
    print('Name:', result['name'])
    print("Address:", " ".join(result["location"]["display_address"]))
    print('Phone', result['phone'])
    print('Rating', result['rating'])
    print('Link', result['url'])
    print('image_url', result['image_url'])

    request.session['result'] = result
    return redirect('/result')
