# examples/example_usage.py

import pandas as pd
from dclean import clean_data, preprocess_data, anonymize_data, encrypt_data, decrypt_data, generate_key

data = {
    'CustomerID': [1, 2, 2, 4, 5, None],
    'Name': ['Alice', 'Bob', 'Bob', 'David', 'Eva', 'Frank'],
    'Age': [25, 30, 30, None, 40, 50],
    'Income': [50000, 60000, 60000, 70000, None, 80000]
}
df = pd.DataFrame(data)

cleaned_df = clean_data(df)
preprocessed_df = preprocess_data(cleaned_df, strategy='median')
anonymized_df = anonymize_data(preprocessed_df)

key = generate_key()
encrypted_data = encrypt_data(anonymized_df.to_csv(), key)
decrypted_data = decrypt_data(encrypted_data, key)

from io import StringIO
decrypted_df = pd.read_csv(StringIO(decrypted_data))

print("Original Data:")
print(df)
print("\nCleaned Data:")
print(cleaned_df)
print("\nPreprocessed Data:")
print(preprocessed_df)
print("\nAnonymized Data:")
print(anonymized_df)
print("\nDecrypted Data:")
print(decrypted_df)
