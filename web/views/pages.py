from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from api.models import Incident


def landing_view(request):
    """Public landing page with project info and MVPs."""
    return render(request, 'web/pages/landing.html')


@login_required
def dashboard_view(request):
    """Logged-in dashboard with navigation tiles."""
    return render(request, 'web/pages/dashboard.html')


@login_required
def analysis_view(request):
    """Incident analysis dashboard with stats and trends."""
    incidents = Incident.objects.all()
    context = {
        'total_incidents': incidents.count(),
        'violence_count': incidents.filter(incident_type='violence').count(),
        'sos_count': incidents.filter(incident_type='hand_sos').count(),
        'lost_child_count': incidents.filter(incident_type='lost_child').count(),
        'recent_incidents': incidents.order_by('-detected_at')[:10]
    }
    return render(request, 'web/pages/analysis.html', context)


def home_view(request):
    """Legacy/Internal home page."""
    return render(request, 'web/pages/home.html')
