import re

def predict_hoax(text):
    text = text.lower()
    score = 0

    hoax_features = {
        "menyembuhkan semua penyakit": 4,
        "100% ampuh": 4,
        "obat ajaib": 3,
        "jamin sembuh": 3,
        "viral wajib share": 3,
        "tanpa efek samping": 2,
        "langsung sembuh": 3,
        "sebarkan": 2,
        "viralkan": 2,
        "jangan sampai dihapus": 3,
        "sebelum terlambat": 2,
        "rahasia pemerintah": 3,
        "media tidak berani memberitakan": 3,
        "bagikan ke semua grup": 3,
        "gratis": 1,
        "klik link": 2
    }

    for phrase, weight in hoax_features.items():
        if phrase in text:
            score += weight

    clickbait = ["viral", "heboh", "shock", "mengejutkan", "mengerikan", "terbongkar"]
    for word in clickbait:
        if word in text:
            score += 1

    if re.search(r"\b100\s*%\b", text):
        score += 3

    if "!!!" in text:
        score += 1

    trusted = ["bmkg", "kemenkes", "kominfo", "bank indonesia", "data resmi", "situs resmi", "penelitian"]
    for t in trusted:
        if t in text:
            score -= 3

    return "Hoax" if score >= 4 else "Tidak Hoax"