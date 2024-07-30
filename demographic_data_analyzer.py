import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    CSV_path = "/workspace/boilerplate-demographic-data-analyzer/adult.data.csv"
    df = pd.read_csv(CSV_path)

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    men_df = df[df['sex'] == 'Male']
    average_age_men = men_df['age'].mean()

    # What is the percentage of people who have a Bachelor's degree?
    bachelors_count = df[df['education'] == 'Bachelors'].shape[0]
    total_count = df.shape[0]
    percentage_bachelors = (bachelors_count / total_count) * 100

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education_0 = ['Bachelors', 'Masters', 'Doctorate']
    higher_edu_df = df[df['education'].isin(higher_education_0)]
    high_income_higher_edu_df = higher_edu_df[higher_edu_df['salary'] == '>50K']
    higher_education = (len(high_income_higher_edu_df) / len(higher_edu_df)) * 100

    non_higher_education = ~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    high_income = df['salary'] == '>50K'
    non_higher_education_high_income_df = df[non_higher_education & high_income]
    non_higher_education_df = df[non_higher_education]
    lower_education = (len(non_higher_education_high_income_df) / len(non_higher_education_high_income_df)) * 100

    # percentage with salary >50K
    higher_education_rich = higher_education
    lower_education_rich = lower_education

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df['hours-per-week'].min()

    min_hours_df = df[df['hours-per-week'] == num_min_workers]

    rich_min_hours_df = min_hours_df[min_hours_df['salary'] == '>50K']

    if len(min_hours_df) > 0:  
        rich_percentage = (len(rich_min_hours_df) / len(min_hours_df)) * 100
    else:
        rich_percentage = 0  

    # What country has the highest percentage of people that earn >50K?
    total_count = df.groupby('native-country').size()
    high_income_count = df[df['salary'] == '>50K'].groupby('native-country').size()
    percentage_high_income = (high_income_count / total_count) * 100
    highest_earning_country = percentage_high_income.idxmax()
    highest_earning_country_percentage = percentage_high_income.max()

    # Identify the most popular occupation for those who earn >50K in India.
    india_df = df[df['native-country'] == 'India']

    high_income_india_df = india_df[india_df['salary'] == '>50K']

    top_IN_occupation = high_income_india_df['occupation'].mode()[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
calculate_demographic_data()
