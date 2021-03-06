# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.core.cache import cache
from django.views.generic import ListView, DetailView

from .models import Category, Story
from config.models import SideBar


def cache_it(func):
    def wrapper(self, *args, **kwargs):
        key = repr((func.__name__, args, kwargs))
        result = cache.get(key)
        if result:
            print('Hit cache')
            return result
        print('Hit db')
        result = func(self, *args, **kwargs)
        cache.set(key, result, 60*5)
        return result
    return wrapper


class CommonMixin(object):
    @cache_it
    def get_category_context(self):
        """ 分类
          1、导航分类 nav_cates= Category.objects.filter(is_nav=True)
          2、普通分类 cates = Category.objects.filter(is_nav=False)
        """
        categories = Category.objects.all()
        nav_cates = []
        cates = []
        for category in categories:
            if category.is_nav:
                nav_cates.append(category)
            else:
                cates.append(category)
        return {
            'nav_cates': nav_cates,
            'cates': cates,
        }

    def get_context_data(self, **kwargs):
        sidebar = SideBar.objects.all()
        hot_reading = Story.objects.filter(status=1).order_by('-pv')[:5]
        recently_book = Story.objects.filter(status=1)[:5]
        kwargs.update({
            'sidebars': sidebar,
            'hot_readings': hot_reading,
            'recently_books': recently_book, })
        kwargs.update(self.get_category_context())
        return super(CommonMixin, self).get_context_data(**kwargs)


class BaseBookView(CommonMixin, ListView):
    """
    1、IndexView和CategoryView都是指向book的，所以这里创建一个父类，缩短代码
    """
    model = Story
    template_name = 'book/list.html'
    context_object_name = 'books'
    paginate_by = 4


class IndexView(BaseBookView):
    def get_queryset(self):
        query = self.request.GET.get('query')
        qs = super(IndexView, self).get_queryset()
        if query:
            qs = qs.filter(name__icontains=query)
        return qs

    def get_context_data(self, **kwargs):
        query = self.request.GET.get('query')
        return super(IndexView, self).get_context_data(query=query)


class CategoryView(BaseBookView):
    def get_queryset(self):
        qs = super(CategoryView, self).get_queryset()
        cate_id = self.kwargs.get('category_id')
        qs = qs.filter(category_id=cate_id)
        return qs


class BookView(CommonMixin, DetailView):
    model = Story
    template_name = 'book/detail.html'
    context_object_name = 'story'

    def get(self, request, *args, **kwargs):
        # 覆写get方法是因为每当文章被访问一次，pvuv就+1
        # get方法会返回一个HttpResponse实例
        response = super(BookView, self).get(request, *args, **kwargs)
        self.pv_uv()
        return response

    def pv_uv(self):
        sessionid = self.request.COOKIES.get('sessionid')
        if not sessionid:
            return

        # set(key, value, timeout) get(key)
        # key必须是str
        pv_key = 'pv:%s:%s' % (sessionid, self.request.path)
        if not cache.get(pv_key):
            self.object.increase_pv()
            cache.set(pv_key, 1, 30)

        uv_key = 'uv:%s:%s' % (sessionid, self.request.path)
        if not cache.get(uv_key):
            self.object.increase_uv()
            cache.set(uv_key, 1, 60*60*24)


# def get_common_context():
#     """ 分类
#        1、导航分类 nav_cates= Category.objects.filter(is_nav=True)
#        2、普通分类 cates = Category.objects.filter(is_nav=False)
#     """
#     categories = Category.objects.all()
#     nav_cates = []
#     cates = []
#     for category in categories:
#         if category.is_nav:
#             nav_cates.append(category)
#         else:
#             cates.append(category)
#
#     sidebar = SideBar.objects.all()
#     hot_reading = Story.objects.filter(status=1)[:5]
#     recently_book = Story.objects.filter(status=1)[:5]
#
#     context = {
#         'nav_cates': nav_cates,
#         'cates': cates,
#         'sidebars': sidebar,
#         'hot_readings': hot_reading,
#         'recently_books': recently_book,
#     }
#     return context

#
# def book_list(request, category_id=None):
#     page = request.GET.get('page', 1)
#     page_size = 4
#     try:
#         page = int(page)
#     except TypeError:
#         page = 1
#
#     queryset = Story.objects.all()
#     if category_id:
#         queryset = queryset.filter(category_id=category_id)
#
#     paginator = Paginator(queryset, page_size)
#     try:
#         books = paginator.page(page)
#     except EmptyPage:
#         books = paginator.page(paginator.num_pages)
#
#     context = {
#         'books': books,
#     }
#     common_comtext = get_common_context()
#     # 把common_context添加到context中
#     context.update(common_comtext)
#     return render(request, 'book/list.html', context=context)
#
#
# def book_detail(request, pk=None):
#     try:
#         queryset = Story.objects.get(pk=pk)
#     except queryset.DoesNotExist:
#         return Http404('Book is not exist!')
#     context = {
#         'story': queryset,
#     }
#     common_context = get_common_context()
#     context.update(common_context)
#     return render(request, 'book/detail.html', context=context)
