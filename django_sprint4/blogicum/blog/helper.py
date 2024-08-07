from django.core.paginator import Paginator
from django.db.models import Count
from django.utils import timezone

from .constants import PAGINATOR_PER_PAGE


def get_published_posts(queryset):
    return (get_all_posts(queryset).filter(
            pub_date__lte=timezone.now(),
            is_published=True,
            category__is_published=True))


def get_all_posts(queryset):
    return (
        queryset.objects.select_related(
            'category',
            'location',
            'author'
        )
    )


def annotate_comments(queryset):
    return (queryset
            .annotate(comment_count=Count('comments'))
            .order_by('-pub_date'))


def paginate_queryset(request, queryset):
    paginator = Paginator(queryset, PAGINATOR_PER_PAGE)
    page_number = request.GET.get('page')
    return paginator.get_page(page_number)
