import streamlit as st
import os

def read_markdown_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def display_folder_contents(folder_path):
    items = os.listdir(folder_path)
    for item in items:
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path):
            if st.button(f'📂 {item}', key=item_path):
                st.session_state['current_path'] = item_path
        elif item.endswith('.md'):
            if st.button(f'📄 {item}', key=item_path):
                st.session_state['selected_file'] = item_path

def main():
    st.title('Thư viện kiến thức lập trình')
    
    if 'current_path' not in st.session_state:
        st.session_state['current_path'] = '.'
    
    if 'selected_file' in st.session_state:
        st.sidebar.button('Back to Folder', on_click=lambda: st.session_state.pop('selected_file'))
        content = read_markdown_file(st.session_state['selected_file'])
        st.markdown(content)
    else:
        st.sidebar.button('Back to Root', on_click=lambda: st.session_state.update({'current_path': '.'}))
        display_folder_contents(st.session_state['current_path'])

if __name__ == '__main__':
    main()
