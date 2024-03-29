from django.urls import path
from core.views import endpoint_test, registrar_usuario, actualizar_usuario
from core.views import eliminar_usuario, obtener_detalle_usuario, obtener_todos_usuarios
from core.views import create_client, update_client, delete_client, get_customer_client, get_all_customers
from core.views import create_store, update_store, delete_store, get_customer_store, get_all_store
from core.views import create_product, update_product, delete_product,get_customer_product,get_all_product
from core.views import create_employee, update_employee, delete_employee, get_customer_employee, get_all_employee
from core.views import create_transaccion, get_customer_transaccion


urlpatterns=[
   path('endpoint_test',endpoint_test),
   path('registrar_usuario',registrar_usuario),
   path('actualizar_usuario',actualizar_usuario),
   path('eliminar_usuario',eliminar_usuario),
   path('obtener_detalle_usuario',obtener_detalle_usuario),
   path('obtener_todos_usuarios',obtener_todos_usuarios),
   path('create_client', create_client),
   path('update_client', update_client),
   path('delete_client', delete_client),
   path('get_customer_client', get_customer_client),
   path('get_all_customers', get_all_customers),
   path('create_store', create_store),
   path('update_store', update_store),
   path('delete_store', delete_store),
   path('get_customer_store', get_customer_store),
   path('get_all_store', get_all_store),
   path('create_product', create_product),
   path('update_product', update_product),
   path('delete_product', delete_product),
   path('get_customer_product', get_customer_product),
   path('get_all_product', get_all_product),
   path('create_employee', create_employee),
   path('update_employee', update_employee),
   path('delete_employee', delete_employee),
   path('get_customer_employee', get_customer_employee),
   path('get_all_employee', get_all_employee),
   path('create_transaccion', create_transaccion),
   path('get_customer_transaccion', get_customer_transaccion)
   
   ]

#from core.views import #create_product, create_client, create_employee, create_store
 #path('create_employee', create_employee),
   #path('create_product', create_product),