import unittest
from datetime import date, time, datetime, timedelta

class TestDatetimeLib(unittest.TestCase):

    def test_create_easter_2024_date(self):
        #Fixture Setup

        #Exercise SUT
        easter_2024 = date(2024, 3, 31)
        
        #Result Verification
        self.assertEqual(2024, easter_2024.year)
        self.assertEqual(3, easter_2024.month)
        self.assertEqual(31, easter_2024.day)

        #Fixture Teardown

    def test_create_beginning_of_class_time(self):
        #Fixture Setup

        #Exercise SUT
        beggining_of_class = time(8, 20, 0)

        #Result Verification
        self.assertEqual(8, beggining_of_class.hour)
        self.assertEqual(20, beggining_of_class.minute)
        self.assertEqual(0, beggining_of_class.second)

        #Fixture Teardown

    def test_create_beggining_of_year_2024_datetime(self):
        #Fixture Setup

        #Exercise SUT
        beggining_of_year = datetime(2024, 1, 1, 0, 0, 0, 0)

        #Result Verification
        self.assertEqual(0, beggining_of_year.microsecond)
        self.assertEqual(0, beggining_of_year.second)
        self.assertEqual(0, beggining_of_year.minute)
        self.assertEqual(0, beggining_of_year.hour)
        self.assertEqual(1, beggining_of_year.day)
        self.assertEqual(1, beggining_of_year.month)
        self.assertEqual(2024, beggining_of_year.year)

        #Fixture Teardown

    def test_sum_30_days_with_timedelta(self):
        #Fixture Setup
        beggining_of_year = datetime(2024, 1, 1, 0, 0, 0, 0)

        #Exercise SUT
        future_datetime_after_30_days = beggining_of_year + timedelta(days=30)

        #Result Verifications
        self.assertEqual(0, future_datetime_after_30_days.microsecond)
        self.assertEqual(0, future_datetime_after_30_days.second)
        self.assertEqual(0, future_datetime_after_30_days.minute)
        self.assertEqual(0, future_datetime_after_30_days.hour)
        self.assertEqual(31, future_datetime_after_30_days.day)
        self.assertEqual(1, future_datetime_after_30_days.month)
        self.assertEqual(2024, future_datetime_after_30_days.year)

        #Fixture Teardown

    def test_sum_60_days_with_timedelta(self):
        #Fixture Setup
        beggining_of_year = datetime(2024, 1, 1, 0, 0, 0, 0)

        #Exercise SUT
        future_datetime_after_30_days = beggining_of_year + timedelta(days=60)

        #Result Verifications
        self.assertEqual(0, future_datetime_after_30_days.microsecond)
        self.assertEqual(0, future_datetime_after_30_days.second)
        self.assertEqual(0, future_datetime_after_30_days.minute)
        self.assertEqual(0, future_datetime_after_30_days.hour)
        self.assertEqual(1, future_datetime_after_30_days.day)
        self.assertEqual(3, future_datetime_after_30_days.month)
        self.assertEqual(2024, future_datetime_after_30_days.year)

        #Fixture Teardown

    def test_create_invalid_date_with_negative_day(self):
        #Fixture Setup

        #Exercise SUT
        with self.assertRaises(ValueError):
            invalid_date = date(2024, 1, -1)

        #Result Verification
            
        #Fixture Teardown
            
    def test_create_invalid_date_with_negative_month(self):
        #Fixture Setup

        #Exercise SUT
        with self.assertRaises(ValueError):
            invalid_date = date(2024, -1, 1)

        #Result Verification
            
        #Fixture Teardown
            
    def test_create_invalid_date_with_negative_year(self):
        #Fixture Setup

        #Exercise SUT
        with self.assertRaises(ValueError):
            invalid_date = date(-2024, 1, 1)

        #Result Verification
            
        #Fixture Teardown
            
    def test_create_invalid_date_with_string_day(self):
        #Fixture Setup

        #Exercise SUT
        with self.assertRaises(TypeError):
            invalid_date = date(2024, 1, '1')

        #Result Verification
            
        #Fixture Teardown
            
    def test_create_invalid_date_with_string_month(self):
        #Fixture Setup

        #Exercise SUT
        with self.assertRaises(TypeError):
            invalid_date = date(2024, '1', 1)

        #Result Verification
            
        #Fixture Teardown
            
    def test_create_invalid_date_with_string_year(self):
        #Fixture Setup

        #Exercise SUT
        with self.assertRaises(TypeError):
            invalid_date = date('2023', 1, 1)

        #Result Verification
            
        #Fixture Teardown

    def test_replace_day_to_26(self):
        #Fixture Setup
        created_date = date(2024, 1, 1)

        #exercise SUT
        date_replaced_day = created_date.replace(day=26)

        #Result Verification
        self.assertEqual(26, date_replaced_day.day)

        #Fixture Teardown
        
    def test_replace_month_to_12(self):
        #Fixture Setup
        created_date = date(2024, 1, 1)

        #exercise SUT
        date_replaced_month = created_date.replace(month=12)

        #Result Verification
        self.assertEqual(12, date_replaced_month.month)

        #Fixture Teardown
        
    def test_replace_year_to_2023(self):
        #Fixture Setup
        created_date = date(2024, 1, 1)

        #exercise SUT
        date_replaced_year = created_date.replace(year=2023)

        #Result Verification
        self.assertEqual(2023, date_replaced_year.year)

        #Fixture Teardown

    def test_replace_hour_to_12(self):
        #Fixture Setup
        created_time = time(8, 20, 0)

        #exercise SUT
        time_replaced_hour = created_time.replace(hour=12)

        #Result Verification
        self.assertEqual(12, time_replaced_hour.hour)

        #Fixture Teardown

    def test_replace_minute_to_50(self):
        #Fixture Setup
        created_time = time(8, 20, 0)

        #exercise SUT
        time_replaced_minute = created_time.replace(minute=50)

        #Result Verification
        self.assertEqual(50, time_replaced_minute.minute)

        #Fixture Teardown

    def test_replace_second_to_1(self):
        #Fixture Setup
        created_time = time(8, 20, 0)

        #exercise SUT
        time_replaced_second = created_time.replace(second=1)

        #Result Verification
        self.assertEqual(1, time_replaced_second.second)

        #Fixture Teardown

    def test_invalid_replace_time_with_negative_hour(self):
        #Fixture Setup
        created_time = time(8, 20, 0)

        #exercise SUT
        with self.assertRaises(ValueError):
            invalid_rpleaced_time = created_time.replace(hour=-1)

        #Result Verification

        #Fixture Teardown
            
    def test_invalid_replace_time_with_negative_minute(self):
        #Fixture Setup
        created_time = time(8, 20, 0)

        #exercise SUT
        with self.assertRaises(ValueError):
            invalid_rpleaced_time = created_time.replace(minute=-1)

        #Result Verification

        #Fixture Teardown
            
    def test_invalid_replace_time_with_negative_second(self):
        #Fixture Setup
        created_time = time(8, 20, 0)

        #exercise SUT
        with self.assertRaises(ValueError):
            invalid_rpleaced_time = created_time.replace(second=-1)

        #Result Verification

        #Fixture Teardown
            
    def test_invalid_replace_time_with_string_hour(self):
        #Fixture Setup
        created_time = time(8, 20, 0)

        #exercise SUT
        with self.assertRaises(TypeError):
            invalid_rpleaced_time = created_time.replace(hour='1')

        #Result Verification

        #Fixture Teardown
            
    def test_invalid_replace_time_with_string_minute(self):
        #Fixture Setup
        created_time = time(8, 20, 0)

        #exercise SUT
        with self.assertRaises(TypeError):
            invalid_rpleaced_time = created_time.replace(minute='1')

        #Result Verification

        #Fixture Teardown
            
    def test_invalid_replace_time_with_string_second(self):
        #Fixture Setup
        created_time = time(8, 20, 0)

        #exercise SUT
        with self.assertRaises(TypeError):
            invalid_rpleaced_time = created_time.replace(second='1')

        #Result Verification

        #Fixture Teardown
        
    def test_invalid_replace_date_with_negative_year(self):
        #Fixture Setup
        created_date = date(2023, 11, 2)

        #exercise SUT
        with self.assertRaises(ValueError):
            invalid_rpleaced_date = created_date.replace(year=-2023)

        #Result Verification

        #Fixture Teardown
            
    def test_invalid_replace_date_with_negative_month(self):
        #Fixture Setup
        created_date = date(2023, 11, 2)

        #exercise SUT
        with self.assertRaises(ValueError):
            invalid_rpleaced_date = created_date.replace(month=-1)

        #Result Verification

        #Fixture Teardown
            
    def test_invalid_replace_date_with_negative_day(self):
        #Fixture Setup
        created_date = date(2023, 11, 2)

        #exercise SUT
        with self.assertRaises(ValueError):
            invalid_rpleaced_date = created_date.replace(day=-1)

        #Result Verification

        #Fixture Teardown

    def test_invalid_replace_date_with_string_year(self):
        #Fixture Setup
        created_date = date(2023, 11, 2)

        #exercise SUT
        with self.assertRaises(TypeError):
            invalid_rpleaced_date = created_date.replace(year='2023')

        #Result Verification

        #Fixture Teardown
            
    def test_invalid_replace_date_with_string_month(self):
        #Fixture Setup
        created_date = date(2023, 11, 2)

        #exercise SUT
        with self.assertRaises(TypeError):
            invalid_rpleaced_date = created_date.replace(year='12')

        #Result Verification

        #Fixture Teardown
            
    def test_invalid_replace_date_with_string_day(self):
        #Fixture Setup
        created_date = date(2023, 11, 2)

        #exercise SUT
        with self.assertRaises(TypeError):
            invalid_rpleaced_date = created_date.replace(year='22')

        #Result Verification

        #Fixture Teardown
            
    def test_invalid_replace_date_with_out_of_range_day(self):
        #Fixture Setup
        created_date = date(2023, 11, 2)

        #exercise SUT
        with self.assertRaises(ValueError):
            invalid_rpleaced_date = created_date.replace(day=33)

        #Result Verification

        #Fixture Teardown
            
    def test_invalid_replace_date_with_out_of_range_month(self):
        #Fixture Setup
        created_date = date(2023, 11, 2)

        #exercise SUT
        with self.assertRaises(ValueError):
            invalid_rpleaced_date = created_date.replace(month=13)

        #Result Verification

        #Fixture Teardown
            
    def test_invalid_replace_time_with_out_of_range_hour(self):
        #Fixture Setup
        created_time = time(2, 2, 2)

        #exercise SUT
        with self.assertRaises(ValueError):
            invalid_rpleaced_date = created_time.replace(hour=25)

        #Result Verification

        #Fixture Teardown
            
    def test_invalid_replace_time_with_out_of_range_minute(self):
        #Fixture Setup
        created_time = time(2, 2, 2)

        #exercise SUT
        with self.assertRaises(ValueError):
            invalid_rpleaced_date = created_time.replace(minute=72)

        #Result Verification

        #Fixture Teardown

if __name__ == '__main__':
    unittest.main()

