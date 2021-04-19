from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        "name", "used_by"
    )

    def used_by(self,obj):
        return obj.rooms.count()
    pass



@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition"""


    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "address", "price")},
        ),
        (
            "Times",
            {"fields": ("check_in", "check_out", "instant_book",)}
        ),
        (
            "More about the Space",
            
            {
                "classes": ("collapse",),
                "fields": ("amenities", "house_rules", "facilities",)
            }
        ),
        (
            "Spaces",
            {"fields": ("beds", "bedrooms", "baths")}
        ),
        (
            "Last Details",
            {"fields": ("host",)}
        ),
    )

    ordering = ('name', 'price')

    list_display = (
        "name",
        "description",
        "country",
        "city",
        "price",
        "address",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
    )

    list_filter = (
        "host__superhost",
        "room_type",
        "amenities",
        "facilities",
        "city",
        "country",
        "instant_book"
    )


    search_fields = ("=city","^host__username", )

    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rules",
    )

    pass


    def count_amenities(self, obj):
        return obj.amenities.count()

    def count_photos(self,obj):
        return obj.photos.count()



@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """Photo Admin Definition"""

    pass