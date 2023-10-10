from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from Django import settings
from products.views import home_page, ShopPage, ShopPageDetail, RegisterView, LoginView, ProfileView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('shop/', ShopPage.as_view(), name='shop'),
    path('singup', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('accounts/profile', ProfileView.as_view(), name='profile'),
    path('shop/<int:pk>', ShopPageDetail.as_view(), name='shop-detail'),
    path('accounts/', include('allauth.urls')),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

