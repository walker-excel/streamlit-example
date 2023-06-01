import requests
import streamlit as st

# Function to make API requests
def make_api_request(url, headers=None):
    response = requests.get(url, headers=headers)
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
    request_url = st.text_input("Enter the request URL")

    # Input orgcode
    orgcode = st.text_input("Enter the orgcode")

    # Button to trigger API request
    if st.button("Fetch Data"):
        if api_key and request_url and orgcode:
            # Set the API key and orgcode in the headers
            headers = {
                "accept": "application/json",
                "apikey": api_key,
                "orgcode": orgcode
            }

            try:
                # Make API request to the provided URL
                response = make_api_request(request_url, headers=headers)
                st.json(response)
            except requests.exceptions.HTTPError as e:
                st.error(f"Error: {e}")
        else:
            st.warning("Please enter your API key, request URL, and orgcode.")

# Run the Streamlit app
if __name__ == "__main__":
    main()
