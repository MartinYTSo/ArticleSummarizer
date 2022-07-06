## News Summarizer
Quickly summarize your news article with a click of a button!

### Dependencies
This program is dependent on the following packages:  
- `requests`  
- `newspaper3k`  
- `validators`

### Background  
This is my first attempt in exploring the realm of text mining. I made this program to help me retrive a summary of a news article. One of the duties at my day job working for the government is to summarize open-source news articles. I thought this tool that I made would be handy in my workflow, so I decided to do a quick project on making an article summarizer. I also think this would be a great addition to my personal project portfolio!

### App Layout  
They layout will look like this upon opening the app:
![image](https://user-images.githubusercontent.com/72810148/177448741-5897b1ad-53fc-48b1-a445-88499bb9ede7.png)

Originally, I had an entry of the author and the date when the article was published. However, due to inconsistency in the NLP picking up the author name and the date, I decided to leave it out.

### Usage

Copy and paste the full URL of the article in the URL entry box and click the `Summarize` button. An example article would be [here](https://www.nature.com/articles/d41586-022-01730-y). Upon pasting the link in the URL entry box and clicking `Summarize`, the app will summarize the article as seen in the image below:

![image](https://user-images.githubusercontent.com/72810148/177449323-bd0a038d-4b02-4c0d-a311-bf16db1337fd.png)
