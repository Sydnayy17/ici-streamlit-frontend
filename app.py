import streamlit as st
import requests

st.title("🔍 ICI Professor Finder")

query = st.text_input("Enter a research topic:")
if st.button("Search") and query:
    url = f"https://ici-fastapi-backend.onrender.com//search?keyword={query}"  # ← Replace this with your actual API URL
    res = requests.get(url)
    if res.ok:
        results = res.json()
        for prof in results:
            st.subheader(prof['name'])
            st.image(prof['image_url'], width=200)
            st.write(f"🎓 Education: {prof['education']}")
            st.write(f"📚 Research Area: {prof['research_area']}")
    else:
        st.error("Failed to get results.")
