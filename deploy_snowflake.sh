#!/bin/bash

# Script para desplegar la aplicación en Snowflake
echo "🚀 Iniciando despliegue en Snowflake..."

# Verificar que Snowflake CLI esté instalado
if ! command -v snowflake &> /dev/null; then
    echo "❌ Snowflake CLI no está instalado"
    echo "📦 Instalando Snowflake CLI..."
    pip install snowflake-cli-labs
fi

# Verificar que estamos en el directorio correcto
if [ ! -f "app.py" ]; then
    echo "❌ No se encontró app.py. Asegúrate de estar en el directorio correcto"
    exit 1
fi

echo "✅ Verificando archivos necesarios..."

# Verificar archivos requeridos
required_files=("app.py" "requirements.txt" "config.py" "streamlit_app.py")
for file in "${required_files[@]}"; do
    if [ ! -f "$file" ]; then
        echo "❌ Archivo requerido no encontrado: $file"
        exit 1
    fi
done

echo "✅ Todos los archivos requeridos están presentes"

# Inicializar Snowflake si es necesario
if [ ! -f "snowflake.toml" ]; then
    echo "🔧 Inicializando Snowflake..."
    snowflake init
fi

# Configurar la aplicación
echo "⚙️ Configurando la aplicación..."
snowflake app create

# Configurar variables de entorno
echo "🔑 Configurando variables de entorno..."
snowflake app set-env OPENAI_API_KEY="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"

# Desplegar la aplicación
echo "🚀 Desplegando la aplicación..."
snowflake app deploy

# Verificar el estado
echo "📊 Verificando estado de la aplicación..."
snowflake app status

echo "🎉 ¡Despliegue completado!"
echo "🌐 Tu aplicación estará disponible en: https://TU_APP_ID.snowflake.app"
echo ""
echo "📋 Comandos útiles:"
echo "  - Ver logs: snowflake app logs"
echo "  - Ver estado: snowflake app status"
echo "  - Reiniciar: snowflake app restart"
echo "  - Actualizar: snowflake app deploy"
