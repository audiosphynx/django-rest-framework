from django.urls import include, path
from rest_framework.routers import DefaultRouter
from snippets import views

# Create a router and register our viewsets with it.
# Using viewsets is less explicit than building your views individually.
router = DefaultRouter()
router.register('snippets', views.SnippetViewSet)
router.register('users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls))
]

# API endpoints
# urlpatterns = format_suffix_patterns([
#    path('', api_root),
#    path('snippets/', snippet_list, name='snippet-list'),
#    path('snippets/<pk>/', snippet_detail, name='snippet-detail'),
#    path('snippets/<pk>/highlight/', snippet_highlight, name='snippet-highlight'),
#    path('users/', user_list, name='user-list'),
#    path('users/<pk>/', user_detail, name='user-detail')
# ])
