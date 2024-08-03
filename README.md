# UIO24EMC : Lawmaking Coordination? Explaining Referral Failure in Federated Judicial Systems

Here is what we will do. You will first gather all the operative judgements for the most recent caselaw. Then you will use it as a 


## Project Structure Usage
- The `raw` directory should be used for all the input datatasets that you scrape or borrow from other projects.
- The `data` directory should be used for the strcutured datatsets that will be used on your project or publication. 
- The `nbs` is for the jupyter or qmd notebooks that you use on your projects.
- The `figures` dir  is for publication quality figures.
- The `scripts` dir is for any stand alone scripts required during the projects that might be instantiated across or independent of the notebooks (e.g. update real time dataset)          

### Data Collectio 



### Required Dataframes specifications

{TABLE} Applications
- `iuropa_decision_id` **dec level**: 
- `iuropa_decision_date` **dec level**:
- `referring_court_name` **dec level**:
- `ms_origin_name`**dec level**:
- `app_questions_number` **dec level**:
- `iuropa_decision_fulltext`: **dec level**
- `iuropa_decision_id_par` **par level**: 
- `iuropa_decision_id_par_txt` **par level**: 
- `iuropa_cited_items` **par level**: 

- `question_in_judgment_text` **par level:**
- `iuropa_judgment_id_par` **par level:**
- `judge_coop_flag` **par level:** whether judgment text includes question even if rephrased.

{TABLE} Operative Judgements


### Feature Engineering Functions