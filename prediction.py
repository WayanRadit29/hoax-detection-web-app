def predict_hoax(text):
    text = text.lower()

    hoax_keywords = [
        "viral",
        "sebarkan",
        "100%",
        "terbukti",
        "jangan sampai",
        "rahasia",
        "konspirasi",
        "obat ampuh"
    ]

    for keyword in hoax_keywords:
        if keyword in text:
            return "Hoax"

    return "Tidak Hoax"