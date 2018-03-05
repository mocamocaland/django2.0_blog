from django.shortcuts import render, redirect
from .forms import DayCreateForm


def index(request):
    return render(request, 'blog/day_list.html')


def add(request):
    # 送信内容を基にフォームを作る。POSTでなければ空フォーム
    form = DayCreateForm(request.POST or None)

    # method=POST,送信ボタンを押した時、入力内容が問題なければ
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('diary:index')

    # 通常のアクセスページや、入力内容に誤りがあればまたぺーじを表示
    context = {
        'form': form
    }
    return render(request, 'blog/day_form.html', context)