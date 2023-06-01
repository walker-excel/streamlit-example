import requests
import json
import streamlit as st

# Function to make API requests
def make_api_request(url, headers=None, data=None):
    response = requests.post(url, headers=headers, json=data)
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

    # Input orgcode
    orgcode = st.text_input("Enter the orgcode")

    # Button to trigger API request
    if st.button("Fetch Data"):
        if api_key and orgcode:
            # Set the API key and orgcode in the headers
            headers = {
                "accept": "application/json",
                "apikey": api_key,
                "orgcode": orgcode
            }

            #headers_data= json.dumps(headers)

            # Prepare the request data
            request_data = {
            "pageNumber": 1,
            "pageSize": 10,
            "includeInactive": True,
            "sortParameters": [{"fieldName": "string", "isAscending": True}],
            "filterParameters": [{"fieldName": "string", "fieldValue": "string", "isLikeSearch": True}]
            }

            # Convert request_data to JSON
            data = json.dumps(request_data)

            try:
                # Make API request to the provided URL
                response = make_api_request("https://restapina.ticketsearch.com/venue/api/v1/venues", headers=headers, data=data)
                
                # Display the response data
                st.subheader("Response Data")
                st.json(response)
                
            except requests.exceptions.HTTPError as e:
                st.error(f"Error: {e}")
                st.write(orgcode)
                st.write(api_key)
                st.write(headers)
        else:
            st.warning("Please enter your API key and orgcode.")

# Run the Streamlit app
if __name__ == "__main__":
    main()
