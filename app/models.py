from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=120, unique=True)
    password = models.CharField(max_length=60)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return f"{self.username} ({self.email})"


class HealthPlan(models.Model):
    user = models.ForeignKey(
        User, related_name='health_plans', on_delete=models.CASCADE)
    plan_name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.plan_name} for {self.user.username}"


class Medication(models.Model):
    user = models.ForeignKey(
        User, related_name='medications', on_delete=models.CASCADE)
    medication_name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50, null=True, blank=True)
    frequency = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.medication_name} for {self.user.username}"


class AppointmentReminder(models.Model):
    user = models.ForeignKey(
        User, related_name='appointment_reminders', on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    description = models.TextField(null=True, blank=True)
    reminder_time = models.DateTimeField()

    def __str__(self):
        return (
            f"Appointment on {self.appointment_date} for {self.user.username}"
            )


class MotivationalSupport(models.Model):
    user = models.ForeignKey(
        User, related_name='motivational_supports', on_delete=models.CASCADE)
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
                f"Motivational message for {self.user.username} "
                f"on {self.date_sent}"
                )
