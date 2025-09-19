from django.urls import path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from . import views
from .views import MessageView

schema_view = get_schema_view(
    openapi.Info(
        title="ChatBot API",
        default_version="v1",
        description="Oddiy ChatBot API hujjatlari",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="admin@example.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("", views.index, name="index"),
    # path("ask/", views.ask, name="ask"),
    # path('messages/', views.load_messages, name='load_messages'),
    path("api/message/", MessageView.as_view(), name="message"),

    # Swagger va Redoc
    re_path(r"^swagger(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
