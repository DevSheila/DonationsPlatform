from django.urls import path
from .views import DonationTracking
from django.conf import settings
from django.conf.urls.static import static

app_name = "maps"

urlpatterns = [
    path("map/", DonationTracking.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)