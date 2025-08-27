import boto3
from datetime import datetime

# Configura DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('WebhookEvents')

# Datos de prueba
item = {
    'eventId': 'evt12345',  # Clave primaria, única
    'timestamp': int(datetime.utcnow().timestamp()),  # Clave de ordenación
    'productId': 12345,
    'eventType': 'product/updated',
    'storeHash': 'hp1ltb9vhs'
}

# Insertar en la tabla
try:
    table.put_item(Item=item)
    print("✅ Item insertado correctamente")
except Exception as e:
    print("❌ Error insertando item:", e)
