from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def home(request):
    packages = [
	{'name':'adminlettuce', 'url': 'http://pypi.python.org/pypi/adminlettuce/0.0.6'},
	{'name':'aa_airtable', 'url': 'http://pypi.python.org/pypi/aa_airtable/0.2'},
	{'name':'aa_stripe', 'url': 'http://pypi.python.org/pypi/aa_stripe/0.4.1'},
	{'name':'admin_bootstrap', 'url': 'http://pypi.python.org/pypi/admin_bootstrap/0.7.0'},
    ]
    context = {
        'title': 'anand-crowdbotics-23',
        'packages': packages
    }
    return render(request, 'home/index.html', context)
