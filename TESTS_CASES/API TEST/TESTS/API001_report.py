import pytest
import requests

def test_webhook_trigger():
    # Aquí va tu prueba real, por ejemplo llamar API y validar respuesta
    response = requests.post("https://tu-api-endpoint.com/webhook", json={"id": 118})
    assert response.status_code == 200
