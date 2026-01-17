import streamlit as st
import plotly.express as px
from Module.aplication import *
from eda import eda_app
from PIL import Image
 
def main():
    st.set_page_config(**PAGE_CONFIG)
   
    menu = ["Inicio", "Gastos BBVA"]

    choice = st.sidebar.selectbox(label = "Menu", options = menu, index = 0)
 
    if choice == "Inicio":
        
        
        st.header(body = "GASTOS  CUENTA BBVA CONJUNTA")

        st.subheader("DESGLOSE GASTOS CUENTA BANCO BBVA")

        image = Image.open("Source/Colorful Modern Line Chart Diagram Graph.png")
        st.image(image           = image, 
                 width=500)
        

    elif choice == "Exploratory Data Analysis":
        eda_app()



if __name__ == "__main__":
    main()

