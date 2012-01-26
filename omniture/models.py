import re
from django.conf import settings

class Omniture(object) :

	defaults = {
		"debug" : False,
		"site" : "",
		"url" : "",
		"section" : "",
		"subsection" : "",
		"date" : "",
		"title" : "",
		"type" : "misc",
		"author" : "",
		"search_terms" : "",
		"site_format" : "",
		"media_type" : "regular",
		"tags": "",
		"section_slug":""
	}

	def __init__(self, section_slug=None, **kwargs):
		"""
		Creates an omniture obj with values loaded from settings.OMNITURE_DEFAULTS or **kwargs if there are any
		"""
		attrs = {}
		attrs.update(self.defaults)
		if hasattr(settings, 'OMNITURE_DEFAULTS'):
			attrs.update(settings.OMNITURE_DEFAULTS)
		attrs.update(kwargs)
		self.__dict__.update(attrs)

		super(Omniture, self).__init__()

	def __getattr__(self, name):
		""" If the requested attribute is not set, return the default version
		"""
		return self.defaults[name]

	#Utility functions 
	def format(self, text):

		if hasattr(text, "__iter__"):
			return ":".join(map(format, text))
		
		text = re.sub(r"[^A-Za-z0-9\s]+", "", unicode(text))
		text = re.sub("  ", " ", unicode(text))
		return text.lower()
		
	def conjoin(self, values, separator=" - "):

		# Filter out blank spaces and None values
		f = lambda x: False if x == "" or x is None else True
		values = filter(f, values)

		# Format the values
		values = map(self.format, values)

		return separator.join(values)
	
	#Setter functions
	def mobile(self):
		self.site_format = "mobile"
		
	def slideshow(self):
		self.media_type = "slideshow"

	def landing(self):
		self.type = "landing"
		return ""

	# Getter functions
	def channel(self):
		return self.format(self.section)
		
	def server(self):
		return self.format(self.site)
		
	def pagename(self):
		return self.conjoin([self.title, self.section, self.author])

	def prop1(self):
		return ""
	
	def prop2(self):
		return ""
	
	def prop3(self):
		return self.conjoin([self.title, self.section, self.author])
		
	def prop4(self):
		return self.url
		
	def prop5(self):
		return self.format(self.subsection)
		
	def prop6(self):
		return self.section
		
	def prop7(self):
		return self.conjoin([self.section, self.subsection])
		
	def prop8(self):
		return self.conjoin([self.section, self.subsection, self.type])
		
	def prop9(self):
		return self.format(self.subsection)
		
	def prop10(self):
		return ""
		
	def prop11(self):
		return ""
	
	def prop12(self):
		return ""

	def prop13(self):
		return ""
	
	def prop14(self):
		return ""
		
	def prop15(self):
		return self.format(self.author)

	def prop16(self):
		try:
			return self.conjoin(self.tags, separator=":")
		except AttributeError:
			return ""

	def prop17(self):
		return self.title

	def prop18(self):
		if self.date != "":
			return self.date.strftime("%B %d, %Y %I:%M %p").lower()
		else:
			return self.date

	def prop19(self):
		return self.pagename()

	def prop20(self):
		return ""

	def prop21(self):
		if self.prop20():
			return "|".join([self.prop19()[0:25], self.prop20()[0:25]])
		else:
			return self.prop19()
			
	def prop22(self):
		return ""

	def prop23(self):
		return self.site_format
		
	def prop24(self):
		return self.media_type
		
	def prop25(self):
		return self.media_type
		
	def prop26(self):
		return self.media_type
		
	def prop27(self):
		return ""
		
	def hier1(self):
		return self.conjoin([self.section, self.subsection, self.type, self.title], separator="/")
		
	def hier2(self):
		return ""
		
	def hier3(self):
		return ""
