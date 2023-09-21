from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from database.models import database


def home(request):
    return render(request, "index.html")


def price(request):
    return render(request, "price.html")


def qwert(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        service = request.POST.get('service')
        message = request.POST.get('message')

        # Create a database object and save it
        en = database(name=name, email=email, service=service, message=message)
        en.save()
        print("Data saved successfully")

    return render(request, "quote.html")


def contact(request):
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
         # Get other form fields as needed
            message = request.POST.get('message')

         # Create the congratulatory message
            congratulatory_message = f"Hello {name},\n\nCongratulations! Your message has been received. We will get back to you soon.\n\nThank you for SANJAY!\n"

         # Send the congratulatory email
            send_mail(
                'Congratulations on Contacting Us',
                congratulatory_message,
                'your_email@example.com',  # Replace with your email address
                [email],  # The recipient's email address
                fail_silently=False,
            )
            print("success")
    except Exception as e:

        print(e)
    return render(request, "contact.html")


def quote(request):

    return render(request, "quote.html")
