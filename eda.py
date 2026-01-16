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
    model_tienda_options = ["All"] + list(df_sidebar["Tienda"].unique())
    model_tienda = st.sidebar.multiselect(label   = "Select Tienda:",
                                      options = model_tienda_options,
                                      default= ["All"])
    

    if "All" in model_tienda:
        df_sidebar = df_sidebar  # Si "All" está seleccionado, mostrar todos los datos
    else:
        df_sidebar = df_sidebar[df_sidebar["Tienda"].isin(model_tienda)]


    ### Platform
    platform_options = ["All"] + list(df_sidebar["año"].unique())
    platform_type = st.sidebar.multiselect(label   = "Select año:",
                                         options =  platform_options,
                                         default = ["All"])
    
    if "All" in platform_type:
        df_sidebar = df_sidebar  # Si "All" está seleccionado, mostrar todos los datos
    else:
        df_sidebar = df_sidebar[df_sidebar["año"].isin(platform_type)]

    

     # fig1

    productos_por_tienda = df_sidebar.groupby('Tienda')['Productos'].sum().reset_index()
    productos_por_tienda_año = df_sidebar.groupby(['Tienda', 'año'])['Productos'].sum().reset_index()
    ingreso_por_tienda = df_sidebar.groupby('Tienda')['Ingreso'].sum().reset_index()
    ingreso_por_tienda_año = df_sidebar.groupby(['Tienda', 'año'])['Ingreso'].sum().reset_index() 
    fig1 = px.bar(productos_por_tienda, x='Tienda', y='Productos', color= 'Tienda', title='Suma de productos vendidos por tienda')
    fig1.update_layout(width=1200, height=600)

    # fig2

    fig2 = px.bar(productos_por_tienda_año, x='Tienda', y='Productos', color='año', title='Suma de productos vendidos por tienda y año')
    fig2.update_layout(width=1200, height=600)

    # fig3

    fig3 = px.bar(ingreso_por_tienda, x='Tienda', y='Ingreso', color= 'Tienda', title='Suma de ingresos por tienda')
    fig3.update_layout(width=1200, height=600)
    
    # fig4

    fig4 = px.bar(ingreso_por_tienda_año, x='Tienda', y='Ingreso', color='año', title='Suma de ingresos por tienda y año')
    fig4.update_layout(width=1200, height=600)

    # fig5

    fig5 = px.histogram(data_frame = df_sidebar,
             x          = "dia",
             y  = "Productos",
            color = 'Tienda',
            title='Suma de productos vendidos por dia de la semana')
    fig5.update_layout(width=1200, height=600)

    # fig6

    fig6 = px.histogram(data_frame = df_sidebar,
             x          = "dia",
             y = "Productos",
             facet_col      = "año",
             color ='Tienda',
             nbins      = 50,
             title='Suma de productos vendidos por dia de la semana cada año')
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