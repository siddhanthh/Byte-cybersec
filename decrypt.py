#program to decrypt the flag
import base64

def decrypt_input(encrypted_str):
    # Reversing XOR operation with key 9
    def xor_with_key(hex_input, key):
        xored = ""
        for i in range(0, len(hex_input), 2):
            hex_char = int(hex_input[i:i+2], 16)
            hex_char ^= key
            xored += chr(hex_char)
        return xored

    #Converting hex to string
    def from_hex(hex_str):
        bytes_object = bytes.fromhex(hex_str)
        return bytes_object.decode()

    #Reverse character shifting by 25 positions
    def reverse_shift(input_str, amount):
        result = ""
        for c in input_str:
            if c.isalpha():
                base = 'A' if c.isupper() else 'a'
                offset = (ord(c) - ord(base) - amount) % 26
                if offset < 0:
                    offset += 26
                c = chr(ord(base) + offset)
            result += c
        return result

    def reverse_str(input_str):
        return input_str[::-1]

    def from_base64(input_str):
        return base64.b64decode(input_str).decode()

    # Known encrypted flag jo dusre code se uthaya hai
    known_encrypted_flag = "34395e5039624e476c6e4f6a7e6b3a5e705c5f45714c4f507d5c3a683d3138507e3d5f7339624f457b484e6d707b3a506e7e6558"
    # Calling the functions on the known encrypted flag
    # Reverse XOR operation
    xored = xor_with_key(known_encrypted_flag, 9)
    print("After XOR:", xored)

    # Convert hex to string
    hex_str = ''.join(f'{ord(c):02x}' for c in xored)
    original_str = from_hex(hex_str)
    print("After hex conversion:", original_str)

    # Reverse character shifting
    shifted_str = reverse_shift(original_str, 25)
    print("After reversing shift:", shifted_str)

    # Reverse the string
    reversed_str = reverse_str(shifted_str)
    print("After reversing:", reversed_str)

    # Base64 decoding
    original_input = from_base64(reversed_str)
    print("Original input:", original_input)

    return original_input

# Run the decryption process
original_input = decrypt_input("34395e5039624e476c6e4f6a7e6b3a5e705c5f45714c4f507d5c3a683d3138507e3d5f7339624f457b484e6d707b3a506e7e6558")
print("The original input is:", original_input)
