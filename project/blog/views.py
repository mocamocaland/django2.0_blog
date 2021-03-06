from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .forms import DayCreateForm
from .models import Day


class IndexView(generic.ListView):
    model = Day
    paginate_by = 3 # 3件ずつ


class AddView(LoginRequiredMixin, generic.CreateView):
    model = Day
    form_class = DayCreateForm # fields = '__all__'でもかける
    success_url = reverse_lazy('blog:index') # /blog/


class UpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Day
    form_class = DayCreateForm
    success_url = reverse_lazy('blog:index')

class DeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Day
    success_url = reverse_lazy('blog:index')


class DetailView(generic.DetailView):
    model = Day

 
'''
def index(request):
    context = {
        'day_list': Day.objects.all(),
    }
    return render(request, 'blog/day_list.html', context)


def add(request):
    # 送信内容を基にフォームを作る。POSTでなければ空フォーム
    form = DayCreateForm(request.POST or None)

    # method=POST,送信ボタンを押した時、入力内容が問題なければ
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('blog:index')

    # 通常のアクセスページや、入力内容に誤りがあればまたぺーじを表示
    context = {
        'form': form
    }
    return render(request, 'blog/day_form.html', context)


def update(request, pk):
    # urlのpkを基にDayを取得
    day = get_object_or_404(Day, pk=pk)

    #フォームに取得したDayを紐付ける
    form = DayCreateForm(request.POST or None, instance=day)

    # method=POST, つまり送信ボタンを押した時、入力なうように問題がなければ
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('blog:index')

    # 通常時のページアクセスや、入力内容に誤りがあればまたページを表示
    context = {
        'form': form,
    }
    return render(request, 'blog/day_form.html', context)

def delete(request, pk):
    # urlのpkを基にDayを取得
    day = get_object_or_404(Day, pk=pk)

    # method=POST, つまり送信ボタンを押した時、入力なうように問題がなければ
    if request.method == 'POST':
        day.delete()
        return redirect('blog:index')

    # 通常時のページアクセスや、入力内容に誤りがあればまたページを表示
    context = {
        'day': day,
    }
    return render(request, 'blog/day_confirm_delete.html', context)


def detail(request, pk):
    # urlのpkを基にDayを取得
    day = get_object_or_404(Day, pk=pk)

    # 通常時のページアクセスや、入力内容に誤りがあればまたページを表示
    context = {
        'day': day,
    }
    return render(request, 'blog/day_detail.html', context)
'''
