# Backend URL
BACKEND_URL = "https://backend-service.onrender.com/ask"  # Update with actual Render backend URL

st.title("🔍 AI-Powered ICI Professor Finder")

# Input question
question = st.text_input("Enter your research topic:")

if st.button("Submit"):
    if question.strip():
        with st.spinner("Getting your answer..."):
            try:
                response = requests.post(BACKEND_URL, json={"question": question})
                if response.status_code == 200:
                    data = response.json()
                    st.success("Answer:")
                    st.write(data.get("answer", "No answer found."))
                else:
                    st.error(f"Error: {response.status_code}")
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a question.")
