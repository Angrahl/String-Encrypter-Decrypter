PY = python3

all:
	$(PY) encryption.py
	$(PY) decryption.py

encrypt:
	$(PY) encryption.py

decrypt:
	$(PY) decryption.py

clean:
	$(RM) encryption_key.key encrypted_msg.txt
	rm -rf __pycache__