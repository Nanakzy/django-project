from django.shortcuts import render, redirect
from .models import User, HealthPlan, Medication
from .models import AppointmentReminder, MotivationalSupport
from django.http import JsonResponse


def index(request):
    return render(request, 'index.html')


def add_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        age = request.POST.get('age')
        gender = request.POST.get('gender')

        user = User.objects.create(
            username=username,
            email=email,
            password=password,
            age=age,
            gender=gender
        )
        user.save()
        return redirect('index')
    return render(request, 'add_user.html')


def get_users(request):
    users = User.objects.all()
    users_list = [
            {"username": user.username, "email": user.email}
            for user in users
            ]
    return JsonResponse(users_list, safe=False)


def add_appointment_reminder(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        appointment_date = request.POST.get('appointment_date')
        description = request.POST.get('description')
        reminder_time = request.POST.get('reminder_time')

        user = User.objects.get(id=user_id)
        reminder = AppointmentReminder.objects.create(
            user=user,
            appointment_date=appointment_date,
            description=description,
            reminder_time=reminder_time
        )
        reminder.save()
        return redirect('index')
    return render(request, 'add_appointment_reminder.html')


def add_motivational_support(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        message = request.POST.get('message')

        user = User.objects.get(id=user_id)
        support = MotivationalSupport.objects.create
        (user=user, message=message)
        support.save()
        return redirect('index')
    return render(request, 'add_motivational_support.html')
