from django.shortcuts import render ,redirect
from mypage.models import Contact 
# from django.contrib import messages

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name').strip()
        email = request.POST.get('email').strip()
        number = request.POST.get('number').strip()
        content = request.POST.get('content').strip()

        # Name validation
        if not (2 <= len(name) <= 30):
            # messages.error(request, 'Length of name should be between 2 and 30 characters.')
            return render(request, 'invalid_name.html')

        # Email validation (basic)
        if not (6 <= len(email) <= 254):
            # messages.error(request, 'Invalid email length, try again.')
            return render(request, 'invalid_email.html')

        # Number validation (only if provided)
        if number:
            if not (10 <= len(number) <= 12 and number.isdigit()):
                # messages.error(request, 'Invalid number: must be 10–12 digits.')
                return render(request, 'invalid_no.html')

        # Save to DB
            Contact.objects.create(
            name = name,
            email = email,
            content = content,
            number = number if number else None
        )
        # messages.success(request, 'Thank you for contacting me! Your message has been saved.')
        print('Data has been saved to database')

        return render(request, 'thanks.html')

    return render(request, 'home.html')
