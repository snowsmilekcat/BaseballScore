from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import redirect#リダイレクト機能のインポート
from django.urls import reverse_lazy
from django.views import generic#汎用クラスベースビュー機能のインポート
from django.views.generic import FormView, CreateView, ListView, UpdateView
from .models import User#Userモデルのインポート
from .forms import UserForm#定義したフォームをインポート

# Create your views here.
#def user_list(request,id):
def user_list(request):
    users = User.objects.values('id','name','back_number','position')
    pageId = {"users":users
             ,"pageId":"user_list"}
    return render(request, 'user/user_list.html', pageId)

def user_main(request):
    pageId = {"pageId":"user_main"}
    return render(request, 'user/user_main.html', pageId)

#def user_create(request):
    #users = User.objects.values('id','name','back_number','position')
    #form = UserForm()#インポートしたモデルフォームのインスタンス化
    #pageId = {"users":users
             #,"pageId":"user_create"
             #,"form":form}
    #return render(request, 'user/user_edit.html', pageId)

#def user_create(request):
    #users = User.objects.values('id','name','back_number','position')
    #if request.method == "POST":#リクエストがPOSTとしてきているかを確認
       #form = UserForm(request.POST)#インポートしたモデルフォームのインスタンス化
       #if form.is_valid():#一通りの検証処理を実行
          #user = form.save(commit=False)
          #user.author = request.user
          #user.published_date = timezone.now()
          #user.save()
          #return redirect('user_list')#登録成功後は、一覧へリダイレクトさせる。
    #else:
       #form = UserForm()
       #pageId = {"users":users
                #,"pageId":"user_create"
                #,"form":form}
       #return render(request, 'user/user_edit.html', pageId)#新規登録画面へ遷移

#def user_update(request,userId):
    #if request.method == "POST":#リクエストがPOSTとしてきているかを確認
       #user = User.objects.filter(id=userId)
       #pageId = {"user":user
                #,"pageId":"user_update2"
                #,"form":form}
       #return render(request, 'user/user_update.html', pageId)#編集画面へ遷移

    #else:
       #user = User.objects.values('id','name','back_number','position','sub_position').filter(id=userId)
       #form = UserForm()
       #pageId = {"user":user
                #,"pageId":"user_update"
                #,"form":form}
       #return render(request, 'user/user_update.html', pageId)#編集画面へ遷移

class user_index(generic.ListView):#  generic.ListViewを継承
    model = User# 使用するモデル
    paginate_by = 5# 1ページあたりの表示件数をカスタマイズ
    ordering = ['-created_date']# 並び順を更新時刻が新しい順にカスタマイズ
    template_name = 'user/user_index.html' # 表示に使用するテンプレート

    def get_context_data(self, **kwargs):#ジェネリックビューでパラメータを渡すときに使用
        context = super().get_context_data(**kwargs) # はじめに継承元のメソッドを呼び出す
        context["pageId"] = "user_index"
        return context

class user_detail(generic.DetailView):
    model = User
    template_name = 'user/user_detail.html'

    def get_context_data(self, **kwargs):#ジェネリックビューでパラメータを渡すときに使用
        context = super().get_context_data(**kwargs) # はじめに継承元のメソッドを呼び出す
        context["pageId"] = "user_detail"
        return context

class user_create(generic.edit.CreateView):
    model = User
    form_class = UserForm
    template_name = 'user/user_create.html'
    success_url = reverse_lazy('user_index')

    def get_context_data(self, **kwargs):#ジェネリックビューでパラメータを渡すときに使用
        context = super().get_context_data(**kwargs) # はじめに継承元のメソッドを呼び出す
        context["pageId"] = "user_create"
        return context

class user_update(UpdateView):
    model = User
    #fields = ['name', 'back_number','position','sub_position']
    form_class = UserForm
    template_name = 'user/user_update.html'
    success_url = reverse_lazy('user_index')

    def get_context_data(self, **kwargs):#ジェネリックビューでパラメータを渡すときに使用
        context = super().get_context_data(**kwargs) # はじめに継承元のメソッドを呼び出す
        context["pageId"] = "user_update"
        return context

class user_delete(generic.edit.DeleteView):
    model = User
    template_name = 'user/user_delete.html'
    success_url = reverse_lazy('user_index')

    def get_context_data(self, **kwargs):#ジェネリックビューでパラメータを渡すときに使用
        context = super().get_context_data(**kwargs) # はじめに継承元のメソッドを呼び出す
        context["pageId"] = "user_delete"
        return context
