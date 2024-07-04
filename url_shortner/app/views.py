from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from .models import UrlToken
from .utils.token_generator import generate_token
from urllib.parse import quote


def home(request):
    return render(request, "app/index.html")


def shorten_url(request):
    if request.method == "POST":
        url = request.POST["link"]
        alias = request.POST["alias"]

        if alias:
            token = quote(alias[:20])
        else:
            token = generate_token()

        if UrlToken.objects.filter(token=token).exists():
            print("Token already exists, generating new token.")
            token = token + generate_token(4)
        data = UrlToken(url=url, token=token)

        try:
            data.full_clean()
        except Exception as e:
            print("Error: ", e)
            return JsonResponse({"status": "error", "msg": "Please try again"})
        else:
            data.save()
            return JsonResponse({"status": "success", "msg": request.META["HTTP_HOST"] + "/" + token})


def redirect_url(request, token):
    if request.method == "GET":
        try:
            data = UrlToken.objects.get(token=token)
        except UrlToken.DoesNotExist:
            return redirect("home")
        url = data.url

        return redirect(url)
