# Streamlit Indian Startup Funding Data Visualization

This project aims to visualize Indian startup funding data using pandas and Plotly for interactive plots. The project is built using Streamlit, a popular Python library for building web applications. The dataset used for analysis is sourced from Kaggle, specifically the <a href="https://www.kaggle.com/datasets/sudalairajkumar/indian-startup-funding" target="_blank" > Indian Startup Funding </a> dataset.

## Features

The website provides a comprehensive set of visualizations and analysis for the Indian startup funding dataset. The features and sections of the website are as follows:

### Section 1: Overall Analysis

Upon landing on the website, the user is presented with an overall analysis of startups and investors. This section includes the following metrics:

1. Total Investments Made So Far: Displays the total amount of investments made in startups.

2. Maximum Investment: Shows the highest investment amount made in a startup.

3. Average Investment: Displays the average investment amount across all startups.

4. Total Funded Startups: Shows the total count of startups that received funding.

Following the metrics, the section includes the following visualizations:

1. Month-on-Month Line Graph - Total Amount of Funding: Shows the trend of the total amount of funding over different months.

2. Month-on-Month Line Graph - Total Funded Startups: Displays the trend of the number of funded startups over different months.

3. Line Graph - Total Funded Indian Startups Month-on-Month: Illustrates the trend of the number of funded Indian startups over different months.

4. Horizontal Bar Graph - Top 10 Most Funded Sectors (2015-2020): Shows the top 10 sectors that received the most funding between 2015 and 2020.

5. Horizontal Bar Graph - Top Investors by Investment Value: Displays the top investors based on their investment values.

6. 3D Bar Graph - Top 10 Most Funded Startups (Year-on-Year): Shows the top 10 startups that received the most funding in each year.

7. Horizontal Bar Graph - Top 10 Most Funded Cities: Illustrates the top 10 cities with the most funded startups.

8. Horizontal Bar Graph - Top 10 Most Funded Types of Rounds: Shows the top 10 types of funding rounds that received the most funding.

At the end of this section, a Heatmap is provided to visualize the funding amount by year and month.

### Section 2: Startup Analysis

In this section, users can select an individual startup from a dropdown menu to view specific analysis for that startup. The section includes the following:

1. Selected Startup Name: Displays the name of the selected startup.

2. Streamlit Metrics:
   - Total Investments (In Crore Rs): Shows the total amount of investments made in the selected startup.
   - Sector of Startup: Displays the sector to which the selected startup belongs.
   - Subsector of Startup: Shows the subsector of the selected startup.
   - Stage of Funding: Displays the funding stage at which the selected startup was funded.
   - Investors: Lists the investors who have funded the selected startup.

Following the metrics, a subsection titled "Similar Startups" displays other startups belonging to the same sector as the selected startup.

### Section 3: Investor Analysis

Similar to the startup analysis section, this section allows users to select an individual investor from a dropdown menu for specific analysis. The section includes the following:

1. Selected Investor Name: Displays the name of the selected investor.

2. Recent Investments Dataframe: Shows a dataframe consisting of the five most recent investments made by the selected investor. The columns include:
   - Date of Investment
   - Startup Name
   - Vertical
   - City
   - Investors

Following the dataframe, the section includes the following visualizations:

1. Bar

 Chart - Biggest Investments: Illustrates the biggest investments made by the selected investor in terms of amount.

2. Pie Chart - Most Invested City: Displays the city in which the selected investor has made the most investments in terms of amount.

3. Pie Chart - Most Invested Sector: Shows the sector in which the selected investor has made the most investments in terms of amount.

4. Pie Chart - Most Invested Subsector: Illustrates the subsector in which the selected investor has made the most investments in terms of amount.

5. Pie Chart - Most Invested Investment Type: Displays the investment type in which the selected investor has made the most investments in terms of amount.

6. Line Graph - Year-on-Year Investment: Shows the year-on-year trend of investments made by the selected investor in terms of amount.

At the end of the section, a subsection titled "Similar Investors" displays four investors who have invested in the same sectors as the selected investor.


## Running the Application

To run the web application locally, follow these steps:

1. Clone the GitHub repository to your local machine.

2. Ensure that you have Python installed (recommended version: Python 3.7+).

3. Open a terminal or command prompt and navigate to the project directory.

4. Install the required Python packages by running the following command:

   ```shell
   pip install -r requirements.txt
   ```

5. Once the dependencies are installed, start the application by running the following command:

   ```shell
   streamlit run app.py
   ```

6. The application will start running, and the terminal will display a local URL (e.g., `http://localhost:8501`).

7. Open a web browser and enter the URL displayed in the terminal to access the web application.

8. Interact with the different sections and features of the web application to explore the Indian startup funding data visualizations.

Note: The application requires an internet connection to access the Plotly library for generating interactive plots.

## Conclusion

The Streamlit Indian Startup Funding Data Visualization project provides an interactive web interface for exploring and analyzing the Indian startup funding dataset. The website offers comprehensive visualizations, metrics, and analysis for overall startup and investor insights, as well as individual startup and investor analysis. Users can navigate through the various sections and explore the data using interactive plots, dropdown menus, and tooltips for additional information.

By leveraging the power of pandas, Plotly, and Streamlit, this project enables users to gain valuable insights into the Indian startup funding ecosystem and make data-driven decisions.
