from django.shortcuts import render, redirect, get_object_or_404

from .models import Messages,report


# Create your views here.


def favoriteMessage(request, idMessage):
    if request.method == "POST":
        message = get_object_or_404(Messages, pk=idMessage)
        favr = message.favorite
        print(message.favorite)
        message.favorite = not favr
        print(message.favorite)
        message.save()
        return redirect("account:dashboard")
    else:
        return redirect("account:dashboard")


def deleteMessage(request, idMessage):
    if request.method == "POST":
        message = get_object_or_404(Messages, pk=idMessage)
        message.delete()
        return redirect("account:dashboard")
    else:
        return redirect("account:dashboard")


def reportMessage(request, idMessage):
    if request.method == "POST":
        message = get_object_or_404(Messages, pk=idMessage)
        favr = message.notreport
        print(message.notreport)
        message.notreport = not favr
        print(message.notreport)
        message.save()
        re = report(mess=message)

        re.save()
        return redirect("account:dashboard")
    else:
        return redirect("account:dashboard")
