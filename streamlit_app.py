import streamlit as st
import requests

API_URL = "https://api.example.com"  # Replace with your API URL

def get_field_names():
    url = f"{API_URL}/openapi.json"
    response = requests.get(url)
    if response.status_code == 200:
        api_spec = response.json()
        field_names = []
        for path in api_spec["paths"]:
            for method in api_spec["paths"][path]:
                parameters = api_spec["paths"][path][method].get("parameters", [])
                for parameter in parameters:
                    name = parameter["name"]
                    field_names.append(name)
        return field_names
    else:
        st.error("Failed to retrieve API specifications")

def main():
    st.title("Field Names Viewer")

    field_names = get_field_names()
    if field_names:
        st.header("Field Names")
        for i, field in enumerate(field_names[:10], 1):
            st.write(f"{i}. {field}")
    else:
        st.error("Field names could not be retrieved")

if __name__ == "__main__":
    main()
