import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from module.aplication import *

def eda_app():

    st.subheader(body = "Gastos BBVA")

    st.write("Analisis detallado de la cuenta del BBVA .")

    st.sidebar.markdown("*"*10)
    
    st.sidebar.markdown("Selecciona para analizar por categoria o periodo.")

    df = read_eda()


    # SIDEBAR
    df_sidebar = df.copy()

    ### Model Type
    model_categoria_options = ["Todos"] + list(df_sidebar["Gasto"].unique())
    model_categoria = st.sidebar.multiselect(label   = "Selecciona categoria:",
                                      options = model_categoria_options,
                                      default= ["Todos"])
    

    if "Todos" in model_categoria:
        df_sidebar = df_sidebar  # Si "All" está seleccionado, mostrar todos los datos
    else:
        df_sidebar = df_sidebar[df_sidebar["Gasto"].isin(model_categoria)]

         ### Año
    año_options = ["Todos"] + list(df_sidebar["año"].unique())
    año_type = st.sidebar.multiselect(label   = "Selecciona año:",
                                         options =  año_options,
                                         default = ["Todos"])
    
    if "Todos" in año_type:
        df_sidebar = df_sidebar  # Si "All" está seleccionado, mostrar todos los datos
    else:
        df_sidebar = df_sidebar[df_sidebar["año"].isin(año_type)]


    ### Mes
    mes_options = ["Todos"] + list(df_sidebar["mes"].unique())
    mes_type = st.sidebar.multiselect(label   = "Selecciona mes:",
                                         options =  mes_options,
                                         default = ["Todos"])
    
    if "Todos" in mes_type:
        df_sidebar = df_sidebar  # Si "All" está seleccionado, mostrar todos los datos
    else:
        df_sidebar = df_sidebar[df_sidebar["mes"].isin(mes_type)]


     # fig1

    ingresos = df_sidebar.loc[df_sidebar['Gasto'] == "Ingreso", 'Importe'].sum()
    categorias_gastos = ["Hogar", "Niñas", "Coche", "Varios"]
    gastos = df_sidebar.loc[df_sidebar['Gasto'].isin(categorias_gastos), 'Importe'].sum()
    resumen = pd.DataFrame({'Tipo': ['Ingresos', 'Gastos'],'Importe': [ingresos, gastos]})

    fig1 = px.bar(resumen,x='Tipo',y='Importe',color="Tipo",title='Ingresos vs Gastos')
    fig1.update_layout(width=1200, height=600)

    # fig2

    df_gasto = (df_sidebar.groupby("Gasto", as_index=False)["Importe"].sum())

    fig2 = px.bar(df_gasto,x="Gasto",y="Importe",color="Gasto",title="Gasto total por categoría")
    fig2.update_layout(width=1200, height=600)

    # fig3

    df_hogar = (df_sidebar[df_sidebar["Gasto"] == "Hogar"].groupby("Categoria", as_index=False)["Importe"].sum())

    fig3 = px.bar(df_hogar,x="Categoria",y="Importe",color="Categoria",title="Gasto Hogar por Categoría")
    fig3.update_layout(width=1200, height=600)
    
    # fig4

    df_niñas = (df_sidebar[df_sidebar["Gasto"] == "Niñas"].groupby("Categoria", as_index=False)["Importe"].sum())
    fig4 = px.bar(df_niñas,x="Categoria",y="Importe",color="Categoria",title="Gasto Niñas por Categoría")
    fig4.update_layout(width=1200, height=600)

    # fig5

    df_coche = (df_sidebar[df_sidebar["Gasto"] == "Coche"].groupby("Categoria", as_index=False)["Importe"].sum())
    fig5 = px.bar(df_coche,x="Categoria",y="Importe",color="Categoria",title="Gasto coche por Categoría")
    fig5.update_layout(width=1200, height=600)

    # fig6

    df_varios = (df_sidebar[df_sidebar["Gasto"] == "Varios"].groupby("Categoria", as_index=False)["Importe"].sum())
    fig6 = px.bar(df_varios,x="Categoria",y="Importe",color="Categoria",title="Gasto coche por Categoría")
    fig6.update_layout(width=1200, height=600)

    # fig7

    fig7 = px.histogram(data_frame = df_sidebar,
             x          = "mes",
             y = "Productos",
             facet_col      = "año",
             color ='Tienda',
             nbins      = 50,
             title='Suma de productos vendidos por mes')
    fig7.update_layout(width=1000, height=700)

    #fig8

    productos_por_tiendas = df_sidebar.groupby(['Tienda', 'año'])['Productos'].sum().reset_index()
    fig8 = px.line(
    productos_por_tiendas,
    x='año',
    y='Productos',
    color='Tienda',
    title='Ventas de Productos por Tienda a lo largo de los años',
    markers=True
    )

    #fig9

    productos_por_año = df_sidebar.groupby('año')['Productos'].sum().reset_index()
    fig9 = px.line(productos_por_año, x='año', y='Productos', title='Tendencia ventas por año')

    # Plots

    st.plotly_chart(figure_or_data = fig1, use_container_width = True)
    st.plotly_chart(figure_or_data = fig2, use_container_width = True)
    st.plotly_chart(figure_or_data = fig3, use_container_width = True)
    st.plotly_chart(figure_or_data = fig4, use_container_width = True)
    st.plotly_chart(figure_or_data = fig5, use_container_width = True)
    st.plotly_chart(figure_or_data = fig6, use_container_width = True)
    st.plotly_chart(figure_or_data = fig7, use_container_width = True)
    st.plotly_chart(figure_or_data = fig8, use_container_width = True)
    st.plotly_chart(figure_or_data = fig9, use_container_width = True)

    

if __name__ == "__eda_app__":
    eda_app()