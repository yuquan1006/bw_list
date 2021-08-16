from django.contrib import admin
from bw_list_search.models import Bw_list
# Register your models here.
admin.site.site_header = '黑白名单后台'  # 设置header
admin.site.site_title = '黑白名单后台'  # 设置title
admin.site.index_title = '黑白名单后台'



@admin.register(Bw_list)
class Bw_listAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_name', 'type', 'status', 'detail')
    list_per_page = 30
    ordering = ('-id',)
    search_fields = ('company_name',)
    list_editable = ('detail',)

