from coffin.template import Library, Context
from coffin.template.loader import get_template

register = Library()



@register.object
def omniture_embed(omniture):
	
	dict = {"omniture": omniture}
	ctx = Context(dict)
	return get_template('embed.html').render(ctx)