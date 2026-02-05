import requests
from django.shortcuts import render, redirect
from django.conf import settings
# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request, 'about.html')

def certifications(request):
    return render(request, 'certifications.html')

def education(request):
    return render(request, 'education.html')

BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
CHAT_ID = "YOUR_CHAT_ID_HERE"

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        text = f"""
📩 New Contact Message

👤 Name: {name}
📧 Email: {email}

💬 Message:
{message}
        """

        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        payload = {
            "chat_id": CHAT_ID,
            "text": text
        }

        requests.post(url, data=payload)

        return redirect("index")

    return render(request, "contact.html")