from banco.banco import Banco

hoteis = Banco()

hotel1 = dict(nome="Hotel Plaza",  classificacao=4, preco=340, ano="1985-09-15",
              endereco=dict(rua="7 de Setembro", cidade="Blumenau", uf="SC", regiao="1"),
              comodidades=dict(piscina=1, academia=1, refeicoes=1))
hotel2 = dict(nome="Hotel Ibiz",  classificacao=2, preco=120, ano="2005-11-10",
              endereco=dict(rua="XV de Novembro", cidade="Blumenau", uf="SC", regiao="1"),
              comodidades=dict(piscina=0, academia=1, refeicoes=1))

# hoteis.remove_hotel("Hotel Plaza")
# hoteis.insert_hotel(hotel1)
# hoteis.insert_hotel(hotel2)
# hoteis.remove_hotel("Hotal Plaza")

# novos_valores = dict(nome="Plaza Hotel", classificacao=5, preco=586)
# hoteis.update_hotel("Hotel Plaza", **novos_valores)
# hoteis.update_hotel("Plaza Hotel", classificacao=4)
# hoteis.get_all()

