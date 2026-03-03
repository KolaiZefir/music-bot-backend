@echo off
"C:\Program Files\OpenSSL-Win64\bin\openssl.exe" req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes -subj "/CN=localhost"
echo ✅ Сертификаты созданы!
echo - key.pem
echo - cert.pem
pause