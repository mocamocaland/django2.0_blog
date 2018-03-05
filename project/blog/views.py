from django.shortcuts import render, redirect, get_object_or_404
from .forms import DayCreateForm
from .models import Day


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
