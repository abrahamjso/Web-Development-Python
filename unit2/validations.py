import cgi

months = ['January',
			'February',
			'March',
			'April',
			'May',
			'June',
			'July',
			'August',
			'September',
			'October',
			'November',
			'December']

month_abbvs = dict((m[:3].lower(), m) for m in months)

def valid_month(month):
	if month:
		short_month = month[:3].lower()
		return month_abbvs.get(short_month)

def valid_day(day):
	if day and day.isdigit():
		day = int(day)
		if 0 < day <= 31:
			return day

def valid_year(year):
	if year and year.isdigit():
		year= int(year)
		if 1900 < year <= 2020:
			return year

def escape_html(s):
	return cgi.escape(s, quote = True)