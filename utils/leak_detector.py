# utils/leak_detector.py
import re

AADHAAR_REGEX = r"\b\d{4}[\s-]?\d{4}[\s-]?\d{4}\b"
PAN_REGEX = r"\b[A-Z]{5}[0-9]{4}[A-Z]\b"
BANK_REGEX = r"\b(?:IFSC|ACCOUNT|ICICI|HDFC|SBI|KOTAK)\b"
EMAIL_REGEX = r"\b[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+\b"
CITIZEN_REGEX = r"\b(?:815 million|indian citizens|kyc|aadhaar|pan card|passport|upi id|fullz|dump)\b"

def detect_leaks(text):
    leaks = []
    if re.search(AADHAAR_REGEX, text): leaks.append("Aadhaar")
    if re.search(PAN_REGEX, text): leaks.append("PAN")
    if re.search(BANK_REGEX, text): leaks.append("Bank Info")
    if re.search(EMAIL_REGEX, text): leaks.append("Email ID")
    if re.search(CITIZEN_REGEX, text): leaks.append("Indian Citizens Mentioned")
    return leaks
