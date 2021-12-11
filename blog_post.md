# Forecasting Your General Well-Being

Los Tres Locos is here to help give you an idea of where your health might be at! Using the annual [National Health and Nutrition Examination Survey (NHANES) from 2017-2018](https://wwwn.cdc.gov/nchs/nhanes/continuousnhanes/default.aspx?BeginYear=2017), we can use numerous factors pertaining to one's life circumstances to try and determine their health condition.

## Exploratory Data Analysis

The first thing we needed to accomplish was to figure out what we are dealing with within the NHANES dataset. What values did NHANES record in their survey? Which of these factors would be useful to us? The NHANES overall survey consists of numerous datasets spanning from general demographic and household information to specific medical conditions and health data. We desired to create a model using certain demographic and income situations instead of health conditions. This leads to the big question we are trying to answer: does lifestyle and circumstances affect the way people view their personal health? To solve this question, we chose to take a look at the following datasets:
* [Demographics](https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/DEMO_J.htm)
* [Occupation](https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/OCQ_J.htm)
* [Income](https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/INQ_J.htm)
* [Current Health Status](https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/HSQ_J.htm)
* [Body Measures](https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/BMX_J.htm)

When looking at these datasets, the first item we needed to address was deciphering NHANES coded column names. The resultant datasets' columns must be decoded by using the labels through the links above. We manually converted the column names within in our script from the data provided and were able to combine the datasets so we could start taking a critical look as to what features we would need and how we would clean them.

## Data Cleaning and Features



## Model Evaluation

Percieved health may vary.
### GHC
### BMI
### Accuracy
### Challenges
### Cross-Validation

## Next Steps
Next time let's pick better features
