from django.shortcuts import render

# Create your views here.
import requests

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "87a16a94a4msh743e5484107193dp1cc668jsncc64f55fdce3"
    }

response = requests.request("GET", url, headers=headers).json()

#print(response.text)


def hello(request):
   
    noofres =int(response['results'])
    mylist=[]
    for x in range(0,noofres):
        mylist.append(response['response'][x]['country'])

    if request.method =="POST":
        selectedcountry=request.POST['selectedcountry']
        #print(selectedcountry)
       
        noofres =int(response['results'])
        
        for x in range(0,noofres):
            if selectedcountry==response['response'][x]['country']:
               
                new=response['response'][x]['cases']['new']
                active =response['response'][x]['cases']['active']
                critical =response['response'][x]['cases']['critical']
                recovered =response['response'][x]['cases']['recovered']
                total=response['response'][x]['cases']['total']
                deaths =int(total)-int(active)-int(recovered)
                #print(response['response'][x]['cases'])


        context={'selectedcountry':selectedcountry,'mylist':mylist,'new':new,'active':active,'critical':critical,'recovered':recovered,'total':total,'deaths':deaths}
        return render(request,'hell.html',context)
    
    
    #intially this part will execute after this avove post code will execute
    #noofres =int(response['results'])
    #mylist=[]
   # for x in range(0,noofres):
        #mylist.append(response['response'][x]['country'])
        #print(response['response'][x])
    context ={'mylist': mylist}
    return render(request,'hell.html',context)