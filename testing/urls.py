from rest_framework import routers
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from testing import views

"""
router.register(a, b)는 url 뒤에 a로 끝나면 b의 메소드들을 실행시켜주는 형태입니다.
만약 get 메소드라면 list를, post면 create를 합니다.
만약 뒤에 /{lookup}/형태로, lookup 자리에 pk에 해당하는 값을 주면
해당하는 pk의 데이터에 대해 조작할 수 있습니다.
이 때의 get은 retrieve, post는 update입니다.
만약 pk가 아닌 속성의 수가 2개 이상일 때 일부의 속성만 update를 하면 partial_update가 호출됩니다. 
"""
router = routers.SimpleRouter()
router.register('user', views.UserViewSets)
router.register('testing', views.TestClassViewSets)

"""
user_ret은 폼을 이용하여, post 방식으로 검색하도록 하는 user_ret 하위의 retrieve 함수와 연결됩니다.
폼에 입력된 값을 기반으로 검색 결과를 반환합니다.
아래에 적힌 것처럼, post 메소드만이 허용되어 있습니다. 필요에 따라 get, delete 등을 추가할 수 있습니다.
"""
user_ret = views.UserRetViewSets.as_view({
    'post': 'retrieve'
})

"""
user_ret처럼 custom_view를 생성할 경우에는 urlpatterns에 아래와 같이 path를 이용하여 추가하면 됩니다.
router를 쓴 경우는 가장 마지막 줄을 통해 router로 작성한 모든 view가 연결됩니다.
"""
urlpatterns = format_suffix_patterns([
    path('userRet/', user_ret, name='user_ret')
])
urlpatterns += router.urls
