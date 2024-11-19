from django.urls import path
from . import views


app_name = "polls"
urlpatterns = [
    # path("", views.index, name="index"),
    # path("<int:question_id>/", views.detail, name="detail"),
    # path("<int:question_id>/results/", views.results, name="results"),
    # path("<int:question_id>/vote/", views.vote, name="vote"),

    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]


"""
在 polls.urls 模块中的 path() 函数中定义了 name 参数，你可以通过使用 {% url %} 模板标签来消除对 url 配置中定义的特定 URL 路径的依赖：
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
"""

"""
从 <question_id> 更改为 <pk>。这是因为我们将使用 DetailView 通用视图来替换我们的 detail() 和 results() 视图，
它期望从 URL 中捕获的主键值被称为 "pk"。
"""