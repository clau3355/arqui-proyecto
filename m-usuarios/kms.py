import os
from google.cloud import kms
import base64

serviceAccount = r'fastdeliveryproject-e62677747c15.json'
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = serviceAccount

def crc32c(data):
    import crcmod
    import six
    crc32c_fun = crcmod.predefined.mkPredefinedCrcFun('crc-32c')
    return crc32c_fun(six.ensure_binary(data))

kms_client = kms.KeyManagementServiceClient()
key_name = kms_client.crypto_key_path(
                'fastdeliveryproject', "us-central1", "keyring-delivery", "contrasena")

def encriptar(txt):
    plaintext_bytes = txt.encode('utf-8')
    # Recomendación usar CRC32C para la verificación de la integración de los datos.
    plaintext_crc32c = crc32c(plaintext_bytes)

    encrypt_response = kms_client.encrypt(
                    request={'name': key_name, 'plaintext': plaintext_bytes, "plaintext_crc32c": plaintext_crc32c})

    if not encrypt_response.verified_plaintext_crc32c:
        raise Exception(
            'The request sent to the server was corrupted in-transit.')

    if not encrypt_response.ciphertext_crc32c == crc32c(encrypt_response.ciphertext):
        raise Exception(
            'The response received from the server was corrupted in-transit.')

    print(encrypt_response.ciphertext)
    text_encriptado = base64.b64encode(encrypt_response.ciphertext).decode()
    print(text_encriptado)
    return text_encriptado

def desencriptar(txt):
    plaintext_bytes = txt.encode('utf-8')
    # Recomendación usar CRC32C para la verificación de la integración de los datos.
    plaintext_crc32c = crc32c(plaintext_bytes)

    encrypt_response = kms_client.encrypt(
                    request={'name': key_name, 'plaintext': plaintext_bytes, "plaintext_crc32c": plaintext_crc32c})

    if not encrypt_response.verified_plaintext_crc32c:
        raise Exception(
            'The request sent to the server was corrupted in-transit.')

    if not encrypt_response.ciphertext_crc32c == crc32c(encrypt_response.ciphertext):
        raise Exception(
            'The response received from the server was corrupted in-transit.')
    
    # plaintext_bytes = text_encriptado.encode('utf-8')

    decrypt_response = kms_client.decrypt(
        request={'name': key_name, 'ciphertext': encrypt_response.ciphertext, "ciphertext_crc32c": encrypt_response.ciphertext_crc32c}
    )

    if not decrypt_response.plaintext_crc32c == crc32c(decrypt_response.plaintext):
            raise Exception('The response received from the server was corrupted in-transit.')
        
    print(decrypt_response.plaintext)

    return decrypt_response.plaintext
