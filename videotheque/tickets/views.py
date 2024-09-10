from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required # Permet de vérifier si l'utilisateur est connecté 
from django.http import HttpResponseForbidden
from django.core.paginator import Paginator

from django.template.loader import render_to_string

# Create your views here.

@login_required
def creer_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.auteur = request.user
            ticket.save()
            return redirect('liste_tickets')

    else: 
        form = TicketForm()

    return render(request, 'creer_ticket.html', {'form': form})





"""
Si on avait plusieurs tickets on pourrait utiliser la pagination et éviter de charger trop d'éléments dans la page
=> Utiliser Django Paginator (import)
"""
# def liste_tickets(request):
#     tickets = Ticket.objects.all()
#     return render(request, 'liste_tickets.html', {'tickets': tickets})

def liste_tickets(request):
    tickets_liste = Ticket.objects.all()
    paginator = Paginator(tickets_liste, 10)
    page_number = request.GET.get('page')
    tickets = paginator.get_page(page_number)
    return render(request, 'liste_tickets.html', {'tickets': tickets})



@login_required
def modifier_ticket(request, pk):
    ticket = get_object_or_404(Ticket, id=pk)
    if ticket.auteur != request.user and not request.user.is_superuser:
        return HttpResponseForbidden('Vous n\'avez pas le droit de modifier ce ticket')
    
    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('liste_tickets')
        
    else: 
        form = TicketForm(instance=ticket)

    return render(request, 'modifier_ticket.html', {'form': form})




@login_required
def supprimer_ticket(request, pk):
    ticket = get_object_or_404(Ticket, id=pk)
    if ticket.auteur != request.user and not request.user.is_superuser:
        return HttpResponseForbidden('Vous n\'avez pas le droit de supprimer ce ticket')
    
    ticket.delete()
    return redirect('liste_tickets')


    