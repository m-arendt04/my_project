from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from scraper_bs4.scrape_functions import scrape_budim, scrape_dd, scrape_victoria
from my_flat.models import Post, Topics


class MainPage(View):

    def get(self, request):
        return render(request, 'my_flat/main_page.html')


# Think about how to split this three functions into one.
class DevInvestmentBud(View):

    def get(self, request):
        scrape_budim()
        ctx = {
            "ctx": scrape_budim()
        }
        return render(request, 'my_flat/dev_investment.html', ctx)


class DevInvestmentDD(View):

    def get(self, request):
        scrape_dd()
        ctx = {
            "ctx": scrape_dd()
        }
        return render(request, 'my_flat/dd_invest.html', ctx)


class DevInvestmentVictoria(View):

    def get(self, request):
        scrape_victoria()
        ctx = {
            "ctx": scrape_victoria()
        }
        return render(request, 'my_flat/victoria_invest.html', ctx)


# class not in use
class ForumView(View):

    def get(self, request):
        topics = {
            'topics': Topics.objects.all()
        }
        # print(Topics.objects.get(pk=1).title)
        return render(request, 'my_flat/main_forum_view.html', topics)


class PostsListView(View):
    # model = Post
    # template_name = 'my_flat/forum_view.html'
    # context_object_name = 'posts'
    # ordering = ['date_posted']
    def get(self, request, pk):
        posts = Post.objects.filter(topic_id=pk)
        ctx = {
            'posts': posts,
            'topic_id': pk
        }
        return render(request, 'my_flat/forum_view.html', ctx)


class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdatePostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):  # iheritance order is important
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class DeletePostView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
