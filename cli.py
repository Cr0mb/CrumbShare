import argparse
from encrypt_decrypt.py import FileEncryptor
from p2p_connection import P2PConnection
from auth import Auth
import asyncio

def encrypt(args):
    encryptor = FileEncryptor(args.password)
    encryptor.encrypt_file(args.file, args.output)

def decrypt(args):
    encryptor = FileEncryptor(args.password)
    encryptor.decrypt_file(args.file, args.output)

async def share(args):
    connection = P2PConnection(args.peer)
    await connection.connect()
    await connection.send_file(args.file)
    await connection.close()

async def receive(args):
    connection = P2PConnection(args.peer)
    await connection.connect()
    await connection.receive_file(args.output)
    await connection.close()

def main():
    parser = argparse.ArgumentParser(description='SecureFileShare CLI')
    subparsers = parser.add_subparsers()

    encrypt_parser = subparsers.add_parser('encrypt')
    encrypt_parser.add_argument('--file', required=True, help='File to encrypt')
    encrypt_parser.add_argument('--output', required=True, help='Output file path')
    encrypt_parser.add_argument('--password', required=True, help='Password for encryption')
    encrypt_parser.set_defaults(func=encrypt)

    decrypt_parser = subparsers.add_parser('decrypt')
    decrypt_parser.add_argument('--file', required=True, help='File to decrypt')
    decrypt_parser.add_argument('--output', required=True, help='Output file path')
    decrypt_parser.add_argument('--password', required=True, help='Password for decryption')
    decrypt_parser.set_defaults(func=decrypt)

    share_parser = subparsers.add_parser('share')
    share_parser.add_argument('--file', required=True, help='File to share')
    share_parser.add_argument('--peer', required=True, help='Peer address to share file with')
    share_parser.set_defaults(func=lambda args: asyncio.run(share(args)))

    receive_parser = subparsers.add_parser('receive')
    receive_parser.add_argument('--peer', required=True, help='Peer address to receive file from')
    receive_parser.add_argument('--output', required=True, help='Output file path')
    receive_parser.set_defaults(func=lambda args: asyncio.run(receive(args)))

    args = parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()
