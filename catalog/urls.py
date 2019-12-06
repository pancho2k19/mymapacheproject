
"""locallibreria URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from.import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

urlpatterns = [

 path('', views.index, name = 'index'),
 path('Piezas/' , views.PiezaListView.as_view(), name = 'pieza'),
 path('Pieza/<int:pk>' , views.PiezaDetailView.as_view() , name = 'detalle')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += [
    path('Pieza/create/', views.PiezaCreate.as_view(), name='pieza_create'),
    path('Pieza/<int:pk>/update/', views.PiezaUpdate.as_view(), name='pieza_update'),
    path('Pieza/<int:pk>/delete/', views.PiezaDelete.as_view(), name='pieza_delete'),
]