import blog.views
import blog.templates.blog
from django.urls import path,include


urlpatterns = [
    path('',blog.views.get_index_page),
    path('details/<int:article_id>',blog.views.get_details_page),
    path('category_page/<int:category_id>',blog.views.get_category_list),
    path('live.html',blog.views.get_live_page),
    path('about.html',blog.views.get_about_page)
]