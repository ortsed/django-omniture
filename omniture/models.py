import re
from django.conf import settings
from datetime import datetime

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
		"search_results_count": 0,
		"site_format" : "",
		"media_type" : "regular",
		"tags": "",
		"section_slug":"",
        "oref": "",
		"omniture_domain":"122.2o7.net",
		"account": "",
		"_prop1": "",
		"_prop2": "",
		"_prop3": "",
		"_prop4": "",
		"_prop5": "",
		"_prop6": "",
		"_prop7": "",
		"_prop8": "",
		"_prop9": "",
		"_prop10": "",
		"_prop12": "",
		"_prop13": "",
		"_prop14": "",
		"_prop15": "",
		"_prop16": "",
		"_prop17": "",
		"_prop18": "",
		"_prop19": "",
		"_prop20": "",
		"_prop21": "",
		"_prop22": "",
		"_prop23": "",
		"_prop24": "",
		"_prop25": "",
		"_prop26": "",
		"_prop27": "",
		"_prop28": "",
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

	def __getattribute__(self, name):
		try:
			return object.__getattribute__(self, name)
		except:
			return ""
			
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

	# Getter functions
	def channel(self):
		return self.format(self.section)
		
	def server(self):
		return self.format(self.site)
		
	def pagename(self):
		return self.conjoin([self.title, self.section, self.author])

	def prop1(self):
		if self._prop1:
			return self.format(self._prop1)
		else:
			return self.search_terms
	
	def prop2(self):
		if self._prop2:
			return self.format(self._prop2)
		else:
			return self.search_results_count

	def prop3(self):
		if self._prop3:
			return self.format(self._prop3)
		else:
			return self.conjoin([self.title, self.section, self.author])
		
	def prop4(self):
		if self._prop4:
			return self.format(self._prop4)
		else:
			return self.url
		
	def prop5(self):
		if self._prop5:
			return self.format(self._prop5)
		else:
			return self.format(self.subsection)
		
	def prop6(self):
		if self._prop6:
			return self.format(self._prop6)
		else:
			return self.section
		
	def prop7(self):
		if self._prop7:
			return self.format(self._prop7)
		else:
			return self.conjoin([self.section, self.subsection])
		
	def prop8(self):
		if self._prop8:
			return self.format(self._prop8)
		else:
			return self.conjoin([self.section, self.subsection, self.type])
		
	def prop9(self):
		if self._prop9:
			return self.format(self._prop9)
		else:
			return self.format(self.subsection)
		
	def prop10(self):
		return self.format(self._prop10)
		
	def prop11(self):
		if self._prop11:
			return self.format(self._prop11)
		elif isinstance(self.date, datetime):
			return self.date.strftime("%H:00")
		else:
			return self.date
			
	def prop12(self):
		if self._prop12:
			return self.format(self._prop12)
		elif isinstance(self.date, datetime):
			return self.date.strftime("%A")
		else:
			return self.date
			
	def prop13(self):
		if self._prop13:
			return self.format(self._prop13)
		elif isinstance(self.date, datetime) and self.date.strftime("%w") > 4:
			return "weekend"
		else:
			return "weekday"
	
	def prop14(self):
		if self._prop14:
			return self.format(self._prop14)
		else:
			return self.oref
	
	def prop15(self):
		if self._prop15:
			return self.format(self._prop15)
		else:
			return self.format(self.author)

	def prop16(self):
		if self._prop16:
			return self.format(self._prop16)
		else:
			try:
				return self.conjoin(self.tags, separator=":")
			except AttributeError:
				return ""

	def prop17(self):
		if self._prop17:
			return self.format(self._prop17)
		else:
			return self.title

	def prop18(self):
		if self._prop18:
			return self.format(self._prop18)
		elif isinstance(self.date, datetime):
			return self.date.strftime("%B %d, %Y %I:%M %p").lower()
		else:
			return self.date

	def prop19(self):
		if self._prop19:
			return self.format(self._prop19)
		else:
			return self.pagename()

	def prop20(self):
		return self.format(self._prop20)


	def prop21(self):
		if self._prop21:
			return self.format(self._prop21)
		elif self.prop20():
			return "|".join([self.prop19()[0:25], self.prop20()[0:25]])
		else:
			return self.prop19()
			

	def prop22(self):
		return self.format(self._prop22)


	def prop23(self):
		if self._prop23:
			return self.format(self._prop23)
		else:
			return self.site_format
		
	def prop24(self):
		if self._prop24:
			return self.format(self._prop24)
		else:
			return self.media_type
		
	def prop25(self):
		if self._prop25:
			return self.format(self._prop25)
		else:
			return self.media_type
		
	def prop26(self):
		if self._prop26:
			return self.format(self._prop26)
		else:
			return self.media_type
		
	def prop27(self):
		return self.format(self._prop27)

		
	def hier1(self):
		return self.conjoin([self.section, self.subsection, self.type, self.title], separator="/")
		
	def hier2(self):
		return ""
		
	def hier3(self):
		return ""
