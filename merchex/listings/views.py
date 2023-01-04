from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from listings.models import Band
from listings.models import Listing
from listings.forms import BandForm, ListingForm, ContactUsForm
from django.core.mail import send_mail
from django.shortcuts import redirect


# from rest_auth.registration.views import VerifyEmailView, RegisterView


def band_list(request):
    bands = Band.objects.all()
    return render(request,
                  'listings/band_list.html',
                  {'bands': bands})


# listings/views.py
def band_detail(request, id):  # notez le paramètre id supplémentaire
    band = Band.objects.get(id=id)
    return render(request,
                  'listings/band_detail.html',
                  {'band': band})  # nous passons l'id au modèle


# def listing(request):
def listing_list(request):
    articles = Listing.objects.all()
    return render(request,
                  'listings/listing_list.html',
                  {'articles': articles})


def listing_detail(request, id):  # notez le paramètre id supplémentaire

    article = Listing.objects.get(id=id)
    return render(request,
                  'listings/listing_detail.html',
                  {'article': article})  # nous passons l'id au modèle


def contact(request):

    #print('La méthode de requête est : ', request.method)
    #print('Les données POST sont : ', request.POST)

    if request.method == 'POST':
        # créer une instance de notre formulaire et le remplir avec les données POST
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
            )
            # si le formulaire n'est pas valide, nous laissons l'exécution continuer jusqu'au return
            # ci-dessous et afficher à nouveau le formulaire (avec des erreurs).
        #return redirect('email-sent')  # ajoutez cette instruction de retour. FAUX:
        #EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' suffit pour afficher
        # en console

    else:
        # ceci doit être une requête GET, donc créer un formulaire vide
        form = ContactUsForm()

    return render(request, 'listings/contact.html', {'form': form})


def about(request):
    return render(request,
                  'listings/about.html'
                  )


def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect('band-detail', band.id)
    else:
        form = BandForm()
    return render(request, 'listings/band_create.html', {'form': form})


def band_update(request, id):
    band = Band.objects.get(id=id)

    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('band-detail', kwargs={'id': band.id}))
    else:
        form = BandForm(instance=band)

    return render(request, 'listings/band_update.html', {'form': form})


def listing_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('listing-detail', article.id)
    else:
        form = ListingForm()
    return render(request, 'listings/listing_create.html', {'form': form})


def data_update(request, id):
    article = Listing.objects.get(id=id)

    if request.method == 'POST':
        form = ListingForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('listing-detail', kwargs={'id': article.id}))
    else:
        form = ListingForm(instance=article)

    return render(request, 'listings/data_update.html', {'form': form})


def band_del(request, id):
    band = Band.objects.get(id=id)

    if request.method == 'POST':
        band.delete()
        return HttpResponseRedirect(reverse('band-list'))

    return render(request, 'listings/band_del.html', {'band': band})


def listing_del(request, id):
    article = Listing.objects.get(id=id)

    if request.method == 'POST':
        article.delete()
        return HttpResponseRedirect(reverse('listing-list'))

    return render(request, 'listings/listing_del.html', {'article': article})

