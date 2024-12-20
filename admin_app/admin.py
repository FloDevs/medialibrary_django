from django.contrib import admin
from .models.loan_model import Loan
from .models.book_model import Book
from .models.dvd_model import Dvd
from .models.cd_model import Cd
from .models.board_game_model import BoardGame


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ('member', 'get_media_title', 'loan_date', 'return_date', 'is_overdue', 'is_active_loan')
    list_filter = ('return_date',)
    search_fields = ('member__username', 'get_media_title')  # Remarque : il faut media__name ici
    actions = ['mark_as_returned']

    def get_media_title(self, obj):
        
        return str(obj.media)  # Appelle la méthode __str__ de Media (et donc Book, CD, DVD)

    get_media_title.short_description = 'Titre du Média'  
    
    def is_overdue(self, obj):
        """ Indique si l'emprunt est en retard """
        from datetime import timedelta
        from django.utils.timezone import now
        if obj.return_date is None and obj.loan_date < now().date() - timedelta(days=7):
            return True
        return False

    is_overdue.boolean = True

    def is_active_loan(self, obj):
        """ Indique si l'emprunt est toujours actif """
        return obj.return_date is None

    is_active_loan.boolean = True

    @admin.action(description='Marquer comme retourné')
    def mark_as_returned(self, request, queryset):
        for loan in queryset:
            loan.return_media()
        self.message_user(request, f"{queryset.count()} emprunts marqués comme retournés.")

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'is_available')
    list_filter = ('is_available',)
    search_fields = ('name', 'author')

@admin.register(Cd)
class CDAdmin(admin.ModelAdmin):
    list_display = ('name', 'artist', 'is_available')
    list_filter = ('is_available',)
    search_fields = ('name', 'artist')

@admin.register(Dvd)
class DVDAdmin(admin.ModelAdmin):
    list_display = ('name', 'director', 'is_available')
    list_filter = ('is_available',)
    search_fields = ('name', 'director')

@admin.register(BoardGame)
class BoardGameAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ()
    search_fields = ('name', 'creator')