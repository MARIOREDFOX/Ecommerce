from django.urls import path
from .views import item_list


app_name = 'djecommerceapp'

urlpatterns = [
	path('', item_list, name='item_list')

]