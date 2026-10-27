# Depósito Social - E-commerce Platform

Sistema de e-commerce profesional para venta de productos de ferretería, herramientas, pinturas y materiales de construcción.

## Arquitectura

- **Frontend**: React con diseño moderno y responsive
- **Backend**: Django + Django REST Framework
- **Base de Datos**: SQLite (desarrollo) / PostgreSQL (producción)
- **Pagos**: Integración con ePayco (PSE)

## Características

✅ Catálogo de productos con categorías
✅ Carrito de compras con persistencia
✅ Checkout y pago con PSE (ePayco)
✅ Panel de administración Django personalizado
✅ APIs REST completas
✅ Diseño profesional y responsive
✅ Búsqueda de productos
✅ Filtros por categoría
✅ Notificaciones toast profesionales

## Requisitos

- Python 3.9+
- Node.js 14+

## Instalación

### 1. Clonar el repositorio

```bash
cd ProyectoDianaMargarita
```

### 2. Configurar Backend

```bash
cd backend

# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Migrar base de datos
python manage.py migrate

# Cargar productos de ferretería
python cargar_productos_ferreteria.py

# Crear superusuario para Django Admin
# Usuario: admin, Contraseña: admin (ya creado)
python manage.py shell
>>> from django.contrib.auth.models import User
>>> User.objects.create_superuser('admin', 'admin@depositosocial.com', 'admin')

# Iniciar servidor
python manage.py runserver
```

El backend estará disponible en: `http://localhost:8000`

> **Producción:** define `DJANGO_DEBUG=false`, `DJANGO_SECRET_KEY` (una clave larga y aleatoria, por ejemplo `python -c "import secrets; print(secrets.token_urlsafe(50))"`) y `DJANGO_ALLOWED_HOSTS` (dominios separados por comas). Cambia también la contraseña del superusuario `admin`.

### 3. Configurar Frontend

```bash
cd ../frontend

# Instalar dependencias
npm install

# Iniciar servidor de desarrollo
npm start
```

El frontend estará disponible en: `http://localhost:3000`

## Uso

### Panel de Administración

1. Acceder a: `http://localhost:8000/admin`
2. Login con: **usuario:** admin, **contraseña:** admin
3. Gestionar productos, categorías y pedidos

### Tienda Online

1. Acceder a: `http://localhost:3000`
2. Navegar por categorías (Herramientas Eléctricas, Pinturas, Plomería, etc.)
3. Agregar productos al carrito
4. Realizar checkout con PSE

## APIs Disponibles

### Productos
- `GET /api/productos/` - Listar productos
- `GET /api/productos/:id/` - Detalle de producto
- `GET /api/productos/?categoria=Pinturas` - Filtrar por categoría
- `GET /api/productos/?search=pintura` - Buscar productos

### Categorías
- `GET /api/categorias/` - Listar categorías

### Pedidos
- `POST /api/pedidos/` - Crear pedido
- `GET /api/pedidos/` - Listar pedidos
- `GET /api/pedidos/:id/` - Detalle de pedido

### Pagos
- `POST /api/pago/epayco/` - Crear pago con ePayco

## Estructura del Proyecto

```
ProyectoDianaMargarita/
├── backend/
│   ├── ecommerce/          # Configuración Django
│   ├── productos/          # App de productos
│   ├── pedidos/            # App de pedidos
│   ├── templates/          # Templates admin personalizados
│   ├── manage.py
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/     # Componentes React
│   │   ├── pages/          # Páginas
│   │   ├── services/       # APIs
│   │   ├── contexts/       # Context API
│   │   └── App.js
│   └── package.json
└── README.md
```

## Modelo de Datos

### Producto (Django Model)
```python
{
  categoria: String,
  marca: String,
  nombre: String,
  descripcion: Text,
  presentaciones: JSONField,
  caracteristicas: JSONField,
  precio: Decimal,
  imagen: URL,
  activo: Boolean
}
```

### Pedido (Django Model)
```python
{
  cliente_nombre: String,
  cliente_email: Email,
  cliente_telefono: String,
  cliente_direccion: String,
  cliente_ciudad: String,
  items: JSONField,
  subtotal: Decimal,
  total: Decimal,
  estado: String,
  metodo_pago: String,
  notas: Text
}
```

## Categorías Disponibles

- Herramientas Eléctricas
- Herramientas Manuales
- Pinturas y Accesorios
- Plomería
- Electricidad
- Construcción

## Productos Pre-cargados

El sistema incluye 15 productos de ferretería con imágenes reales de marcas reconocidas:
- DeWalt, Makita, Bosch (Herramientas eléctricas)
- Stanley, Truper (Herramientas manuales)
- Pintuco, Corona (Pinturas)
- FV, Pavco (Plomería)
- Centelsa, Bticino, Philips (Electricidad)
- Argos (Construcción)

## Diseño

El sistema utiliza una paleta de colores moderna:
- **Azul oscuro**: #1a365d (principal)
- **Naranja**: #ff6b35 (acento)
- Diseño responsive y profesional
- Animaciones suaves y efectos hover
- Componentes de notificación toast

## Integración ePayco

El sistema está configurado para usar ePayco como pasarela de pagos con PSE:

1. El usuario completa el checkout
2. Se crea el pedido en la base de datos
3. Se muestra página de confirmación
4. (En producción) Se redirige a ePayco para pago real

## Desarrollo

### Agregar nuevos productos

Usar el Django Admin en `http://localhost:8000/admin`

### Personalizar diseño

Los estilos están en archivos CSS individuales en `frontend/src/`.

## Producción

Para desplegar en producción:

1. Configurar variables de entorno
2. Cambiar a PostgreSQL
3. Usar Gunicorn como servidor WSGI
4. Configurar nginx como reverse proxy
5. Configurar SSL/HTTPS
6. Build del frontend: `npm run build`
7. Configurar credenciales reales de ePayco

## Credenciales

### Django Admin
- **Usuario**: admin
- **Contraseña**: admin

## Licencia

Proyecto de Depósito Social - 50 Años de Confianza
