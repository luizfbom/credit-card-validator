import os
from azure.storage.blob import BlobServiceClient
import streamlit as st
from utils.config import Config

def upload_file_to_blob(file, fileName):
    try:
        blob_service_client = BlobServiceClient.from_connection_string(Config.STORAGE_CONNECTION_STRING)
        blob_client = blob_service_client.get_blob_client(container=Config.CONTAINER_NAME, blob=fileName)
        blob_client.upload_blob(file, overwrite=True)
        return blob_client.url
    except Exception as e:
        st.error(f"Erro ao enviar arquivo: {str(e)}")
        return None
