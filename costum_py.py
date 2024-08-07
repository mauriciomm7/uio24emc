
def check_match(df, col1, col2):
    """
    Check if values in `col1` match `col2` and return mismatches.

    Parameters:
    df (pd.DataFrame): DataFrame with columns to compare.
    col1 (str): First column to compare.
    col2 (str): Second column to compare.

    Returns:
    pd.DataFrame: Rows where `col1` and `col2` do not match.

    Prints:
    Total matches and non-matches.
    """
    df['Match'] = df[col1] == df[col2]
    df['Status'] = df['Match'].apply(lambda x: 'Yes' if x else 'No')
    
    not_matching_df = df[df['Status'] == 'No']
    
    print(f"Total exact matches: {df['Match'].sum()}")
    print(f"Total non-matches: {len(df) - df['Match'].sum()}")
    
    return not_matching_df


# Function to create the unique ID

def create_unique_id(row):
    # Extract year and case number from iuropa_case_id
    parts = row['iuropa_case_id'].split('_')
    year = parts[2]  # Extracts YYYY from 'CASE_C_YYYY_XXXXX'
    case_number = parts[3]  # Extracts XXXXX from 'CASE_C_YYYY_XXXXX'
    
    # Extract court code from iuropa_national_court_id
    court_code = row['iuropa_national_court_id'].split('_')[2]  # Extracts NE from 'COURT_NE_...'
    
    # Combine parts into the unique ID
    unique_id = f"REF_{year}_{case_number}{court_code}"
    return unique_id


