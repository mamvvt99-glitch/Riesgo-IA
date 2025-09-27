# 📊 Evaluación de Perfil de Riesgo Financiero con IA

Una aplicación web desarrollada en Streamlit que evalúa el perfil de riesgo financiero de los usuarios mediante análisis de IA de sus respuestas a preguntas abiertas.

## 🚀 Características

- **5 Preguntas Abiertas**: Formulario interactivo con preguntas diseñadas para evaluar la propensión al riesgo
- **Análisis con IA**: Utiliza OpenAI GPT para analizar cada respuesta y asignar puntuaciones de riesgo
- **Diagnóstico Personalizado**: Genera un perfil de riesgo con porcentaje y descripción detallada
- **Visualizaciones Interactivas**: Gráficos de barras, radar y gauge para visualizar el perfil
- **Recomendaciones Personalizadas**: Sugerencias financieras basadas en el perfil de riesgo
- **Reporte Descargable**: Exporta los resultados en formato JSON

## 📋 Preguntas de Evaluación

1. ¿En una palabra, qué te genera la idea de usar inteligencia artificial para tus decisiones financieras?
2. Si recibieras $1,000,000 inesperados, ¿qué es lo primero que harías con ellos?
3. ¿Cuál es tu principal meta financiera y en cuánto tiempo te gustaría alcanzarla?
4. ¿Cómo describes tu disposición a probar tecnologías nuevas para manejar tu dinero?
5. ¿Dejarías que la IA tomara decisiones por ti?

## 🛠️ Instalación

### **Despliegue Local**

1. **Clona o descarga el proyecto**
   ```bash
   git clone https://github.com/TU_USUARIO/riesgo-ia-financiero.git
   cd riesgo-ia-financiero
   ```

2. **Instala las dependencias**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecuta la aplicación**
   ```bash
   streamlit run app.py
   ```

### **Despliegue en Streamlit Community Cloud**

1. **Fork este repositorio** o clónalo a tu cuenta de GitHub
2. **Ve a [Streamlit Community Cloud](https://share.streamlit.io/)**
3. **Haz clic en "New app"**
4. **Conecta tu cuenta de GitHub**
5. **Selecciona el repositorio**: `riesgo-ia-financiero`
6. **Branch**: `main`
7. **Main file path**: `app.py`
8. **Haz clic en "Deploy!"**

La aplicación estará disponible públicamente en una URL como:
`https://TU_USUARIO-riesgo-ia-financiero-app-XXXXXX.streamlit.app/`

### **Despliegue en Snowflake (Recomendado)**

1. **Instala Snowflake CLI**:
   ```bash
   pip install snowflake-cli-labs
   ```

2. **Ejecuta el script de despliegue**:
   ```bash
   ./deploy_snowflake.sh
   ```

3. **O sigue los pasos manuales**:
   ```bash
   snowflake init
   snowflake app create
   snowflake app set-env OPENAI_API_KEY="tu_api_key"
   snowflake app deploy
   ```

La aplicación estará disponible en: `https://TU_APP_ID.snowflake.app`

**Ventajas de Snowflake:**
- ✅ Más rápido y confiable
- ✅ Mejor manejo de variables de entorno
- ✅ Logs detallados
- ✅ Escalabilidad automática

## 🔧 Configuración

### Variables de Entorno (Opcional)
Puedes crear un archivo `.env` con tu API key:
```
OPENAI_API_KEY=tu_api_key_aqui
```

### Configuración de OpenAI
- La aplicación utiliza GPT-3.5-turbo para el análisis
- Se puede configurar la API key directamente en la interfaz
- El análisis se realiza con un prompt optimizado para evaluar propensión al riesgo

## 📊 Perfiles de Riesgo

La aplicación clasifica a los usuarios en 5 categorías:

- **Muy Averso al Riesgo (0-20%)**: Prefiere inversiones seguras y estables
- **Averso al Riesgo (21-40%)**: Enfoque cauteloso con las finanzas
- **Neutral al Riesgo (41-60%)**: Equilibrio entre seguridad y crecimiento
- **Propenso al Riesgo (61-80%)**: Dispuesto a asumir riesgos moderados
- **Muy Propenso al Riesgo (81-100%)**: Alta tolerancia al riesgo

## 🎯 Funcionalidades

### Análisis Inteligente
- Cada respuesta se analiza individualmente con IA
- Puntuación de 0-100 para cada pregunta
- Explicación detallada del análisis

### Visualizaciones
- **Gráfico de Barras**: Puntuación por pregunta
- **Gráfico Radar**: Vista 360° del perfil
- **Gauge**: Indicador visual del nivel de riesgo general

### Recomendaciones Personalizadas
- Sugerencias de inversión basadas en el perfil
- Estrategias de cartera recomendadas
- Consejos sobre el uso de IA financiera

## 📱 Uso

1. **Completa el Formulario**: Responde las 5 preguntas de manera honesta
2. **Análisis Automático**: La IA analiza tus respuestas
3. **Revisa tu Perfil**: Ve tu clasificación y explicación
4. **Explora Visualizaciones**: Interactúa con los gráficos
5. **Lee Recomendaciones**: Aplica las sugerencias personalizadas
6. **Descarga tu Reporte**: Guarda los resultados para referencia futura

## 🔒 Privacidad y Seguridad

- Las respuestas se procesan localmente
- La API key se maneja de forma segura
- No se almacenan datos personales
- Los reportes se generan localmente

## 🚨 Limitaciones

- Requiere conexión a internet para el análisis con IA
- Depende de la disponibilidad de la API de OpenAI
- Los resultados son orientativos, no constituyen asesoramiento financiero profesional

## 📈 Próximas Mejoras

- [ ] Integración con más modelos de IA
- [ ] Análisis de sentimientos más avanzado
- [ ] Comparación con perfiles de referencia
- [ ] Seguimiento temporal del perfil de riesgo
- [ ] Integración con APIs financieras

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:
1. Fork el proyecto
2. Crea una rama para tu feature
3. Commit tus cambios
4. Push a la rama
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## ⚠️ Disclaimer

Esta aplicación es solo para fines educativos y de entretenimiento. No constituye asesoramiento financiero profesional. Siempre consulta con un asesor financiero calificado antes de tomar decisiones de inversión.
