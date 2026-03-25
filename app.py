from __future__ import annotations

from pathlib import Path
from typing import Dict, Optional

import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Indicadores Financieros - Empresa C",
    page_icon="📊",
    layout="wide",
)

BASE_DIR = Path(__file__).resolve().parent
DEFAULT_FILE = BASE_DIR / "data" / "tablas_FIR_industria3_anio14_normalizado_streamlit.xlsx"

REQUIRED_SHEETS = [
    "companies",
    "scores_company",
    "investor_history_long",
    "income_statement_long",
    "balance_sheet_long",
    "financial_stats_long",
]

DISPLAY_NAMES = {
    "Beneficios_por_accion": "BPA",
    "ROE": "ROE",
    "Precio_accion": "Precio de la acción",
    "Calificacion_crediticia": "Calificación crediticia",
    "Calificacion_imagen": "Calificación de imagen",
    "Ingresos_Internet": "Ingresos Internet",
    "Ingresos_Mayoreo": "Ingresos Mayoreo",
    "Ingresos_MarcaP": "Ingresos Marca Privada",
    "Ingresos_Total": "Ingresos Totales",
    "Costo_Pares_Vendidos": "Costo de pares vendidos",
    "Almacen_Gastos": "Gastos de almacén",
    "Marketing_Gastos": "Gastos de marketing",
    "Admin_Gastos": "Gastos administrativos",
    "Beneficio_Operativo": "Beneficio operativo",
    "Interes_Exp_Inc": "Interés exp./inc.",
    "Ingresos_Impuestos": "Impuestos",
    "Beneficio_Neto": "Beneficio neto",
    "Efectivo_en_Caja": "Efectivo en caja",
    "Corriente_Activos": "Activos corrientes",
    "Activo_Fijo": "Activo fijo",
    "Total_Activos": "Activos totales",
    "Pasivos_Actuales": "Pasivos corrientes",
    "Prestamos_Largo_Plazo": "Préstamos largo plazo",
    "Total_Pasivo": "Pasivos totales",
    "Capital_Inicial": "Capital inicial",
    "Venta_de_Existencias": "Venta de existencias",
    "Beneficios_Retenidos": "Beneficios retenidos",
    "Final_Equity": "Capital contable final",
    "Margen_Bruto": "Margen bruto",
    "Margen_Operativo": "Margen operativo",
    "Margen_Neto": "Margen neto",
    "Div_por_Accion": "Dividendo por acción",
    "Total_Div_Pago_000s": "Pago total de dividendos",
    "Pago_pct_Beneficio": "Pago % beneficio",
    "Intereses_Cobertura_Ratio": "Cobertura de intereses",
    "Ratio_Deuda_Activos": "Deuda / activos",
    "Ratio_Riesgo_de_Falla": "Riesgo de falla (ratio)",
    "Riesgo_de_Falla": "Riesgo de falla",
    "Ratio_Actual": "Razón circulante",
    "Dias_de_Inventario": "Días de inventario",
    "Acciones_Circulacion_000s": "Acciones en circulación",
}

NUMERIC_HISTORY_METRICS = [
    "Beneficios_por_accion",
    "ROE",
    "Precio_accion",
    "Calificacion_imagen",
]

PERCENT_METRICS = {
    "ROE",
    "Margen_Bruto",
    "Margen_Operativo",
    "Margen_Neto",
    "Pago_pct_Beneficio",
    "Ratio_Deuda_Activos",
    "Ratio_Riesgo_de_Falla",
}

MULTIPLE_METRICS = {
    "Intereses_Cobertura_Ratio",
    "Ratio_Actual",
}

COUNT_METRICS = {
    "Dias_de_Inventario",
    "Acciones_Circulacion_000s",
    "Calificacion_imagen",
}

TEXT_METRICS = {
    "Calificacion_crediticia",
    "Riesgo_de_Falla",
}

MONEY_METRICS = {
    "Beneficios_por_accion",
    "Precio_accion",
    "Ingresos_Internet",
    "Ingresos_Mayoreo",
    "Ingresos_MarcaP",
    "Ingresos_Total",
    "Costo_Pares_Vendidos",
    "Almacen_Gastos",
    "Marketing_Gastos",
    "Admin_Gastos",
    "Beneficio_Operativo",
    "Interes_Exp_Inc",
    "Ingresos_Impuestos",
    "Beneficio_Neto",
    "Efectivo_en_Caja",
    "Corriente_Activos",
    "Activo_Fijo",
    "Total_Activos",
    "Pasivos_Actuales",
    "Prestamos_Largo_Plazo",
    "Total_Pasivo",
    "Capital_Inicial",
    "Venta_de_Existencias",
    "Beneficios_Retenidos",
    "Final_Equity",
    "Div_por_Accion",
    "Total_Div_Pago_000s",
}

SUMMARY_KPIS = [
    "Ingresos_Total",
    "Beneficio_Operativo",
    "Beneficio_Neto",
    "Margen_Operativo",
    "Margen_Neto",
    "Efectivo_en_Caja",
    "Total_Activos",
    "Final_Equity",
]

STATEMENT_ORDER = [
    "Ingresos_Internet",
    "Ingresos_Mayoreo",
    "Ingresos_MarcaP",
    "Ingresos_Total",
    "Costo_Pares_Vendidos",
    "Almacen_Gastos",
    "Marketing_Gastos",
    "Admin_Gastos",
    "Beneficio_Operativo",
    "Interes_Exp_Inc",
    "Ingresos_Impuestos",
    "Beneficio_Neto",
]

BALANCE_ORDER = [
    "Efectivo_en_Caja",
    "Corriente_Activos",
    "Activo_Fijo",
    "Total_Activos",
    "Pasivos_Actuales",
    "Prestamos_Largo_Plazo",
    "Total_Pasivo",
    "Capital_Inicial",
    "Venta_de_Existencias",
    "Beneficios_Retenidos",
    "Final_Equity",
]

RATIOS_ORDER = [
    "Margen_Bruto",
    "Margen_Operativo",
    "Margen_Neto",
    "Div_por_Accion",
    "Total_Div_Pago_000s",
    "Pago_pct_Beneficio",
    "Intereses_Cobertura_Ratio",
    "Ratio_Deuda_Activos",
    "Ratio_Riesgo_de_Falla",
    "Riesgo_de_Falla",
    "Ratio_Actual",
    "Dias_de_Inventario",
    "Acciones_Circulacion_000s",
]


@st.cache_data(show_spinner=False)
def load_workbook(file_source: Optional[str | Path] = None, file_bytes: Optional[bytes] = None) -> Dict[str, pd.DataFrame]:
    if file_bytes is not None:
        excel = pd.ExcelFile(file_bytes)
    else:
        excel = pd.ExcelFile(file_source)

    missing = [sheet for sheet in REQUIRED_SHEETS if sheet not in excel.sheet_names]
    if missing:
        raise ValueError(f"Faltan hojas requeridas: {', '.join(missing)}")

    return {sheet: pd.read_excel(excel, sheet_name=sheet) for sheet in excel.sheet_names}


@st.cache_data(show_spinner=False)
def get_default_data() -> Dict[str, pd.DataFrame]:
    return load_workbook(file_source=DEFAULT_FILE)


@st.cache_data(show_spinner=False)
def get_uploaded_data(file_bytes: bytes) -> Dict[str, pd.DataFrame]:
    return load_workbook(file_bytes=file_bytes)


def label(metric: str) -> str:
    return DISPLAY_NAMES.get(metric, metric.replace("_", " "))


def format_value(metric: str, value) -> str:
    if pd.isna(value):
        return "-"

    if metric in TEXT_METRICS:
        return str(value)

    if metric in PERCENT_METRICS:
        return f"{float(value):.1%}"

    if metric in MULTIPLE_METRICS:
        return f"{float(value):.2f}x"

    if metric == "Dias_de_Inventario":
        return f"{int(round(float(value)))} días"

    if metric == "Acciones_Circulacion_000s":
        return f"{float(value):,.0f} mil"

    if metric in MONEY_METRICS:
        return f"${float(value):,.0f}"

    if metric in COUNT_METRICS:
        return f"{float(value):,.0f}"

    if isinstance(value, (int, float)):
        return f"{float(value):,.2f}"

    return str(value)


def format_delta(metric: str, company_value, avg_value) -> str:
    if pd.isna(company_value) or pd.isna(avg_value):
        return ""
    delta = float(company_value) - float(avg_value)

    if metric in PERCENT_METRICS:
        sign = "+" if delta >= 0 else ""
        return f"{sign}{delta:.1%} vs media"

    if metric in MULTIPLE_METRICS:
        sign = "+" if delta >= 0 else ""
        return f"{sign}{delta:.2f}x vs media"

    if metric in MONEY_METRICS:
        sign = "+" if delta >= 0 else "-"
        return f"{sign}${abs(delta):,.0f} vs media"

    sign = "+" if delta >= 0 else ""
    return f"{sign}{delta:,.2f} vs media"


def safe_metric_value(df: pd.DataFrame, company_code: str, metric_name: str):
    subset = df[(df["company_code"] == company_code) & (df["metric_name"] == metric_name)]
    return subset["value"].iloc[0] if not subset.empty else pd.NA


def safe_history_value(df: pd.DataFrame, company_code: str, metric_name: str, year: Optional[int] = None):
    subset = df[(df["entity_code"] == company_code) & (df["metric_name"] == metric_name)]
    if year is not None:
        subset = subset[subset["year"] == year]
    return subset["value"].iloc[0] if not subset.empty else pd.NA


def build_comparison_table(df: pd.DataFrame, company_code: str, metric_order: list[str]) -> pd.DataFrame:
    rows = []
    for metric in metric_order:
        company_value = safe_metric_value(df, company_code, metric)
        avg_value = safe_metric_value(df, "Media", metric)
        if pd.isna(company_value) and pd.isna(avg_value):
            continue
        row = {
            "Métrica": label(metric),
            "Empresa seleccionada": format_value(metric, company_value),
            "Media industria": format_value(metric, avg_value),
        }
        if metric not in TEXT_METRICS and not pd.isna(company_value) and not pd.isna(avg_value):
            row["Diferencia"] = format_delta(metric, company_value, avg_value)
        else:
            row["Diferencia"] = "-"
        rows.append(row)
    return pd.DataFrame(rows)


def build_sector_comparison(df: pd.DataFrame, metric_name: str) -> pd.DataFrame:
    out = df[df["metric_name"] == metric_name].copy()
    out = out[out["company_code"].isin(["A", "B", "C", "D", "Media"])]
    out["Empresa"] = out["company_name"].fillna(out["company_code"])
    out["Valor_num"] = pd.to_numeric(out["value"], errors="coerce")
    out["Valor_texto"] = out["value"].apply(lambda x: format_value(metric_name, x))
    return out[["company_code", "Empresa", "Valor_num", "Valor_texto"]]


st.title("📊 Indicadores financieros de la Empresa C")
st.caption("Dashboard en Streamlit para CNomada Sport a partir del archivo normalizado del reporte BSG.")

with st.sidebar:
    st.header("Configuración")
    uploaded_file = st.file_uploader(
        "Cargar otro archivo normalizado (.xlsx)",
        type=["xlsx"],
        help="Si no cargas nada, la app usa el archivo incluido en el paquete.",
    )

    try:
        if uploaded_file is not None:
            data = get_uploaded_data(uploaded_file.getvalue())
            st.success("Archivo cargado correctamente.")
        else:
            if DEFAULT_FILE.exists():
                data = get_default_data()
                st.info("Usando el archivo incluido en la carpeta data/.")
            else:
                st.error("No se encontró el archivo por defecto. Carga un Excel normalizado.")
                st.stop()
    except Exception as exc:
        st.error(f"No se pudo leer el archivo: {exc}")
        st.stop()

    companies_df = data["companies"].copy()
    companies_df["display"] = companies_df["company_code"] + " - " + companies_df["company_name"]
    default_idx = companies_df.index[companies_df["company_code"] == "C"]
    default_idx = int(default_idx[0]) if len(default_idx) else 0
    selected_display = st.selectbox("Empresa", companies_df["display"].tolist(), index=default_idx)
    selected_company = companies_df.loc[companies_df["display"] == selected_display, "company_code"].iloc[0]
    selected_company_name = companies_df.loc[companies_df["company_code"] == selected_company, "company_name"].iloc[0]

    selected_hist_metrics = st.multiselect(
        "Métricas históricas",
        options=NUMERIC_HISTORY_METRICS,
        default=["Beneficios_por_accion", "ROE", "Precio_accion"],
        format_func=label,
    )
    show_targets = st.toggle("Comparar contra objetivo del inversionista", value=True)

# Prepare data
investor_history = data["investor_history_long"].copy()
investor_history["year"] = pd.to_numeric(investor_history["year"], errors="coerce")

company_history = investor_history[
    (investor_history["entity_type"] == "Empresa") & (investor_history["entity_code"] == selected_company)
].copy()

objectives_history = investor_history[investor_history["entity_type"] == "Objetivo"].copy()

available_years = sorted(company_history["year"].dropna().astype(int).unique().tolist())
first_year = min(available_years) if available_years else None
last_year = max(available_years) if available_years else None

scores_df = data["scores_company"].copy()
current_score = scores_df[(scores_df["company_code"] == selected_company) & (scores_df["score_view"] == "Marcador_al_dia")]
if current_score.empty:
    current_score = scores_df[(scores_df["company_code"] == selected_company)].head(1)

income_df = data["income_statement_long"].copy()
balance_df = data["balance_sheet_long"].copy()
ratios_df = data["financial_stats_long"].copy()

company_income = income_df[income_df["company_code"] == selected_company]
company_balance = balance_df[balance_df["company_code"] == selected_company]
company_ratios = ratios_df[ratios_df["company_code"] == selected_company]

st.markdown(
    f"""
<div style="padding: 0.9rem 1rem; border-radius: 0.8rem; background: #f6f8fb; border: 1px solid #e6e9ef; margin-bottom: 1rem;">
<b>Empresa seleccionada:</b> {selected_company_name} &nbsp;|&nbsp;
<b>Serie histórica disponible:</b> {first_year if first_year else '-'} a {last_year if last_year else '-'} &nbsp;|&nbsp;
<b>Detalle financiero puntual:</b> Año 14
</div>
""",
    unsafe_allow_html=True,
)

if first_year and first_year > 10:
    st.info(
        f"El archivo actual no trae datos desde el Año 10. La serie histórica disponible inicia en el Año {first_year}."
    )

summary_left, summary_right = st.columns([3, 1])
with summary_left:
    kpi_cols = st.columns(4)
    for idx, metric in enumerate(SUMMARY_KPIS):
        col = kpi_cols[idx % 4]
        company_value = safe_metric_value(income_df if metric in STATEMENT_ORDER else balance_df if metric in BALANCE_ORDER else ratios_df, selected_company, metric)
        avg_value = safe_metric_value(income_df if metric in STATEMENT_ORDER else balance_df if metric in BALANCE_ORDER else ratios_df, "Media", metric)
        col.metric(label(metric), format_value(metric, company_value), format_delta(metric, company_value, avg_value))

with summary_right:
    if not current_score.empty:
        score_row = current_score.iloc[0]
        rank = score_row.get("rank", "-")
        gtd = score_row.get("GTD_Score_Global", "-")
        st.metric("Ranking Año 14", f"#{int(rank)}" if pd.notna(rank) else "-")
        st.metric("G-T-D Score", f"{int(gtd)}" if pd.notna(gtd) else "-")

st.caption("Las cifras monetarias del estado de resultados y balance se muestran en el mismo formato monetario del reporte normalizado.")

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    [
        "Resumen ejecutivo",
        "Tendencias históricas",
        "Estado de resultados",
        "Balance y liquidez",
        "Comparativo sectorial",
    ]
)

with tab1:
    c1, c2 = st.columns(2)

    with c1:
        income_mix = company_income[company_income["metric_name"].isin(["Ingresos_Internet", "Ingresos_Mayoreo", "Ingresos_MarcaP"])]
        income_mix = income_mix.copy()
        income_mix["Métrica"] = income_mix["metric_name"].map(label)
        fig_mix = px.pie(
            income_mix,
            names="Métrica",
            values="value",
            title="Composición de ingresos Año 14",
            hole=0.45,
        )
        fig_mix.update_layout(margin=dict(l=10, r=10, t=50, b=10), legend_title_text="")
        st.plotly_chart(fig_mix, use_container_width=True)

    with c2:
        capital_structure = pd.DataFrame(
            {
                "Concepto": ["Pasivos totales", "Capital contable final"],
                "Valor": [
                    safe_metric_value(balance_df, selected_company, "Total_Pasivo"),
                    safe_metric_value(balance_df, selected_company, "Final_Equity"),
                ],
            }
        )
        fig_cap = px.bar(
            capital_structure,
            x="Concepto",
            y="Valor",
            text="Valor",
            title="Estructura financiera Año 14",
        )
        fig_cap.update_traces(texttemplate="$%{text:,.0f}", textposition="outside")
        fig_cap.update_layout(margin=dict(l=10, r=10, t=50, b=10), yaxis_title="Valor")
        st.plotly_chart(fig_cap, use_container_width=True)

    st.subheader("Lectura rápida")
    eps_y14 = safe_history_value(company_history, selected_company, "Beneficios_por_accion", 14)
    roe_y14 = safe_history_value(company_history, selected_company, "ROE", 14)
    price_y14 = safe_history_value(company_history, selected_company, "Precio_accion", 14)
    credit_y14 = safe_history_value(company_history, selected_company, "Calificacion_crediticia", 14)
    img_y14 = safe_history_value(company_history, selected_company, "Calificacion_imagen", 14)

    quick_text = f"""
- En el Año 14, **{selected_company_name}** reporta **{format_value('Ingresos_Total', safe_metric_value(income_df, selected_company, 'Ingresos_Total'))} en ingresos totales y {format_value('Beneficio_Neto', safe_metric_value(income_df, selected_company, 'Beneficio_Neto'))}** de beneficio neto.
- Sus márgenes clave son **{format_value('Margen_Operativo', safe_metric_value(ratios_df, selected_company, 'Margen_Operativo'))}** operativo y **{format_value('Margen_Neto', safe_metric_value(ratios_df, selected_company, 'Margen_Neto'))}** neto.
- Frente al mercado de capitales, el Año 14 cierra con **BPA {format_value('Beneficios_por_accion', eps_y14)}**, **ROE {format_value('ROE', roe_y14)}**, **precio de acción {format_value('Precio_accion', price_y14)}**, **crédito {format_value('Calificacion_crediticia', credit_y14)}** e **imagen {format_value('Calificacion_imagen', img_y14)}**.
- En liquidez y solvencia, la empresa muestra **efectivo {format_value('Efectivo_en_Caja', safe_metric_value(balance_df, selected_company, 'Efectivo_en_Caja'))}**, **razón circulante {format_value('Ratio_Actual', safe_metric_value(ratios_df, selected_company, 'Ratio_Actual'))}** y **deuda / activos {format_value('Ratio_Deuda_Activos', safe_metric_value(ratios_df, selected_company, 'Ratio_Deuda_Activos'))}**.
"""
    st.markdown(quick_text)

with tab2:
    st.subheader("Series históricas")
    if not selected_hist_metrics:
        st.warning("Selecciona al menos una métrica histórica en la barra lateral.")
    else:
        hist_chart = company_history[company_history["metric_name"].isin(selected_hist_metrics)].copy()
        hist_chart["Serie"] = hist_chart["metric_name"].map(label)
        hist_chart["Valor"] = pd.to_numeric(hist_chart["value"], errors="coerce")
        hist_chart["Fuente"] = selected_company_name

        if show_targets:
            target_chart = objectives_history[objectives_history["metric_name"].isin(selected_hist_metrics)].copy()
            target_chart["Serie"] = target_chart["metric_name"].map(label)
            target_chart["Valor"] = pd.to_numeric(target_chart["value"], errors="coerce")
            target_chart["Fuente"] = "Objetivo del inversionista"
            chart_df = pd.concat([hist_chart, target_chart], ignore_index=True)
        else:
            chart_df = hist_chart

        fig_hist = px.line(
            chart_df,
            x="year",
            y="Valor",
            color="Serie",
            line_dash="Fuente",
            markers=True,
            title="Evolución histórica",
        )
        fig_hist.update_layout(xaxis_title="Año", yaxis_title="Valor", legend_title_text="")
        st.plotly_chart(fig_hist, use_container_width=True)

    st.subheader("Tabla histórica")
    hist_pivot = company_history.copy()
    hist_pivot["Métrica"] = hist_pivot["metric_name"].map(label)
    pivot = hist_pivot.pivot_table(index="year", columns="Métrica", values="value", aggfunc="first").reset_index()
    st.dataframe(pivot, use_container_width=True, hide_index=True)

with tab3:
    st.subheader(f"Estado de resultados - {selected_company_name} vs media de la industria")
    income_table = build_comparison_table(income_df, selected_company, STATEMENT_ORDER)
    st.dataframe(income_table, use_container_width=True, hide_index=True)

    op_df = company_income[company_income["metric_name"].isin(["Ingresos_Total", "Beneficio_Operativo", "Beneficio_Neto"])]
    op_df = op_df.copy()
    op_df["Métrica"] = op_df["metric_name"].map(label)
    fig_ops = px.bar(op_df, x="Métrica", y="value", text="value", title="Ingresos y utilidades Año 14")
    fig_ops.update_traces(texttemplate="$%{text:,.0f}", textposition="outside")
    fig_ops.update_layout(margin=dict(l=10, r=10, t=50, b=10), yaxis_title="Valor")
    st.plotly_chart(fig_ops, use_container_width=True)

with tab4:
    left, right = st.columns(2)
    with left:
        st.subheader("Balance general")
        balance_table = build_comparison_table(balance_df, selected_company, BALANCE_ORDER)
        st.dataframe(balance_table, use_container_width=True, hide_index=True)

    with right:
        st.subheader("Ratios y calidad financiera")
        ratios_table = build_comparison_table(ratios_df, selected_company, RATIOS_ORDER)
        st.dataframe(ratios_table, use_container_width=True, hide_index=True)

    balance_chart_df = company_balance[company_balance["metric_name"].isin(["Efectivo_en_Caja", "Total_Activos", "Total_Pasivo", "Final_Equity"])]
    balance_chart_df = balance_chart_df.copy()
    balance_chart_df["Métrica"] = balance_chart_df["metric_name"].map(label)
    fig_balance = px.bar(balance_chart_df, x="Métrica", y="value", text="value", title="Balance resumido Año 14")
    fig_balance.update_traces(texttemplate="$%{text:,.0f}", textposition="outside")
    fig_balance.update_layout(margin=dict(l=10, r=10, t=50, b=10), yaxis_title="Valor")
    st.plotly_chart(fig_balance, use_container_width=True)

with tab5:
    st.subheader("Comparativo sectorial")
    sector_metric = st.selectbox(
        "Selecciona una métrica",
        options=STATEMENT_ORDER + BALANCE_ORDER + [m for m in RATIOS_ORDER if m not in TEXT_METRICS],
        index=(STATEMENT_ORDER + BALANCE_ORDER + [m for m in RATIOS_ORDER if m not in TEXT_METRICS]).index("Ingresos_Total"),
        format_func=label,
    )

    comparison = build_sector_comparison(
        income_df if sector_metric in STATEMENT_ORDER else balance_df if sector_metric in BALANCE_ORDER else ratios_df,
        sector_metric,
    )
    comparison = comparison.sort_values("Valor_num", ascending=False, na_position="last")
    fig_sector = px.bar(
        comparison,
        x="Empresa",
        y="Valor_num",
        text="Valor_texto",
        title=f"{label(sector_metric)} por empresa",
    )
    fig_sector.update_traces(textposition="outside")
    fig_sector.update_layout(margin=dict(l=10, r=10, t=50, b=10), yaxis_title=label(sector_metric))
    st.plotly_chart(fig_sector, use_container_width=True)

    st.dataframe(
        comparison[["Empresa", "Valor_texto"]].rename(columns={"Valor_texto": label(sector_metric)}),
        use_container_width=True,
        hide_index=True,
    )

st.divider()

with st.expander("Descargas"):
    export_income = build_comparison_table(income_df, selected_company, STATEMENT_ORDER).to_csv(index=False).encode("utf-8-sig")
    export_balance = build_comparison_table(balance_df, selected_company, BALANCE_ORDER).to_csv(index=False).encode("utf-8-sig")
    export_ratios = build_comparison_table(ratios_df, selected_company, RATIOS_ORDER).to_csv(index=False).encode("utf-8-sig")

    d1, d2, d3 = st.columns(3)
    d1.download_button("Descargar estado de resultados CSV", export_income, file_name=f"estado_resultados_{selected_company.lower()}.csv", mime="text/csv")
    d2.download_button("Descargar balance CSV", export_balance, file_name=f"balance_{selected_company.lower()}.csv", mime="text/csv")
    d3.download_button("Descargar ratios CSV", export_ratios, file_name=f"ratios_{selected_company.lower()}.csv", mime="text/csv")
