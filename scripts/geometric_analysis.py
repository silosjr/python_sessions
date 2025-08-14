"""Utilitário para Cálculo de Distância Euclidiana.

Este script contém uma função para calcular a distância em linha reta
entre dois pontos em um plano 2D.

Quando executado diretamente, o script demonstra o uso da função
com dois pontos de exemplo e imprime o resultado formatado no console.
"""

__author__ = 'Enock Silos'
__version__ = '1.0.0' 
__email__ = 'init.caucasian722@passfwd.com'
__status__ = 'Development'

from typing import Tuple, List 
import math
import copy 

class Point:
     """
     Representa um ponto em um espaço 2D.

     Atributos:
          x (float): A coordenada no eixo x.
          y (float): A coordenada no eixo y.
     """
     def __init__(self, x: float = 0.0, y: float = 0.0) -> None:
          """
          Inicializa uma nova instância do objeto Point.
          
          Args:
          x (float, optional): O valor inicial para a coordenada x. Padrão é 0.0.
          y (float, optional): O valor inicial para a coordenada y. Padrão é 0.0.
          """
          self.x = x
          self.y = y 

     def __str__(self) -> str:
         """
         Retorna a representação em string do ponto no formato (x, y).
         """
         return f'({self.x}, {self.y})'
     
     def __add__(self, other: 'Point') -> 'Point':
         """
          Retorna a soma vetorial de dois objetos `Point` usando o operador `+`.

          Este método sobrecarrega o operador `+`, permitindo a soma direta de duas 
          instâncias de `Point`. Ele cria e retorna um novo objeto `Point` sem modificar
          as instâncias originais.

          Args:
               other (Point): O outro objeto `Point` a ser somado a este.

          Returns:
               Point: Um novo objeto `Point` cujas coordenadas (x, y) são a 
                      soma das coordenadas dos dois pontos originais.
         """
         return Point(self.x + other.x, self.y + other.y)

class Rectangle:
    """
    Representa um retângulo.
    """
    def __init__(self, width: float = 0.0, height: float = 0.0, corner: Point = Point()):
        """
        Inicializa um objeto Rectangle.

        Args:
          width (float): A largura do retângulo.
          height (float): A altura do retângulo.
          corner (object): Um objeto Point representando o canto inferior esquerdo.
        """
        self.width: float = width
        self.height: float = height
        self.corner: Point = corner 

class Circle:
    """
    Representa a figura geométrica de um círculo.
    """
    def __init__(self, center: Point, radius: float):
     """
        Inicializa um objeto Circle.

        Args:
          center (object): Um objeto Point representando o centro do Círculo.
          radius (float): Um número (float ou int) representando o raio.
     """
     self.center: object = center
     self.radius: float = radius

def distance_between_points(point_1: Tuple[float, float], point_2: Tuple[float, float]) -> float:
    """
    Calcula a distância euclidiana entre dois pontos em um plano 2D.

    Args:
        point_1 (Tuple[float, float]): Uma tupla (x1, y1) representando o primeiro ponto.
        point_2 (Tuple[float, float]): Uma tupla (x2, y2) representando o segundo ponto.

    Returns:
        A distância como um número de ponto flutuante (float).
    """ 
    dx: float = (point_2[0] - point_1[0]) ** 2
    dy: float = (point_2[1] - point_1[1]) ** 2
    distance: float = math.sqrt(dx + dy)
    return distance

def point_in_circle(circle:Circle, point: Point) -> bool: 
     """
     Verifica se um ponto está dentro ou no limite de um círculo.
     
     Args:
          circle (Circle): O objeto Circle de referência.
          point (Point): O objeto Point a ser verificado.

     Returns:
          True se o ponto está dentro ou no limite, False caso contrário.
     """
     return distance_between_points(point, circle.center) <= circle.radius

def find_rectangle_corners(rectangle: Rectangle) -> List[Point]:
     """
     Calcula as coordenadas dos quatro cantos de um retângulo.

     Args:
          rectangle (object): O objeto Rectangle a ser analisado.

     Returns: 
          Uma lista contendo os quatro objetos Point dos cantos.
     """
     p1 = rectangle.corner
     p2 = Point(p1.x + rectangle.width, p1.y)
     p3 = Point(p1.x, p1.y + rectangle.height)
     p4  = Point(p1.x + rectangle.width, p1.y + rectangle.height)

     return [p1, p2, p3, p4]

def rectangle_in_circle(circle: Circle, rectangle: Rectangle) -> bool:
     """
     Verifica se um retângulo está totalmente dentro de um círculo.

     Args:
          circle (Circle): O objeto Circle de referência.
          rectangle (Rectangle): O objeto Rectangle a ser verificado.

     Returns:
          True se todos os cantos do retângulo estão dentro do círculo.
     """
     for corner in find_rectangle_corners(rectangle.width, rectangle.height, rectangle.corner):
          if not point_in_circle(circle, corner):
               return False
     return True 

def rectangle_circle_overlap(circle: Circle, rectangle: Rectangle) -> bool:
     """
     Verifica se algum canto de um retângulo está dentro de um círculo.

     Args:
          circle (Circle): O objeto Circle de referência.
          rectangle (Rectangle): O objeto Rectangle a ser verificado.

     Returns:
          True se pelo menos um canto do retângulo está dentro do círculo.
     """
     for corner in find_rectangle_corners(rectangle.width, rectangle.height, rectangle.corner):
          if point_in_circle(circle, corner):
               return True 
     return False 

def move_rectangle(rectangle: Rectangle, dx: float, dy: float) -> None:
    """
    Move um retângulo alterando as coordenadas de seu canto.

    Args:
        rectangle (Rectangle): O objeto Rectangle a ser modificado.
        dx (float): O deslocamento a ser adicionado à coordenada x.
        dy (float): O deslocamento a ser adicionado à coordenada y.

    Side Effects:
        Modifica diretamente os atributos do objeto `rectangle` passado.
    """
    rectangle.corner.x += dx 
    rectangle.corner.y += dy 

def move_rectangle_new(rectangle: Rectangle, dx: float, dy: float) -> Rectangle:
    """
    Cria um novo retângulo que é uma versão deslocada do original.

    Esta função não modifica o objeto original.

    Args:
        rectangle (Rectangle): O objeto Rectangle original a ser copiado e movido.
        dx (float): O deslocamento a ser aplicado à coordenada x da cópia.
        dy (float): O deslocamento a ser aplicado à coordenada y da cópia.

    Returns:
        Um novo objeto Rectangle na posição deslocada.
    """
    new_rectangle = copy.deepcopy(rectangle)
    new_rectangle.corner.x += dx 
    new_rectangle.corner.y += dy 
    
    return new_rectangle

if __name__ == '__main__':
    # Criando instâncias com o novo construtor
    ponto_origem = Point()
    ponto_a = Point(3.0, 4.0)
    ponto_b = Point(x=5.0) # y será 0.0 por padrão.

    print('--- Demonstração da Classe Point ---\n')
    print(f'Ponto na origem: {ponto_origem}')
    print(f'Ponto A: {ponto_a}')
    print(f'Ponto B: {ponto_b}')

    # Testando o método __add__ com o operador `+`
    ponto_soma = ponto_a + ponto_b
    print(f'A soma de A + B: {ponto_soma}\n')

    # Criação e configuração do retângulo inicial
    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 0.0
    box.corner.y = 0.0

    print('--- Demonstração da Função Original (Modifica o Original) ---\n')
    print(f'Posição inicial do canto: ({box.corner.x}, {box.corner.y})')
    move_rectangle(box, 50.0, 100.0)
    print(f'Nova posição do canto: ({box.corner.x}, {box.corner.y})\n')

    # Cria um novo retângulo, movido a partir da posição atual de `box`
    box_2 = move_rectangle_new(box, 30.0, 40.0)

    print(f'Posição do novo box_2: ({box_2.corner.x}, {box_2.corner.y})')
    print(f'Posição do box original NÃO foi alterada: ({box.corner.x}, {box.corner.y})\n')

    # Criação dos objetos para o exemplo
    circle_center = Point(150.0, 100.0)
    radius_circle = 75.0

    # Instanciando o círculo principal do exercício
    main_circle = Circle(circle_center, radius_circle)

    print('Objeto Círculo criado com sucesso:')
    print(f'   - Centro nas coordenadas: ({main_circle.center.x}, {main_circle.center.y})')
    print(f'   - Raio: {main_circle.radius}\n')

    # Bloco para cálculo da distância entre dois pontos
    p1 = (1.0, 2.0)
    p2 = (4.0, 6.0)

    distance = distance_between_points(p1, p2)

    print(f'O ponto 1 é {p1}')
    print(f'O ponto 2 é: {p2}')
    print(f'A distância entre os dois pontos é: {distance:.2f}\n')
   


