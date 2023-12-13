from django.urls import path 
from .router import router 


from .views import      ViajesListView \
                    ,   ViajesDetailView \
                    ,   ViajesCreateView \
                    ,   ViajesUpdateView \
                    ,   ViajesDeleteView

app_name = "viajes"

urlpatterns = [
    path("", ViajesListView.as_view(), name="all"),
    path("create/", ViajesCreateView.as_view(), name="create"),
    path("<int:pk>/detail/", ViajesDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", ViajesUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", ViajesDeleteView.as_view(), name="delete")

]

urlpatterns += router.urls