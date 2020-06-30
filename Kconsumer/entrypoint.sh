#!/bin/sh

echo "$CA" > /tmp/ca.crt
echo "$CERT" > /tmp/user-cert.crt
echo "$KEY" > /tmp/key.pem

cat /tmp/ca.crt
cat /tmp/user-cert.crt
cat /tmp/key.pem

exec python3 consumer.py