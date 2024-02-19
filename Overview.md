# Pandas: Python Data Analysis Library

### What is Pandas?

Pandas, meaning **Pan**el **Da**ta Analysi**s**, is a widely-used open-source Python library for working with data [[ref]](https://www.w3schools.com/python/pandas/pandas_intro.asp#:~:text=What%20is%20Pandas%3F,by%20Wes%20McKinney%20in%202008.).<br>


### Why use Pandas?

When it comes to data, Pandas does just about everything:

- **Data Importing**<br>
Pandas provides methods of importing large datasets in several formats [[ref]](https://pandas.pydata.org/pandas-docs/stable/reference/io.html). In my EA, I've chosen a simple CSV file, but Pandas supports a myriad of other formats - such as Excel, JSON, HTML, and more. In-taking such a large dataset without Pandas, using the base Python File I/O methods, would be messy and hard to manage.

- **Data Manipulation**<br>
Pandas grants capabilities for filtering, sorting, and merging data [[ref]](https://pandas.pydata.org/docs/user_guide/merging.html). In my EA, I use Pandas to filter out irrelevant movies from the dataset to create a DataFrame that acts as a view for the particular preferences the user has inputed.

- **Data Analysis**<br>
Pandas is also capable of descriptive statistics, data visualization, and time series analysis [[ref]](https://pandas.pydata.org/docs/user_guide/visualization.html). These features are beyond the scope of the program I've created, but they are still of note as they are among the key features that make Pandas so popular. Graphically, Pandas lets you plot line charts, box plots, bar plots, scatter plots - all the plots [[ref]](https://pandas.pydata.org/docs/user_guide/visualization.html#basic-plotting-plot).

**For this project in particular:** I wanted to use a library for manipulating datasets. I've always known that Python was the language of choice for data scientists, however, I never had any hands-on experience working with large datasets myself. By undertaking some basic Pandas, I was able to build a simple program that sifts through thousands of rows to return the ones I want - which I think is pretty neat.  

### Why should you keep using Pandas?

Learning Pandas is essentially learning Python. In practice, most people will use atleast a few different supplemental packages/libraries when they are using Python. Depending on your ambitions, Pandas and packages like it are especially important if you want to do data science related tasks. Working with large datasets is often necessary even outside pure data science - so it's good to have some experience with a library like this. However, in my case, I don't work with large datasets regularly, so I probably will not pursue Pandas much further - but I would recommend to anyone learning Python to try it out.
