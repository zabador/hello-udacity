import webapp2
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
	<label>Month <input type="text" name="month" value="%(month)s"></label>
	<label>Day <input type="text" name="day" value="%(day)s"></label>
	<label>Year <input type="text" name="year" value="%(year)s"></label>
	<div style="color: red">%(error)s</div>
	<input type='submit'>
</form>
"""
class MainPage(webapp2.RequestHandler):

	def write_form(self, error="", month="", day="", year=""):
		self.response.out.write(form % {"error": error, "month": cgi.escape(month), "day": cgi.escape(day), "year": cgi.escape(year)})
	def get(self):
		self.write_form(form)
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
			self.redirect("/thanks")

class ThanksHandler(webapp2.RequestHandler):
	def get(self):
		self.response.out.write("Thanks! That's is a valid day")

app = webapp2.WSGIApplication([
	('/', MainPage),
	('/thanks', ThanksHandler),
], debug=True)
