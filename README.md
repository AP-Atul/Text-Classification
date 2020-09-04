# Text-Classification
For perfoming text classification we need some kind of labelled dataset. So the first thought came to mind was to find a dataset on Kaggle and use sklearn functions and walla text classification.

But that's no fun. I wanted to learn scraping and collecting data and going through the process of pre-processing data, so here's a implementation.

So I needed a candidate for scraping, also I needed to label the dataset. Also, I wanted to do text processing on my mother tongue 'Marathi'. Finally decided to scrap news headlines, since they each have category, so if I scrap each category, I will have data and labels. Easy so I implemented the scraper with beautiful soup. After running into multiple issue finised the scraper and it worked.
It's not much but it's honest work ;)

After scraping and labelling, created a data frame and created a standard csv file. 

Then with sklearn I trained a model and got good accuracy, might improve the code later on, but for now I'm satisfied with it. First time text processing on data collected by myself.

## Execution 

* All files are independent, you can use the scraper file to scrap the new website, since it is specifically implemented for ABP Live Marathi, it will only work on that site.

* I have also provided my collected and processed csv file, you can directly do classification on that.

* Preprocessing file in really not that important since we have really a small amount of data and we don't want to remove stop words and stemming unnecessarily.


