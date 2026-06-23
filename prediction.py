import re

def predict_hoax(text):
    text = text.lower()
    score = 0

    # ================= HOAX FEATURES =================
    hoax_features = {
        "menyembuhkan semua penyakit": 4,
        "100% ampuh": 4,
        "obat ajaib": 3,
        "jamin sembuh": 3,
        "viral wajib share": 3,
        "tanpa efek samping": 2,
        "langsung sembuh": 3
    }

    for phrase, weight in hoax_features.items():
        if phrase in text:
            score += weight

    # ================= CLICKBAIT =================
    clickbait = ["viral", "heboh", "shock", "mengerikan"]
    for word in clickbait:
        if word in text:
            score += 1

    # ================= PATTERN =================
    if re.search(r"\b100%\b", text):
        score += 3

    if "!!!" in text:
        score += 1

    # ================= TRUST SIGNAL (NEGATIVE) =================
    trusted = ["bmkg", "polisi", "penelitian", "data resmi"]
    for t in trusted:
        if t in text:
            score -= 3

    # ================= DECISION =================
    return "Hoax" if score >= 4 else "Tidak Hoax"