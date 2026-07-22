from django.shortcuts import render
from django.contrib.auth.decorators import (
    login_required,
    permission_required,
)
from django.contrib.auth.models import User

from accounts.models import UserProfile
from assets.models import Asset
from access.models import AccessRequest
from habilitations.models import Permission
from audit.models import AuditLog
from compliance.models import ComplianceCheck


@login_required
@permission_required(
    "dashboard.view_dashboard",
    raise_exception=True
)
def index(request):
    context = {

        "users_count": User.objects.count(),

        "profiles_count": UserProfile.objects.count(),

        "assets_count": Asset.objects.count(),

        "requests_count": AccessRequest.objects.count(),

        "permissions_count": Permission.objects.count(),

        "audit_count": AuditLog.objects.count(),

        "compliance_count": ComplianceCheck.objects.count(),

        "latest_requests": AccessRequest.objects.order_by(
            "-created_at"
        )[:5],

        "latest_logs": AuditLog.objects.order_by(
            "-created_at"
        )[:5],

    }

    return render(

        request,

        "dashboard/index.html",

        context

    )