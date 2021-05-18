from django import template
from lists import models as list_models

register = template.Library()


@register.simple_tag(takes_context=True)
def on_favs(context, room):
    user = context.request.user
    try:
        the_rooms_list = list_models.List.objects.get_or_none(user=user, name="My Favorite Places").rooms.all()
    except (AttributeError, TypeError) as error:
        the_rooms_list = []
    return room in the_rooms_list