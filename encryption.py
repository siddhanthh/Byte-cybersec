#this code was obtained on https://byte-cybersec-ps.vercel.app/almost_there_hc8z6ov72i
import base64

def encrypt_input(input_str):
    flag = input_str
    flag = to_base64(flag)
    print("After first Base64:", flag)
    flag = reverse_str(flag)
    print("After reversing:", flag)
    flag = shift(flag, 25)
    print("After shifting:", flag)
    flag = to_hex(flag)
    print("After hex conversion:", flag)
    flag = xor_with_key(flag, 9)
    print("After XOR:", flag)
    return flag

def check_flag(encrypted_input):
    known_encrypted_flag = "34395e5039624e476c6e4f6a7e6b3a5e705c5f45714c4f507d5c3a683d3138507e3d5f7339624f457b484e6d707b3a506e7e6558"
    return encrypted_input == known_encrypted_flag

def to_base64(input_str):
    return base64.b64encode(input_str.encode()).decode()

def reverse_str(input_str):
    return input_str[::-1]

def shift(input_str, amount):
    result = ""
    for c in input_str:
        if c.isalpha():
            base = 'A' if c.isupper() else 'a'
            offset = (ord(c) - ord(base) + amount) % 26
            if offset < 0:
                offset += 26
            c = chr(ord(base) + offset)
        result += c
    return result

def to_hex(input_str):
    return ''.join(f'{ord(c):02x}' for c in input_str)

def xor_with_key(hex_input, key):
    xored = ""
    for i in range(0, len(hex_input), 2):
        hex_char = int(hex_input[i:i+2], 16)
        hex_char ^= key
        xored += f'{hex_char:02x}'
    return xored

def main():
    user_input = input("Flag: ")
    encrypted_input = encrypt_input(user_input)
    print("Encrypted input:", encrypted_input)
    if check_flag(encrypted_input):
        print("Correct flag! Congratulations!")
    else:
        print("Incorrect flag! Please try again.")

if __name__ == "__main__":
    main()
