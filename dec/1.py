# Encoding base64 in Python

import base64
import pwinput

def encode_text(encode):

    input_bytes = encode.encode("ascii")
    base64_bytes = base64.b64encode(input_bytes)
    base64_message = base64_bytes.decode('ascii')

    print(f"Your text in base64 is: {base64_message}")
    return base64_message

def decode_text(decode):

    base64_message = decode
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')

    print(f"Your text was: {message}")

if __name__=='__main__':
    text_to_encode = pwinput.pwinput(prompt='Put your text to encode: ', mask='*')
    
    to_decode = encode_text(encode=text_to_encode)
    
    decode_text(decode=to_decode)
