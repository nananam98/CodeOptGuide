import streamlit as st
import os
from display_names import display_names  # Import từ điển tên hiển thị

# Hàm đọc nội dung file markdown
def read_markdown_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Hàm lấy tên hiển thị thân thiện
def get_display_name(name):
    return display_names.get(name, name)

# Hàm hiển thị nội dung thư mục
def display_folder_contents(folder_path, search_query=""):
    items = os.listdir(folder_path)
    for item in items:
        if item in display_names and search_query.lower() in get_display_name(item).lower():
            item_path = os.path.join(folder_path, item)
            if os.path.isdir(item_path):
                if st.button(f'📂 {get_display_name(item)}', key=item_path):
                    st.session_state['current_path'] = item_path
            elif item.endswith('.md'):
                if st.button(f'📄 {get_display_name(item)}', key=item_path):  # Hiển thị tên thân thiện
                    st.session_state['selected_file'] = item_path
                    if 'viewed_files' not in st.session_state:
                        st.session_state['viewed_files'] = []
                    if item_path not in st.session_state['viewed_files']:
                        st.session_state['viewed_files'].append(item_path)

# Hàm chính
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
        
        search_query = st.sidebar.text_input("Tìm kiếm")
        display_folder_contents(st.session_state['current_path'], search_query)

        if 'viewed_files' in st.session_state and st.session_state['viewed_files']:
            st.sidebar.markdown("### Các file đã xem")
            for file_path in st.session_state['viewed_files']:
                if st.sidebar.button(f"📄 {get_display_name(os.path.basename(file_path))}", key=file_path):
                    st.session_state['selected_file'] = file_path

if __name__ == '__main__':
    main()
