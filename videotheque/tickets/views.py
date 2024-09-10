from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required # Permet de vérifier si l'utilisateur est connecté 
from django.http import HttpResponseForbidden

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



def liste_tickets(request):
    tickets = Ticket.objects.all()
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


    