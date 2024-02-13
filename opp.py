class Personaje:
    def __init__(self, nombre: str, fuerza: int, inteligencia: int, defensa: int, vida: int):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
        
    def atributos(self) -> None:
        print(f'{self.nombre} ')
        print(f'Fuerza: {self.fuerza}')
        print(f'Inteligencia: {self.inteligencia}')
        print(f'Defensa: {self.defensa}')
        print(f'Vida: {self.vida}')
        
    def subir_nivel(self, fuerza: int, inteligencia: int, defensa: int) -> None:
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa
        
    def esta_vivo(self) -> bool:
        return self.vida > 0
    
    def morir(self) -> None:
        self.vida = 0
        print(f'{self.nombre} esta muerto')
        
    def danio(self, enemigo) -> int:
        return self.fuerza - enemigo.defensa
    
    def atacar(self, enemigo) -> None:
        danio = self.danio(enemigo)
        enemigo.vida = enemigo.vida - danio
        print(f'{self.nombre} ha causado {danio} puntos de danio a {enemigo.nombre}')
        if enemigo.esta_vivo():
            print(f'Vida de {enemigo.nombre} es {enemigo.vida}')
        else:
            enemigo.morir()


class Guerrero(Personaje):
    def __init__(self, nombre: str, fuerza: int, inteligencia: int, defensa: int, vida: int, espada: int):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada
        
    def cambiar_arma(self) -> None:
        opcion = int(input('Elije un arma: 1) Acero: 8 - 2) Dragonslayer: 16\n'))
        if opcion == 1:
            self.espada = 8
        elif opcion == 2:
            self.espada = 16
        else:
            print('Numero incorrecto')
            
    def atributos(self) -> None:
        super().atributos()
        print(f'Espada: {self.espada}')
        
    def danio(self, enemigo) -> int:
        return self.fuerza * self.espada - enemigo.defensa


class Mago(Personaje):
    def __init__(self, nombre: str, fuerza: int, inteligencia: int, defensa: int, vida: int, libro: int):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro
        
    def atributos(self) -> None:
        super().atributos()
        print(f'Libro: {self.libro}')
        
    def danio(self, enemigo) -> int:
        return self.inteligencia * self.libro - enemigo.defensa
    
    
goku = Personaje('Goku', 10, 8, 10, 100)
guts = Guerrero('Guts', 10, 8, 10, 100, 5)
maria = Mago('Maria', 10, 15, 10, 100, 5)

def combate(p1, p2):
    turno = 0
    while p1.esta_vivo() and p2.esta_vivo():
        p1.atacar(p2)
        p2.atacar(p1)
        turno += 1
    
    if p1.esta_vivo():
        print('Jugador 1 gana')
    elif p2.esta_vivo():
        print('Jugador 2 gana')
    else:
        print('Empate')

combate(guts, maria)
# goku.atacar(guts)
# guts.atacar(maria)
# maria.atacar(goku)

goku.atributos()
guts.atributos()
maria.atributos()


# Polimorfismo
class Cafe():
    def que_soy(self):
        print('soy un cafe')

class Te():
    def que_soy(self):
        print('soy un te')
        
def def_bebida(bebida):
    bebida.que_soy()
    
# def_bebida(Te())















# mi_personaje = Personaje('Bruce', 10, 8, 7, 100)
# mi_enemigo = Personaje('Orko', 12, 9, 4, 2)
# mi_personaje.atacar(mi_enemigo)
# mi_enemigo.atributos()
# print(f'Nombre del jugador: {mi_personaje.nombre}')
# print(f'Fuerza del jugador: {mi_personaje.fuerza}')
# mi_personaje.atributos()
# mi_personaje.subir_nivel(5, 3, 3)
# mi_personaje.atributos()
# vivo = mi_personaje.esta_vivo()
# print(vivo)
# mi_personaje.morir()
# mi_enemigo.atributos()
# print(f'Danio al enemigo: {mi_personaje.danio(mi_enemigo)}')
# mi_enemigo.atributos()


# Encapsulacion
'''class Personaje:
    def __init__(self, nombre: str, fuerza: int, inteligencia: int, defensa: int, vida: int):
        self.__nombre = nombre
        self.__fuerza = fuerza
        self.__inteligencia = inteligencia
        self.__defensa = defensa
        self.__vida = vida
        
    def get_fuerza(self):
        return self.__fuerza
    
    def set_fuerza(self, fuerza: int):
        if fuerza < 0:
            print('Error, debe ser mayor a 0')
        else:
            self.__fuerza = fuerza
        
    def atributos(self) -> None:
        print(f'{self.__nombre} ')
        print(f'Fuerza: {self.__fuerza}')
        print(f'Inteligencia: {self.__inteligencia}')
        print(f'Defensa: {self.__defensa}')
        print(f'Vida: {self.__vida}')
        
    def subir_nivel(self, fuerza: int, inteligencia: int, defensa: int) -> None:
        self.__fuerza = self.__fuerza + fuerza
        self.__inteligencia = self.__inteligencia + inteligencia
        self.__defensa = self.__defensa + defensa
        
    def esta_vivo(self) -> bool:
        return self.__vida > 0
    
    def __morir(self) -> None:
        self.__vida = 0
        print(f'{self.__nombre} esta muerto')
        
    def danio(self, enemigo) -> int:
        return self.__fuerza - enemigo.__defensa
    
    def atacar(self, enemigo) -> None:
        danio = self.danio(enemigo)
        enemigo.__vida = enemigo.__vida - danio
        print(f'{self.__nombre} ha causado {danio} puntos de danio a {enemigo.__nombre}')
        if enemigo.esta_vivo():
            print(f'Vida de {enemigo.__nombre} es {enemigo.__vida}')
        else:
            enemigo.__morir()'''