from django.urls import path
from . import views
urlpatterns=[
#    path('translate/<int:pk>/save/',views.translate_save,name='translate_save'),
#    path('translate/rewrite/<int:pk>/',views.translate_rewrite,name='translate_rewrite'),
    path('resident/search/', views.search_resident, name = 'search_resident'),
#選択して読む
    path('record/search/',   views.search_record,   name = 'search_record'),
#新規登録と変換
    path('check_translate/', views.check_translate, name = 'check_translate'),
    path('record/new/',      views.record_new,      name = 'record_new'),
    path('account/mode/',    views.change_mode,     name = 'change_mode'),
    path('write_all',        views.write_all,       name = 'write_all'),
    path('',                 views.search_record,   name = 'search_record'),
    path('select_kind',        views.select_kind,       name = 'select_kind'),
]
