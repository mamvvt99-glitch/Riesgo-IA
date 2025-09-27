# 🚀 Despliegue en Snowflake

Esta guía te ayudará a desplegar tu aplicación de Evaluación de Perfil de Riesgo Financiero en Snowflake.

## 📋 Prerrequisitos

1. **Cuenta de Snowflake** - Si no tienes una, regístrate en [snowflake.com](https://snowflake.com)
2. **Snowflake CLI** instalado
3. **Código de la aplicación** listo

## 🛠️ Instalación de Snowflake CLI

### Opción 1: Usando pip
```bash
pip install snowflake-cli-labs
```

### Opción 2: Usando conda
```bash
conda install -c conda-forge snowflake-cli-labs
```

### Opción 3: Usando npm
```bash
npm install -g @snowflake/snowflake-cli
```

## 🚀 Pasos de Despliegue

### Paso 1: Inicializar Snowflake
```bash
cd "/Users/pro2020/RiesgoIA /V2 riesgo IA"
snowflake init
```

### Paso 2: Configurar la aplicación
```bash
snowflake app create
```

### Paso 3: Configurar variables de entorno
En Snowflake, configura la variable de entorno:
```bash
snowflake app set-env OPENAI_API_KEY="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"
```

### Paso 4: Desplegar la aplicación
```bash
snowflake app deploy
```

## 🌐 Acceso a la Aplicación

Una vez desplegada, tu aplicación estará disponible en:
- **URL**: `https://TU_APP_ID.snowflake.app`
- **Dashboard**: Accede desde tu consola de Snowflake

## 🔧 Configuración Avanzada

### Variables de Entorno
Puedes configurar variables adicionales en Snowflake:
```bash
snowflake app set-env VARIABLE_NAME="valor"
```

### Logs y Monitoreo
```bash
# Ver logs de la aplicación
snowflake app logs

# Ver estado de la aplicación
snowflake app status
```

### Actualizar la Aplicación
```bash
# Desplegar cambios
snowflake app deploy

# Reiniciar la aplicación
snowflake app restart
```

## 📊 Características de la Aplicación

- ✅ **5 Preguntas Abiertas** sobre riesgo financiero
- ✅ **Análisis con IA** usando OpenAI GPT
- ✅ **Diagnóstico Personalizado** con porcentaje de riesgo
- ✅ **Visualizaciones Interactivas** (barras, radar, gauge)
- ✅ **Recomendaciones Personalizadas**
- ✅ **Reporte Descargable** en formato JSON

## 🔒 Seguridad

- La API key de OpenAI está configurada como variable de entorno
- Los datos se procesan de forma segura
- No se almacenan respuestas de usuarios

## 🆘 Solución de Problemas

### Error de API Key
```bash
# Verificar variables de entorno
snowflake app env

# Reconfigurar API key
snowflake app set-env OPENAI_API_KEY="tu_nueva_api_key"
```

### Error de Dependencias
```bash
# Verificar requirements.txt
cat requirements.txt

# Reinstalar dependencias
snowflake app deploy --force
```

### Logs de Error
```bash
# Ver logs detallados
snowflake app logs --follow
```

## 📞 Soporte

Si tienes problemas con el despliegue:
1. Revisa los logs: `snowflake app logs`
2. Verifica la configuración: `snowflake app status`
3. Consulta la documentación de Snowflake
4. Contacta al soporte de Snowflake

## 🎉 ¡Listo!

Tu aplicación de Evaluación de Perfil de Riesgo Financiero estará disponible públicamente en Snowflake con todas las funcionalidades de IA integradas.
