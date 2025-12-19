# 🚀 Guía Rápida - Depósito Social E-commerce

## Inicio Rápido

### 1️⃣ Iniciar el Proyecto

**Manual:**
```bash
# Terminal 1 - Backend
cd backend
source venv/bin/activate
python manage.py runserver

# Terminal 2 - Frontend
cd frontend
npm start
```

### 2️⃣ Cargar Datos de Ejemplo
```bash
cd backend
source venv/bin/activate
python cargar_productos_ferreteria.py
```

### 3️⃣ Acceso al Sistema

**Usuario Admin:**
- Usuario: `admin`
- Contraseña: `admin`

## 🌐 URLs del Sistema

| Servicio | URL | Descripción |
|----------|-----|-------------|
| **Frontend** | http://localhost:3000 | Tienda online |
| **Backend API** | http://localhost:8000/api | APIs REST |
| **Admin Panel** | http://localhost:8000/admin | Panel de administración |

## 📦 Funcionalidades Principales

### Frontend (React)
- ✅ Catálogo de productos con diseño profesional
- ✅ Búsqueda y filtros por categoría
- ✅ Carrito de compras (persistente)
- ✅ Checkout completo
- ✅ Integración con ePayco (PSE)
- ✅ Responsive design
- ✅ Notificaciones toast profesionales
- ✅ Diseño moderno con colores azul oscuro y naranja

### Backend (Django)
- ✅ API REST completa
- ✅ Gestión de productos
- ✅ Gestión de pedidos
- ✅ Panel de administración personalizado
- ✅ Base de datos SQLite
- ✅ Templates admin con branding corporativo

## 🛠️ Gestión de Productos

### Desde Django Admin
1. Ir a http://localhost:8000/admin
2. Login: **admin** / **admin**
3. Sección "Productos" > "Productos"
4. Crear/Editar/Eliminar productos

### Estructura de Producto
```python
{
  "categoria": "Herramientas Eléctricas",
  "marca": "DeWalt",
  "nombre": "Taladro Percutor 20V MAX",
  "descripcion": "Descripción del producto...",
  "presentaciones": ["Solo herramienta", "Con batería"],
  "caracteristicas": ["Característica 1", "Característica 2"],
  "precio": 450000,
  "imagen": "https://...",
  "activo": true
}
```

## 📊 APIs Disponibles

### Productos
```bash
# Listar todos
GET http://localhost:8000/api/productos/

# Por categoría
GET http://localhost:8000/api/productos/?categoria=Herramientas+Eléctricas

# Buscar
GET http://localhost:8000/api/productos/?search=taladro

# Detalle
GET http://localhost:8000/api/productos/{id}/
```

### Pedidos
```bash
# Crear pedido
POST http://localhost:8000/api/pedidos/
Content-Type: application/json

{
  "cliente": {
    "nombre": "Juan Pérez",
    "email": "juan@example.com",
    "telefono": "3001234567",
    "direccion": "Calle 123",
    "ciudad": "Bogotá"
  },
  "items": [{
    "producto_id": "...",
    "nombre": "Producto",
    "cantidad": 2,
    "precio": 50000
  }],
  "subtotal": 100000,
  "total": 100000,
  "metodo_pago": "PSE"
}
```

## 🎨 Categorías Disponibles

1. **Herramientas Eléctricas** - Taladros, sierras, pulidoras
2. **Herramientas Manuales** - Juegos de llaves, martillos
3. **Pinturas y Accesorios** - Pinturas, rodillos, brochas
4. **Plomería** - Grifos, tubos, accesorios
5. **Electricidad** - Cables, interruptores, bombillas
6. **Construcción** - Cemento, mezclas, herramientas

## 💳 Flujo de Pago

1. Cliente agrega productos al carrito
2. Procede al checkout
3. Completa formulario de datos
4. Click en "Pagar con PSE"
5. Se crea el pedido
6. Página de confirmación con número de pedido
7. (Producción) Redirección a ePayco para pago real

## 🎨 Diseño

**Colores corporativos:**
- Azul oscuro: #1a365d (principal)
- Azul medio: #2d5a8f (degradados)
- Naranja: #ff6b35 (acento)
- Naranja claro: #ff8555 (hover/degradados)

**Características de diseño:**
- Hero section con degradados y SVG
- Cards con efectos hover y bordes animados
- Botones con sombras y transiciones suaves
- Tipografía moderna y espaciado generoso
- Responsive en todos los dispositivos

## 🔧 Solución de Problemas

### Error de puerto ocupado (Backend)
```bash
# Matar proceso en puerto 8000
lsof -ti:8000 | xargs kill -9
```

### Error de puerto ocupado (Frontend)
```bash
# Matar proceso en puerto 3000
lsof -ti:3000 | xargs kill -9
```

### Reinstalar dependencias
```bash
# Backend
cd backend
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Frontend
cd frontend
rm -rf node_modules package-lock.json
npm install
```

### Resetear base de datos
```bash
cd backend
rm db.sqlite3
python manage.py migrate
python cargar_productos_ferreteria.py

# Recrear usuario admin
python manage.py shell
>>> from django.contrib.auth.models import User
>>> User.objects.create_superuser('admin', 'admin@depositosocial.com', 'admin')
```

## 📝 Productos Pre-cargados

El sistema incluye 15 productos de ferretería con marcas reales:
- **DeWalt**: Taladro percutor, Sierra circular
- **Makita**: Esmeril angular
- **Stanley**: Juego de llaves
- **Truper**: Martillo
- **Pintuco**: Viniltex, Esmalte sintético
- **Corona**: Rodillo, Brocha
- **FV**: Grifo monomando
- **Pavco**: Tubo PVC
- **Centelsa**: Cable THW
- **Bticino**: Interruptor doble
- **Philips**: Bombilla LED
- **Bosch**: Rotomartillo
- **Argos**: Cemento gris

## 🚀 Deploy a Producción

Ver archivo README.md para instrucciones detalladas de deployment.

## 📞 Soporte

Para preguntas o problemas, verificar:
- README.md (documentación completa)
- Logs de Django: Terminal del backend
- Logs de React: Terminal del frontend
- Panel de admin: http://localhost:8000/admin/

---

**Depósito Social - 50 Años de Confianza**
