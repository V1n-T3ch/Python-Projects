import hashlib

message=input("Enter message to Encrpyt:")

Enc_Message=hashlib.sha256(message.encode()).hexdigest()

print("Encrypted Message is\n",Enc_Message)
