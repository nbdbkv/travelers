from django.contrib import admin

from posts.models import Country, Tag, PostImage, Comment, Post


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


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'parent', 'text')
    list_display_links = list_display
    inlines = (CommentInline,)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related('post', 'parent')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('topic', 'user', 'country', 'is_shown')
    list_display_links = list_display
    inlines = (PostImageInline, CommentInline)
