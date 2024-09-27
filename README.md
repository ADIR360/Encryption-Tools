# Encryption Tools

### Overview
This repository contains various encryption tools starting with the **Caesar Cipher**. These tools are designed to help understand and apply fundamental cryptography techniques. The project will grow to include more encryption algorithms in the future.

---

## Tools

### 1. Caesar Cipher
The **Caesar Cipher** is a simple substitution cipher where each letter in the plaintext is shifted by a certain number of positions in the alphabet.

#### How It Works:
- **Encryption**: The user inputs a text, and each letter is shifted right by the specified number of positions.
- **Decryption**: The user can shift the encrypted text left by the same number of positions to restore the original message.
  
#### Features:
- Supports both encryption and decryption.
- Input validation ensures that only alphabetic characters are processed.
  
#### Encryption Example:
- Original text: `hello`
- Shift: `3`
- Encrypted text: `khoor`

#### Decryption Example:
- Encrypted text: `khoor`
- Shift: `3`
- Decrypted text: `hello`

---

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/ADIR360/Encryption-Tools.git
    cd Encryption-Tools
    ```

2. Run the Caesar Cipher scripts:
    - **For encryption**:
      ```bash
      python caesar_cipher_encrypt.py
      ```
    - **For decryption**:
      ```bash
      python caesar_cipher_decrypt.py
      ```

---

### Future Plans

This repository will be expanded to include:
- **Vigenère Cipher**
- **AES Encryption**
- Other modern cryptographic techniques.

---

### Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests for new features, improvements, or bug fixes.

1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b new-feature
    ```
3. Commit your changes:
    ```bash
    git commit -m "Add new encryption tool"
    ```
4. Push to the branch:
    ```bash
    git push origin new-feature
    ```
5. Open a Pull Request.

---

### License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.
