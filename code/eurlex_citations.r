library(tidyverse)
library(eurlex)
library(dplyr)
library(conflicted)
conflict_prefer("select", "dplyr")
conflict_prefer("filter", "dplyr")
# Include Citations_detailed
app_citations <- elx_make_query( resource_type = "caselaw", 
                                 include_citations_detailed = TRUE ) |> elx_run_query()

all_cited_detailed_celex <- elx_make_query(resource_type = "caselaw", 
                                   include_citations_detailed = TRUE, ) |> elx_run_query()

all_cited_celex <- elx_make_query(resource_type = "caselaw", 
                                  include_citations = TRUE, ) |> elx_run_query()


all_cited_celex <- all_cited_celex %>%
  rename(apps_celex = celex) #NEW LEFT OLD RIGHT 

setwd("C:/gitprojects/uio24emc/raw/")
# Read the first CSV file
df1 <- read.csv("./iu_uio24emc/apps_scraping.csv")


apps_citations <- left_join(df1, all_cited_celex, by = "apps_celex")
write.csv(apps_citations, "./iu_uio24emc/apps_with_citations.csv")

# COUNT unqiue  group_by_all() %>%  group_by_all() %>% summarise(COUNT = n())


