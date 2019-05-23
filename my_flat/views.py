from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from scraper_bs4.scrape_functions import scrape_budim, scrape_dd, scrape_victoria

from my_flat.models import Post, Topics
from scraper_bs4.models import BudimexInfo, DomDevelopmentInfo


class MainPage(View):
    def get(self, request):
        return render(request, 'my_flat/main_page.html')


class DevInvestmentBud(View):
    def get(self, request):
        all_investments = BudimexInfo.objects.all()
        ctx = {
            "all_investments": all_investments
        }
        return render(request, 'my_flat/budimex_investment.html', ctx)


class DevInvestmentDD(View):
    def get(self, request):
        all_investments = DomDevelopmentInfo.objects.all()
        ctx = {
            "all_investments": all_investments
        }
        return render(request, 'my_flat/dd_invest.html', ctx)


class DevInvestmentVictoria(View):
    def get(self, request):
        scrape_victoria()
        ctx = {
            "ctx": scrape_victoria()
        }
        return render(request, 'my_flat/victoria_invest.html', ctx)


class ForumView(ListView):
    model = Topics
    template_name = 'my_flat/main_forum_view.html'
    context_object_name = 'topics'
    ordering = ['date_posted']
    paginate_by = 5


class CreateNewTopic(LoginRequiredMixin, CreateView):
    model = Topics
    fields = ['title']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('main-forum')


class DeleteTopicView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Topics

    def test_func(self):
        topic = self.get_object()
        if self.request.user == topic.author:
            return True
        return False

    def get_success_url(self):
        return reverse_lazy('main-forum')


class PostsListView(ListView):
    model = Post
    template_name = 'my_flat/topic_posts_view.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.filter(topic_id=self.kwargs['pk']).order_by('date_posted')

    def get_context_data(self, **kwargs):
        context = super(PostsListView, self).get_context_data(**kwargs)
        context['topic_id'] = self.kwargs['pk']
        return context


class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.topic_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('forum-topic-posts', kwargs={'pk': self.kwargs['pk']})


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

    def get_success_url(self):
        current_post = Post.objects.get(pk=self.kwargs['pk'])
        topic_id = current_post.topic_id
        return reverse_lazy('forum-topic-posts', kwargs={'pk': topic_id})


class DeletePostView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def get_success_url(self):
        current_post = Post.objects.get(pk=self.kwargs['pk'])
        topic_id = current_post.topic_id
        return reverse_lazy('forum-topic-posts', kwargs={'pk': topic_id})

