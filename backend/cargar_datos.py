import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from productos.models import Producto, Categoria

# Crear categorías
categorias_data = [
    {"nombre": "Pinturas", "descripcion": "Pinturas para interior y exterior", "orden": 1},
    {"nombre": "Impermeabilizantes", "descripcion": "Productos impermeabilizantes", "orden": 2},
    {"nombre": "Herramientas", "descripcion": "Herramientas de construcción", "orden": 3},
    {"nombre": "Construcción", "descripcion": "Materiales de construcción", "orden": 4},
    {"nombre": "Automotriz", "descripcion": "Productos automotrices", "orden": 5},
]

print("🗂️  Creando categorías...")
for cat_data in categorias_data:
    cat, created = Categoria.objects.get_or_create(
        nombre=cat_data['nombre'],
        defaults=cat_data
    )
    if created:
        print(f"  ✅ {cat.nombre}")

# Crear productos
productos_data = [
    {
        "categoria": "Pinturas",
        "subcategoria": "Vinilos",
        "marca": "Pintuco",
        "nombre": "VINILTEX Advanced Mate",
        "descripcion": "Pintura premium base agua, ultra lavable, antibacterial 99.9%. Ideal para interiores residenciales y comerciales. Bajo VOC.",
        "presentaciones": ["Caneca 5 Gals", "Balde 2.5 Gals", "Galón 3.75 L", "1/4 0.946 L"],
        "uso": "Interior",
        "caracteristicas": ["Bajo VOC", "Antibacterial 99.9%", "Alta durabilidad", "Ultra lavable", "Acabado mate"],
        "precio": 125000,
        "activo": True,
    },
    {
        "categoria": "Pinturas",
        "subcategoria": "Vinilos",
        "marca": "Pintuco",
        "nombre": "VINILTEX Professional",
        "descripcion": "Pintura vinílica para interiores con excelente rendimiento y cubrimiento. Fácil aplicación.",
        "presentaciones": ["Galón 3.75 L", "1/4 0.946 L"],
        "uso": "Interior",
        "caracteristicas": ["Excelente cubrimiento", "Fácil aplicación", "Secado rápido", "Lavable"],
        "precio": 85000,
        "activo": True,
    },
    {
        "categoria": "Pinturas",
        "subcategoria": "Esmaltes",
        "marca": "Pintuco",
        "nombre": "ESMALTE Súper Brillante",
        "descripcion": "Esmalte sintético de alta resistencia y brillo superior. Para madera y metal.",
        "presentaciones": ["Galón 3.75 L", "1/4 0.946 L", "1/8 0.473 L"],
        "uso": "Interior/Exterior",
        "caracteristicas": ["Alto brillo", "Resistente a rayones", "Protección anticorrosiva", "Durabilidad superior"],
        "precio": 95000,
        "activo": True,
    },
    {
        "categoria": "Impermeabilizantes",
        "subcategoria": "Acrílicos",
        "marca": "Sika",
        "nombre": "Sikafill Impermeabilizante",
        "descripcion": "Impermeabilizante acrílico flexible para techos, terrazas y azoteas. Alta elasticidad.",
        "presentaciones": ["Caneca 20 Lt", "Caneca 5 Lt", "Galón 3.75 L"],
        "uso": "Exterior",
        "caracteristicas": ["Alta elasticidad", "Resistente a UV", "Fácil aplicación", "Durabilidad 5 años"],
        "precio": 180000,
        "activo": True,
    },
    {
        "categoria": "Herramientas",
        "subcategoria": "Rodillos",
        "marca": "Truper",
        "nombre": "Rodillo Profesional 9 pulgadas",
        "descripcion": "Rodillo profesional para pintura. Incluye mango telescópico extensible.",
        "presentaciones": ["Unidad"],
        "uso": "Interior/Exterior",
        "caracteristicas": ["Mango ergonómico", "Extensible", "Alta absorción", "Lavable"],
        "precio": 35000,
        "activo": True,
    },
    {
        "categoria": "Herramientas",
        "subcategoria": "Brochas",
        "marca": "Truper",
        "nombre": "Brocha Profesional 4 pulgadas",
        "descripcion": "Brocha de cerda natural para acabados profesionales. Mango de madera.",
        "presentaciones": ["Unidad"],
        "uso": "Interior/Exterior",
        "caracteristicas": ["Cerda natural", "Mango ergonómico", "Acabado profesional", "Durable"],
        "precio": 25000,
        "activo": True,
    },
    {
        "categoria": "Construcción",
        "subcategoria": "Estucos",
        "marca": "Corona",
        "nombre": "Estuco Plástico Premium",
        "descripcion": "Estuco plástico para reparación de superficies. Fácil lijado y excelente adherencia.",
        "presentaciones": ["Caneca 25 Kg", "Caneca 5 Kg"],
        "uso": "Interior",
        "caracteristicas": ["Fácil lijado", "Excelente adherencia", "No se agrieta", "Listo para usar"],
        "precio": 65000,
        "activo": True,
    },
    {
        "categoria": "Automotriz",
        "subcategoria": "Pinturas",
        "marca": "DuPont",
        "nombre": "Pintura Automotriz Base Agua",
        "descripcion": "Pintura automotriz profesional base agua. Bajo VOC, acabado profesional.",
        "presentaciones": ["Litro"],
        "uso": "Automotriz",
        "caracteristicas": ["Base agua", "Bajo VOC", "Acabado profesional", "Secado rápido"],
        "precio": 220000,
        "activo": True,
    },
]

print("\n📦 Creando productos...")
for prod_data in productos_data:
    prod, created = Producto.objects.get_or_create(
        nombre=prod_data['nombre'],
        marca=prod_data['marca'],
        defaults=prod_data
    )
    if created:
        print(f"  ✅ {prod.marca} - {prod.nombre}")

print("\n✅ ¡Datos cargados exitosamente!")
print(f"📊 Total categorías: {Categoria.objects.count()}")
print(f"📦 Total productos: {Producto.objects.count()}")
