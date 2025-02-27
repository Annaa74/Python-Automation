import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import io

def scrape_website(url, target_tags, attributes):
    """Scrapes data from a website based on provided tags and attributes."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        soup = BeautifulSoup(response.content, 'html.parser')
        data = []
        for tag, attr in zip(target_tags, attributes):
            elements = soup.find_all(tag, attr)
            data.extend([element.text.strip() for element in elements]) #extract text and remove leading/trailing spaces
        return data
    except requests.exceptions.RequestException as e:
        st.error(f"Error during scraping: {e}")
        return None
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
        return None



def main():
    st.title("Web Scraping Application")

    url = st.text_input("Enter the website URL:")
    target_tags_input = st.text_input("Enter target HTML tags (comma-separated, e.g., h1, p, a):")
    attributes_input = st.text_input("Enter attributes (JSON format, comma-separated, e.g., {'class': 'title'}, {'id': 'content'}):")

    if st.button("Scrape"):
        if url and target_tags_input and attributes_input:
            try:
                target_tags = [tag.strip() for tag in target_tags_input.split(",")]
                attributes = [eval(attr.strip()) for attr in attributes_input.split(",")] #eval is used to parse the JSON
                if len(target_tags) != len(attributes):
                    st.error("Number of tags and attributes must match.")
                    return

                scraped_data = scrape_website(url, target_tags, attributes)

                if scraped_data:
                    df = pd.DataFrame({"General Entries": scraped_data})
                    st.dataframe(df)

                    csv_buffer = io.StringIO()
                    df.to_csv(csv_buffer, index=False)
                    csv_data = csv_buffer.getvalue()

                    st.download_button(
                        label="Download CSV",
                        data=csv_data,
                        file_name="scraped_data.csv",
                        mime="text/csv",
                    )
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter the URL, tags, and attributes.")

if __name__ == "__main__":
    main()