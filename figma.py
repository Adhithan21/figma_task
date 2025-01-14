import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# Sidebar with styled header
st.sidebar.header(":blue[Menu]")
menu = st.sidebar.radio(
    "Navigate",  # This adds a title for the radio buttons
    ["Home", "Top Recipes", "Brand Shoes", "About Us"],  # Options for the menu
    index=0
)

# Main Content
if menu == "Home":
    st.title(":red[Get Everything]")
    st.subheader(":gray[We'll give you the best.]")
    
    # Top Recipes Section
    st.markdown("## Top Recipes")
    cols = st.columns(3)

    with cols[0]:
        st.image("https://github.com/Adhithan21/figma_task/blob/main/images/food.png.png", caption="Food Types")
    with cols[1]:
        st.markdown("## Top Brands")
        st.image(r"https://github.com/Adhithan21/figma_task/blob/main/images/brand.png.png", caption="Brand Shoes")
    with cols[2]:
        st.markdown("## Top Stores")
        st.image(r"https://github.com/Adhithan21/figma_task/blob/main/images/stor.png.jpg", caption="Store")
       
    st.markdown("## Get Everything")
    st.text("Explore it...")

elif menu == "Top Recipes":
    st.title(":blue[Top Recipes]")
    st.markdown("Here you can find all your favorite recipes!")
    st.image(r"images/shoes.png", caption="Brand Shoes")

elif menu == "Brand Shoes":
    st.title(":green[Brand Shoes]")
    st.markdown("Discover the latest trending shoes!")
    st.image(r"images/store.png", caption="Store")

elif menu == "About Us":
    st.title(":red[About Us]")
    st.markdown("We are dedicated to giving you the best experience!")
