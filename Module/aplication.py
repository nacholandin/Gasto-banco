import streamlit as st
import numpy as np
import pandas as pd


PAGE_CONFIG = {"page_title"             : "Gastos BBVA - Streamlit",  
                 "layout"                : "wide"}

def read_eda():
     df = pd.read_csv("source/bbva.csv")
     return df