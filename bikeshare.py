import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello there!, this is the US bikeshare databse')
    print('discover usefull insights about US bikeshare by eploring the database', '\n')
    
    valid_cities = ['chicago' , 'new york city', 'washington']
    valid_months = ['all','january','febuary','march','april','may','june']
    valid_days = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    
    print(f'valid cities are: {valid_cities}\nvalid months type are: {valid_months}\nvalid day format are: {valid_days}', '\n')
    print('Let\'s do some exploration')
    
    city = ""
    month = ""
    day = ""
    success = True
    # get user input for city
    while success is True:
        city_input = (input("which city you would like to explore. chicago, new york city, or washington? ")).lower()
        if city_input in valid_cities:
            city = city_input
            break
        else:
            print('wrong input. please enter either chicago, new york city, or washington')
        success = True
        
    # get user input for month (all, january, ...  june)
    while success is True:
        month_input = (input('which month would you like to filter by? (january, february, ... , june) or all: ')).lower()
        if month_input in valid_months:
            month = month_input
            break
        else:
            print('wrong input. please refer to the acceptable month list above')
        success = True
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while success is True:
        day_input = (input('which day of the week would you like to filter by? (sunday, monday, ... , saturday) or all: ')).lower()
        if day_input in valid_days:
            day = day_input
            break
        else:
            print('wrong input. please refer to the acceptable days list above')
            success = True
    print('-'*40)
    print('calculating statistics')
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('The most freqent month integer is', df['month'].mode()[0])

    # display the most common day of week
    print(f'The most freqent day is:', df['day_of_week']..mode()[0])
   
    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].value_counts().idxmax()
    print(f'The most freqent hour is: {common_hour}')
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40, '\n')
    print('calculating next statistics')

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #display most commonly used start station
    popular_start_station = df['Start Station'].value_counts().idxmax()
    print(f'The most common start station is: {popular_start_station}')

    #display most commonly used end station
    popular_end_station = df['End Station'].value_counts().idxmax()
    print(f'The most commonly used end station is: {popular_end_station}')

    #display most frequent combination of start station and end station trip
    df['concat_stations'] = df['Start Station'] + ' -- ' + df['End Station']
    most_frequent_combined_station = df['concat_stations'].value_counts().idxmax()
    print(f'The most commonly used combined station is: {most_frequent_combined_station}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40, '\n')
    print('calculating next statistics')


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print(f'Total travel time is:', df['Trip Duration'].sum())
    # display average travel time
    print(f'The average trip duration is:', df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40, '\n')
    print('calculating next statistics')

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('what are the user type brreakdowns?')
    user_types = df['User Type'].value_counts()
    try:
        print(user_types, '\n')
    except KeyError as err:
        print(f'KeyError occurred: {err}')
    print('calculating next statistics', '\n')

    # Display counts of gender
    print('what is the breakdown of users by gender?')
    
    try:
        gender = df['Gender'].value_counts()
        print(gender, '\n')
    except KeyError:
        print('Error: there is no gender column in the dataframe')
    print('calculating next statistics', '\n')

    # Display earliest, most recent, and most common year of birth
    print('what are the earliest, most recent, and most common year of birth?')
    try:
        print(f"The oldest rider was born in: ", df['Birth Year'].min())
        print(f"The youngest rider was born in: ", df['Birth Year'].max())
        print(f"The most frequent riders were born in: ", df['Birth Year'].mode()[0])
    except KeyError:
        print("Error : Birth Year column Does not exist in this Dataframe")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print('done calculating' '\n')
    
def display_raw_data(df):
    """Displays 5 rows repeatedly of individual trip data based on user choice."""
    print('\ndisplaying individual trip data...\n')
    start_time = time.time()
    
    view_data = (input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')).lower()
    start_loc = 0
    while view_data != 'no':
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()
    print('you are no longer viewing individual trip data')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
