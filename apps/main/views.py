from django.shortcuts import render

# Create your views here.
def main(request):
    context = {}
    return render(template_name="main.html", context=context, request=request)