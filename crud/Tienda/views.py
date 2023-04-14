from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from Tienda.models import Comic, Profile, Mensaje
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def about(request):
    return render(request, "Tienda/about.html")

def index(request):
    context = {
        "comics": Comic.objects.all()
    }
    return render(request, "Tienda/index.html", context)

class ComicList(ListView):
    model = Comic
    context_object_name = "comics"

class ComicDetail(DetailView):
    model = Comic
    
class ComicCreate(LoginRequiredMixin, CreateView):
    model = Comic
    success_url = reverse_lazy("comic-list")
    fields = ['comic','tomo', 'titulo', 'info', 
                'precio','imagen']


    def form_valid(self, form):
        form.instance.publisher = self.request.user
        return super().form_valid(form)

class ComicUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comic
    success_url = reverse_lazy("comic-list")
    fields = ['comic','tomo', 'titulo', 'info', 
                'precio','imagen']

    def test_func(self):
        user_id = self.request.user.id
        comic_id = self.kwargs.get('pk')
        return Comic.objects.filter(publisher=user_id, id=comic_id).exists()

    def handle_no_permission(self):
        return render(self.request, "Tienda/not_found.html")

class ComicDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comic
    success_url = reverse_lazy("comic-list")

    def test_func(self):
        user_id = self.request.user.id
        comic_id = self.kwargs.get('pk')
        return Comic.objects.filter(publisher=user_id, id=comic_id).exists()

    def handle_no_permission(self):
        return render(self.request, "Tienda/not_found.html")


class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('profile-create')


class Login(LoginView):
    next_page = reverse_lazy("comic-list")

class Logout(LogoutView):
    template_name = 'registration/logout.html'

class ProfileCreate(LoginRequiredMixin, CreateView):
    model = Profile
    success_url = reverse_lazy("comic-list")
    fields = ['instagram','imagen']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProfileUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    success_url = reverse_lazy("comic-list")
    fields = ['instagram','imagen']

    def test_func(self):
        user_id = self.request.user.id
        profile_id = self.kwargs.get('pk')
        return Profile.objects.filter(user=user_id, id=profile_id).exists()

    def handle_no_permission(self):
        return render(self.request, "Tienda/not_found.html")


class MensajeCreate(CreateView):
    model = Mensaje
    success_url = reverse_lazy('mensaje-create')
    fields = '__all__'

class  MensajeList(LoginRequiredMixin, ListView):
    model = Mensaje
    context_object_name = "mensajes"
    
    def get_queryset(self):
        return Mensaje.objects.filter(destinatario=self.request.user.id).all()

class MensajeDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model= Mensaje
    success_url = reverse_lazy("mensaje-list")

    def test_func(self):
        user_id = self.request.user.id
        mensaje_id = self.kwargs.get('pk')
        return Mensaje.objects.filter(destinatario=user_id).exists()

    def handle_no_permission(self):
        return render(self.request, "Tienda/not_found.html")


