from django.shortcuts import render

def static_pages(request):
    if 'about' in request.path:
        return render(request, 'staticpages/about.html')

    if 'terms' in request.path:
        return render(request, 'staticpages/terms.html')

    if 'safety'in request.path:
        return render(request, 'staticpages/safety.html')

    if 'privacy' in request.path:
        return render(request, 'staticpages/privacy.html')

    if 'upgrade' in request.path:
        return render(request, 'staticpages/upgrade.html')
        
    if 'contact' in request.path:
        return render(request, 'staticpages/contact.html')