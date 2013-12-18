import webapp2

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


def valid_month(month):
		if month.capitalize() in months:
			return month.capitalize

def valid_day(day):
	if day.isdigit():
		if int(day) in range(1,32):
			return int(day)

def valid_year(year):
	if year.isdigit():
		if int(year) in range(1900,2020):
			return int(year)
	

form="""
<form method='post'> 
	What is you birthday
	<br>
	<input type="text" name="month" value="%(month)s">
	<input type="text" name="day" value="%(day)s">
	<input type="text" name="year" value="%(year)s">
	<div style="color: red">%(error)s</div>
	<input type='submit'>
</form>
"""
class MainPage(webapp2.RequestHandler):

	def write_form(self, error="", month="", day="", year=""):
		self.response.out.write(form % {"error": error, "month": month, "day": day, "year": year})
	def get(self):
		self.response.out.write(form)
	def post(self):
		user_month = self.request.get('month')
		user_day = self.request.get('day')
		user_year = self.request.get('year')

		month = valid_month(user_month)
		day = valid_day(user_day)
		year = valid_year(user_year)
		
		if not (month and day and year):
			self.write_form("That is not valid", user_month, user_day, user_year)
		else:
			self.write_form("Thanx that is a valid day")


app = webapp2.WSGIApplication([
	('/', MainPage),
], debug=True)
