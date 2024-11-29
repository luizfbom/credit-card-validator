from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from utils.config import Config

def detect_credit_card_info(blob_url):

    credential = AzureKeyCredential(Config.SUBSCRIPTION_KEY)
    document_client = DocumentIntelligenceClient(Config.ENDPOINT, credential)
    card_info = document_client.begin_analyze_document("prebuilt-creditCard", AnalyzeDocumentRequest(url_source=blob_url))
    result = card_info.result()

    for document in result.documents:
        fields = document.get('fields', {})

        return {
            "CardHolderName": fields.get("CardHolderName", {}).get("content"),
            "CardNumber": fields.get("CardNumber", {}).get("content"),
            "ExpirationDate": fields.get("ExpirationDate", {}).get("content"),
            "IssuingBank": fields.get("IssuingBank", {}).get("content"),
            "PaymentNetwork": fields.get("PaymentNetwork", {}).get("content"),
        }

