#!/bin/bash

echo "🚀 Iniciando Diana Margarita E-commerce..."

# Verificar MongoDB
if ! pgrep -x "mongod" > /dev/null; then
    echo "⚠️  MongoDB no está corriendo. Por favor inicia MongoDB primero."
    echo "   macOS: brew services start mongodb-community"
    echo "   Linux: sudo systemctl start mongod"
    exit 1
fi

echo "✅ MongoDB está corriendo"

# Iniciar Backend
echo "🔧 Iniciando Backend Django..."
cd backend
source venv/bin/activate
python manage.py runserver &
BACKEND_PID=$!
cd ..

sleep 3

# Iniciar Frontend
echo "⚛️  Iniciando Frontend React..."
cd frontend
npm start &
FRONTEND_PID=$!
cd ..

echo ""
echo "✅ Servidores iniciados!"
echo ""
echo "📱 Frontend: http://localhost:3000"
echo "🔧 Backend: http://localhost:8000"
echo "⚙️  Admin: http://localhost:8000/admin"
echo ""
echo "Presiona Ctrl+C para detener los servidores"

# Esperar señal de interrupción
trap "kill $BACKEND_PID $FRONTEND_PID; exit" INT
wait
