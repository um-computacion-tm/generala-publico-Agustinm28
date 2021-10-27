import unittest
from generala import Jugadores, Dados, Tabla, Generala


class TestJugadores(unittest.TestCase):     

    def test_agregar_jugadores(self):
        jugadores_e = Jugadores()
        jugadores_e.cantidad = 2
        jugadores_e.jugadores = ['Agustín', 'Mauro']
        self.assertEqual(len(jugadores_e.jugadores), 2)
    
    def test_agregar_jugadores_II(self):
        jugadores_e = Jugadores()
        jugadores_e.cantidad = 3
        jugadores_e.jugadores = ['Agustín', 'Mauro', 'Bruno']
        self.assertEqual(len(jugadores_e.jugadores), 3)

    def test_agregar_jugadores_III(self):
        jugadores_e = Jugadores()
        jugadores_e.cantidad = 4
        jugadores_e.jugadores = ['Agustín', 'Mauro', 'Bruno', 'Nico']
        self.assertEqual(len(jugadores_e.jugadores), 4)

    def test_agregar_jugadores_IV(self):
        jugadores_e = Jugadores()
        jugadores_e.cantidad = 5
        jugadores_e.jugadores = ['Agustín', 'Mauro', 'Bruno', 'Nico', 'Tobi']
        self.assertEqual(len(jugadores_e.jugadores), 5)

class TestDados(unittest.TestCase):         
    
    def test_tirada(self):
        dados_e = Dados()
        dados_e.realizar_tirada()
        self.assertEqual(len(dados_e.dados), 5)
        
    def test_dados(self):
        dados_e = Dados()
        dados_e.realizar_tirada()
        dados_e.dados = [2,2,2,4,1]
        self.assertEqual((dados_e.dados), [2,2,2,4,1])
        
    def test_apartar_dados(self):
        dados_e = Dados()
        dados_e.realizar_tirada()
        dados_e.dados = [2,2,2,4,1]
        dados_e.apartar_dados()
        dados_e.ordenar_repetidos()
        self.assertEqual((dados_e.repetidos), [2,2,2])

    def test_sumar_dados(self):
        dados_e = Dados()
        dados_e.realizar_tirada()
        dados_e.dados = [2,2,2,4,6]
        dados_e.apartar_dados()
        dados_e.ordenar_repetidos()
        dados_e.sumar_dados()
        self.assertEqual((dados_e.puntaje_c), 16)

    def test_sumar_dados_II(self):
        dados_e = Dados()
        dados_e.realizar_tirada()
        dados_e.dados = [6,6,6,6,6]
        dados_e.apartar_dados()
        dados_e.ordenar_repetidos()
        dados_e.sumar_dados()
        self.assertEqual((dados_e.puntaje_c), 30)

    def test_determinar_categoria_sin_categoria(self):
        dados_e = Dados()
        dados_e.realizar_tirada()
        dados_e.dados = [1,2,2,4,5]
        dados_e.apartar_dados()
        dados_e.ordenar_repetidos()
        dados_e.determinar_categoria()
        self.assertEqual((dados_e.cat), 'Sin categoria')

    def test_determinar_categoria_poker(self):
        dados_e = Dados()
        dados_e.realizar_tirada()
        dados_e.dados = [1,1,1,1,2]
        dados_e.apartar_dados()
        dados_e.ordenar_repetidos()
        dados_e.determinar_categoria()
        self.assertEqual((dados_e.cat), 'Poker')

    def test_determinar_categoria_full(self):
        dados_e = Dados()
        dados_e.realizar_tirada()
        dados_e.dados = [2,2,2,4,4]
        dados_e.apartar_dados()
        dados_e.ordenar_repetidos()
        dados_e.determinar_categoria()
        self.assertEqual((dados_e.cat), 'Full')

    def test_determinar_categoria_generala(self):
        dados_e = Dados()
        dados_e.realizar_tirada()
        dados_e.dados = [3,3,3,3,3]
        dados_e.apartar_dados()
        dados_e.ordenar_repetidos()
        dados_e.determinar_categoria()
        self.assertEqual((dados_e.cat), 'Generala')

    def test_determinar_categoria_escalera(self):
        dados_e = Dados()
        dados_e.realizar_tirada()
        dados_e.dados = [1,2,3,4,5]
        dados_e.apartar_dados()
        dados_e.ordenar_repetidos()
        dados_e.determinar_categoria()
        self.assertEqual((dados_e.cat), 'Escalera')

class TestTabla(unittest.TestCase):
    
    def test_generar_tabla(self):
        tabla = Tabla()
        jugadores = Jugadores()
        jugadores.cantidad = 2
        jugadores.jugadores = ['Agustin','Mauro']
        tabla.generar_tabla(jugadores)
        print(tabla.tabla)
        self.assertEqual((tabla.puntaje_a), [])
        self.assertEqual((tabla.puntaje_b), [])
        self.assertEqual(len(tabla.tabla), 4)  

    def test_iniciar_juego(self):
        tabla_e = Tabla()
        jugadores_n = Jugadores()
        dados_n = Dados()
        jugadores_n.cantidad = 2
        jugadores_n.jugadores = ['Agustin','Mauro']
        tabla_e.iniciar_juego(jugadores_n,dados_n)
        self.assertEqual(len(tabla_e.orden_final), 2)

    def test_iniciar_juego_II(self):
        tabla_e = Tabla()
        jugadores_n = Jugadores()
        dados_n = Dados()
        jugadores_n.cantidad = 3
        jugadores_n.jugadores = ['Agustin','Mauro','Bruno']
        tabla_e.iniciar_juego(jugadores_n,dados_n)
        self.assertEqual(len(tabla_e.orden_final), 3)

    def test_iniciar_juego_III(self):
        tabla_e = Tabla()
        jugadores_n = Jugadores()
        dados_n = Dados()
        jugadores_n.cantidad = 4
        jugadores_n.jugadores = ['Agustin','Mauro','Bruno','Nico']
        tabla_e.iniciar_juego(jugadores_n, dados_n)
        self.assertEqual(len(tabla_e.orden_final), 4)

    def test_iniciar_juego_IV(self):
        tabla_e = Tabla()
        jugadores_n = Jugadores()
        dados_n = Dados()
        jugadores_n.cantidad = 4
        jugadores_n.jugadores = ['Agustin','Mauro','Bruno','Nico','Mariano']
        tabla_e.iniciar_juego(jugadores_n, dados_n)
        self.assertEqual(len(tabla_e.orden_final), 5)

    def test_tabla_final(self):
        tabla = Tabla()
        jugadores = Jugadores()
        dados = Dados()
        jugadores.cantidad = 2
        jugadores.jugadores = ['Agustin','Mauro']
        tabla.generar_tabla(jugadores)
        tabla.iniciar_juego(jugadores,dados)
        tabla.tabla_final(jugadores)
        self.assertEqual(len(tabla.tabla), 4)
        
        
if __name__ == '__main__':
    unittest.main(buffer=True)