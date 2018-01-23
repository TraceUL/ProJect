
from django.conf.urls import url
from django.contrib import admin
from blog.views import baselist,indexlist,LoginView,indexlistview,detailview
from Blog1.settings import STATIC_ROOT
from django.views.static import serve
import xadmin



urlpatterns = [


    url(r'^admin/', xadmin.site.urls),
    url(r'^base/',baselist.basehtml),
    url(r'^home/',indexlist.indexhtml),
    url(r'^login/', LoginView.as_view()),
    # url(r'^register/', LoginView.as_view()),

    url(r'^indexlist/', indexlistview.as_view()),
    url(r'^search/', indexlistview.as_view()),
    url(r'^detail/(?P<blog_id>\d+)/$',detailview.as_view(),name="blog_detail"),


]
