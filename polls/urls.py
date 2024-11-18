from django.urls import path
from . import views


app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]


"""
在 polls.urls 模块中的 path() 函数中定义了 name 参数，你可以通过使用 {% url %} 模板标签来消除对 url 配置中定义的特定 URL 路径的依赖：
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
"""

