from django.shortcuts import render, get_object_or_404
from .models import Package, Test
from cart.forms import CartAddTestForm
from django.contrib.auth.decorators import login_required


@login_required
def test_list(request, package_slug=None):
    package = None
    packages = Package.objects.all()
    tests = Test.objects.filter()
    if package_slug:
        package = get_object_or_404(Package, slug=package_slug)
        tests = tests.filter(package=package)
    return render(request, 'testapp/test/list.html', {'package': package,
                                                      'packages': packages,
                                                      'tests': tests})

@login_required
def test_detail(request, id, slug):
    test = get_object_or_404(Test, id=id, slug=slug)
    cart_test_form = CartAddTestForm()
    return render(request,
                  'testapp/test/detail.html',
                  {'test': test,
                  'cart_test_form': cart_test_form})
