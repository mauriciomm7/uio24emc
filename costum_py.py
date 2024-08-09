
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




# # FUNCTION that returns calculates the set ratio of citations
# # CREATE cols set_ratio_rephrase_avg
# def set_ratio_rephrase(dataframe):
# 	"""
# 	In: UoM dataframe.
# 	Requires: cols  'nat_citations', 'ecj_citations', 'iuropa_decision_id',
# 	Out: SELF plus ['set_ratio_rephrase','set_ratio_rephrase_avg' ] 
#     M = dataframe with case-application dyads 
#     X = dataframe with question-case-application dyads
#     j = iuropa_case_id
#     X_n = temporary subset of X when j
# 	"""
# 	# copy data
# 	X = dataframe.copy()
# 	set_ratio_rephrase = []
# 	set_ratio_rephrase_avg = []
# 	for j in X['uoa_dyad_id']:
# 		# SUBSET for decision j
# 		mask_for_j = X['iuropa_decision_id'] == j
# 		X_n = X[mask_for_j]
# 		for index, row in X_n.iterrows():
# 		set_ratio_citations =  set(row['nat_citations'])- (set(row['nat_citations'])-set(row['ecj_citations'])) / set(row['nat_citations'])
# 		# Update 
# 		X.at[i.index '`set_ratio_rephrase'] = set_ratio_citations
# 	j_set_ratio_avg = X_n['set_ratio_citations'].mean()
# 	X.loc[mask_for_j, 'set_ratio_rephrase_avg'] = j_set_ratio_avg
# 	output = X
# 	return(output)


# set_ratio_reformulation = []
# set_ratio_reformulation_avg = []


# # [] Make into a function

# for j in M:
# 	mask_for_j = X['iuropa_case_id'] == j
# 	X_n = X[mask_for_j]
# 	for index, row in X_n.iterrows():
# 		set_ratio_citations =  set(row['nat_citations'])- (set(row['nat_citations'])-set(row['ecj_citations'])) / set(row['nat_citations'])
# 		 X.at[i.index '`set_ratio_citations'] = set_ratio_citations
# 	j_set_ratio_avg = X_n['set_ratio_citations'].mean()
# 	X.loc[mask_for_j, 'set_ratio_reformulation_avg'] = j_set_ratio_avg


def extract_questions(file_content):
    # Compile regex pattern to match "Question referred" or "Questions Referred"
    pattern = re.compile(r"(Question referred|Questions Referred)\s*(.*?)(?=\n\n|\Z)", re.IGNORECASE | re.DOTALL)
    
    # Find all matches in the text
    matches = pattern.findall(file_content)
    
    # Initialize list to store questions
    questions = []
    
    # Process each match
    for i, (heading, question) in enumerate(matches, start=1):
        # Clean and split the question text
        question = question.strip()
        questions.append({"question_1": f"Question {i}", "question_txt": question})
    
    # Convert the list to a DataFrame
    df = pd.DataFrame(questions)
    
    return df