"""
2. Создать пользовательский класс данных (или использовать) один из классов,
реализованных в курсе Python.Основы. Реализовать класс с применением слотов
и обычным способом. Для объекта обычного класса проверить отображение словаря
атрибутов. Сравнить, сколько выделяется памяти для хранения атрибутов обоих
классов.
"""

from memory_profiler import profile
from pympler import asizeof


class TestClass_1(object):
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3


class TestClass_2(object):
    __slots__ = "p1", "p2", "p3"

    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3


cd = TestClass_1(1, "Q", (1,2,3,))
cs = TestClass_2(1, "Q", (1,2,3,))

print(f"\n\"TestClass_1\": \n - словарь атрибутов: {cd.__dict__}\n"
      f" - объёмы памяти выделенные для хранения атрибутов класса: "
      f"{asizeof.asized(list(cd.__dict__.items()), detail=1).format()}")

print(f" \n\"TestClass_2\": \n - слоты атрибутов: {cs.__slots__}\n"
      f" - объёмы памяти выделенные для хранения атрибутов класса: "
      f"{asizeof.asized([cs.__getattribute__(a) for a in cs.__slots__], detail=1).format()}")

"""
Из полученных результатов анализа, явно видно преимущество использования слотов, а части утилизации памяти.
При исппользовании слотов, образуется экономия ~ 35% 
"""