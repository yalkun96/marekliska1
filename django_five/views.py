from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import get_template
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from django.core.paginator import Paginator

from .models import *
from .forms import *



def home(request):
    user = request.user
    data = Article.objects.all()
    username = User.objects.all()
    paginator = Paginator(data, 2)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'django_five/home.html', {'data': data, 'username': username, 'page_obj': page_obj})


def search(request):
    if request.method == 'POST':
        search_query = request.POST.get('search', '')
        if search_query:
            venue = Article.objects.filter(content__icontains=search_query)
            return render(request, 'django_five/search.html', {'search_query': search_query, 'venue': venue})
        else:
            return render(request, 'django_five/not_found_exception.html')
    else:
        return render(request, 'django_five/not_found_exception.html')

def contact(request):
    task = Article.objects.all()
    contacts = ContactInfo.objects.all()
    context = {}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_message(form.cleaned_data['name'], form.cleaned_data['email'], form.cleaned_data['message'])
            messages.success(request, 'Thank you!')
            form = ContactForm()

    else:
        form = ContactForm()

    return render(request, 'django_five/contact.html', {'form': form, 'context': context, 'contacts': contacts, 'task': task})



def send_message(name, email, message):
    text = get_template('django_five/message.html')
    html = get_template('django_five/message.html')
    context = {'name': name, 'e-mail': email, 'message': message}
    subject = "Message from user"
    from_email = 'from@example.com'
    text_content = text.render(context)
    html_content = text.render(context)

    msg = EmailMultiAlternatives(subject, text_content, from_email, ['manager@example.com'])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()


class AddNoteView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = AddForm
    template_name = 'django_five/addartice.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



@login_required
def edit(request, slug):
    model = get_object_or_404(Article, slug=slug)
    if request.user != model.user:
        return render(request, 'django_five/exceptions.html')

    form = AddForm(instance=model)

    if request.method == 'POST':
        form = AddForm(request.POST, instance=model)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'django_five/updatearticle.html', {'form': form})


@login_required
def delete_post(request, slug):
    model = get_object_or_404(Article, slug=slug)
    if request.user != model.user:
        return render(request, 'django_five/exceptions.html')

    if request.method == 'GET':
        return render(request, 'django_five/delete_page.html', {'model': model})

    elif request.method == 'POST':
        model.delete()
        return redirect('home')

def article(request, slug):
    post = get_object_or_404(Article, slug=slug)
    review = ReviewModel.objects.all()

    return render(request, 'django_five/article.html', {'post': post, 'review': review})
@login_required()
def leave_comment(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ReviewForm()
    return render(request, 'django_five/leave_comment.html', {'form': form})

