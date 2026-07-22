from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def reports(request):
    return render(request, "core/reports.html")


@login_required
def settings(request):
    return render(request, "core/settings.html")
