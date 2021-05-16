from django.contrib import admin
from . import models
from django.utils.html import mark_safe
# Register your models here.

@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        "name", "used_by"
    )

    def used_by(self,obj):
        return obj.rooms.count()
    pass


class PhotoInLine(admin.TabularInline):

    model = models.Photo



@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition"""

    inlines = (PhotoInLine,)


    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "address", "price", "city")},
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
        "total_rating",
        "count_reviews",
        "id"
    )

    list_filter = (
        "host__superhost",
        "room_type",
        "amenities",
        "facilities",
        "city",
        "country",
        "instant_book",
        "created",
    )

    raw_id_fields = ("host",)

    search_fields = ("=city","^host__username","name","id")

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

    count_photos_short_description = 'Photo Count'

    def count_reviews(self,obj):
        return obj.reviews.count()

    count_reviews_short_description = 'Review Count'


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """Photo Admin Definition"""

    list_display = (
        '__str__',
        'get_thumbnail',
    )

    def get_thumbnail(self, obj):
        print(obj.file.url)
        return mark_safe(f'<img width = "50px" src = "{obj.file.url}"/>')

    get_thumbnail_short_description = "Thumbnail"