from django.contrib import admin
<<<<<<< HEAD
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('track/', include('maps.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
=======
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Donor_Login_Register.urls')),
    path('consumer/',include('Consumer_Login_Register.urls'))
    
    
     
]
>>>>>>> main
