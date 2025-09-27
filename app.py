import streamlit as st
from openai import OpenAI
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import json
import re
import os

# Configuración de OpenAI - usa secretos de Streamlit o fallback
try:
    OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
except:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "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")

# Configuración de la página
st.set_page_config(
    page_title="Evaluación de Perfil de Riesgo Financiero",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Título principal
st.title("📊 Evaluación de Perfil de Riesgo Financiero con IA")
st.markdown("---")

# Sidebar con información
st.sidebar.header("⚙️ Configuración")
st.sidebar.success("✅ API Key configurada")
st.sidebar.info("La aplicación está lista para analizar tus respuestas con IA")

# Preguntas del formulario
preguntas = [
    "¿En una palabra, qué te genera la idea de usar inteligencia artificial para tus decisiones financieras?",
    "Si recibieras $1,000,000 inesperados, ¿qué es lo primero que harías con ellos?",
    "¿Cuál es tu principal meta financiera y en cuánto tiempo te gustaría alcanzarla?",
    "¿Cómo describes tu disposición a probar tecnologías nuevas para manejar tu dinero?",
    "¿Dejarías que la IA tomara decisiones por ti?"
]

# Función para analizar respuestas con IA
def analizar_respuesta_con_ia(pregunta, respuesta, api_key):
    """Analiza una respuesta usando OpenAI para determinar el nivel de riesgo"""
    if not api_key:
        return {"puntuacion": 0, "explicacion": "API key no configurada"}
    
    try:
        client = OpenAI(api_key=api_key)
        
        prompt = f"""
        Analiza la siguiente respuesta a una pregunta financiera y determina el nivel de propensión al riesgo (0-100).
        
        Pregunta: {pregunta}
        Respuesta: {respuesta}
        
        Considera estos factores:
        - 0-20: Muy averso al riesgo (conservador)
        - 21-40: Averso al riesgo (cauteloso)
        - 41-60: Neutral al riesgo (equilibrado)
        - 61-80: Propenso al riesgo (agresivo)
        - 81-100: Muy propenso al riesgo (muy agresivo)
        
        Responde en formato JSON:
        {{
            "puntuacion": [número del 0-100],
            "explicacion": "[explicación breve de por qué esta puntuación]",
            "categoria": "[conservador/cauteloso/equilibrado/agresivo/muy_agresivo]"
        }}
        """
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200,
            temperature=0.3
        )
        
        resultado = json.loads(response.choices[0].message.content)
        return resultado
        
    except Exception as e:
        return {"puntuacion": 50, "explicacion": f"Error en análisis: {str(e)}", "categoria": "equilibrado"}

# Función para calcular el perfil de riesgo general
def calcular_perfil_riesgo(puntuaciones):
    """Calcula el perfil de riesgo general basado en las puntuaciones"""
    promedio = sum(puntuaciones) / len(puntuaciones)
    
    if promedio <= 20:
        perfil = "Muy Averso al Riesgo"
        color = "#2E8B57"  # Verde oscuro
        descripcion = "Prefieres inversiones seguras y estables, priorizando la preservación del capital."
    elif promedio <= 40:
        perfil = "Averso al Riesgo"
        color = "#32CD32"  # Verde
        descripcion = "Eres cauteloso con tus finanzas, prefiriendo opciones de bajo riesgo."
    elif promedio <= 60:
        perfil = "Neutral al Riesgo"
        color = "#FFD700"  # Dorado
        descripcion = "Tienes un enfoque equilibrado, considerando tanto seguridad como crecimiento."
    elif promedio <= 80:
        perfil = "Propenso al Riesgo"
        color = "#FF6347"  # Tomate
        descripcion = "Estás dispuesto a asumir riesgos moderados para obtener mayores rendimientos."
    else:
        perfil = "Muy Propenso al Riesgo"
        color = "#DC143C"  # Rojo oscuro
        descripcion = "Tienes una alta tolerancia al riesgo y buscas oportunidades de alto rendimiento."
    
    return {
        "perfil": perfil,
        "porcentaje": round(promedio, 1),
        "color": color,
        "descripcion": descripcion
    }

# Función para crear visualizaciones
def crear_visualizaciones(puntuaciones, perfil_general):
    """Crea las visualizaciones del perfil de riesgo"""
    
    # Gráfico de barras de puntuaciones por pregunta
    fig_barras = px.bar(
        x=[f"Pregunta {i+1}" for i in range(len(puntuaciones))],
        y=puntuaciones,
        title="Puntuación de Riesgo por Pregunta",
        color=puntuaciones,
        color_continuous_scale="RdYlGn_r",
        labels={"x": "Preguntas", "y": "Puntuación de Riesgo (0-100)"}
    )
    fig_barras.update_layout(height=400)
    
    # Gráfico de radar
    categorias = ['IA Financiera', 'Manejo de Dinero', 'Metas Financieras', 
                  'Tecnología', 'Automatización']
    
    fig_radar = go.Figure()
    fig_radar.add_trace(go.Scatterpolar(
        r=puntuaciones,
        theta=categorias,
        fill='toself',
        name='Tu Perfil',
        line_color=perfil_general['color']
    ))
    fig_radar.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )),
        showlegend=True,
        title="Perfil de Riesgo - Vista Radar"
    )
    
    # Gráfico de gauge
    fig_gauge = go.Figure(go.Indicator(
        mode = "gauge+number+delta",
        value = perfil_general['porcentaje'],
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Perfil de Riesgo General"},
        delta = {'reference': 50},
        gauge = {
            'axis': {'range': [None, 100]},
            'bar': {'color': perfil_general['color']},
            'steps': [
                {'range': [0, 20], 'color': "lightgray"},
                {'range': [20, 40], 'color': "gray"},
                {'range': [40, 60], 'color': "yellow"},
                {'range': [60, 80], 'color': "orange"},
                {'range': [80, 100], 'color': "red"}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 90
            }
        }
    ))
    fig_gauge.update_layout(height=400)
    
    return fig_barras, fig_radar, fig_gauge

# Interfaz principal
def main():
    st.markdown("### 📝 Responde las siguientes preguntas para evaluar tu perfil de riesgo financiero")
    
    # Formulario de respuestas
    respuestas = {}
    
    with st.form("evaluacion_riesgo"):
        for i, pregunta in enumerate(preguntas):
            st.markdown(f"**{i+1}. {pregunta}**")
            respuestas[f"pregunta_{i+1}"] = st.text_area(
                f"Tu respuesta:",
                key=f"respuesta_{i+1}",
                height=100,
                placeholder="Escribe tu respuesta aquí..."
            )
            st.markdown("---")
        
        submitted = st.form_submit_button("🚀 Evaluar Mi Perfil de Riesgo", use_container_width=True)
    
    # Procesamiento de respuestas
    if submitted:
        
        # Verificar que todas las respuestas estén completas
        respuestas_vacias = [i+1 for i, resp in enumerate(respuestas.values()) if not resp.strip()]
        if respuestas_vacias:
            st.error(f"⚠️ Por favor, responde todas las preguntas. Faltan: {respuestas_vacias}")
            return
        
        # Mostrar progreso
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        # Analizar cada respuesta
        puntuaciones = []
        analisis_detallado = []
        
        for i, (pregunta, respuesta) in enumerate(zip(preguntas, respuestas.values())):
            status_text.text(f"Analizando pregunta {i+1}...")
            resultado = analizar_respuesta_con_ia(pregunta, respuesta, OPENAI_API_KEY)
            
            puntuaciones.append(resultado['puntuacion'])
            analisis_detallado.append({
                'pregunta': pregunta,
                'respuesta': respuesta,
                'puntuacion': resultado['puntuacion'],
                'explicacion': resultado['explicacion'],
                'categoria': resultado['categoria']
            })
            
            progress_bar.progress((i + 1) / len(preguntas))
        
        status_text.text("¡Análisis completado!")
        
        # Calcular perfil general
        perfil_general = calcular_perfil_riesgo(puntuaciones)
        
        # Mostrar resultados
        st.markdown("---")
        st.markdown("## 🎯 Resultados de tu Evaluación")
        
        # Métricas principales
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(
                label="Perfil de Riesgo",
                value=perfil_general['perfil'],
                delta=f"{perfil_general['porcentaje']}%"
            )
        
        with col2:
            st.metric(
                label="Puntuación Promedio",
                value=f"{perfil_general['porcentaje']}/100",
                delta=f"Pregunta más alta: {max(puntuaciones)}"
            )
        
        with col3:
            st.metric(
                label="Consistencia",
                value=f"{100 - (max(puntuaciones) - min(puntuaciones))}%",
                delta="Estabilidad en respuestas"
            )
        
        # Descripción del perfil
        st.markdown(f"### 📋 Descripción de tu Perfil")
        st.info(f"**{perfil_general['perfil']}**: {perfil_general['descripcion']}")
        
        # Visualizaciones
        st.markdown("### 📊 Visualizaciones de tu Perfil")
        
        fig_barras, fig_radar, fig_gauge = crear_visualizaciones(puntuaciones, perfil_general)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.plotly_chart(fig_barras, use_container_width=True)
            st.plotly_chart(fig_gauge, use_container_width=True)
        
        with col2:
            st.plotly_chart(fig_radar, use_container_width=True)
        
        # Análisis detallado por pregunta
        st.markdown("### 🔍 Análisis Detallado por Pregunta")
        
        for i, analisis in enumerate(analisis_detallado):
            with st.expander(f"Pregunta {i+1}: {analisis['pregunta'][:50]}..."):
                st.write(f"**Tu respuesta:** {analisis['respuesta']}")
                st.write(f"**Puntuación:** {analisis['puntuacion']}/100")
                st.write(f"**Categoría:** {analisis['categoria'].title()}")
                st.write(f"**Explicación:** {analisis['explicacion']}")
        
        # Recomendaciones
        st.markdown("### 💡 Recomendaciones Personalizadas")
        
        if perfil_general['porcentaje'] <= 40:
            st.success("""
            **Recomendaciones para Perfil Conservador:**
            - Considera certificados de depósito (CDs) y cuentas de ahorro de alto rendimiento
            - Invierte en bonos del gobierno y fondos de bonos
            - Mantén una cartera diversificada con 70% bonos, 30% acciones
            - Usa herramientas de IA para monitoreo y alertas, no para decisiones automáticas
            """)
        elif perfil_general['porcentaje'] <= 60:
            st.warning("""
            **Recomendaciones para Perfil Equilibrado:**
            - Considera una cartera 60/40 (60% acciones, 40% bonos)
            - Invierte en fondos indexados diversificados
            - Usa IA para análisis de mercado y recomendaciones, pero mantén control final
            - Considera robo-advisors para automatización parcial
            """)
        else:
            st.error("""
            **Recomendaciones para Perfil Agresivo:**
            - Considera una cartera con 80%+ en acciones
            - Invierte en ETFs de sectores específicos y acciones individuales
            - Usa IA avanzada para trading algorítmico y análisis técnico
            - Considera inversiones alternativas como criptomonedas (con límites)
            """)
        
        # Descargar reporte
        st.markdown("### 📄 Descargar Reporte")
        
        reporte = {
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "perfil_general": perfil_general,
            "puntuaciones": puntuaciones,
            "analisis_detallado": analisis_detallado
        }
        
        st.download_button(
            label="📥 Descargar Reporte Completo (JSON)",
            data=json.dumps(reporte, indent=2, ensure_ascii=False),
            file_name=f"perfil_riesgo_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
            mime="application/json"
        )

if __name__ == "__main__":
    main()
