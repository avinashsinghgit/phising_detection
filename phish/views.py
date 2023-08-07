from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse
# Create your views here.

def index(request):
    return render(request,"index.html")

def about(request):
    return HttpResponse("this is About Page")

def search(request):
    query = request.POST.get('query', '')  # Get the 'query' parameter from the URL

    def ip(url):
        try:
            ip_check = url.split("//")[1].split("/")[0]  # extracts the domain
            if (ip_check.replace('.','').replace(':','').isnumeric() == True):    # checks whether the domain name contains only numerical values
                return -1
            if (ip_check.replace('.', '').replace(':','').isalnum() == True):         # to check in case of hexadecimal IP address value
                return -1
            else:
                return 1
        except:
            return -1
    
    results = ip(query)  # Call the Python function to process the query
    
    return render(request, 'search.html', {'results': results})

