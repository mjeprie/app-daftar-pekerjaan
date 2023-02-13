import functions
import streamlit as st

list_pekerjaan = functions.get_pekerjaan()
def tambah_pekerjaan():
    pekerjaan_baru = st.session_state['pekerjaan_baru']
    pekerjaan_baru = pekerjaan_baru.capitalize()
    list_pekerjaan.append(pekerjaan_baru + '\n')
    functions.tulis_pekerjaan(list_pekerjaan)

st.title("Daftar Pekerjaan")
st.subheader("Aplikasi pekerjaan")
st.write("Digunakan untuk mengatur daftar pekerjaan")

for pekerjaan in list_pekerjaan:
    st.checkbox(pekerjaan)

st.text_input(label="", placeholder="Tambah pekerjaan baru",
              on_change=tambah_pekerjaan, key='pekerjaan_baru')
st.button(label='Tambah', key='tambah', on_click=tambah_pekerjaan)
st.button(label='Hapus', key='hapus')

st.session_state