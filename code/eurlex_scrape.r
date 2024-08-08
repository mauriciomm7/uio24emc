library(tidyverse)
library(eurlex)
library(conflicted)
conflict_prefer("select", "dplyr")
conflict_prefer("filter", "dplyr")
# Include Citations_detailed
app_citations <- elx_make_query( resource_type = "caselaw", include_citations_detailed = TRUE ) |> elx_run_query()

all_cited_celex <- elx_make_query( resource_type = "any", include_citations_detailed = TRUE ) |> elx_run_query()
# Legal Basis Only works for Legislation
# lbs <- elx_make_query( resource_type = "caselaw", 
#                       include_lbs = TRUE,
#                       limit =10 ) |> elx_run_query()

# Include Citations only includes items from the cellar already in the IUROPA DB {citations}
# test <- elx_make_query( resource_type = "caselaw",
#                        include_citations_detailed = TRUE) |> elx_run_query()

################################################ #
## GET footnotes from AG Opinions not included ##
# TRY EURLEX XML
# LEFT-Outer JOIN based on common columns  
# rol_decision_celex_key$celex <- rol_decision_celex_key$cited_celex # MATCH column name
# test1 <- rol_decision_celex_key  |> dplyr::left_join(eurlex_data)x||
