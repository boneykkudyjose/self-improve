import streamlit as st
import os
import random

# Function to get all text files from the directory
def get_all_text_files(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

# Function to read the content of a text file and extract the title
def read_text_file(file_path):
    print(file_path)
    with open(file_path, 'r') as file:
        lines = file.readlines()
    # Assuming the first line is the title, prefixed by "Title: "
    title = lines[0].strip().replace("Title: ", "")
    content = ''.join(lines[1:]).strip()  # Join the rest of the lines as the content
    return title, content

# Function to generate random pastel gradient colors
def get_random_gradient():
    gradients = [
        "linear-gradient(135deg, #FFDEE9, #B5FFFC)",
        "linear-gradient(135deg, #FF9A9E, #FAD0C4)",
        "linear-gradient(135deg, #FBC2EB, #A6C1EE)",
        "linear-gradient(135deg, #A1C4FD, #C2E9FB)",
        "linear-gradient(135deg, #FCE38A, #F38181)",
        "linear-gradient(135deg, #FFB199, #FF0844)",
        "linear-gradient(135deg, #FDEB71, #F8D800)",
        "linear-gradient(135deg, #FAACA8, #DDD6F3)",
        "linear-gradient(135deg, #FFF1EB, #ACE0F9)",
        "linear-gradient(135deg, #A1FFCE, #FAFFD1)"
    ]
    return random.choice(gradients)

# Custom CSS for enhanced styling
st.markdown("""
    <style>
    body {
        font-family: 'Arial', sans-serif;
        background-color: #f4f4f9;
        color: #333;
    }
    .title-box {
        color: #ffffff;
        padding: 15px;
        border-radius: 8px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        cursor: pointer;
        font-size: 1.2em;
        text-align: center;
        font-weight: bold;
        height: 150px;
        display: flex;
        justify-content: center;
        align-items: center;
        word-wrap: break-word;
        margin-bottom: 20px;
    }
    .title-box:hover {
        box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.2);
    }
    .content-box {
        background-color: white;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.1);
        margin-top: 20px;
    }
    .content-box p {
        font-size: 1.2em;
        line-height: 1.6;
        color: #555;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 8px;
        font-size: 1.2em;
        cursor: pointer;
        margin-top: 20px;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
    </style>
""", unsafe_allow_html=True)

# Streamlit app
def main():

    # Directory containing the text files
    text_directory = "responses"

    # Get all text files
    files = get_all_text_files(text_directory)

    # If a file is selected, show its content
    if 'selected_file' in st.session_state:
        title, content = read_text_file(os.path.join(text_directory, st.session_state.selected_file))
        st.markdown(f"<div class='title-box' style='background: {get_random_gradient()};'>{title}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='content-box'><p>{content}</p></div>", unsafe_allow_html=True)
        if st.button("Back to Titles"):
            del st.session_state.selected_file
    else:
        # Display all titles as clickable boxes in a grid layout with 4 per row
        cols = st.columns(4)
        for i, file in enumerate(files):
            title, _ = read_text_file(os.path.join(text_directory, file))
            gradient = get_random_gradient()
            with cols[i % 4]:
                if st.button(f" ", key=file):
                    st.session_state.selected_file = file
                st.markdown(f"""
                    <div class='title-box' style='background: {gradient};'>
                        {title}
                    </div>
                """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
