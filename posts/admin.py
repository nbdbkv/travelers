from django.contrib import admin

from posts.models import Country, Tag, PostImage, Post


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'alpha2Code', 'alpha3Code', 'capital', 'region')
    list_display_links = list_display
    search_fields = list_display
    ordering = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 0


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('topic', 'user', 'country', 'is_shown')
    list_display_links = list_display
    inlines = (PostImageInline,)
