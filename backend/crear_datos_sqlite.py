import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from productos.models import ProductoManager, CategoriaManager

producto_manager = ProductoManager()
categoria_manager = CategoriaManager()

print("✅ Cargando datos de ejemplo en MongoDB...")
print("📦 Productos disponibles a través de la API")
print("")
print("🚀 El sistema está listo. Los productos se gestionan vía MongoDB.")
print("   Para cargar productos de ejemplo, ejecuta:")
print("   python load_sample_data.py")
