import random #use to generate
import math#use gcd


def is_prime(number): #checking to see if a number is prime
    if number < 2:
        return False
    for i in range(2, number // 2 + 1):#range between 2 and the half the number plus 1, iterating through those numbers
        if number % i == 0:#if mod of number / i is 0 then return false becasue it is not prime
            return False
    return True


def generate_prime(min_value, max_value):#generating a prime number
    prime = random.randint(min_value, max_value)#generating a random number between and including the min and max number
    while not is_prime(prime):#if is_prime returned False then generate a new prime number then return the prime number
        prime = random.randint(min_value, max_value)
    return prime

def mod_inverse(e, phi):# find d with this function 
    for d in range(3, phi):#iterating between 3 and phi
        if(d * e) % phi == 1:#if (d*e) / phi gives a remainder of 1 then we found d
            return d
    raise ValueError("mod_inverse does not exist")# raise error for invalid number

p, q = generate_prime(1000, 5000), generate_prime(1000, 5000)#generating prime numbers with min and max range

while p == q:#incase the numbers are generated the same
    q = generate_prime(1000, 5000)

#calculating n and phi
n = p*q
phi_n = (p-1) * (q-1)

e = random.randint(3, phi_n-1)#generating an e with range
while math.gcd(e, phi_n) != 1:#as long as they are not co prime then generate another e
    e = random.randint(3, phi_n-1)

d = mod_inverse(e, phi_n)#generate the private key

#printing the values
print("Public Key: ", e)
print("Private Key: ", d)
print("n: ", n)
print("Phi of n:", phi_n)
print("p: ", p)
print("q: ", q)


message = "Hello World"

message_encode = [ord(ch) for ch in message]#creating a list and turning every character in the message into its ordinal character
# (m ^ e) mod n = c
ciphertext = [pow(ch, e, n) for ch in message_encode]#pow(ch, e, n) == ch^e mod n iterating through every character in the encoded message

#opening and closing a file to print the cipher text
ciphertext_file = open('ciphertext_file', 'w')
ciphertext_file.write(str(ciphertext))
ciphertext_file.close

#decrypting
message_encode = [pow(ch, d, n) for ch in ciphertext]#ch^d mod n for each number in the ciphertext, turning each ordnial into its character

message = ''.join(chr(ch) for ch in message_encode)#join takes all characters from the decryption and puts thems into a string, chr() function gets the unicode from the charcater and prints the character
print("Message:", message)