import re
from pathlib import Path

import pandas as pd


RAW_DATA_PATH = Path("data/Meta Data.xlsx")
OUTPUT_PATH = Path("data/hoax_data_final.csv")


def extract_date_from_link(link):
    match = re.search(r"/(\d{4})/(\d{2})/(\d{2})/", str(link))

    if match:
        year, month, day = match.groups()
        return f"{year}-{month}-{day}"

    return "2021-04-25"

def clean_title(value):
    text = clean_text(value)

    prefixes = [
        r"^\[FALSE\]\s*",
        r"^\[SALAH\]\s*",
        r"^\[HOAKS\]\s*",
        r"^\[HOAX\]\s*",
        r"^\[MISLEADING\]\s*",
        r"^\(FALSE\)\s*",
        r"^\(SALAH\)\s*",
    ]

    for prefix in prefixes:
        text = re.sub(prefix, "", text, flags=re.IGNORECASE)

    return text.strip()

def detect_topic(title, content):
    text = f"{title} {content}".lower()

    topic_keywords = {
        "Health": [
            "vaksin", "covid", "virus", "obat", "penyakit", "kanker",
            "kesehatan", "dokter", "rumah sakit", "masks", "vaccine"
        ],
        "Government": [
            "pemerintah", "presiden", "menteri", "polisi", "tni",
            "pemilu", "pilpres", "kementerian", "government"
        ],
        "Economy": [
            "uang", "bank", "rupiah", "pajak", "bantuan", "bbm",
            "harga", "ekonomi", "pertamina"
        ],
        "Education": [
            "sekolah", "kampus", "mahasiswa", "siswa", "ujian",
            "universitas", "education"
        ],
        "Weather": [
            "gempa", "banjir", "hujan", "cuaca", "bmkg", "tsunami",
            "angin"
        ],
        "Technology": [
            "whatsapp", "facebook", "twitter", "instagram", "akun",
            "aplikasi", "link", "website", "free fire"
        ],
    }

    for topic, keywords in topic_keywords.items():
        for keyword in keywords:
            if keyword in text:
                return topic

    return "General"


def clean_text(value):
    if pd.isna(value):
        return ""

    text = str(value)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def main():
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    df = pd.read_excel(RAW_DATA_PATH, sheet_name="Hasil Scrapping")

    df = df[["Header", "Content", "Link"]]
    df = df.dropna(subset=["Header", "Content", "Link"])
    df = df.drop_duplicates(subset=["Header"])

    final_df = pd.DataFrame()
    final_df["title"] = df["Header"].apply(clean_title)
    final_df["content"] = df["Content"].apply(clean_text)
    final_df["source"] = "TurnBackHoax"
    final_df["topic"] = final_df.apply(
        lambda row: detect_topic(row["title"], row["content"]),
        axis=1
    )
    final_df["publication_date"] = df["Link"].apply(extract_date_from_link)
    final_df["label"] = "Hoax"

    final_df = final_df[
        ["title", "content", "source", "topic", "publication_date", "label"]
    ]

    final_df.to_csv(OUTPUT_PATH, index=False, encoding="utf-8-sig")

    print("Preprocessing completed.")
    print(f"Total data: {len(final_df)}")
    print(f"Output file: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()