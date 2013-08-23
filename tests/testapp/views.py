from django.views.generic.base import TemplateView


class SecureView(TemplateView):
    template_name = "base.html"


class UnsecureView(TemplateView):
    template_name = "base.html"

