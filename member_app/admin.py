from django.contrib import admin
from .models.member_model import Member

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_blocked', 'active_loans_count', 'overdue_loans_count')
    list_filter = ('is_blocked',)
    search_fields = ('user__username', 'user__email')

    def active_loans_count(self, obj):
        return obj.user.loan_set.filter(return_date__isnull=True).count()
    
    def overdue_loans_count(self, obj):
        from datetime import timedelta
        from django.utils.timezone import now
        return obj.user.loan_set.filter(
            return_date__isnull=True, 
            loan_date__lt=now().date() - timedelta(days=7)
        ).count()
