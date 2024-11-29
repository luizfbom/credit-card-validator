import streamlit as st
from services.blob_service import upload_file_to_blob
from services.credit_card_service import detect_credit_card_info

def configure_interface():
    st.title("Upload de Arquivos DIO - Desafio 1 - Azure - Fake Docs")
    upload_file = st.file_uploader("Upload de Arquivos", type=["png", "jpg", "jpeg"])
    if upload_file is not None:
        fileName = upload_file.name
        
        blob_url = upload_file_to_blob(upload_file, fileName)
        if blob_url is not None:
            st.success(f"Arquivo {fileName} enviado com sucesso!")
            credit_card_info = detect_credit_card_info(blob_url)
            show_image_and_validation(blob_url, credit_card_info)
        else:
            st.error("Erro ao enviar arquivo!")

def show_image_and_validation(blob_url, credit_card_info):
    st.image(blob_url, caption="Arquivo enviado", use_container_width=True)
    st.subheader("Informações do Cartão de Crédito")
    if credit_card_info and credit_card_info["CardNumber"]:
        st.markdown("<h1 style='text-align: center;color: green;'>Cartão de Crédito Válido</h1>", unsafe_allow_html=True)
        st.write(f"Nome do Cliente: {credit_card_info['CardHolderName']}")
        st.write(f"Número do Cartão: {credit_card_info['CardNumber']}")
        st.write(f"Data de Validade: {credit_card_info['ExpirationDate']}")
        st.write(f"Emissor: {credit_card_info['IssuingBank']}")
        st.write(f"Bandeira: {credit_card_info['PaymentNetwork']}")

    else:
        st.markdown("<h1 style='text-align: center;color: red;'>Cartão de Crédito Inválido</h1>", unsafe_allow_html=True)
        st.write("Nenhuma informação de cartão de crédito encontrada.")

def get_credit_card_info(blob_url):
    teste = "teste"
    return teste

if __name__ == "__main__":
    configure_interface()