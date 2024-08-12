"""Ссылка на Google-документ со скриншотами заданий в Яндекс Контест, которые выполнял в течение спринта.
https://docs.google.com/document/d/1l2OS5xjAE1Szu8w7Xa_xossHFwh-YF7HLOkaynejUKo/edit?usp=sharing """


"""
ID посылки из Яндекс-Контест: 116812845
Теперь само решение финального задания.
Будем сортировать веса роботов и пробовать упаковать их на платформу
по принципу "самого лёгкого" и "самого тяжёлого" робота, чтобы максимально
эффективно использовать грузоподъёмность платформы.
"""


def bubble_sort(weights: list[int]) -> list[int]:
    n = len(weights)
    # На каждой итерации переменная last_index будет уменьшаться на 1.
    for last_index in range(n - 1, 0, -1):
        # На этом проходе перестановок ещё не было:
        swapped = False
        # Вложенный цикл будет перебирать значения от 0 до last_index
        for item_index in range(last_index):
            if weights[item_index] > weights[item_index+1]:
                # Если значения надо поменять местами - меняем.
                weights[item_index], weights[item_index + 1] = (
                    weights[item_index + 1], weights[item_index]
                )
                # Выставляем флаг "выполнена перестановка".
                swapped = True
                # После окончания внутреннего цикла проверяем значение флага. 
                # Если перестановок не было...
        if not swapped:
            # ...то выходим из внешнего цикла.
            break
    return weights


def min_platforms(weights: list[int], limit: int) -> int:  # Аннотация типов в наличии
    # Сортируем массив весов, чтобы можно было найти самого легко и самого тяжелого робота
    # при помощи пузырьковой сортировки
    weights = bubble_sort(weights)

    left = 0  # Указатель на самого легкого робота
    right = len(weights) - 1  # Указатель на самого тяжелого робота
    platforms_value = 0  # Количество платформ

    while left <= right:
        # Проверяем, можем ли мы разместить двух роботов
        if weights[left] + weights[right] <= limit:  # Можно перевезти легкого и тяжелого робота вместе
            left += 1  # Добавляем легкого робота
        right -= 1  # Тяжелого робота добавляем всегда, если не влезет с легким, поедет один
        platforms_value += 1  # Каждое действие с платформой увеличивает счетчик

    return platforms_value


if __name__ == '__main__':
    array_weights = list(map(int, input().split()))  # Массив с весами роботов
    lim = int(input())  # Лимит весов
    result = min_platforms(array_weights, lim)
    print(result)
