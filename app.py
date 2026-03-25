from __future__ import annotations

from pathlib import Path
from typing import Dict, Optional

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(
    page_title="Empresa C | CNomada Sport",
    page_icon="📊",
    layout="wide",
)

BASE_DIR = Path(__file__).resolve().parent
DEFAULT_FILE = BASE_DIR / "data" / "tablas_FIR_industria3_anio14_normalizado_streamlit.xlsx"
LOGO_FILE = BASE_DIR / "assets" / "nomada.png"
MARKET_TRENDS_FILE = BASE_DIR / "assets" / "bsg_market_trends_crop.png"

COMPANY_CODE = "C"
COMPANY_NAME = "CNomada Sport"
CURRENT_YEAR = 14

REQUIRED_SHEETS = [
    "companies",
    "scores_company",
    "investor_history_long",
    "investor_scores_long",
    "income_statement_long",
    "balance_sheet_long",
    "financial_stats_long",
    "consumer_attractiveness_long",
    "capacity_long",
    "benchmarks_long",
    "forecast_vs_actual_long",
    "leapfrog_history_long",
    "awards_rsc",
    "awards_competitions",
    "celebrity_bids_long",
    "prodventa_long",
    "csr_reference_long",
    "materials",
    "supply_demand",
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

PERCENT_METRICS = {
    "ROE",
    "Margen_Bruto",
    "Margen_Operativo",
    "Margen_Neto",
    "Pago_pct_Beneficio",
    "Ratio_Deuda_Activos",
    "Ratio_Riesgo_de_Falla",
}

MULTIPLE_METRICS = {"Intereses_Cobertura_Ratio", "Ratio_Actual"}
TEXT_METRICS = {"Calificacion_crediticia", "Riesgo_de_Falla"}
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

REGION_LABELS = {
    "Norteamerica": "Norteamérica",
    "Europa_Africa": "Europa-África",
    "Asia_Pacifico": "Asia-Pacífico",
    "America_Latina": "América Latina",
    "NA": "Norteamérica",
    "EA": "Europa-África",
    "AP": "Asia-Pacífico",
    "AL": "América Latina",
}
REGION_ORDER = ["Norteamérica", "Europa-África", "América Latina", "Asia-Pacífico"]


@st.cache_data(show_spinner=False)
def load_workbook(file_source: Optional[str | Path] = None, file_bytes: Optional[bytes] = None) -> Dict[str, pd.DataFrame]:
    excel = pd.ExcelFile(file_bytes if file_bytes is not None else file_source)
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


def region_label(value: str) -> str:
    return REGION_LABELS.get(value, value)


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
    if isinstance(value, (int, float)):
        return f"{float(value):,.2f}"
    return str(value)


def format_generic(value, as_percent: bool = False, as_money: bool = False, suffix: str = "") -> str:
    if pd.isna(value):
        return "-"
    if as_percent:
        return f"{float(value):.1%}{suffix}"
    if as_money:
        return f"${float(value):,.0f}{suffix}"
    return f"{float(value):,.0f}{suffix}"


def format_delta(metric: str, company_value, avg_value) -> str:
    if pd.isna(company_value) or pd.isna(avg_value):
        return "-"
    delta = float(company_value) - float(avg_value)
    sign = "+" if delta >= 0 else "-"
    if metric in PERCENT_METRICS:
        return f"{sign}{abs(delta):.1%} vs media"
    if metric in MULTIPLE_METRICS:
        return f"{sign}{abs(delta):.2f}x vs media"
    if metric in MONEY_METRICS:
        return f"{sign}${abs(delta):,.0f} vs media"
    return f"{sign}{abs(delta):,.2f} vs media"


def safe_metric_value(df: pd.DataFrame, company_code: str, metric_name: str):
    subset = df[(df["company_code"] == company_code) & (df["metric_name"] == metric_name)]
    return subset["value"].iloc[0] if not subset.empty else pd.NA


def safe_history_value(df: pd.DataFrame, metric_name: str, year: int):
    subset = df[(df["entity_code"] == COMPANY_CODE) & (df["metric_name"] == metric_name) & (df["year"] == year)]
    return subset["value"].iloc[0] if not subset.empty else pd.NA


def build_comparison_table(df: pd.DataFrame, metric_order: list[str]) -> pd.DataFrame:
    rows = []
    for metric in metric_order:
        company_value = safe_metric_value(df, COMPANY_CODE, metric)
        avg_value = safe_metric_value(df, "Media", metric)
        if pd.isna(company_value) and pd.isna(avg_value):
            continue
        rows.append(
            {
                "Métrica": label(metric),
                COMPANY_NAME: format_value(metric, company_value),
                "Media industria": format_value(metric, avg_value),
                "Diferencia": format_delta(metric, company_value, avg_value),
            }
        )
    return pd.DataFrame(rows)


def build_summary_kpi_source(metric: str) -> str:
    if metric in STATEMENT_ORDER:
        return "income"
    if metric in BALANCE_ORDER:
        return "balance"
    return "ratios"


def build_score_detail_table(investor_scores: pd.DataFrame) -> pd.DataFrame:
    score_df = investor_scores[(investor_scores["entity_type"] == "Empresa") & (investor_scores["entity_code"] == COMPANY_CODE)].copy()
    if score_df.empty:
        return pd.DataFrame()
    pivot = score_df.pivot_table(index="metric_name", columns="attribute", values="value", aggfunc="first").reset_index()
    cols = [
        "metric_name",
        "Peso_Medio",
        "A14_PEI",
        "A14_MEI",
        "MarcDia_PEI",
        "MarcDia_MEI",
        "Media_A12_A14",
    ]
    available = [c for c in cols if c in pivot.columns]
    pivot = pivot[available].copy()
    rename_map = {
        "metric_name": "Métrica",
        "Peso_Medio": "Valor de referencia",
        "A14_PEI": "A14 PEI",
        "A14_MEI": "A14 MEI",
        "MarcDia_PEI": "Marcador al día PEI",
        "MarcDia_MEI": "Marcador al día MEI",
        "Media_A12_A14": "Media A12-A14",
    }
    pivot = pivot.rename(columns=rename_map)
    pivot["Métrica"] = pivot["Métrica"].map(label)
    return pivot


def build_market_attractiveness(df: pd.DataFrame) -> pd.DataFrame:
    work = df[df["company_code"].isin(["A", "B", "C", "D"])].copy()
    work["region_label"] = work["region"].map(region_label)
    total = work.groupby("region_label", as_index=False)["consumer_attractiveness_year15"].sum().rename(columns={"consumer_attractiveness_year15": "Total_mercado"})
    company_c = work[work["company_code"] == COMPANY_CODE][["region_label", "consumer_attractiveness_year15"]].rename(columns={"consumer_attractiveness_year15": "Empresa_C"})
    merged = company_c.merge(total, on="region_label", how="left")
    merged["Otras_3_empresas"] = merged["Total_mercado"] - merged["Empresa_C"]
    merged["Participacion_C"] = merged["Empresa_C"] / merged["Total_mercado"]
    merged["Region"] = pd.Categorical(merged["region_label"], categories=REGION_ORDER, ordered=True)
    merged = merged.sort_values("Region")
    return merged[["region_label", "Empresa_C", "Otras_3_empresas", "Total_mercado", "Participacion_C"]].rename(columns={"region_label": "Región"})


def build_capacity_vs_others(df: pd.DataFrame) -> pd.DataFrame:
    work = df[(df["metric_family"] == "Equipo") & (df["year"] == 14) & (df["region"].notna()) & (df["region"] != "T")].copy()
    work["region_label"] = work["region"].map(region_label)
    total = work[work["company_code"] == "Total"][["region_label", "value"]].rename(columns={"value": "Total_sector"})
    company_c = work[work["company_code"] == COMPANY_CODE][["region_label", "value"]].rename(columns={"value": "Empresa_C"})
    merged = company_c.merge(total, on="region_label", how="left")
    merged["Otras_3_empresas"] = merged["Total_sector"] - merged["Empresa_C"]
    merged["Participacion_C"] = merged["Empresa_C"] / merged["Total_sector"]
    merged["region_label"] = pd.Categorical(merged["region_label"], categories=REGION_ORDER, ordered=True)
    merged = merged.sort_values("region_label")
    return merged.rename(columns={"region_label": "Región"})


def build_market_context(prodventa_df: pd.DataFrame) -> pd.DataFrame:
    work = prodventa_df[prodventa_df["region"] != "Media_Total"].copy()
    work["Región"] = work["region"].map(region_label)

    def get(metric_category: str, subcategory: Optional[str], metric_name: str, col_name: str):
        subset = work[(work["category"] == metric_category) & (work["metric_name"] == metric_name)]
        if subcategory is None:
            subset = subset[subset["subcategory"].isna()]
        else:
            subset = subset[subset["subcategory"] == subcategory]
        return subset[["Región", "value"]].rename(columns={"value": col_name})

    context = get("Demanda", "Actual", "(000s de pares)", "Demanda real A14")
    context = context.merge(get("Demanda", "Previsión", "(000s de pares)", "Previsión A14"), on="Región", how="left")
    context = context.merge(get("Marca", None, "Pares disponibles (000s)", "Pares disponibles"), on="Región", how="left")
    context = context.merge(get("Marca", None, "Pares vendidos (internet + mayoreo)", "Pares vendidos"), on="Región", how="left")
    context = context.merge(get("General", None, "Utilización de la capacidad de producción", "Utilización capacidad"), on="Región", how="left")
    context["Brecha oferta-demanda"] = context["Pares disponibles"] - context["Demanda real A14"]
    context["Región"] = pd.Categorical(context["Región"], categories=REGION_ORDER, ordered=True)
    return context.sort_values("Región")


def build_nonfinancial_history(history_df: pd.DataFrame) -> pd.DataFrame:
    work = history_df[(history_df["entity_code"] == COMPANY_CODE) & (history_df["metric_name"].isin(["Calificacion_imagen", "Calificacion_crediticia"]))].copy()
    work["Serie"] = work["metric_name"].map(label)
    return work


def credit_table_from_history(history_df: pd.DataFrame) -> pd.DataFrame:
    work = history_df[(history_df["entity_code"] == COMPANY_CODE) & (history_df["metric_name"] == "Calificacion_crediticia")][["year", "value"]].copy()
    work = work.rename(columns={"year": "Año", "value": "Calificación crediticia"})
    return work


def build_forecast_table(df: pd.DataFrame) -> pd.DataFrame:
    work = df[df["company_code"] == COMPANY_CODE].copy()
    if work.empty:
        return work
    work["Métrica"] = work["metric_name"].replace({"Ingresos": "Ingresos totales", "BPA": "BPA", "Imagen": "Imagen"})
    work = work.rename(
        columns={
            "forecast_value": "Pronóstico A14",
            "actual_value": "Real A14",
            "variance_value": "Varianza",
            "award_year14": "Bull's Eye A14",
            "cumulative_awards": "Premios acumulados",
        }
    )
    return work[["Métrica", "Pronóstico A14", "Real A14", "Varianza", "Bull's Eye A14", "Premios acumulados"]]


def build_awards_summary(awards_rsc: pd.DataFrame, awards_comp: pd.DataFrame) -> pd.DataFrame:
    rows = []
    rsc_row = awards_rsc[awards_rsc["year"] == 14].head(1)
    if not rsc_row.empty:
        rows.append(
            {
                "Indicador": "Premio RSC A14",
                "Resultado Empresa C": "Ganador" if str(rsc_row.iloc[0].get("winner", "")) == COMPANY_NAME else "No ganador",
                "Detalle": f"Ganador: {rsc_row.iloc[0].get('winner', '-')}; segundo lugar: {rsc_row.iloc[0].get('runner_up', '-')}",
            }
        )
    comp_rows = awards_comp[(awards_comp["company_code"] == COMPANY_CODE) & (awards_comp["year"] == 14)].copy()
    for _, row in comp_rows.iterrows():
        rows.append(
            {
                "Indicador": f"{row['award']} A14",
                "Resultado Empresa C": row.get("award_won", "-"),
                "Detalle": f"Premios acumulados: {int(row['cumulative_awards']) if pd.notna(row['cumulative_awards']) else 0}",
            }
        )
    return pd.DataFrame(rows)


def build_leapfrog_table(df: pd.DataFrame) -> pd.DataFrame:
    work = df[df["company_code"] == COMPANY_CODE].copy()
    if work.empty:
        return work
    work = work.rename(columns={"year": "Año", "points": "Puntos", "delta_vs_prior_year": "Δ vs año previo", "cumulative_awards": "Premios acumulados"})
    return work[["Año", "Puntos", "Δ vs año previo", "Premios acumulados"]]


def build_csr_table(df: pd.DataFrame) -> pd.DataFrame:
    work = df[df["year"].between(11, 14)].copy()
    work["$ por unidad"] = work["dolares_por_unidad"]
    work = work.rename(columns={"year": "Año", "level": "Nivel", "total_dolares_000s": "Total ($000s)", "puntos_imagen": "Puntos imagen"})
    return work[["Año", "Nivel", "Total ($000s)", "$ por unidad", "Puntos imagen"]]


def build_celebrity_table(df: pd.DataFrame) -> pd.DataFrame:
    work = df[df["company_code"] == COMPANY_CODE].copy()
    if work.empty:
        return work
    work = work.rename(columns={"celebrity": "Famoso", "holder_year15": "Titular A15", "num_offers": "Núm. ofertas", "offer_rank": "Posición de oferta C", "offer_amount": "Oferta de C"})
    return work[["Famoso", "Titular A15", "Núm. ofertas", "Posición de oferta C", "Oferta de C"]].sort_values(["Posición de oferta C", "Oferta de C"], ascending=[True, False])


def build_benchmark_region_table(df: pd.DataFrame, region_name: str) -> pd.DataFrame:
    bench = df.copy()
    bench["RegionLabel"] = bench["Region"]
    subset = bench[bench["RegionLabel"] == region_name].copy()
    if subset.empty:
        return pd.DataFrame()
    pivot = subset.pivot_table(index=["Grupo", "Segmento", "Metrica"], columns="benchmark_level", values="value", aggfunc="first").reset_index()
    desired = [c for c in ["Bajo", "Media", "Alta", "Empresa_C"] if c in pivot.columns]
    pivot = pivot[["Grupo", "Segmento", "Metrica", *desired]].copy()
    rename = {"Empresa_C": COMPANY_NAME}
    pivot = pivot.rename(columns=rename)
    return pivot


def build_exec_text(income_df: pd.DataFrame, balance_df: pd.DataFrame, ratios_df: pd.DataFrame, score_row: pd.Series | None, investor_history: pd.DataFrame) -> str:
    ingresos = format_value("Ingresos_Total", safe_metric_value(income_df, COMPANY_CODE, "Ingresos_Total"))
    op = format_value("Beneficio_Operativo", safe_metric_value(income_df, COMPANY_CODE, "Beneficio_Operativo"))
    neto = format_value("Beneficio_Neto", safe_metric_value(income_df, COMPANY_CODE, "Beneficio_Neto"))
    margen_op = format_value("Margen_Operativo", safe_metric_value(ratios_df, COMPANY_CODE, "Margen_Operativo"))
    margen_neto = format_value("Margen_Neto", safe_metric_value(ratios_df, COMPANY_CODE, "Margen_Neto"))
    efectivo = format_value("Efectivo_en_Caja", safe_metric_value(balance_df, COMPANY_CODE, "Efectivo_en_Caja"))
    bpa = format_value("Beneficios_por_accion", safe_history_value(investor_history, "Beneficios_por_accion", 14))
    precio = format_value("Precio_accion", safe_history_value(investor_history, "Precio_accion", 14))
    imagen = format_value("Calificacion_imagen", safe_history_value(investor_history, "Calificacion_imagen", 14))
    credito = format_value("Calificacion_crediticia", safe_history_value(investor_history, "Calificacion_crediticia", 14))
    ranking = int(score_row["rank"]) if score_row is not None and pd.notna(score_row.get("rank")) else "-"
    gtd = int(score_row["GTD_Score_Global"]) if score_row is not None and pd.notna(score_row.get("GTD_Score_Global")) else "-"

    return (
        f"En el Año {CURRENT_YEAR}, {COMPANY_NAME} cerró con {ingresos} en ingresos totales, "
        f"{op} de beneficio operativo y {neto} de beneficio neto. "
        f"Su rentabilidad fue de {margen_op} a nivel operativo y {margen_neto} a nivel neto, con {efectivo} en efectivo. "
        f"Desde la perspectiva del inversionista, la empresa terminó el año con BPA {bpa}, precio de acción {precio}, "
        f"imagen {imagen}, calificación crediticia {credito}, ranking #{ranking} y G-T-D Score {gtd}."
    )


with st.sidebar:
    st.header("Fuente de datos")
    uploaded_file = st.file_uploader(
        "Cargar otro Excel normalizado (.xlsx)",
        type=["xlsx"],
        help="Si no cargas nada, la app usa el archivo incluido en la carpeta data/.",
    )

    try:
        if uploaded_file is not None:
            data = get_uploaded_data(uploaded_file.getvalue())
            st.success("Archivo cargado correctamente.")
        else:
            if DEFAULT_FILE.exists():
                data = get_default_data()
                st.info("Usando el archivo incluido en el proyecto.")
            else:
                st.error("No se encontró el archivo por defecto. Carga un Excel normalizado.")
                st.stop()
    except Exception as exc:
        st.error(f"No se pudo leer el archivo: {exc}")
        st.stop()

    st.markdown("---")
    st.write("**Empresa analizada:** CNomada Sport")
    st.write("**Cobertura histórica:** A11-A14 en indicadores del inversionista + lámina visual A10-A14 en tendencias de mercado.")
    st.write("**Detalle financiero puntual:** Año 14")

# Data prep
investor_history = data["investor_history_long"].copy()
investor_history["year"] = pd.to_numeric(investor_history["year"], errors="coerce")
company_history = investor_history[(investor_history["entity_type"] == "Empresa") & (investor_history["entity_code"] == COMPANY_CODE)].copy()

scores_df = data["scores_company"].copy()
score_row = scores_df[(scores_df["company_code"] == COMPANY_CODE) & (scores_df["score_view"] == "Marcador_al_dia")]
if score_row.empty:
    score_row = scores_df[scores_df["company_code"] == COMPANY_CODE].head(1)
score_row = score_row.iloc[0] if not score_row.empty else None

income_df = data["income_statement_long"].copy()
balance_df = data["balance_sheet_long"].copy()
ratios_df = data["financial_stats_long"].copy()
investor_scores = data["investor_scores_long"].copy()
consumer_attr = data["consumer_attractiveness_long"].copy()
capacity_df = data["capacity_long"].copy()
benchmarks_df = data["benchmarks_long"].copy()
forecast_df = data["forecast_vs_actual_long"].copy()
leapfrog_df = data["leapfrog_history_long"].copy()
awards_rsc_df = data["awards_rsc"].copy()
awards_comp_df = data["awards_competitions"].copy()
celebrity_df = data["celebrity_bids_long"].copy()
prodventa_df = data["prodventa_long"].copy()
csr_df = data["csr_reference_long"].copy()
materials_df = data["materials"].copy()
supply_df = data["supply_demand"].copy()

company_income = income_df[income_df["company_code"] == COMPANY_CODE].copy()
company_balance = balance_df[balance_df["company_code"] == COMPANY_CODE].copy()
company_ratios = ratios_df[ratios_df["company_code"] == COMPANY_CODE].copy()
market_attractiveness = build_market_attractiveness(consumer_attr)
capacity_vs_others = build_capacity_vs_others(capacity_df)
market_context = build_market_context(prodventa_df)
score_detail_table = build_score_detail_table(investor_scores)
forecast_table = build_forecast_table(forecast_df)
awards_summary = build_awards_summary(awards_rsc_df, awards_comp_df)
leapfrog_table = build_leapfrog_table(leapfrog_df)
csr_table = build_csr_table(csr_df)
celebrity_table = build_celebrity_table(celebrity_df)
credit_history_table = credit_table_from_history(investor_history)
nonfinancial_history = build_nonfinancial_history(investor_history)

# Header
if LOGO_FILE.exists():
    st.image(str(LOGO_FILE), use_container_width=True)

st.title("Empresa C | Dashboard de CNomada Sport")
st.caption("Aplicación enfocada en la Empresa C para revisar resultados financieros, posicionamiento por mercado y desempeño no financiero.")

exec_text = build_exec_text(income_df, balance_df, ratios_df, score_row, investor_history)
st.markdown(
    f"""
<div style="padding: 1rem 1.1rem; border-radius: 0.9rem; background: #f6f8fb; border: 1px solid #e6e9ef; margin-bottom: 1rem;">
<b>Resumen principal:</b> {exec_text}
</div>
""",
    unsafe_allow_html=True,
)

kpi_cols = st.columns(4)
for idx, metric in enumerate(SUMMARY_KPIS):
    col = kpi_cols[idx % 4]
    source = build_summary_kpi_source(metric)
    source_df = income_df if source == "income" else balance_df if source == "balance" else ratios_df
    company_value = safe_metric_value(source_df, COMPANY_CODE, metric)
    avg_value = safe_metric_value(source_df, "Media", metric)
    col.metric(label(metric), format_value(metric, company_value), format_delta(metric, company_value, avg_value))

right_a, right_b, right_c = st.columns(3)
rank_display = f"#{int(score_row['rank'])}" if score_row is not None and pd.notna(score_row.get("rank")) else "-"
gtd_display = f"{int(score_row['GTD_Score_Global'])}" if score_row is not None and pd.notna(score_row.get("GTD_Score_Global")) else "-"
score_display = f"{int(score_row['Punt_Media_Ponderada'])}" if score_row is not None and pd.notna(score_row.get("Punt_Media_Ponderada")) else "-"
right_a.metric("Ranking A14", rank_display)
right_b.metric("G-T-D Score", gtd_display)
right_c.metric("Puntuación ponderada A14", score_display)

st.info(
    "La app mantiene los indicadores financieros principales del dashboard anterior. "
    "El archivo normalizado solo trae series numéricas históricas de inversionista desde A11; "
    "para integrar A10 se añadió la lámina visual de tendencias de mercado (precios y S/Q) del reporte."
)

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "Resumen ejecutivo",
        "Resultados financieros",
        "Análisis mercado",
        "Indicadores no financieros",
    ]
)

with tab1:
    st.subheader("Lectura rápida de la Empresa C")
    text_left, text_right = st.columns([1.3, 1])

    with text_left:
        st.markdown(
            f"""
**CNomada Sport** terminó el Año 14 en el **puesto {rank_display}** del sector.

- Ingresos totales: **{format_value('Ingresos_Total', safe_metric_value(income_df, COMPANY_CODE, 'Ingresos_Total'))}**
- Beneficio operativo: **{format_value('Beneficio_Operativo', safe_metric_value(income_df, COMPANY_CODE, 'Beneficio_Operativo'))}**
- Beneficio neto: **{format_value('Beneficio_Neto', safe_metric_value(income_df, COMPANY_CODE, 'Beneficio_Neto'))}**
- BPA del Año 14: **{format_value('Beneficios_por_accion', safe_history_value(investor_history, 'Beneficios_por_accion', 14))}**
- Precio de la acción: **{format_value('Precio_accion', safe_history_value(investor_history, 'Precio_accion', 14))}**
- Imagen: **{format_value('Calificacion_imagen', safe_history_value(investor_history, 'Calificacion_imagen', 14))}**
- Calificación crediticia: **{format_value('Calificacion_crediticia', safe_history_value(investor_history, 'Calificacion_crediticia', 14))}**

En el tablero de indicadores, la empresa presenta una base sólida de caja, pero todavía queda rezagada frente a la media sectorial en rentabilidad y puntuación global.
"""
        )

    with text_right:
        score_table_small = pd.DataFrame(
            {
                "Indicador": ["PEI", "MEI", "Cambio vs Y13", "Bono puntos"],
                "Valor": [
                    score_row.get("Punt_Expectativa_Inversor", "-") if score_row is not None else "-",
                    score_row.get("Punt_Mejor_Sector", "-") if score_row is not None else "-",
                    score_row.get("Cambio_vs_Y13", "-") if score_row is not None else "-",
                    score_row.get("Bono_Puntos", "-") if score_row is not None else "-",
                ],
            }
        )
        st.dataframe(score_table_small, use_container_width=True, hide_index=True)

    c1, c2 = st.columns(2)
    with c1:
        income_mix = company_income[company_income["metric_name"].isin(["Ingresos_Internet", "Ingresos_Mayoreo", "Ingresos_MarcaP"])].copy()
        income_mix["Métrica"] = income_mix["metric_name"].map(label)
        fig_mix = px.pie(income_mix, names="Métrica", values="value", hole=0.45, title="Composición de ingresos A14")
        fig_mix.update_layout(margin=dict(l=10, r=10, t=50, b=10), legend_title_text="")
        st.plotly_chart(fig_mix, use_container_width=True)

    with c2:
        capital_structure = pd.DataFrame(
            {
                "Concepto": ["Pasivos totales", "Capital contable final"],
                "Valor": [
                    safe_metric_value(balance_df, COMPANY_CODE, "Total_Pasivo"),
                    safe_metric_value(balance_df, COMPANY_CODE, "Final_Equity"),
                ],
            }
        )
        fig_cap = px.bar(capital_structure, x="Concepto", y="Valor", text="Valor", title="Estructura financiera A14")
        fig_cap.update_traces(texttemplate="$%{text:,.0f}", textposition="outside")
        fig_cap.update_layout(margin=dict(l=10, r=10, t=50, b=10), yaxis_title="Valor")
        st.plotly_chart(fig_cap, use_container_width=True)

    st.subheader("Detalle de puntuaciones por métrica")
    if not score_detail_table.empty:
        st.dataframe(score_detail_table, use_container_width=True, hide_index=True)

with tab2:
    st.subheader("Resultados financieros de CNomada Sport")
    f1, f2 = st.columns(2)

    with f1:
        st.markdown("**Estado de resultados | Empresa C vs media**")
        st.dataframe(build_comparison_table(income_df, STATEMENT_ORDER), use_container_width=True, hide_index=True)

    with f2:
        st.markdown("**Balance y liquidez | Empresa C vs media**")
        combined_balance = pd.concat(
            [
                build_comparison_table(balance_df, BALANCE_ORDER),
                build_comparison_table(ratios_df, RATIOS_ORDER),
            ],
            ignore_index=True,
        )
        st.dataframe(combined_balance, use_container_width=True, hide_index=True)

    g1, g2 = st.columns(2)
    with g1:
        op_df = company_income[company_income["metric_name"].isin(["Ingresos_Total", "Beneficio_Operativo", "Beneficio_Neto"])].copy()
        op_df["Métrica"] = op_df["metric_name"].map(label)
        fig_ops = px.bar(op_df, x="Métrica", y="value", text="value", title="Ingresos y utilidades A14")
        fig_ops.update_traces(texttemplate="$%{text:,.0f}", textposition="outside")
        fig_ops.update_layout(margin=dict(l=10, r=10, t=50, b=10), yaxis_title="Valor")
        st.plotly_chart(fig_ops, use_container_width=True)

    with g2:
        ratio_focus = pd.DataFrame(
            {
                "Métrica": ["Margen operativo", "Margen neto", "Razón circulante", "Cobertura de intereses"],
                "Valor": [
                    safe_metric_value(ratios_df, COMPANY_CODE, "Margen_Operativo"),
                    safe_metric_value(ratios_df, COMPANY_CODE, "Margen_Neto"),
                    safe_metric_value(ratios_df, COMPANY_CODE, "Ratio_Actual"),
                    safe_metric_value(ratios_df, COMPANY_CODE, "Intereses_Cobertura_Ratio"),
                ],
                "Tipo": ["Porcentaje", "Porcentaje", "Múltiplo", "Múltiplo"],
            }
        )
        fig_ratio = go.Figure()
        for _, row in ratio_focus.iterrows():
            fig_ratio.add_trace(go.Bar(name=row["Métrica"], x=[row["Métrica"]], y=[row["Valor"]]))
        fig_ratio.update_layout(title="Ratios clave A14", showlegend=False, margin=dict(l=10, r=10, t=50, b=10), yaxis_title="Valor")
        st.plotly_chart(fig_ratio, use_container_width=True)

with tab3:
    st.subheader("Análisis por mercado: Empresa C vs otras 3 empresas")
    st.markdown("La comparación contra las otras empresas se basa en indicadores regionales disponibles en el archivo: atractivo al consumidor, equipo de producción instalado y contexto de demanda/oferta.")

    m1, m2 = st.columns(2)
    with m1:
        attr_chart = market_attractiveness.melt(id_vars=["Región", "Participacion_C", "Total_mercado"], value_vars=["Empresa_C", "Otras_3_empresas"], var_name="Grupo", value_name="Valor")
        fig_attr = px.bar(attr_chart, x="Región", y="Valor", color="Grupo", barmode="group", title="Atractivo al consumidor A15")
        fig_attr.update_layout(margin=dict(l=10, r=10, t=50, b=10), legend_title_text="")
        st.plotly_chart(fig_attr, use_container_width=True)

    with m2:
        cap_chart = capacity_vs_others.melt(id_vars=["Región", "Participacion_C", "Total_sector"], value_vars=["Empresa_C", "Otras_3_empresas"], var_name="Grupo", value_name="Valor")
        fig_cap = px.bar(cap_chart, x="Región", y="Valor", color="Grupo", barmode="group", title="Equipo de producción A14 (000s pares)")
        fig_cap.update_layout(margin=dict(l=10, r=10, t=50, b=10), legend_title_text="")
        st.plotly_chart(fig_cap, use_container_width=True)

    summary_market = market_attractiveness.copy()
    summary_market["Participación C"] = summary_market["Participacion_C"].apply(lambda x: f"{x:.1%}")
    summary_market["Empresa C"] = summary_market["Empresa_C"].round(0).astype(int)
    summary_market["Otras 3 empresas"] = summary_market["Otras_3_empresas"].round(0).astype(int)
    summary_market["Total mercado"] = summary_market["Total_mercado"].round(0).astype(int)
    st.dataframe(summary_market[["Región", "Empresa C", "Otras 3 empresas", "Total mercado", "Participación C"]], use_container_width=True, hide_index=True)

    st.subheader("Lectura por mercado")
    region_tabs = st.tabs(REGION_ORDER)
    for tab, region_name in zip(region_tabs, REGION_ORDER):
        with tab:
            region_attr = market_attractiveness[market_attractiveness["Región"] == region_name].iloc[0]
            region_cap = capacity_vs_others[capacity_vs_others["Región"] == region_name].iloc[0]
            region_ctx = market_context[market_context["Región"] == region_name].iloc[0]
            left, right = st.columns([1.1, 1])
            with left:
                st.markdown(
                    f"""
**{region_name}**

- Atractivo al consumidor de C: **{int(region_attr['Empresa_C'])}**
- Atractivo conjunto de las otras 3: **{int(region_attr['Otras_3_empresas'])}**
- Participación de C dentro del atractivo regional: **{region_attr['Participacion_C']:.1%}**
- Equipo de producción de C: **{int(region_cap['Empresa_C']):,}** mil pares
- Equipo de las otras 3 empresas: **{int(region_cap['Otras_3_empresas']):,}** mil pares
- Demanda real A14 del mercado: **{int(region_ctx['Demanda real A14']):,}** mil pares
- Brecha oferta-demanda: **{int(region_ctx['Brecha oferta-demanda']):,}** mil pares
"""
                )
            with right:
                mini = pd.DataFrame(
                    {
                        "Grupo": [COMPANY_NAME, "Otras 3 empresas"],
                        "Atractivo": [region_attr["Empresa_C"], region_attr["Otras_3_empresas"]],
                    }
                )
                fig_mini = px.bar(mini, x="Grupo", y="Atractivo", title=f"Atractivo | {region_name}", text="Atractivo")
                fig_mini.update_traces(textposition="outside")
                fig_mini.update_layout(margin=dict(l=10, r=10, t=45, b=10), showlegend=False)
                st.plotly_chart(fig_mini, use_container_width=True)

            region_bench = build_benchmark_region_table(benchmarks_df, region_name)
            if not region_bench.empty:
                st.markdown("**Benchmark operativo de la Empresa C**")
                st.dataframe(region_bench, use_container_width=True, hide_index=True)

    st.subheader("Tendencias de precios y S/Q desde Año 10")
    if MARKET_TRENDS_FILE.exists():
        st.image(str(MARKET_TRENDS_FILE), use_container_width=True, caption="Lámina del reporte con tendencias regionales de precio en internet, precio al por mayor y S/Q desde el Año 10.")
    else:
        st.warning("No se encontró la imagen de tendencias A10-A14.")

with tab4:
    st.subheader("Indicadores no financieros y operativos")

    nf1, nf2 = st.columns(2)
    with nf1:
        st.markdown("**Imagen y crédito**")
        image_history = nonfinancial_history[nonfinancial_history["metric_name"] == "Calificacion_imagen"].copy()
        if not image_history.empty:
            image_history["value_num"] = pd.to_numeric(image_history["value"], errors="coerce")
            fig_img = px.line(image_history, x="year", y="value_num", markers=True, title="Calificación de imagen A11-A14")
            fig_img.update_layout(margin=dict(l=10, r=10, t=45, b=10), xaxis_title="Año", yaxis_title="Puntos")
            st.plotly_chart(fig_img, use_container_width=True)
        st.dataframe(credit_history_table, use_container_width=True, hide_index=True)

    with nf2:
        st.markdown("**Pronóstico vs real**")
        if not forecast_table.empty:
            st.dataframe(forecast_table, use_container_width=True, hide_index=True)
        st.markdown("**Premios y bonificaciones**")
        if not awards_summary.empty:
            st.dataframe(awards_summary, use_container_width=True, hide_index=True)

    st.markdown("**Leap Frog y evolución del desempeño**")
    if not leapfrog_table.empty:
        l1, l2 = st.columns([1.2, 1])
        with l1:
            st.dataframe(leapfrog_table, use_container_width=True, hide_index=True)
        with l2:
            lf = leapfrog_table.copy()
            fig_lf = px.line(lf, x="Año", y="Puntos", markers=True, title="Puntuación anual")
            fig_lf.update_layout(margin=dict(l=10, r=10, t=45, b=10), xaxis_title="Año", yaxis_title="Puntos")
            st.plotly_chart(fig_lf, use_container_width=True)

    op1, op2 = st.columns(2)
    with op1:
        st.markdown("**RSC y ciudadanía**")
        st.dataframe(csr_table, use_container_width=True, hide_index=True)
    with op2:
        st.markdown("**Patrocinios de famosos relacionados con C**")
        if not celebrity_table.empty:
            celeb_show = celebrity_table.copy()
            celeb_show["Oferta de C"] = celeb_show["Oferta de C"].apply(lambda x: f"${x:,.0f}" if pd.notna(x) else "-")
            st.dataframe(celeb_show, use_container_width=True, hide_index=True)

    st.markdown("**Operación y contexto del sector**")
    x1, x2 = st.columns(2)
    with x1:
        st.markdown("Materiales")
        st.dataframe(materials_df, use_container_width=True, hide_index=True)
    with x2:
        st.markdown("Oferta y demanda global")
        st.dataframe(supply_df, use_container_width=True, hide_index=True)

    st.markdown("**Contexto regional del mercado**")
    market_context_show = market_context.copy()
    for col in ["Demanda real A14", "Previsión A14", "Pares disponibles", "Pares vendidos", "Brecha oferta-demanda"]:
        market_context_show[col] = market_context_show[col].round(0).astype(int)
    market_context_show["Utilización capacidad"] = market_context_show["Utilización capacidad"].apply(lambda x: f"{x:.1%}" if pd.notna(x) else "-")
    st.dataframe(market_context_show, use_container_width=True, hide_index=True)

st.divider()
with st.expander("Descargas"):
    d1, d2, d3 = st.columns(3)
    d1.download_button(
        "Resumen financiero CSV",
        build_comparison_table(income_df, STATEMENT_ORDER).to_csv(index=False).encode("utf-8-sig"),
        file_name="empresa_c_estado_resultados.csv",
        mime="text/csv",
    )
    d2.download_button(
        "Balance y liquidez CSV",
        pd.concat([build_comparison_table(balance_df, BALANCE_ORDER), build_comparison_table(ratios_df, RATIOS_ORDER)], ignore_index=True)
        .to_csv(index=False)
        .encode("utf-8-sig"),
        file_name="empresa_c_balance_liquidez.csv",
        mime="text/csv",
    )
    d3.download_button(
        "Mercados y no financieros CSV",
        market_attractiveness.to_csv(index=False).encode("utf-8-sig"),
        file_name="empresa_c_mercados.csv",
        mime="text/csv",
    )
