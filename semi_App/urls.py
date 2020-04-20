from django.urls import path
from . import views
urlpatterns = [

    path('',views.index),
    path('add_new_show',views.Add_new_show),
    path('create_show', views.Create_Show),
    #tv shows2
    path('show/<int:Id>',views.tv_show),
    path('all_show', views.all_show),

    #Editing Show

    path('edit_show/<int:ed>', views.edit_a_show),
    path('show_id/<int:ed>', views.update_a_show),

    # Delete show
    path('show_deletes/<int:Id>',views.del_show),
    path('show_delete/<int:Id>', views.show_delete)

    
]
