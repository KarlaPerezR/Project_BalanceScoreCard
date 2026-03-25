# Project_BalanceScoreCard
# App Streamlit - Indicadores Financieros Empresa C

Esta aplicación muestra los principales indicadores financieros de **CNomada Sport (Empresa C)** usando el archivo normalizado del reporte BSG.

## Qué incluye

- Resumen ejecutivo del Año 14
- KPIs clave: ingresos, utilidad operativa, utilidad neta, márgenes, efectivo, activos y equity
- Tendencias históricas disponibles en el archivo (la serie actual inicia en **Año 11**)
- Estado de resultados, balance general y ratios
- Comparativo de la Empresa C contra la media de la industria y contra las demás empresas
- Descarga de tablas en CSV

## Archivos

- `app.py`: aplicación principal
- `requirements.txt`: dependencias
- `data/tablas_FIR_industria3_anio14_normalizado_streamlit.xlsx`: archivo base

## Cómo ejecutarla

1. Abre una terminal en esta carpeta.
2. Instala dependencias:

```bash
pip install -r requirements.txt
```

3. Ejecuta la app:

```bash
streamlit run app.py
```

## Nota sobre los años

El archivo actual no trae datos desde Año 10. La serie histórica incluida en este paquete comienza en **Año 11**. La app ya muestra ese aviso automáticamente.

## Uso con otros archivos

También puedes cargar otro Excel normalizado desde la barra lateral de la aplicación.
