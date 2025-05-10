import pandas as pd

def height_to_inches(ht_str):
    try:
        feet, inches = map(int, ht_str.split('-'))
        return feet * 12 + inches
    except:
        return None

def run_etl():
    df = pd.read_csv('player_data.csv')  # Simulate external fetch
    
    # Transform height
    df['Ht_in'] = df['Ht'].apply(height_to_inches)

    # Convert birth date
    df['Birth Date'] = pd.to_datetime(df['Birth Date'], errors='coerce')

    # Drop rows with missing values in key fields
    df.dropna(subset=['Player', 'Ht_in', 'Wt', 'Birth Date'], inplace=True)

    # Save cleaned data
    df[['Player', 'Pos', 'Ht_in', 'Wt', 'Birth Date', 'Colleges']].to_csv('local_data.csv', index=False)

if __name__ == '__main__':
    run_etl()
