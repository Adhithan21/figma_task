import streamlit as st

# Sidebar with styled header
st.sidebar.header(":blue[Menu]")
menu = st.sidebar.radio(
    "Navigate",
    ["Home", "Top Recipes", "Brand Shoes", "About Us"],
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
        st.image("images/food.png.png", caption="Food Types")
    with cols[1]:
        st.markdown("## Top Brands")
        st.image("images/brand.png.png", caption="Brand Shoes")
    with cols[2]:
        st.markdown("## Top Stores")
        st.image("images/stor.png.png", caption="Store")
       
    st.markdown("## Get Everything")
    st.text("Explore it...")

elif menu == "Top Recipes":
    st.title(":blue[Top Recipes]")
    st.markdown("Here you can find all your favorite recipes!")
    st.image("images/food.png.png", caption="Brand Shoes")

elif menu == "Brand Shoes":
    st.title(":green[Brand Shoes]")
    st.markdown("Discover the latest trending shoes!")
    st.image("images/brand.png.png", caption="Store")

elif menu == "About Us":
    st.title(":red[About Us]")
    st.markdown("We are dedicated to giving you the best experience!")
