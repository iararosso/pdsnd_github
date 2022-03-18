import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data from Motivate!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT:
    city = input("Would you like to see data for Chicago, New York or Washington?").lower()
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Which month? All, January, February, March, April, May or June?").lower()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday?").lower()

    print('-'*40)
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
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    most_common_month = df['month'].mode()[0]
    print ("Most common month:", most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df['day'].mode()[0]
    print ("Most common day:", most_common_day)

    # TO DO: display the most common start hour
    most_common_hour = df['hour'].mode()[0]
    print ("Most common start hour:", most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print("Most common start station:", start_station)
    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print("Most common end station:", end_station)
    # TO DO: display most frequent combination of start station and end station trip
    combination =  (df['Start Station'] + df['End Station']).mode() [0]
    print("Most common Start End Station combination: ", combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = (df['Trip Duration'].sum())/60
    print("Total travel time(minutes):", int(total_travel_time))
    # TO DO: display mean travel time
    mean_travel_time = (df['Trip Duration'].mean())/60
    print("Mean travel time(minutes):", int(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df["User Type"].value_counts()
    print("User types:", user_types)

    # TO DO: Display counts of gender
    if  "Gender" in df:
        gender_types = df["Gender"].value_counts()
        print("Gender:", gender_types)
    else:
        print('No gender information')

    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df:
        oldest_customer = pd.Series(df['Birth Year'].min()) [0]
        youngest_customer = pd.Series(df['Birth Year'].max()) [0]
        most_common_year_birth = pd.Series(df['Birth Year'].mode())[0]

        print ("The oldest customer was born in", int(oldest_customer))
        print ("The youngest customer was born in", int(youngest_customer))
        print ("The most common curstomer's year of birth:", int(most_common_year_birth))
    else:
        print('No Birth year information')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """
    Ask the user if he/she want to see 5 lines of raw data.
    Returns 5 lines of raw data if user inputs `yes`.
    Iterates until user enter `no`
    """

    teste = 0
    while True:
        answer = input('Do you want to see 5 lines of raw data? Enter yes or no: ')
        if answer.lower() == 'yes':
            print(df.iloc[teste:teste+5, :])
            teste += 5
        else:
            break
def main():
    while True:
        city, month, day = get_filters()
        try:
            df = load_data(city, month, day)
        except:
            print("oh no, invalid entry! Please enter a valid input")
            continue

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)



        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
