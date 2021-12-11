# Forecasting Your General Well-Being

Los Tres Locos is here to help give you an idea of where your health might be at! Using the annual [National Health and Nutrition Examination Survey (NHANES) from 2017-2018](https://wwwn.cdc.gov/nchs/nhanes/continuousnhanes/default.aspx?BeginYear=2017), we can use numerous factors pertaining to one's life circumstances to try and determine their health condition.

## Exploratory Data Analysis

The first thing we needed to accomplish was to figure out what we are dealing with within the NHANES dataset. What values did NHANES record in their survey? Which of these factors would be useful to us? The NHANES overall survey consists of numerous datasets spanning from general demographic and household information to specific medical conditions and health data. We desired to create a model using certain demographic and income situations instead of health conditions. This leads to the big question we are trying to answer: is a given person healthy or not? Further throughout our research, we made our question more precise: does lifestyle and circumstances affect the way people view their personal health? To solve this question, we chose to take a look at the following datasets:
* [Demographics](https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/DEMO_J.htm)
* [Occupation](https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/OCQ_J.htm)
* [Income](https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/INQ_J.htm)
* [Current Health Status](https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/HSQ_J.htm)
* [Body Measures](https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/BMX_J.htm)

When looking at these datasets, the first item we needed to address was deciphering NHANES coded column names. The resultant datasets' columns must be decoded by using the labels through the links above. We manually converted the column names within in our script from the data provided and were able to combine the datasets so we could start taking a critical look as to what features we would need and how we would clean them.

## Data Cleaning and Features

With our main question in mind, we now needed to decide what we wanted to predict. After a thorough overview of the datasets we had chosen, we decided we should predict the General health Condition (GHC) field in the Current Health Status dataset using a classification model. This label is scaled from 1-5 with 1 being excellent health and 5 being poor health. The features, alongside their column names, and cleaning methods we decided to use to predict GHC are as follows:
* Gender: *HH ref person\'s gender*
  * This column had no null gender values so we did not to clean this feature.
* Age: *HH ref person\'s age in years*
  * This column had no null gender values so we did not to clean this feature.
* Education Level: *HH ref person\'s education level*
  * There were a few null values for this category, so we decided to perform mode imputation and replace the N/A's with the most common education level.
* Ethnicity: *Race/Hispanic origin w/ NH Asian*
  * This column had no null gender values so we did not to clean this feature.
* Savings: *Total savings/cash assets for the family*
  * There were some answers that corresponded with "Refused" or "Don't Know", so we decided to convert those values to N/A and perform mode imputation on all null values.
* Income: *Annual family income*
  * This was the trickiest column to clean. The order of the initial data was not categorized linearly and contained some overlapping categories (i.e. there were 4 categories between $0 and $20,000 and another category at the end of the list as <$20,000).
  * First we decided to combine the 4 categories that were less than $20,000 together with the "Under $20,000" category. We then reordered the category labels from low to high income. We also decided to drop the "Over $20,000" category considering there were few results in that field and there was no easy way to include that in our resultant set.
  * Next, we set all of the "Refused" or "Don't know" to N/A and performed median imputation on the median of all categories for our null values.

For GHC, since this is the category we want to predict, we dropped all of the N/A values and decided to only keep valid values. We also wanted to try and predict someone's BMI through a lienar regression model considering the BMI field is a continous number field instead of a category. We decided that GHC might be a good indicator for attempting to predict BMI because a person may be more likely to percieve their health based on their current BMI. Similarly, we dropped all N/A values from BMI.

## Model Evaluation

Now that we have chosen and cleaned the features we wished to use, we can finally start fitting our model.
### GHC: Decision Tree

We decided to use a decision tree classification model to fit our features and labels. Before fitting our data, we normalized the features to between 0 and 1 to avoid any high outliers. We decided to use 33% of the data for testing. Using all of our initial features, the model returned an accuracy, precision, recall, and F1 score of about 36.6%. After some tinkering, we decided to drop the income feature, which gave us a better accuracy score of about 41.5%.

![image](https://user-images.githubusercontent.com/12586551/145662269-77e6af4f-7b45-4037-9b05-9073200e0c7d.png)

This image shows the confusion matrix heat map of values that our model predicted versus the actual data points. The most immediate thing we can see here is how most of the data ponts, actual and predicted, are clustered around 2-4. We can see see that for most actual values of 2 and 4, the model was likely to predict 3. This makes sense logically as most people would likely see themselves as average. Also, there does not exist an objective method by the surveyers in this study to determine their health condition, therefore the data is likely to be heavily skewed towards the middle. 

We then ran this model on 16 subsets of our feature set to see which categories the mdoel excels on and which it performs poorly with (see these category filters at the bottom of `Full_Analysis.md`). Our model performs well on Non-Hispanic Whites (43.7%) and females (41.9%) and poorly with Non-Hispanic Asians (34.1%) and people with incomes between $35,000 and $65,000 (35.2%).

### GHC: Cross-Validation

To possibly improve our accuracy score, we attempted 2 cross-validation techniques: Graph Search and K-Fold.

For our graph search, we tweaked 3 hyper-paramerters: max_depth, max_features, and min_samples_split. Our cross-validation model found that a max depth of 5, max features of 'auto' (which is the square root of total features we have), and a min. sample split of 3. This improved our accuracy to around 42%. With our K-Fold cross-validation, we noticed with higher folds, the higher the accuracy of our model became. So we decided to use 3000 folds, a little more than half of our total features, which gave us an accuracy of 41.1%, which is actually a decrease in our model performance.

The following is our ROC-curves for each of the 5 well-being classes:

![image](https://user-images.githubusercontent.com/12586551/145663650-eedf81fd-4023-4234-8104-e3b939c7a79e.png)

### Results

The reason our model did not perform as well as it could of is most likely due to the features and feature engineering we decided to use. The features we decided to use are mostly based on demographic data that may not prove to be useful in determining someone's well-being. For example, by dropping the income category, we were able to improve our performance by approximately 5%. A future model should take more measured direct health information into consideration. Secondly, we may have recieved better luck with performing a binary classification, for example, percieved good or bad health. While this may work better to improve our accuracy, it still does not address how the majority of the data points are in the average 3 category, meaning whichever classification, good or bad, has the 3 category, the model would likely be skewed more to that side. Lastly, GHC is a self-reported attribute that has no current way of being measured. People themselves are likely not the best source of information to consider their own health objectively, hence the commonality the 3 category. A future model would be better off trying to predict a different label that is less subjective.

### BMI: Linear Regression

Next, we used GHC as a feature to try and describe BMI through a linear regression. This model did not predict BMI through GHC very well as the model was only 6.3% accurate.

![image](https://user-images.githubusercontent.com/12586551/145664232-f4d748bc-dbfc-497b-ab89-a02f1d7e0b57.png)

The above graph shows the mapping of GHC to BMI. As can be seen, GHC is distributed almost evenly across the different BMI ranges, indicating that there may be little correlation between GHC and BMI. Also note how GHC is not a continous feature as the labels 1 through 5 are categories. We were unlikely to find a method to better predict BMI through GHC so we did not attempt to improve it further.

## Conclusion
The biggest implication we have seen so far from this model is simple: your demographic data is an unlikely indicator on you are currently feeling! While our model could have been improved through a better list of features and a better focus on feature engineering, we can conclude that demographic data such as income, gender, race etc., does not necessarily dictate how someone may feel about their well-being. In other words, money (and a whole bunch of other features), does not buy you well-being!
