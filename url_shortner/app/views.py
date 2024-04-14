from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from .models import UrlToken
from .utils.token_generator import generate_token

# Create your views here.


def home(request):
    return render(request, "app/index.html")


def shorten_url(request):
    if request.method == "POST":
        url = request.POST["link"]
        token = generate_token()
        data = UrlToken(url=url, token=token)

        try:
            data.full_clean()
        except Exception as e:
            print(e)
            return JsonResponse({"status": "error", "msg": "Please try again"})
        else:
            data.save()
            return JsonResponse({"status": "success", "msg": request.META["HTTP_HOST"] + "/" + token})


def redirect_url(request, token):
    if request.method == "GET":
        data = UrlToken.objects.get(token=token)
        url = data.url

        return redirect(url)
