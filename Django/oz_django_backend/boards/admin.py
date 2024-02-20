from django.contrib import admin
from .models import Board

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('title','writer','date','likes','content','updated_at','created_at',)  # 모여지는 항목들
    list_filter = ('date','writer') # 필터  
    search_fields = ('title','content') # 검색 가능 항목
    ordering = ('-date',) # 순서 date / -date
    readonly_fields = ('writer',)   # 수정할 수 없는 데이터로 변경
    fieldsets = (
        (None, {'fields': ('title', 'content')}),
        ('숨기기', {'fields': ('writer', 'likes', 'reviews'), 'classes': ('collapse',)}),
    ) # 'Advanced options' 은 원하는 내용으로 수정 가능

    list_per_page = 1 # 목록 페이지에 표시할 항목

    actions = ('increment_likes',)

    def increment_likes(self, request, queryset):
        # 선택된 게시글들에 대해 'likes' 수를 1씩 증가
        for board in queryset:
            board.likes += 1
            board.save()
    increment_likes.short_description = "선택된 게시글의 좋아요 수 증가"