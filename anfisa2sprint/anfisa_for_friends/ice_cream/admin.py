from django.contrib import admin

# Register your models here.
# Из модуля models импортируем модель Category.
from .models import Category, Topping, Wrapper, IceCream


# Этот вариант сработает для всех моделей приложения.
# Вместо пустого значения в админке будет отображена строка "Не задано".
admin.site.empty_value_display = 'Не задано'


# Создаём класс, в котором будем описывать настройки админки:
class IceCreamAdmin(admin.ModelAdmin):
    # Какие поля будут показаны на странице списка объектов.
    list_display = (
        'title',
        'description',
        'is_published',
        'is_on_main',
        'category',
        'wrapper'
    )
    # Какие поля можно редактировать прямо на странице списка объектов.
    list_editable = (
        'is_published',
        'is_on_main',
        'category'
    )
    # кортеж с перечнем полей, по которым будет проводиться поиск. 
    search_fields = ('title',)
    #  кортеж с полями, по которым можно фильтровать записи. 
    list_filter = ('category',)
    # указывают поля, при клике на которые можно перейти на страницу просмотра и редактирования записи.
    list_display_links = ('title',)
    # Это свойство сработает для всех полей этой модели.
    # Вместо пустого значения будет выводиться строка "Не задано".
    # empty_value_display = 'Не задано'
    # Указываем, для каких связанных моделей нужно включить такой интерфейс:
    filter_horizontal = ('toppings',)


# Подготавливаем модель IceCream для вставки на страницу другой модели.
class IceCreamInLine(admin.StackedInline):
    model = IceCream
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        IceCreamInLine,
    )


# ...и регистрируем её в админке:
admin.site.register(Category, CategoryAdmin)
admin.site.register(Topping)
admin.site.register(Wrapper)

# Регистрируем новый класс: 
# указываем, что для отображения админки модели IceCream
# вместо стандартного класса нужно использовать класс IceCreamAdmin 
admin.site.register(IceCream, IceCreamAdmin)

