from rotor import rotor
from des import DES

#Plain text to be encrypted and decrypted
TEST_MESSAGES = [
    "HOW ARE YOU",
    "HAPPY NEW YEAR",
    "WELCOME TO PUERTO RICO",
]

#Seeds for the rotor and DES key
ROTOR_SEED = 42
DES_KEY = "20262027" 

#Function that calls the encryption and decryption pipeline for a given message
def encrypt(message, rotor_machine, des_cipher):
    
    rotor_ct = rotor_machine.encrypt(message)
    des_ct_bytes = des_cipher.encrypt(rotor_ct)
    des_ct_hex = des_ct_bytes.hex().upper()
    print(f"PT: {message}")
    print(f"Rotor CT: {rotor_ct}")
    print(f"DES CT:   {des_ct_hex}")
    print("----------------------------")

    print("Testing decryption...")
    des_decrypted_bytes = des_cipher.decrypt(des_ct_bytes)
    des_decrypted_text = des_decrypted_bytes.decode()
    rotor_pt = rotor_machine.decrypt(des_decrypted_text)
    if rotor_pt != message:
        print("Decryption mismatch!")
    else:
        print("Decryption successful!")
    print(f"DES Decrypted: {des_decrypted_text}")
    print(f"Rotor Decrypted: {rotor_pt}")
    print("=============================")

if __name__ == "__main__":
    r = rotor(randSeed=ROTOR_SEED)
    d = DES(DES_KEY)

    for msg in TEST_MESSAGES:
        encrypt(msg, r, d)