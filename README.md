# CrumbShare

CrumbShare is a Python-based application designed to provide secure, end-to-end encrypted file sharing over a network. It includes file encryption, secure peer-to-peer (P2P) connections, and a user-friendly command-line interface.

## Features
- File encryption using AES
- Secure P2P connections using WebRTC
- Simple authentication using public/private key pairs
- User-friendly command-line interface (CLI)
- Cross-platform compatibility (Windows, macOS, Linux)

```
CrumbShare
│
├── encrypt_decrypt.py   # Module for file encryption and decryption
├── p2p_connection.py    # Module for establishing P2P connections
├── auth.py              # Module for user authentication
├── cli.py               # Command-line interface implementation
├── requirements.txt     # List of dependencies
└── README.md            # Project documentation
```

## Installation
1. Clone the repository:
```
   git clone https://github.com/Cr0mb/CrumbShare.git
   cd CrumbShare
```
2. Install Dependencies
```
   pip install -r requirements.txt
```

## Usage

Encrypt a file
```
python cli.py encrypt --file mydocument.txt --output encrypted_document.txt --password yourpassword
```

Decrypt a file
```
python cli.py decrypt --file encrypted_document.txt --output mydocument.txt --password yourpassword
```

Share a file securely
```
python cli.py share --file encrypted_document.txt --peer ws://peer_address
```

Receive a file securely
```
python cli.py receive --peer ws://peer_address --output received_document.txt
```

