#!/usr/bin/env python3
"""
Script de prueba para verificar que la aplicación funciona correctamente
"""

def test_imports():
    """Prueba que todas las importaciones funcionen"""
    try:
        import streamlit as st
        from openai import OpenAI
        import pandas as pd
        import plotly.express as px
        import plotly.graph_objects as go
        from datetime import datetime
        import json
        import re
        print("✅ Todas las importaciones funcionan correctamente")
        return True
    except ImportError as e:
        print(f"❌ Error en importaciones: {e}")
        return False

def test_analisis_function():
    """Prueba la función de análisis con datos de ejemplo"""
    try:
        # Importar la función desde app.py
        import sys
        import os
        sys.path.append(os.path.dirname(os.path.abspath(__file__)))
        
        from app import analizar_respuesta_con_ia
        
        # Prueba con datos de ejemplo
        pregunta = "¿En una palabra, qué te genera la idea de usar inteligencia artificial para tus decisiones financieras?"
        respuesta = "expectativa"
        
        # Sin API key (debería devolver error controlado)
        resultado = analizar_respuesta_con_ia(pregunta, respuesta, None)
        print(f"✅ Función de análisis funciona: {resultado}")
        return True
        
    except Exception as e:
        print(f"❌ Error en función de análisis: {e}")
        return False

def test_perfil_calculation():
    """Prueba el cálculo de perfil de riesgo"""
    try:
        from app import calcular_perfil_riesgo
        
        # Prueba con puntuaciones de ejemplo
        puntuaciones = [50, 60, 40, 70, 30, 80]
        perfil = calcular_perfil_riesgo(puntuaciones)
        
        print(f"✅ Cálculo de perfil funciona: {perfil}")
        return True
        
    except Exception as e:
        print(f"❌ Error en cálculo de perfil: {e}")
        return False

def main():
    """Ejecuta todas las pruebas"""
    print("🧪 Iniciando pruebas de la aplicación...")
    print("=" * 50)
    
    tests = [
        ("Importaciones", test_imports),
        ("Función de Análisis", test_analisis_function),
        ("Cálculo de Perfil", test_perfil_calculation)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n🔍 Probando: {test_name}")
        if test_func():
            passed += 1
        else:
            print(f"❌ {test_name} falló")
    
    print("\n" + "=" * 50)
    print(f"📊 Resultados: {passed}/{total} pruebas pasaron")
    
    if passed == total:
        print("🎉 ¡Todas las pruebas pasaron! La aplicación está lista.")
    else:
        print("⚠️  Algunas pruebas fallaron. Revisa los errores arriba.")

if __name__ == "__main__":
    main()
