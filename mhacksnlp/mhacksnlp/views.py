from django.http import HttpResponse
from django.views.generic import TemplateView

class LandingView(TemplateView):
    template_name = "landingpage.html"

landingview = LandingView.as_view()