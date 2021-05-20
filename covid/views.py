from django.shortcuts import render
import requests
import json

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "d9cbda2f6dmshc2bba4bd0e71c1ap1ab42fjsnc01c43dd2e87"
    # 'x-rapidapi-key': "0d010ca254mshe394daf4b26faa1p1f65cajsna499e90ea195"
}

response = requests.request("GET", url, headers=headers).json()

# print(response.text)


def covid(request):
    if request.method == 'POST':
        selectcountry = request.POST['selectcountry']
        noofresult = int(response['results'])
        for x in range(0, noofresult):
            if selectcountry == response['response'][x]['country']:
                new = response['response'][x]['cases']['new']
                active = response['response'][x]['cases']['active']
                critical = response['response'][x]['cases']['critical']
                recovered = response['response'][x]['cases']['recovered']
                total = response['response'][x]['cases']['total']
        data = {
            'new': new,
            'active': active,
            'critical': critical,
            'recovered': recovered,
            'total': total,
            'selectcountry': selectcountry
        }
        return render(request, 'covid/index.html', data)
    noofresult = int(response['results'])
    mylist = []
    for x in range(0, noofresult):
        mylist.append(response['response'][x]['country'])
    data1 = {
        'mylist': mylist
    }
    # data1 = {'response': response}
    return render(request, 'covid/index.html', data1)
