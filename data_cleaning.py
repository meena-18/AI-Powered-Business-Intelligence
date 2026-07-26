
import pandas as pd


class DataCleaning:
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = None

    def load_data(self):
        """Load dataset"""
        self.data = pd.read_csv(self.filepath)
        print("Dataset Loaded Successfully")
        print(f"Rows: {self.data.shape[0]}")
        print(f"Columns: {self.data.shape[1]}")

    def dataset_info(self):
        """Display dataset information"""
        print("\nDataset Information")
        print("-" * 40)
        print(self.data.info())

    def missing_values(self):
        """Display missing values"""
        print("\nMissing Values")
        print("-" * 40)
        print(self.data.isnull().sum())

    def remove_duplicates(self):
        """Remove duplicate rows"""
        before = self.data.shape[0]
        self.data.drop_duplicates(inplace=True)
        after = self.data.shape[0]

        print("\nDuplicate Records Removed")
        print(f"Before : {before}")
        print(f"After  : {after}")

    def fill_missing(self):
        """Fill missing numerical values with median"""
        numeric_columns = self.data.select_dtypes(include=['number']).columns

        for column in numeric_columns:
            self.data[column].fillna(self.data[column].median(), inplace=True)

        print("\nMissing numerical values filled.")

    def convert_dates(self):
        """Convert Order Date if present"""
        if "Order Date" in self.data.columns:
            self.data["Order Date"] = pd.to_datetime(
                self.data["Order Date"],
                errors="coerce"
            )
            print("Order Date converted successfully.")

    def save_cleaned_data(self):
        """Save cleaned dataset"""
        self.data.to_csv("data/cleaned_superstore.csv", index=False)
        print("\nCleaned dataset saved successfully.")


def main():

    cleaner = DataCleaning("data/superstore.csv")

    cleaner.load_data()

    cleaner.dataset_info()

    cleaner.missing_values()

    cleaner.remove_duplicates()

    cleaner.fill_missing()

    cleaner.convert_dates()

    cleaner.save_cleaned_data()


if __name__ == "__main__":
    main()