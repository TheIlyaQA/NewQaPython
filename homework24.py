dates = ['14-Dec', '12-Apr', '13-Apr', '31-Dec', '1-Jan', '12-Jan']
month_to_num = {
    'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
    'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
}
sorted_dates = sorted(dates, key=lambda date: (month_to_num[date.split('-')[1]], int(date.split('-')[0])))
print(sorted_dates)  # ['1-Jan', '12-Jan', '12-Apr', '13-Apr', '14-Dec', '31-Dec']
