import base64
def decrypt(base64_message):
    base64_bytes = base64_message.encode('ascii')    
    message_bytes = base64.b64decode(base64_bytes)
    base64_message = message_bytes.decode('ascii')
    print(base64_message)
    return base64_message