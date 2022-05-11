# onnx-model-encrypt-sample
使用[pyca/cryptography](https://github.com/pyca/cryptography)对ONNX模型进行加密/解密的样例。<br>
※为了方便起见，使用了python脚本执行。<br>
考虑到安全性，我们建议解密的程序使用C++等创建可执行文件。<br>
# Requirement 
* cryptography 36.0.2 or later
* onnxruntime 1.10.0 or later

# Usage
以下是如何运行的示例。运行每个程序后输入任意密码。<br>
实施加密时输出「resnet50-v1-12.dat」(onnx模型加密)<br>
在执行解码时，读取「resnet50-v1-12.dat」。<br>
```bash
python encrypt_sample.py 
Password:
```
```bash
python decrypt_sample.py
Password:
```

# Reference
* [pyca/cryptography](https://github.com/pyca/cryptography)

# Author
高橋かずひと(https://twitter.com/KzhtTkhs)
 
# License 
onnx-model-encrypt-sample is under [Apache-2.0 License](LICENSE).