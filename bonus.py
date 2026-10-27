from task3 import encrypt
from rotor import rotor
from des import DES
#I'm trying a known ciphertext attack
msg = "KNOCK KNOCK"


if __name__ == "__main__":
    r1 = rotor(randSeed=42)
    d1 = DES("20262027")
    
    #brute force against DES:

    MitMd1 = DES("20262027")
    
    capturedCipherText = bytes.fromhex(encrypt(msg,r1,d1))
    # print("\n", capturedCipherText)
    # encoded = capturedCipherText.encode('utf-8')
    # print(encoded)
    # print("\nDecrypted CT", MitMd1.decrypt(capturedCipherText).decode("utf-8"))
    ct = ""
    for attempt in range (20262000, 72000000000000000):
        key = str(attempt).zfill(8)
        MitMd1 = DES(str(key))

        ct = MitMd1.decrypt(capturedCipherText)
        if(ct == b"LEQML LEQML"):
            print(f"GOT IT. CT: {MitMd1.decrypt(capturedCipherText)}")
            break
        # print(attempt)
    strCT = ct.decode("UTF-8")
    print(f"obtained pt: {r1.decrypt(strCT)} vs actual pt: {msg}") 
