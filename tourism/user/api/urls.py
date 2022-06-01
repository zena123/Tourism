from rest_framework.routers import SimpleRouter

from .views import UserViewSet, RegistrationApiView

app_name = "user_api"

router = SimpleRouter()

router.register("users", UserViewSet)
router.register("profile", RegistrationApiView, basename="profile")

urlpatterns = router.urls
