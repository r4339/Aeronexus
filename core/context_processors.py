from django.urls import reverse


def navigation(request):
    """Context shared by the base layout.

    Keep the breadcrumb independent from individual templates so detail and
    form pages cannot silently fall back to "Accueil / Dashboard".
    """
    match = getattr(request, "resolver_match", None)
    if not match:
        return {"breadcrumbs": [], "notifications": [], "notifications_count": 0}

    sections = {
        "accounts": ("Personnel", "accounts:users_list"),
        "assets": ("Ressources", "assets:assets_list"),
        "access": ("Demandes", "access:requests_list"),
        "habilitations": ("Habilitations", "habilitations:permissions_list"),
        "audit": ("Audit", "audit:logs_list"),
        "compliance": ("Conformité", "compliance:checks_list"),
        "dashboard": ("Dashboard", "dashboard:index"),
        "core": ("Plateforme", "dashboard:index"),
    }
    page_labels = {
        "user_detail": "Détail", "user_create": "Nouvel utilisateur", "user_update": "Modifier",
        "asset_detail": "Détail", "asset_create": "Nouvelle ressource", "asset_update": "Modifier",
        "request_detail": "Détail", "request_create": "Nouvelle demande", "request_update": "Modifier",
        "request_delete": "Supprimer", "pending_requests": "En attente", "approved_requests": "Approuvées",
        "rejected_requests": "Refusées", "permission_detail": "Détail", "permission_update": "Modifier",
        "permission_delete": "Supprimer", "expired_permissions": "Expirées", "revoked_permissions": "Révoquées",
        "log_detail": "Détail", "check_detail": "Détail", "reports": "Rapports", "settings": "Paramètres",
    }

    breadcrumbs = [{"label": "Accueil", "url": reverse("dashboard:index")}]
    section = sections.get(match.namespace)
    if section:
        section_label, section_url_name = section
        page_label = page_labels.get(match.url_name, section_label)
        if page_label == section_label:
            breadcrumbs.append({"label": section_label, "url": None})
        else:
            breadcrumbs.extend((
                {"label": section_label, "url": reverse(section_url_name)},
                {"label": page_label, "url": None},
            ))

    notifications = []
    user = getattr(request, "user", None)
    if user and user.is_authenticated and user.has_perm("access.view_accessrequest"):
        # A pending request is actionable by users allowed to consult requests.
        # The records themselves are the notification source, so no migration or
        # duplicate notification rows are necessary.
        from access.models import AccessRequest

        notifications = list(
            AccessRequest.objects.filter(status="PENDING")
            .select_related("requester", "asset")[:5]
        )

    return {
        "breadcrumbs": breadcrumbs,
        "notifications": notifications,
        "notifications_count": len(notifications),
    }
