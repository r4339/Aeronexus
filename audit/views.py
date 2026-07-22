from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import (
    login_required,
    permission_required,
)

from .models import AuditLog
from .services import AuditService

@login_required
@permission_required(
    "audit.view_auditlog",
    raise_exception=True
)
def logs_list(request):

    logs = AuditService.get_all_logs()

    return render(
        request,
        "audit/logs_list.html",
        {
            "logs": logs
        }
    )


@login_required
@permission_required(
    "audit.view_auditlog",
    raise_exception=True
)
def log_detail(request, id):

    log = get_object_or_404(
        AuditLog,
        id=id
    )

    return render(
        request,
        "audit/log_detail.html",
        {
            "log": log
        }
    )


@login_required
@permission_required(
    "audit.view_auditlog",
    raise_exception=True
)
def logs_by_module(request, module):

    logs = AuditService.logs_by_module(module)

    return render(
        request,
        "audit/logs_list.html",
        {
            "logs": logs
        }
    )


@login_required
@permission_required(
    "audit.view_auditlog",
    raise_exception=True
)
def logs_by_action(request, action):

    logs = AuditService.logs_by_action(action)

    return render(
        request,
        "audit/logs_list.html",
        {
            "logs": logs
        }
    )