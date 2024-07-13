from django.utils import timezone

from .models import Post


def get_queryset():
    return (
        Post.objects.select_related(
            'category',
            'location',
            'author'
        ).filter(
            pub_date__lte=timezone.now(),
            is_published=True,
            category__is_published=True
        )
    )
