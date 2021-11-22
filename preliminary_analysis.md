# Project Title

### Group Members
- Nicholas De La Cruz
- Kareem Ibrahim
- Gene Lam

### Repository Structure

For example:
- `data`
  - `raw_twitter.csv`: Raw data from the Twitter API
  - `raw_census.csv`: Raw data from the Census API
- `code`
  - `Premliminary_Analysis.md`: Performs exploratory data analysis and cleans our dataset

### Exploratory Analysis
In our exploratory data analysis, we figured out what features we would like to use to predict the health outcomes of people who took the National Health and Nutrition Examination Survey (NHANES). This is a government funded annual survey to gauge the public's current health status. Within the survey results, there are numerous spreadsheets of reported health information. We merged a few of these spreadsheets together in order to find the features and labels necessary to solve our problem. The features we decided on are 
1. HH ref person's gender
1. HH ref person's age in years                   
1. HH ref person's education level              
1. Race/Hispanic origin w/ NH Asian               
1. Total savings/cash assets for the family    
1. Annual family income                         
1. General health condition                       
1. Body Mass Index (kg/m**2)                     
in order to predict a person's BMI and General Health Condition (GHC). We believe that by using a person's identifiable attributes alongside their household economic status, we can gauge their general health condition. We chose the labels of BMI and GHC because we believe that they can accurately classify a person's healthiness. Note, BMI might be an unreliable label on its own, and GHC is a self-reported value which may also be untrustworthy. However, using both of these as our predicted labels may prove to yield a more accurate analysis of a person's well-being.

### Challenges
Describe any challenges you've encountered so far. Let me know if there's anything you need help with!

### Future Work
Describe what work you are planning to complete for the final analysis.

### Contributions
Describe the contributions that each group member made.
