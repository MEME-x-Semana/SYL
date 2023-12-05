from django.contrib import admin
from django.urls import path , include


from .views import      CrucerosListView   \
                    ,   CrucerosDetailView \
                    ,   CrucerosCreateView \
                    ,   CrucerosUpdateView \
                    ,   CrucerosDeleteView

app_name = "cruceros"

urlpatterns = [
    path("", CrucerosListView.as_view(), name="all"),
    path("create/", CrucerosCreateView.as_view(), name="create"),
    path("<int:pk>/detail/", CrucerosDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", CrucerosUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", CrucerosDeleteView.as_view(), name="delete")

]
