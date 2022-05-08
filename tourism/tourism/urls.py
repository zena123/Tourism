from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.conf import settings
from django.views.generic.base import TemplateView

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from search import views as search_views


def bad(request):
    """ Simulates a server error """
    1 / 0


urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),
]

urlpatterns += i18n_patterns(
    path("bad/", bad),
    path('', include('djvue.urls')),

    path("django-admin/", admin.site.urls),
    path(f"{settings.ADMIN_URL}/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),

    path("search/", search_views.search, name="search"),
    path("tourist-sites/", include("tourist_sites.urls", namespace="tourist_sites")),

    path("user/", include("user.urls", namespace="user")),
    path("api/v1/", include("user.api.urls", namespace="user_api")),

    # For anything not caught by a more specific rule above, hand over to
    # Wagtail"s page serving mechanism. This should be the last pattern in
    # the list:
    path("", include(wagtail_urls)),

)

if settings.DEBUG:
    urlpatterns += [
        # Testing 404 and 500 error pages
        path("404/", TemplateView.as_view(template_name="404.html"), name="404"),
        path("500/", TemplateView.as_view(template_name="500.html"), name="500"),
    ]

    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    import debug_toolbar

    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
