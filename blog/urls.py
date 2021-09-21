from rest_framework import routers
from blog.views import PostViewset


router = routers.SimpleRouter()

router.register(r'posts', PostViewset)

urlpatterns = router.urls