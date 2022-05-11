import base64

import onnxruntime
from cryptography.fernet import Fernet
from cryptography.fernet import InvalidToken
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def decrypt(
    encrypt_data,
    password_text,
    salt=b'salt',
    stretching_iterations=390000,
):
    # 用于盐值和拉伸迭代次数，进行实例化
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=stretching_iterations,
    )

    # 生成密钥
    password = password_text.encode("utf-8")
    key = base64.urlsafe_b64encode(kdf.derive(password))

    # 使用指定密钥生成 Fernet对象
    fernet = Fernet(key)

    # 加密
    decrypt_data = None
    try:
        decrypt_data = fernet.decrypt(encrypt_data)
    except InvalidToken:
        print('Invalid Password')

    return decrypt_data


def main():
    # 读取加密数据
    with open('resnet50-v1-12.dat', 'rb') as f:
        encryp_data = f.read()

    # 输入密码
    password_text = input('Password:')

    # 解密
    decrypt_data = decrypt(encryp_data, password_text)

    # 确认读取解密的 ONNX 模型
    if decrypt_data is not None:
        onnx_session = onnxruntime.InferenceSession(
            decrypt_data,
            providers=['CPUExecutionProvider'],
        )
        print(onnx_session.get_inputs()[0])
        print(onnx_session.get_outputs()[0])


if __name__ == '__main__':
    main()
