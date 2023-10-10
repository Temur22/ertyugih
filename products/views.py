from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, TemplateView

from products.models import ProductModel, CategoryModel


class ShopPage(ListView):
    template_name = 'shop.html'
    queryset = ProductModel.objects.all()
    context_object_name = 'products'
    paginate_by = 10

    def get_gueryset(self):
        qs = ProductModel.objects.all()
        q = self.request.GET.get('q')

        if q:
            qs = qs.filter(title_icontains=q)

        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = CategoryModel.objects.all()
        return context


@login_required
def add_to_favorite(request, product_id):
    product = get_object_or_404(ProductModel, pk=product_id)
    user = request.user

    if product in user.favorite_products.all():
        user.favorite_products.remove(product)
    else:
        user.favorite_products.add(product)

    return redirect('shop')


def home_page(request):
    return render(request, 'index.html', {})


class ShopPageDetail(DetailView):
    template_name = 'shop-details.html'
    queryset = ProductModel.objects.all()
    context_object_name = 'products'


class RegisterView(TemplateView):
    template_name = 'singup.html'


class LoginView(TemplateView):
    template_name = 'login.html'


class ProfileView(TemplateView):
    template_name = 'profile.html'
