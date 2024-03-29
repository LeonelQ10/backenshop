from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError



from core.models import  UserShopModel, UserClientModel, UserStoreModel, UserProductModel, UserEmployeeModel, UserTransaccionModel


#from .serializer import UserShopModelSerializer
# Create your views here.
#UserTransactionModel


@api_view(['GET'])
def endpoint_test(request):

    
    response={
                "status": "success",
                "code": 200,
                "message": "Operacion exitosa",
                "data": 'api test',
                "path": ""
            }
    return Response(response)

@api_view(['POST'])
def registrar_usuario(request):

    body=request.data

    name=body.get('name')
    email=body.get('email')
    password=body.get('password')
    address=body.get('address')
    age=body.get('age')

    instance_user=UserShopModel(name=name,
                  email=email,
                  password=password,
                  address=address,age=age)
    
    instance_user.save()

    response={
                "status": "success",
                "code": 200,
                "message": "Operacion exitosa",
                "data": 'Usuario registrado!!!',
                "path": ""
            }
    return Response(response)

@api_view(['PUT'])
def actualizar_usuario(request):

    body=request.data

    name=body.get('name')
    email=body.get('email')
    password=body.get('password')
    address=body.get('address')
    age=body.get('age')

    usuario=UserShopModel.objects.filter(email=email).last()

    if usuario==None:
        response={
                "status": "success",
                "code": 404,
                "message": "Operacion exitosa",
                "data": 'Oe no me estas enviando un correo que exista',
                "path": ""
            }
        return Response(response)
    else: #si encontró el correo

        usuario.name=name
        usuario.password=password
        usuario.address=address
        usuario.age=age

        usuario.save(update_fields=['name','password','address','age'])

        response={
                "status": "success",
                "code": 404,
                "message": "Operacion exitosa",
                "data": 'Datos actualizado correctamente',
                "path": ""
            }
        return Response(response)

@api_view(['DELETE'])
def eliminar_usuario(request):
    body = request.data
    email = body.get('email')

    usuario = UserShopModel.objects.filter(email=email).last()

    if usuario is None:
        response = {
            "status": "error",
            "code": 404,
            "message": "Operacion fallida",
            "data": "El correo electrónico no existe",
            "path": ""
        }
        return Response(response, status=status.HTTP_404_NOT_FOUND)
    else:
        usuario.delete()

        response = {
            "status": "success",
            "code": 200,
            "message": "Operacion exitosa",
            "data": 'Usuario eliminado correctamente',
            "path": ""
        }
        return Response(response)

@api_view(['GET'])
def obtener_detalle_usuario(request):
    email = request.query_params.get('email')

    usuario = UserShopModel.objects.filter(email=email).last()

    if usuario is None:
        response = {
            "status": "error",
            "code": 404,
            "message": "Operacion fallida",
            "data": "El correo electrónico no existe",
            "path": ""
        }
        return Response(response, status=status.HTTP_404_NOT_FOUND)
    else:
        response_data = {
            "name": usuario.name,
            "email": usuario.email,
            "password": usuario.password,
            "address": usuario.address,
            "age": usuario.age
        }
        response = {
            "status": "success",
            "code": 200,
            "message": "Operacion exitosa",
            "data": response_data,
            "path": ""
        }
        return Response(response)

@api_view(['GET'])
def obtener_todos_usuarios(request):
    
    list_usuarios = UserShopModel.objects.all()

    list_respuesta=[]

    for usuario in list_usuarios:

        informacion={
            'email': usuario.email,
            'age': usuario.age,
            'address': usuario.address,
            'name': usuario.name,
            'password': usuario.password
        }

        list_respuesta.append(informacion)

    response = {
        "status": "success",
        "code": 200,
        "message": "Operacion exitosa",
        "data": list_respuesta,
        "path": ""
    }
    return Response(response)     






#---------------------------------------------
#CRUD DE CLIENTES
@api_view(['POST'])
def create_client(request):
    body = request.data

    # Verificar si los campos requeridos están presentes y no están vacíos
    required_fields = ['name', 'email', 'password', 'age', 'marital_status', 'phone_number', 'country', 'preferred_payment_method']
    for field in required_fields:
        if field not in body or not body[field]:
            response = {
                "status": "error",
                "code": 400,
                "message": f"El campo '{field}' es requerido",
                "data": None,
                "path": request.path
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    instance_user = UserClientModel(
        name=body['name'],
        email=body['email'],
        password=body['password'],
        age=body['age'],
        marital_status=body['marital_status'],
        phone_number=body['phone_number'],
        country=body['country'],
        preferred_payment_method=body['preferred_payment_method']
    )

    try:
        instance_user.full_clean()  # Validar los campos del modelo
        instance_user.save()
    except ValidationError as e:
        response = {
            "status": "error",
            "code": 400,
            "message": "Error de validación del modelo",
            "data": str(e),
            "path": request.path
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        response = {
            "status": "error",
            "code": 500,
            "message": "Error interno del servidor",
            "data": str(e),
            "path": request.path
        }
        return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    response = {
        "status": "success",
        "code": 200,
        "message": "Operación exitosa",
        "data": 'Cliente registrado correctamente',
        "path": ""
    }
    return Response(response)
    
@api_view(['PUT'])
def update_client(request):

    body=request.data

    name=body.get('name')
    email=body.get('email')
    password=body.get('password')
    age=body.get('age')
    marital_status =body.get('marital_status')
    phone_number=body.get('phone_number')
    country=body.get('country')
    preferred_payment_method=body.get('preferred_payment_method')

    usuario=UserClientModel.objects.filter(email=email).last()

    if usuario==None:
        response={
                "status": "success",
                "code": 404,
                "message": "Operacion exitosa",
                "data": 'Oe no me estas enviando un correo que exista',
                "path": ""
            }
        return Response(response)
    else: #si encontró el correo

        usuario.name=name
        usuario.password=password
        usuario.age=age
        usuario.marital_status=marital_status
        usuario.phone_number=phone_number
        usuario.country=country
        usuario.preferred_payment_method=preferred_payment_method

        usuario.save(update_fields=['name','password','age','marital_status','phone_number','country','preferred_payment_method'])

        response={
                "status": "success",
                "code": 404,
                "message": "Operacion exitosa",
                "data": 'Datos actualizado correctamente',
                "path": ""
            }
        return Response(response)

@api_view(['DELETE'])
def delete_client(request):

    body = request.data
    email = body.get('email')

    usuario = UserClientModel.objects.filter(email=email).last()

    if usuario is None:
        response = {
            "status": "error",
            "code": 404,
            "message": "Operacion fallida",
            "data": "El correo electrónico no existe",
            "path": ""
        }
        return Response(response, status=status.HTTP_404_NOT_FOUND)
    else:
        usuario.delete()

        response = {
            "status": "success",
            "code": 200,
            "message": "Operacion exitosa",
            "data": 'Usuario eliminado correctamente',
            "path": ""
        }
        return Response(response)

@api_view(['GET'])
def get_customer_client(request):
    email = request.query_params.get('email')

    usuario = UserClientModel.objects.filter(email=email).last()

    if usuario is None:
        response = {
            "status": "error",
            "code": 404,
            "message": "Operacion fallida",
            "data": "El correo electrónico no existe",
            "path": ""
        }
        return Response(response, status=status.HTTP_404_NOT_FOUND)
    else:
        response_data = {
            "name": usuario.name,
            "email": usuario.email,
            "password": usuario.password,
            "age": usuario.age,
            "marital_status":usuario.marital_status,
            "phone_number":usuario.phone_number,
            "country":usuario.country,
            "preferred_payment_method":usuario.preferred_payment_method

        }
        response = {
            "status": "success",
            "code": 200,
            "message": "Operacion exitosa",
            "data": response_data,
            "path": ""
        }
        return Response(response)

@api_view(['GET'])
def get_all_customers(request):
    
    list_usuarios = UserClientModel.objects.all()

    list_respuesta=[]

    for usuario in list_usuarios:

        informacion={
            'email': usuario.email,
            'age': usuario.age,
            'name': usuario.name,
            'password': usuario.password,
            'marital_status':usuario.marital_status,
            'phone_number':usuario.phone_number,
            'country':usuario.country,
            'preferred_payment_method':usuario.preferred_payment_method
        }

        list_respuesta.append(informacion)

    response = {
        "status": "success",
        "code": 200,
        "message": "Operacion exitosa",
        "data": list_respuesta,
        "path": ""
    }
    return Response(response)



#----------------------------------------------
#CRUD DE LOCALES
@api_view(['POST'])
def create_store(request):
    # Implementa la lógica para crear un nuevo local
    body = request.data

    # Verificar si los campos requeridos están presentes y no están vacíos
    required_fields = ['name', 'location', 'city', 'country', 'phone_number']
    for field in required_fields:
        if field not in body or not body[field]:
            response = {
                "status": "error",
                "code": 400,
                "message": f"El campo '{field}' es requerido",
                "data": None,
                "path": request.path
            }
            return Response(response, status=400)

    # Crear una instancia del modelo de tienda
    instance_store = UserStoreModel(
        name=body['name'],
        location=body['location'],
        city=body['city'],
        country=body['country'],
        phone_number=body['phone_number']
    )

    try:
        # Guardar la instancia de la tienda
        instance_store.full_clean()  # Validar los campos del modelo
        instance_store.save()
    except ValidationError as e:
        # Manejar los errores de validación del modelo
        response = {
            "status": "error",
            "code": 400,
            "message": "Error de validación del modelo",
            "data": str(e),
            "path": request.path
        }
        return Response(response, status=400)
    except Exception as e:
        # Manejar otros errores
        response = {
            "status": "error",
            "code": 500,
            "message": "Error interno del servidor",
            "data": str(e),
            "path": request.path
        }
        return Response(response, status=500)

    # Si todo va bien, devolver una respuesta de éxito
    response = {
        "status": "success",
        "code": 200,
        "message": "Operación exitosa",
        "data": 'Local registrado correctamente',
        "path": ""
    }
    return Response(response)

@api_view(['PUT'])
def update_store(request):

    body=request.data

    name=body.get('name')
    location=body.get('location')
    city=body.get('city')
    country=body.get('country')
    phone_number=body.get('phone_number')

    usuario=UserStoreModel.objects.filter(name=name).last()

    if usuario==None:
        response={
                "status": "success",
                "code": 404,
                "message": "Operacion exitosa",
                "data": 'Oe no me estas enviando un nombre que exista',
                "path": ""
            }
        return Response(response)
    else: #si encontró el correo

        usuario.location=location
        usuario.city=city
        usuario.phone_number=phone_number
        usuario.country=country

        usuario.save(update_fields=['location','city','phone_number','country'])

        response={
                "status": "success",
                "code": 404,
                "message": "Operacion exitosa",
                "data": 'Tienda actualizada correctamente',
                "path": ""
            }
        return Response(response)

@api_view(['DELETE'])
def delete_store(request):

    body = request.data
    name = body.get('name')

    usuario = UserStoreModel.objects.filter(name=name).last()

    if usuario is None:
        response = {
            "status": "error",
            "code": 404,
            "message": "Operacion fallida",
            "data": "El nombre no existe",
            "path": ""
        }
        return Response(response, status=status.HTTP_404_NOT_FOUND)
    else:
        usuario.delete()

        response = {
            "status": "success",
            "code": 200,
            "message": "Operacion exitosa",
            "data": 'Tienda eliminada correctamente',
            "path": ""
        }
        return Response(response)

@api_view(['GET'])
def get_customer_store(request):

    name = request.query_params.get('name')

    usuario = UserStoreModel.objects.filter(name=name).last()

    if usuario is None:
        response = {
            "status": "error",
            "code": 404,
            "message": "Operacion fallida",
            "data": "La Tienda no existe",
            "path": ""
        }
        return Response(response, status=status.HTTP_404_NOT_FOUND)
    else:
        response_data = {
            "name": usuario.name,
            "phone_number": usuario.phone_number,
            "country": usuario.country,
            "location": usuario.location,
            "city": usuario.city,
            

        }
        response = {
            "status": "success",
            "code": 200,
            "message": "Operacion exitosa",
            "data": response_data,
            "path": ""
        }
        return Response(response)

@api_view(['GET'])
def get_all_store(request):
    
    list_usuarios = UserStoreModel.objects.all()

    list_respuesta=[]

    for usuario in list_usuarios:

        informacion={
        
            'name': usuario.name,
            'phone_number':usuario.phone_number,
            'country':usuario.country,
            'location':usuario.location,
            'city':usuario.city
        }

        list_respuesta.append(informacion)

    response = {
        "status": "success",
        "code": 200,
        "message": "Operacion exitosa",
        "data": list_respuesta,
        "path": ""
    }
    return Response(response)


#----------------------------------------------
#CRUD DE PRODUCTOS

###############################################################################################


@api_view(['POST'])
def create_product(request):
    if request.method == 'POST':
        # Obtener los datos del cuerpo de la solicitud
        body = request.data
        
        # Acceder a los campos necesarios de los datos
        name = body.get('name')
        description = body.get('description')
        price = body.get('price')
        quantity = body.get('quantity')
        brand = body.get('brand')
        category = body.get('category')
        userstoreModel_id = body.get('userstoreModel_id')  # Asegúrate de definir esto
        
        # Verificar si todos los campos requeridos están presentes y no están vacíos
        required_fields = ['name', 'description', 'price', 'quantity', 'brand', 'category', 'userstoreModel_id']
        for field in required_fields:
            if field not in body or not body[field]:
                response = {
                    "status": "error",
                    "code": 400,
                    "message": f"El campo '{field}' es requerido",
                    "data": None,
                    "path": request.path
                }
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            # Crear una instancia del modelo de producto
            instance_product = UserProductModel(
                name=name,
                description=description,
                price=price,
                quantity=quantity,
                brand=brand,
                category=category,
                userstoreModel_id=userstoreModel_id
            )
            
            # Guardar la instancia del producto en la base de datos
            instance_product.save()
            
            # Devolver una respuesta indicando que el producto ha sido creado exitosamente
            response_data = {"message": "Producto creado exitosamente"}
            return Response(response_data, status=status.HTTP_201_CREATED)
        except Exception as e:
            # Manejar otros errores
            response = {
                "status": "error",
                "code": 500,
                "message": "Error interno del servidor",
                "data": str(e),
                "path": request.path
            }
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        # Devolver una respuesta de error si no se recibe una solicitud POST
        return Response({"error": "Método no permitido"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        
@api_view(['PUT'])
def update_product(request):
    body = request.data

    name = body.get('name')
    description = body.get('description')
    price = body.get('price')
    quantity = body.get('quantity')
    brand = body.get('brand')
    category = body.get('category')

    usuario = UserProductModel.objects.filter(name=name).last()

    if usuario is None:
        response = {
            "status": "error",
            "code": 404,
            "message": "Operacion fallida",
            "data": "El producto no existe",
            "path": ""
        }
        return Response(response, status=status.HTTP_404_NOT_FOUND)
    else:
        usuario.description = description
        usuario.price = price
        usuario.quantity = quantity
        usuario.brand = brand
        usuario.category = category

        usuario.save(update_fields=['description', 'price', 'quantity', 'brand', 'category'])

        response = {
            "status": "success",
            "code": 200,
            "message": "Operacion exitosa",
            "data": "Producto actualizado correctamente",
            "path": ""
        }
        return Response(response, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def delete_product(request):

    body = request.data
    name = body.get('name')

    usuario = UserProductModel.objects.filter(name=name).last()

    if usuario is None:
        response = {
            "status": "error",
            "code": 404,
            "message": "Operacion fallida",
            "data": "El producto no existe",
            "path": ""
        }
        return Response(response, status=status.HTTP_404_NOT_FOUND)
    else:
        usuario.delete()

        response = {
            "status": "success",
            "code": 200,
            "message": "Operacion exitosa",
            "data": 'Producto eliminado correctamente',
            "path": ""
        }
        return Response(response)

@api_view(['GET'])
def get_customer_product(request):

    name = request.query_params.get('name')

    usuario = UserProductModel.objects.filter(name=name).last()

    if usuario is None:
        response = {
            "status": "error",
            "code": 404,
            "message": "Operacion fallida",
            "data": "El producto no existe",
            "path": ""
        }
        return Response(response, status=status.HTTP_404_NOT_FOUND)
    else:
        response_data = {
            "name": usuario.name,
            "description": usuario.description,
            "price": usuario.price,
            "quantity": usuario.quantity,
            "brand": usuario.brand,
            "category": usuario.category,
            

        }
        response = {
            "status": "success",
            "code": 200,
            "message": "Operacion exitosa",
            "data": response_data,
            "path": ""
        }
        return Response(response)

@api_view(['GET'])
def get_all_product(request):
    
    list_usuarios = UserProductModel.objects.all()

    list_respuesta=[]

    for usuario in list_usuarios:

        informacion={
        
            "name": usuario.name,
            "description": usuario.description,
            "price": usuario.price,
            "quantity": usuario.quantity,
            "brand": usuario.brand,
            "category": usuario.category,
        }

        list_respuesta.append(informacion)

    response = {
        "status": "success",
        "code": 200,
        "message": "Operacion exitosa",
        "data": list_respuesta,
        "path": ""
    }
    return Response(response)
#########################################################################################################
  
#CRUD DE EMPLEADOS

@api_view(['POST'])
def create_employee(request):
    body = request.data

    # Verificar si los campos requeridos están presentes y no están vacíos
    required_fields = ['first_name', 'last_name', 'email', 'date_of_birth', 'gender', 'address', 'phone_number', 'job_title', 'identification_number']
    for field in required_fields:
        if field not in body or not body[field]:
            response = {
                "status": "error",
                "code": 400,
                "message": f"El campo '{field}' es requerido",
                "data": None,
                "path": request.path
            }
            return Response(response, status=400)

    # Crear una instancia del modelo de empleado
    instance_user = UserEmployeeModel(
        first_name=body['first_name'],
        last_name=body['last_name'],
        email=body['email'],
        date_of_birth=body['date_of_birth'],
        gender=body['gender'],
        address=body['address'],
        phone_number=body['phone_number'],
        job_title=body['job_title'],
        identification_number=body['identification_number'],
        userstoreModel_id=body['userstoreModel_id']
    )

    try:
        # Guardar la instancia del empleado
        instance_user.full_clean()  # Validar los campos del modelo
        instance_user.save()
    except ValidationError as e:
        # Manejar los errores de validación del modelo
        response = {
            "status": "error",
            "code": 400,
            "message": "Error de validación del modelo",
            "data": str(e),
            "path": request.path
        }
        return Response(response, status=400)
    except Exception as e:
        # Manejar otros errores
        response = {
            "status": "error",
            "code": 500,
            "message": "Error interno del servidor",
            "data": str(e),
            "path": request.path
        }
        return Response(response, status=500)

    # Si todo va bien, devolver una respuesta de éxito
    response = {
        "status": "success",
        "code": 200,
        "message": "Operación exitosa",
        "data": 'Empleado registrado correctamente',
        "path": ""
    }
    return Response(response)

        
@csrf_exempt
@api_view(['PUT'])
def update_employee(request):
    body = request.data

    first_name = body.get('first_name')
    last_name = body.get('last_name')
    email = body.get('email')
    date_of_birth = body.get('date_of_birth')
    gender = body.get('gender')
    address = body.get('address')
    phone_number = body.get('phone_number')
    job_title = body.get('job_title')
    identification_number = body.get('identification_number')

    # Buscar el empleado a actualizar
    usuario = UserEmployeeModel.objects.filter(
        first_name=first_name,
        last_name=last_name,
        email=email,
        date_of_birth=date_of_birth,
        gender=gender,
        address=address,
        phone_number=phone_number,
        job_title=job_title,
        identification_number=identification_number
    ).last()

    if usuario is None:
        response = {
            "status": "error",
            "code": 404,
            "message": "Operacion fallida",
            "data": "El empleado no existe",
            "path": ""
        }
        return Response(response, status=status.HTTP_404_NOT_FOUND)
    else:
        # Actualizar los campos del empleado
        usuario.first_name = first_name
        usuario.last_name = last_name
        usuario.email = email
        usuario.date_of_birth = date_of_birth
        usuario.gender = gender
        usuario.address = address
        usuario.phone_number = phone_number
        usuario.job_title = job_title
        usuario.identification_number = identification_number

        # Guardar los cambios en la base de datos
        usuario.save(update_fields=['first_name', 'last_name', 'email', 'date_of_birth', 'gender', 'address', 'phone_number', 'job_title', 'identification_number'])

        response = {
            "status": "success",
            "code": 200,
            "message": "Operacion exitosa",
            "data": "Empleado actualizado correctamente",
            "path": ""
        }
        return Response(response, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def delete_employee(request):

    body = request.data
    last_name = body.get('last_name')

    usuario = UserEmployeeModel.objects.filter(last_name=last_name).last()

    if usuario is None:
        response = {
            "status": "error",
            "code": 404,
            "message": "Operacion fallida",
            "data": "El empleado no existe",
            "path": ""
        }
        return Response(response, status=status.HTTP_404_NOT_FOUND)
    else:
        usuario.delete()

        response = {
            "status": "success",
            "code": 200,
            "message": "Operacion exitosa",
            "data": 'Empleado eliminado correctamente',
            "path": ""
        }
        return Response(response)

@api_view(['GET'])
def get_customer_employee(request):
    last_name = request.query_params.get('last_name')

    if not last_name:
        response = {
            "status": "error",
            "code": 400,
            "message": "Operacion fallida",
            "data": "Se requiere el parámetro 'last_name'",
            "path": ""
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    employee = UserEmployeeModel.objects.filter(last_name=last_name).last()

    if employee is None:
        response = {
            "status": "error",
            "code": 404,
            "message": "Operacion fallida",
            "data": "El empleado no existe",
            "path": ""
        }
        return Response(response, status=status.HTTP_404_NOT_FOUND)
    else:
        response_data = {
            "first_name": employee.first_name,
            "last_name": employee.last_name,
            "email": employee.email,
            "date_of_birth": employee.date_of_birth,
            "gender": employee.gender,
            "address": employee.address,
            "phone_number": employee.phone_number,
            "job_title": employee.job_title,
            "identification_number": employee.identification_number,
        }
        response = {
            "status": "success",
            "code": 200,
            "message": "Operacion exitosa",
            "data": response_data,
            "path": ""
        }
        return Response(response)  

@api_view(['GET'])
def get_all_employee(request):
    
    list_usuarios = UserEmployeeModel.objects.all()

    list_respuesta=[]

    for usuario in list_usuarios:

        informacion={
        
            "first_name": usuario.first_name,
            "last_name": usuario.last_name,
            "email": usuario.email,
            "date_of_birth": usuario.date_of_birth,
            "gender": usuario.gender,
            "address": usuario.address,
            "phone_number": usuario.phone_number,
            "job_title": usuario.job_title,
            "identification_number": usuario.identification_number,
            "tienda_id": usuario.userstoreModel.pk,
            "tienda_nombre":usuario.userstoreModel.name
        }

        list_respuesta.append(informacion)

    response = {
        "status": "success",
        "code": 200,
        "message": "Operacion exitosa",
        "data": list_respuesta,
        "path": ""
    }
    return Response(response)

########################################################################################
#CRUD DE TRANSACCIONES 
@api_view(['POST'])
def create_transaccion(request):
    if request.method == 'POST':
        # Crear una instancia del modelo utilizando los datos de la solicitud
        transaccion = UserTransaccionModel(
            userclientModel_id=request.data.get('userclientModel'),
            userproduct_id=request.data.get('userproduct'),
            fecha_registro=request.data.get('fecha_registro')
        )
        
        # Validar los datos recibidos
        try:
            transaccion.full_clean()
        except Exception as e:
            # Si hay errores de validación, devolver una respuesta con los errores y un estado 400 (BAD REQUEST)
            return Response({"errors": str(e)}, status=400)
        
        try:
            # Guardar la transacción en la base de datos
            transaccion.save()
            # Devolver una respuesta con los datos de la transacción y un estado 201 (CREATED)
            return Response({"message": "Transacción creada exitosamente"}, status=201)
        except Exception as e:
            # Manejar cualquier otro error y devolver una respuesta con un estado 500 (INTERNAL SERVER ERROR)
            return Response({"error": str(e)}, status=500)
        


@api_view(['GET'])
def get_customer_transaccion(request):
    userclientModel_id = request.query_params.get('userclientModel_id')

    if not userclientModel_id:
        response = {
            "status": "error",
            "code": 400,
            "message": "Operacion fallida",
            "data": "Se requiere el parámetro 'userclientModel_id'",
            "path": ""
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    transaccion = UserTransaccionModel.objects.filter(userclientModel_id=userclientModel_id).last()

    if transaccion is None:
        response = {
            "status": "error",
            "code": 404,
            "message": "Operacion fallida",
            "data": "La transaccion no existe",
            "path": ""
        }
        return Response(response, status=status.HTTP_404_NOT_FOUND)
    else:
        response_data = {
            "userclientModel": transaccion.userclientModel,
            "userproduct": transaccion.userproduct,
            "fecha_registro": transaccion.fecha_registro,
        }
        response = {
            "status": "success",
            "code": 200,
            "message": "Operacion exitosa",
            "data": response_data,
            "path": ""
        }
        return Response(response)