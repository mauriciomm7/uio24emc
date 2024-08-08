library(tidyverse)
library(eurlex)
library(dplyr)
library(conflicted)
conflict_prefer("select", "dplyr")
conflict_prefer("filter", "dplyr")
# Include Citations_detailed
app_citations <- elx_make_query( resource_type = "caselaw", 
                                 include_citations_detailed = TRUE ) |> elx_run_query()

all_cited_celex <- elx_make_query(resource_type = "caselaw", 
                                   include_citations = TRUE, ) |> elx_run_query()



setwd("C:/gitprojects/uio24emc/raw/")


# Read the first CSV file
df1 <- read.csv("./iu_uio24emc/apps_scraping.csv")
# Read the second CSV file
df2 <- read.csv("path/to/your/file2.csv")

apps_citations <- left_join(df1, df2, by = "celex")