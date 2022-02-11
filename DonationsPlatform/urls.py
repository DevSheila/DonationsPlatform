from django.contrib import admin
<<<<<<< HEAD
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
=======
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
>>>>>>> ft-mappings


urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('', include('Donor_Login_Register.urls')),
    path('consumer/', include('Consumer_Login_Register.urls')),
    path('maps/', include('mapping.urls'))
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
=======
    path('',include('Donor_Login_Register.urls')),
    path('consumer/',include('Consumer_Login_Register.urls'))
    
    
     
]
>>>>>>> main
>>>>>>> ft-mappings
