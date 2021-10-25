from rest_framework import routers
from blog.views import PostViewset, CategoryViewset, TagViewset


router = routers.SimpleRouter()

router.register(r'posts', PostViewset)
router.register(r'categories', CategoryViewset)
router.register(r'tags', TagViewset)

urlpatterns = router.urls