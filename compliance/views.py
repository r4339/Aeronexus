from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import (
    login_required,
    permission_required,
)

from .models import ComplianceCheck
from .services import ComplianceService


@login_required
@permission_required(
    "compliance.view_compliancecheck",
    raise_exception=True
)
def checks_list(request):
    checks = ComplianceService.get_all_checks()

    return render(
        request,
        "compliance/checks_list.html",
        {
            "checks": checks
        }
    )


@login_required
@permission_required(
    "compliance.view_compliancecheck",
    raise_exception=True
)
def check_detail(request, id):

    check = get_object_or_404(
        ComplianceCheck,
        id=id
    )

    return render(
        request,
        "compliance/check_detail.html",
        {
            "check": check
        }
    )


@login_required
@permission_required(
    "compliance.view_compliancecheck",
    raise_exception=True
)
def compliant_checks(request):

    checks = ComplianceService.compliant_checks()

    return render(
        request,
        "compliance/checks_list.html",
        {
            "checks": checks
        }
    )


@login_required
@permission_required(
    "compliance.view_compliancecheck",
    raise_exception=True
)
def warning_checks(request):

    checks = ComplianceService.warning_checks()

    return render(
        request,
        "compliance/checks_list.html",
        {
            "checks": checks
        }
    )


@login_required
@permission_required(
    "compliance.view_compliancecheck",
    raise_exception=True
)
def non_compliant_checks(request):
    checks = ComplianceService.non_compliant_checks()

    return render(
        request,
        "compliance/checks_list.html",
        {
            "checks": checks
        }
    )