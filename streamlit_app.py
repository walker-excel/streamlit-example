import requests
import streamlit as st

# Function to make API requests
def make_api_request(url, api_key, orgcode):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "orgcode": orgcode
    }

    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    return response.json()

# Streamlit app
def main():
    # Set the page title
    st.set_page_config(page_title="API Demo")

    # Display a title and a description
    st.title("API Demo")
    st.markdown("This is a demo of accessing the API using an API key.")

    # Input API key
    api_key = st.text_input("Enter your API key", type="password")

    # Input request URL
    url = st.text_input("Enter the request URL")

    # Input orgcode request body parameter
    orgcode = st.text_input("Enter the orgcode parameter")

    # Button to trigger API request
    if st.button("Fetch Data"):
        if api_key and url and orgcode:
            try:
                # Make API request
                response = make_api_request(url, api_key, orgcode)
                st.json(response)
            except requests.exceptions.HTTPError as e:
                st.error(f"Error: {e}")
        else:
            st.warning("Please enter all the required information.")

# Run the Streamlit app
if __name__ == "__main__":
    main()
