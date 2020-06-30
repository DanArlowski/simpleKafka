#!/bin/sh

echo "$CA" > /tmp/ca.crt
echo "$CERT" > /tmp/user-cert.crt
echo "$KEY" > /tmp/key.pem


exec python3 producer.py