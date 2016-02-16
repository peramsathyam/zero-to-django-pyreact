from django.conf.urls import url

from . import views

# Refer: Why naming the url? Short answer: it can be used in template href
# Tip: Avoid potentially clashing names that other apps might create conflicts
# https://docs.djangoproject.com/en/1.9/topics/http/urls/#naming-url-patterns
urlpatterns = [
    url(r'^$', views.index, name='webshop-index'),  # /webshop/
    url(r'^(?P<product_id>[0-9]+)/$', views.detail,
        name='webshop-product-detail')  # /webshop/2/
]


# ?P<product_id>[0-9]+, here ?P<product_id> will receive the number defined by
# the regular expression [0-9]+ and pass it to the pattern product_id
# Refer: https://docs.djangoproject.com/en/1.9/intro/tutorial03/ (Feb 16,2016)
