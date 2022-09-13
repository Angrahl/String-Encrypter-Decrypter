PY = python3

all:
	$(PY) src/encryption.py
	$(PY) src/decryption.py

encrypt:
	$(PY) src/encryption.py

decrypt:
	$(PY) src/decryption.py

clean:
	$(RM) encryption_key.key encrypted_msg.txt
	rm -rf src/__pycache__