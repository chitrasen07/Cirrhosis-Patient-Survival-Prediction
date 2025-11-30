import pandas as pd
import numpy as np
import os
import sys

def load_dataset():
    """Safely load CSV dataset with error handling"""
    
    # ---- STEP 1: Detect all CSV files automatically ----
    csv_files = [f for f in os.listdir() if f.endswith('.csv')]

    if len(csv_files) == 0:
        print("❌ No CSV files found in this directory. Please upload a dataset.")
        return None

    print("📁 CSV files found:")
    for i, file in enumerate(csv_files, 1):
        file_size = os.path.getsize(file) / 1024  # Size in KB
        print(f"   {i}. {file} ({file_size:.1f} KB)")

    # ---- STEP 2: Ask user to choose dataset ----
    while True:
        try:
            choice = input("\n🔢 Enter file number to load (e.g., 1): ").strip()
            if not choice.isdigit():
                print("❌ Please enter a valid number")
                continue
            
            choice = int(choice) - 1
            if choice < 0 or choice >= len(csv_files):
                print(f"❌ Please enter a number between 1 and {len(csv_files)}")
                continue
            
            dataset_path = csv_files[choice]
            break
        except ValueError:
            print("❌ Invalid input. Please try again.")

    # ---- STEP 3: Load dataset safely ----
    try:
        print(f"\n⏳ Loading: {dataset_path}...")
        
        # Try different encodings if UTF-8 fails
        encodings = ['utf-8', 'latin-1', 'iso-8859-1', 'cp1252']
        df = None
        
        for encoding in encodings:
            try:
                df = pd.read_csv(dataset_path, encoding=encoding)
                print(f"✅ Successfully loaded with encoding: {encoding}")
                break
            except UnicodeDecodeError:
                continue
        
        if df is None:
            print("❌ Could not read file with any encoding. File may be corrupted.")
            return None
            
    except FileNotFoundError:
        print(f"❌ File not found: {dataset_path}")
        return None
    except pd.errors.EmptyDataError:
        print("❌ CSV file is empty")
        return None
    except pd.errors.ParserError as e:
        print(f"❌ Error parsing CSV: {e}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error loading dataset: {e}")
        return None

    # ---- STEP 4: Show dataset info ----
    try:
        print("\n" + "="*60)
        print("📊 DATASET INFORMATION")
        print("="*60)
        print(f"📏 Shape: {df.shape[0]} rows × {df.shape[1]} columns")
        print(f"\n📋 Columns: {list(df.columns)}")
        
        print(f"\n🔍 First 5 rows:")
        print(df.head())
        
        print(f"\n📈 Data types:")
        print(df.dtypes)
        
        print(f"\n❓ Missing values:")
        missing = df.isnull().sum()
        if missing.sum() > 0:
            print(missing[missing > 0])
        else:
            print("   No missing values ✅")
        
        print("="*60)
        
        # ---- STEP 5: Save loaded dataset info ----
        print(f"\n✅ Dataset ready for processing!")
        print(f"   Total records: {len(df)}")
        print(f"   Total features: {len(df.columns)}")
        
        return df
        
    except Exception as e:
        print(f"❌ Error displaying dataset info: {e}")
        return df  # Still return the dataframe even if info display fails


if __name__ == "__main__":
    print("\n" + "█"*60)
    print("█  CIRRHOSIS DATASET LOADER")
    print("█"*60 + "\n")
    
    df = load_dataset()
    
    if df is not None:
        print("\n✅ Dataset loaded successfully!")
        print("\n💾 To use this dataset in your code:")
        print("   df = pd.read_csv('your_file.csv')")
        print("\n📝 Next steps:")
        print("   1. Run your model training script")
        print("   2. Or open the Jupyter notebook")
        print("   3. Or run predict.py for inference")
    else:
        print("\n❌ Failed to load dataset. Please check your file and try again.")
        sys.exit(1)
