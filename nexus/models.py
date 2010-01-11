from django.db import models

SHORT = 5
STD = 50
LONG = 100
XLONG = 200


class Publisher(models.Model):
	name = models.CharField(max_length=STD)

	def __unicode__(self):
		return self.name


class Author(models.Model):
	last_name = models.CharField(max_length=STD)
	first_name = models.CharField(max_length=STD)
	middle_name = models.CharField(max_length=STD, blank=True)

	def __unicode__(self):
		return "%s, %s %s" % (self.last_name, self.first_name, self.middle_name)


class Patron(models.Model):
	patron_no = models.CharField(max_length=SHORT)
	last_name = models.CharField(max_length=STD)
	first_name = models.CharField(max_length=STD)
	middle_name = models.CharField(max_length=STD, blank=True)

	def __unicode__(self):
		return "%s: %s, %s %s" % (self.patron_no, self.last_name, self.first_name, self.middle_name)

class ShelfLocation(models.Model):
	code = models.CharField(max_length=SHORT)
	name = models.CharField(max_length=STD)

	def __unicode__(self):
		return self.name


class Material(models.Model):
	call_number = models.CharField(max_length=SHORT)
	title = models.CharField(max_length=STD)
	shelf_loc = models.ForeignKey(ShelfLocation)
	acquired = models.DateField()
	keywords = models.TextField(blank=True)


class Book(Material):
	BOOK_FORMAT_CHOICES = (
		(u'PB', u'Paperback'),
		(u'HB', u'Hardback'),
	)
	subtitle = models.CharField(max_length=XLONG, blank=True)
	pages = models.IntegerField(null=True, blank=True)
	publisher = models.ForeignKey(Publisher)
	format = models.CharField(max_length=SHORT, choices=BOOK_FORMAT_CHOICES)
	author = models.ForeignKey(Author)

	def __unicode__(self):
		return self.title


class Checkout(models.Model):
	book = models.ForeignKey(Book)
	patron = models.ForeignKey(Patron)
	co_date = models.DateTimeField(auto_now=True)
	due = models.DateField()

	def __unicode__(self):
		return unicode(self.co_date)


class Checkin(models.Model):
	checkout = models.ForeignKey(Checkout)
	ci_date = models.DateTimeField()

	def __unicode__(self):
		return unicode(self.ci_date)

