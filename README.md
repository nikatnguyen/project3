# project3


    We used a Global Country Information Dataset 2023 provided from Kaggle to compare the life expectancies of each country with their respective out of pocket health expenses, their forested area percentages, and their total tax rates. Our base assumptions going into this are that:
    
    -Countries with higher out of pocket health expenses are going to have a shorter life expectancy 
    -Countries with higher percentages of forested area are going to have a higher life expectancy
    -Countries with higher total tax rates are going to have a higher life expectancy
    
    We ultimately found that there was little evidence to suggest a correlation between our chosen variables and life expectancy.

    Link to server: https://project3-visuals.onrender.com/

    HOW TO USE SERVER:
    -Dropdown tool used for only the first visualization, shows distinct selected country in red and other countries in blue
    -Hovering over each point will tell you about the country's forestation percentage and life expectancy
 
 
        #FILES BY FOLDER
        -world-data-2023.csv (dataset downloaded from Kaggle) 
        -project3_db.sql (sql database)
        
        Adina
        -ForestedAreas.ipynb (jupyter notebook)
        -SQL code (code to create table)
        -Resources/Forested_Areas.csv (cleaned csv file)
        -Resources/world-data-2023.csv (dataset downloaded from Kaggle)

        Anika
        -/NguyenAnika Tax Rate Life Expectancy DataFrame & Cleanup.ipynb (jupyter notebook)
        -tax_rate_df.csv (cleaned csv file)
        -tax_rate_life_expectancy.png (image of scatter plot)
        -world-data-2023.csv (dataset downloaded from Kaggle) 

        Garrett
        -out_of_pocket_df.csv (cleaned csv file)
        -out_of_pocket_expenditure_life_expectancy.png (image of scatter plot)
        -out_of_pocket_life_expectancy.ipynb (jupyter notebook)
        -world-data-2023.csv (dataset downloaded from Kaggle) 

        visual_app>src
        -__init__.py (automated)
        -app.py(app for visualization deploy)
        -requirements.txt

