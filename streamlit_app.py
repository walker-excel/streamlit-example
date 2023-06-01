import requests
import streamlit as st

# Define the base URL of the API
base_url = "https://restapina.ticketsearch.com/"

# Function to make API requests
def make_api_request(endpoint, params=None, headers=None):
    url = f"{base_url}/{endpoint}"
    response = requests.get(url, params=params, headers=headers)
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

    # Button to trigger API request
    if st.button("Fetch Data"):
        if api_key:
            # Set the API key in the headers
            headers = {
                "Authorization": f"Bearer {api_key}"
            }

            try:
                # Make API request to the desired endpoint
                response = make_api_request("scanning/swagger/ScanningOpenAPISpecificationv1.0/swagger.json", headers=headers)
                st.json(response)
            except requests.exceptions.HTTPError as e:
                st.error(f"Error: {e}")
        else:
            st.warning("Please enter your API key.")

# Run the Streamlit app
if __name__ == "__main__":
    main()
