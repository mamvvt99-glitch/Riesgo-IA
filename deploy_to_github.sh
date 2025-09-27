#!/bin/bash

# Script para conectar y subir el código a GitHub
# Ejecuta este script después de crear el repositorio en GitHub

echo "🚀 Configurando despliegue a GitHub..."

# Pide al usuario el nombre de usuario de GitHub
read -p "Ingresa tu nombre de usuario de GitHub: " GITHUB_USER
read -p "Ingresa el nombre del repositorio (ej: riesgo-ia-financiero): " REPO_NAME

# Configura el remote origin
echo "📡 Configurando remote origin..."
git remote add origin https://github.com/$GITHUB_USER/$REPO_NAME.git

# Verifica la configuración
echo "🔍 Verificando configuración..."
git remote -v

# Sube el código a GitHub
echo "📤 Subiendo código a GitHub..."
git branch -M main
git push -u origin main

echo "✅ ¡Código subido exitosamente a GitHub!"
echo "🌐 Tu repositorio está disponible en: https://github.com/$GITHUB_USER/$REPO_NAME"
echo ""
echo "📋 Próximos pasos para Streamlit Community Cloud:"
echo "1. Ve a https://share.streamlit.io/"
echo "2. Haz clic en 'New app'"
echo "3. Conecta tu cuenta de GitHub"
echo "4. Selecciona el repositorio: $REPO_NAME"
echo "5. Branch: main"
echo "6. Main file path: app.py"
echo "7. Haz clic en 'Deploy!'"
