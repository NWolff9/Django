from django.shortcuts import render

def index(request):

    dados = {
        1:{"nome":"Nebulosa de Carina",
            "legenda":"Nasa"},
        2:{"nome":"Gamora",
            "legenda":"Alura"},
        3:{"nome":"Aurora boreal",
            "legenda":"irmão urso"},
        4:{"nome":"luzinha no ceu",
            "legenda":"discovery"}
    }

    return render(request,'galeria/index.html', {"cards":dados})

def imagem(request):
    return render(request,'galeria/imagem.html')
