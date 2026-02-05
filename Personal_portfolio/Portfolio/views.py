from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request, 'about.html')

def certifications(request):
    return render(request, 'certifications.html')

def education(request):
    return render(request, 'education.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        full_message = f"""
        Name: {name}
        Email: {email}

        Message:
        {message}
        """

        send_mail(
            subject="New Contact Message",
            message=full_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=["nishantkadu7020@gmail.com"],
            fail_silently=False,
        )

        return redirect("index")  # or same page if you want

    return render(request, "contact.html")