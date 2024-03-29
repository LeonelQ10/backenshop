"""core/models/userFacebook.py"""
from django.db import models
from django.utils import timezone



################################################################################

class UserShopModel(models.Model):
    """UserShopModel"""

    id = models.AutoField(primary_key=True,verbose_name="id user shop")

    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=20)
    address=models.CharField(max_length=150)

    age=models.IntegerField()

    class Meta:
        db_table = "user_shop"
        verbose_name = "Usuario Tienda"
        verbose_name_plural = "Usuarios Tienda"

#####################################################################################


class UserClientModel(models.Model):
    """UserClientModel"""
    id = models.AutoField(primary_key=True, verbose_name="id user client")
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    marital_status = models.CharField(max_length=50, default='')
    phone_number = models.CharField(max_length=20, default='')
    country = country = models.CharField(max_length=100, default='')
    preferred_payment_method = models.CharField(max_length=100, default='')
    # Otros campos relevantes para el cliente

    class Meta:
        db_table = "user_client"
        verbose_name = "Usuario Cliente"
        verbose_name_plural = "Usuarios Cliente"

##########################################################################################

class UserStoreModel(models.Model):
    """UserStoreModel"""
    id = models.AutoField(primary_key=True, verbose_name="id user store")
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, default='')
    
    def __str__(self):
        return self.name


    # Otros campos relevantes para la tienda

    class Meta:
        db_table = "store"
        verbose_name = "Tienda"
        verbose_name_plural = "Tiendas"

#########################################################################################
        

class UserProductModel(models.Model):
        """UserProductModel"""
        id = models.AutoField(primary_key=True, verbose_name="id user product")
        name = models.CharField(max_length=100)
        description = models.TextField()
        price = models.DecimalField(max_digits=10, decimal_places=2)
        quantity = models.IntegerField(default=0)
        brand = models.CharField(max_length=100)
        category = models.CharField(max_length=100)
        userstoreModel = models.ForeignKey(UserStoreModel, on_delete=models.CASCADE, related_name='store_product',null=True)
 
        class Meta:
            db_table = "product"
            verbose_name = "Product"
            verbose_name_plural = "Products"


################################################################
            
class UserEmployeeModel(models.Model):
    """UserEmployeeModel"""
    id = models.AutoField(primary_key=True, verbose_name="id user employee")
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    job_title = models.CharField(max_length=100)
    identification_number = models.CharField(max_length=50, unique=True)

    userstoreModel = models.ForeignKey(UserStoreModel, on_delete=models.CASCADE, related_name='store_employee',null=True)
 
    
    class Meta:
            db_table = "employee"
            verbose_name = "Employee"
            verbose_name_plural = "Employees"


###########################################################

class UserTransaccionModel(models.Model):
    """UserTransaccionModel"""
    id = models.AutoField(primary_key=True, verbose_name="id transaccion")
    userclientModel = models.ForeignKey(UserClientModel, on_delete=models.CASCADE, related_name='client_transaccion')
    userproduct = models.ForeignKey(UserProductModel, on_delete=models.CASCADE,related_name='product_transaccion')
    fecha_registro = models.DateTimeField(default=timezone.now)  # Campo de fecha de registro

    class Meta:
         db_table = "transaccion"
         verbose_name = "Transaccion"
         verbose_name_plural = "Transaccions"

    def __str__(self):
         return f'Transacción de {self.client.name} - {self.product.name}'

    def save(self, *args, **kwargs):
         if not self.pk:
              self.fecha_registro = timezone.now()  # Actualizar fecha y hora al crear el registro
              return super().save(*args, **kwargs)






