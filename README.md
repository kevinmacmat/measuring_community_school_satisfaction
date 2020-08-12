# capstone

---

### Quick Start
Below is the flow of notebooks from gathering, preprocessing, EDA, and modeling. If you would only like to run the models open the final notebook titled "modeling.ipynb" and run cells in order.
1) data_frame_cleaning.ipynb
2) web_scraping.ipynb
3) concat_dataframe.ipynb
4) sentiment_analysis.ipynb
5) sqr_eda.ipynb
6) text_processing_eda.ipynb
7) modeling.ipynb

### Intro
In the eternal debate about public education we often hear from official voices whereas the average parent or student can often feel out of the loop. Although school surveys exist, they have carefully crafted official questions that can feel very formal, and we know from research that people tend to rate things higher than they may truly feel. This project seeks to use Natural Language Processing and multiclass classification to supply the DOE a tool to analyze the strength of trust and ties families feel to the schools their children attend. Using comments to predict a "satisfaction" score can be used as a real time measurement to identify schools that may be prone to poor performance.  

### Data
After cleaning, the dataset contains 985 NYC K-8 schools which are split for training and testing. The data comes from two sources. Firstly data is taken from the NYC Department of Education's annual School Quality Report (SQR). This report is collection of survey and demographic data that seeks to provide a snapshot of the quality of instruction and support. Secondly unfiltered comments are scraped from insideschools.org. This website has a page for every school in NYC with a comments section at the foot. The target variable in this case is a engineered score named "sqr_score" which is the average of the "Strong Family-Community Ties Rating" and the "Trust" rating. These were selected since both contained questions that would pertain to how satisfied a community would be with a school. 

### EDA
The exploratory data analysis phase provides some insight into the concerns and desires of NYC's parents and students. The overall tone of the word tokens and comments tended towards being very positive with high frequency n-grams like "recommend this school" and "great school". 
![](/visuals/trigrams_barchart.png)
Using Named Entity Recognition (NER) there were no findings of significant political bias. Contrary to the many news stories regarding De Blasio and NYC schools his name appears only 20 times while Carmen Fariña's appears (148). The big topic that showed up throughout the EDA process was programs/services. Many instances of Dual Language Programs and specifically Spanish appeared throughout. Other programs/services like the Gifted and Talented program, fund designation, and additional time were also strongly represented. 
![](/visuals/language_freq.png)
A quick look at the correlation matrix shows that there is not much significant positive or negative correlation between variables and the target variable. 
![](/visuals/correlation_matrix.png)
Additionally there seems to be unexpected relationships between the sentiment scores and various variables. As the sentiment goes up one would expect school quality ratings to go up as well. The distribution of the data is much more scattered and random. This could indicate low predictability. ![](/visuals/compound_sqr_scores_dist.png)

### Models
Due to the lack of information seen in the distribution of word frequencies, TF-IDF vectorization was used. TF-IDF takes the product of the term frequency and the inverse document frequency to try to capture words that may be less common but may provide more contextual information. Random Forest, Naive Bayes, and LinearSVC classifiers were used as models. The models were evaluated using accuracy and F1 scores with a higher degree of emphasis placed on the F1 score using the "macro" hyperparameter (harmonic average of precision and recall). The reasoning was to have a more robust model since there is no particular reason a false positive would be more detrimental than a false negative. A dummy classifier with a test accuracy of 0.2105 and a test F1 score of 0.1234 was used as a baseline. All models performed above the baseline but produced testing accuracies with a range of around .23-.35 and F1 scores with a range of around .09-.18. The final model was a compromise of a smaller testing accuracy of 0.2995 but larger F1 score of 0.1826.
![](/visuals/model_tracking.png)

### Conclusion
Currently the models are not production quality. This may have to do with preprocessing as well as the nature of the text itself. For future improvements XGBoost would be used to tune hyperparameters while stacking models would also be used to improve accuracy.  

### Link To Presentation
https://docs.google.com/presentation/d/1hw7rKXQ45Hyizba3RstTXcTRVA5MRhweookCJc3uS9U/edit?usp=sharing