from django.db import models
from django.db.models import Min
from django.db import connection
# Create your models here.

# class Categoria(models.Model):
#     nombre = models.CharField(max_length=100, blank=False, null=False, verbose_name='Nombre Categoría')

#     class Meta:
#         db_table = 'Categoria'
#         verbose_name = "Categoría de producto"
#         verbose_name_plural = "Categorías de productos"
#         ordering = ['nombre']

#     def __str__(self):
#         return f'{fels.id}.{self.nombre}'
    
#     def acciones():
#         return{
#             'accion_eliminar': 'eliminar la Categoría',
#             'accion_actualizar': 'actualizar la Categoría'
#         }
    
#     class Producto(models.Model):
#         Categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, verbose_name='Categoría')
#         nombre = models.Charfield(max_lenght=100, blank=False, null=False, verbose_name='Nombre')
#         descripcion = models.CharField(max_length=400, blank=False, null=False, verbose_name='Descripción')
#         precio = models.IntegerField(blank=False, null=False, verbose_name='Precio')
#         descuento_subscriptor = models.IntegerField(
#             validators=[MinValueValidator(0), MaxValueValidator(100)],
#             blank=False,
#             null=False,
#             verbose_name='% Descuento subscriptor'
#         )

#     imagen = models.ImageField(upload_to='productos/', blank=False, null=False)

#     class Perfil(models.Model):
#         USUARIO_CHOICES = [
#             ('Cliente', 'Cliente'),
#             ('Administrador', 'Administrador'),
#             ('Superusuario', 'Superusuario'),
#         ]
#         usuario = models.OneToOneField(User, on_delete=models.CASCADE)
#         tipo_usuario = models.CharField(
#             choices=USUARIO_CHOICES,
#             max_length=50,
#             blank=False,
#             null=False,
#             verbose_name='Tipo de usuario'
#         )
#         rut = models.CharField(max_lenght=15, blank=False, null=False, verbose_name= 'RUT')
#         direccion = models.CharField ////
#         suscrito = models.BooleanField ////
#         imagen = models.ImageField(upload_to='perfiles/', blank=False, null=False, verbose_name='Imagen')

#         class Meta:
#             db_table = 'Perfil'
#             verbose_name = "Perfil de usuario"
#             verbose_name_plural = "Perfiles de usuarios"
#             ordering = ['tipo_usuario']

#             def __str__(self):
#                 suscrito = ''
#                 if self.tipo_usuario == 'Cliente':
#                     suscrito = ' suscrito' if self.suscrito else ' no suscrito'
#                 return f'{self.usuario.first_name} {self.usuario.last_name} (ID {self.id}'
            
# class Carrito(models.Model):
#     cliente = models.ForeignKey(Perfil, on_delete=models.DO_NOTHING)
#     producto = models.ForeignKey(Producto, on_delete=models.DO_NOTHING)
#     precio = models.IntegerField(blank=False, null=False, verbose_name='Precio')
#     descuento_suscriptor = models.IntegerField(

#     )

# class Boleta(models.Model):
#     ESTADO_CHOICES = [
#         ('Anulado', 'Anulado'),
#         ('Vendido', 'Vendido'),
#         ('Despachado', 'Despachado'),
#         ('Entregado', 'Entregado'),
#     ]

# class Bodega(models.Model):
#     producto = models.ForeignKey(Producto, on_delete=models.DO_NOTHING, verbose_name='Producto')

#     class Meta:
#         db_table = 'Bodega'
#         verbose_name = "Bodega"
#         verbose_name_plural = "Bodegas"

#     def __str__(self):
#         consulta_swl = f'SELECT boleta_id FROM DetalleBoleta WHERE bodega_id={self.id}'
#         with connection.cursor() as cursor:
#             cursor.execute(consulta_sql)
#             resultado = cursor.fetchone()
#             info = f'Vendido (Boleta)'