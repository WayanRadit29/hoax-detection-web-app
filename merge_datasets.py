import pandas as pd
from pathlib import Path

HOAX_PATH = Path("data/hoax_data_final.csv")
NON_HOAX_PATH = Path("data/non_hoax_data.csv")
OUTPUT_PATH = Path("data/final_dataset.csv")


def main():
    hoax_df = pd.read_csv(HOAX_PATH)
    non_hoax_df = pd.read_csv(NON_HOAX_PATH)

    final_df = pd.concat(
        [hoax_df, non_hoax_df],
        ignore_index=True
    )

    final_df = final_df.drop_duplicates(
        subset=["title"],
        keep="first"
    )

    final_df = final_df.sample(
        frac=1,
        random_state=42
    ).reset_index(drop=True)

    final_df.to_csv(
        OUTPUT_PATH,
        index=False,
        encoding="utf-8-sig"
    )

    print("=" * 50)
    print("MERGE COMPLETED")
    print("=" * 50)

    print(f"Hoax data      : {len(hoax_df)}")
    print(f"Non hoax data  : {len(non_hoax_df)}")
    print(f"Final dataset  : {len(final_df)}")

    print("\nLabel distribution:")
    print(final_df["label"].value_counts())

    print("\nTopic distribution:")
    print(final_df["topic"].value_counts())

    print(f"\nOutput saved to: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()