
# def zoffoli_rompe(a:int,b:str,c:str):
#     "questa funzione restituisce il momento esatto in cui Zoffoli ti romperà i maroni"
#     giorni_sett=["Lunedì","Martedì","Mercoledì","Giovedì","Venerdi"]
#     materie=["ML","Inglese","SQL","Python","Statistica","Excel"]
#     a=input("Che giorno è oggi?")
#     b=input("Che materia c'è alla prima ora? ML,Inglese,SQL,Python,Statistica,Excel")
#     c=input("Hai preso il caffè al bar di via AldoMoro? y/n")
#     if c=="y":
#         print("La rottura di maroni arriverà al tra il minuto 1 e il minuto 3. Evita")
#     for day in giorni_sett:
#         for mat in materie:

# from prova2livello.formule import formula_quadrato as f

# # # ris= f(3,5.3)
# # # print(ris)

from prova2livello.formule import Rettangolo

mark = Rettangolo(2,3)

print(mark.area_rettangolo())

print(mark.perimetro_rettangolo())

print(mark.volume_parallelep(5))

from prova2livello.formule import Statistics

pippo = Statistics(100,20,1.2)
print(pippo.coefficiente_variazione(3.5))
print(pippo.mediana())






