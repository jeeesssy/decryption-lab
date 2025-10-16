# Decryption Lab
A simple decryption lab using Caesar cipher and AES-256-CBC encryption.

#  Overview
This lab demonstrates how to decrypt an encrypted file step by step using basic Linux commands, Caesar cipher decoding, and OpenSSL AES-256-CBC decryption.

#  Steps I Completed
```bash
# 1 Explore the Home Directory
ls
# Output:
# Q1.encrypted  README.txt  caesar/

# 2 Read the Instructions
cat README.txt
# Output:
# Your data has been encrypted. To recover your data, you need to solve a cipher
# for a hidden file in the caesar subdirectory.

# 3 Find and Decode the Hidden File
cd caesar
ls -a
cat .leftShift3 | tr 'd-za-cD-ZA-C' 'a-zA-Z'
# Decoded message:
# To recover your files you will need to enter the following command:
# openssl aes-256-cbc -pbkdf2 -a -d -in Q1.encrypted -out Q1.recovered -k ettubrute

# 4 Decrypt the Encrypted File
cd ~
openssl aes-256-cbc -pbkdf2 -a -d -in Q1.encrypted -out Q1.recovered -k ettubrute

# 5 Verify the Result
ls
cat Q1.recovered
