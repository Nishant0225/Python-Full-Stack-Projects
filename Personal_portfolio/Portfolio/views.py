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

BOT_TOKEN = "8427869550:AAFA3vEaNlaiyv0CSquOwIIP7F2JcM6ap8E"
CHAT_ID = "1932082820"   # put your numeric chat id here

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        text = (
            "📩 New Contact Message\n\n"
            f"👤 Name: {name}\n"
            f"📧 Email: {email}\n\n"
            f"💬 Message:\n{message}"
        )

        try:
            requests.post(
                f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                data={
                    "chat_id": CHAT_ID,
                    "text": text
                },
                timeout=10
            )
        except Exception as e:
            print("Telegram error:", e)

        return redirect("index")

    return render(request, "contact.html")