# Measuring Community & School Satisfaction

---

### Quick Start
Below is the project flow folders with included notebooks from gathering, preprocessing, EDA, and modeling. If you would only like to run the models open the final notebook titled "modeling.ipynb" and run cells in order. All original and created data can be found in the csv folder. 

1. web_scraping.ipynb   
2. concat_comments_metadata.ipynb   
3. add_sentiment_scores.ipynb  
4. comments_metadata_eda.ipynb
5. topic_modeling.ipynb

### Intro
In the public education debate, we often hear from official voices whereas the average parent or student are often out of the loop. Although school surveys are meant to capture this, often their questions are carefully crafted in ways that can feel very formal, and research has shown that people tend to rate things more favorably than they may truly feel. This project seeks to utilize sentiment analysis and topic modeling to supply the DOE a tool to analyze topics of concern, and the strength of trust and ties families feel to the schools their children attend. Predicting a "satisfaction" score can be used as a real time measurement to identify schools that are prone to poor performance.  

### Data
After cleaning, the dataset contains 985 NYC K-8 schools which are split for training and testing. The data comes from two sources. Data is first taken from the NYC Department of Education's annual School Quality Report (SQR). This report is collection of survey and demographic data that seeks to provide a snapshot of the quality of instruction and support. Unfiltered comments are then scraped from insideschools.org, a website that has a page for every school in NYC with a comments section for each. Sentiment scores were created with VADER (Valence Aware Dictionary and sEntiment) tool which is tuned to text found in sources like social media. This tool was selected with the idea that the comments would express a positive or negative community sentiment that would match the sentiment score. 

### EDA
The exploratory data analysis phase provides some insight into the concerns and desires of NYC's parents and students. The overall tone of the word tokens and comments tended towards being very positive with high frequency n-grams like "recommend this school" and "great school". 

![](/visuals/trigrams_barchart.png)

Using Named Entity Recognition (NER) there were no findings of significant political bias. Contrary to the many news stories regarding De Blasio and NYC schools his name appears only 20 times while Carmen Fariña's appears 148 times. The big topics that showed up throughout the EDA process was programs/services, testing, and Chancellor Carmen Fariña. Through NER and frequency distributions, dual Language Programs and specifically the Spanish language appeared frequently. Other programs/services like the Gifted and Talented program, fund designation, and additional time were also strongly represented. The same trend was observed through LDA topic modeling. Using bigrams and trigrams with 100 passes, relevant terms that appeared in the first topic contained words like dual language, language program, additional learning time, learning partners program, special needs, test scores, classroom raise outcomes, and Carmen Fariña which describe a similar set of concerns as seen when using NER and looking at word frequency.

![](/visuals/language_freq.png)

Additionally there seems to be unexpected relationships between the sentiment scores and various variables. As the sentiment goes up one would expect school quality ratings to go up as well. The distribution of the data is much more scattered and random.

![](/visuals/compound_sqr_scores_dist.png)

### Conclusion
Through processing and analyzing informal comments, concerns about testing and programming/services appeared throughout. These are important issues that should clearly be communicated to parents through the school and DOE. It is a red flag that parents are expressing concern though an informal channel for such formal services such as dual language programs or special needs accomodations which if not given imply legal ramifications. Next steps should include an information campaign to make sure parents are informed about their rights in regards to services their children are entitled to receive and which programs are currently available in their school. 

The models themselves performed well and could be used in developing a front end where one could copy and paste school review comments to generate a sentiment classification. This could be an ongoing measure to identify schools that may need intervention from the DOE or the UFT (United Federation of Teachers). For future improvements XGBoost would also be used to tune hyperparameters while stacking models would also be used to improve scores.  

### Link To Presentation
https://docs.google.com/presentation/d/1hw7rKXQ45Hyizba3RstTXcTRVA5MRhweookCJc3uS9U/edit?usp=sharing
