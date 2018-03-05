from django.shortcuts import render, redirect
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