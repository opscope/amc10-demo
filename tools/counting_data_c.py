# -*- coding: utf-8 -*-
"""Блок 4 «Комбинаторика и вероятность»: урок 4.5 + тест Т4 + задачи со звёздочкой, RU+EN."""

def F(a, b):
    return f'<span class="frac"><span>{a}</span><span>{b}</span></span>'

L45 = {
 'id': '4.5', 'anchor': 'u45',
 'title': {'ru': 'Пути по решётке, рекуррентный подсчёт, ожидание',
           'en': 'Lattice Paths, Recursive Counting, Expected Value'},
 'theory': {
  'ru': f"""
<p><b>Пути по решётке.</b> Путь из (0;&nbsp;0) в (<var>m</var>,&nbsp;<var>n</var>) шагами вправо и вверх &mdash; это слово из <var>m</var> букв П и <var>n</var> букв В. Путей столько, сколько способов расставить буквы: C(<var>m</var>&nbsp;+&nbsp;<var>n</var>,&nbsp;<var>m</var>). Путь &laquo;через точку <var>P</var>&raquo; &mdash; произведение (до <var>P</var>)&nbsp;&middot;&nbsp;(после <var>P</var>). Путь &laquo;мимо точки <var>P</var>&raquo; &mdash; дополнение: все минус через <var>P</var>.</p>
<div class="frm">Путей из (0;&nbsp;0) в (<var>m</var>,&nbsp;<var>n</var>): C(<var>m</var>&nbsp;+&nbsp;<var>n</var>,&nbsp;<var>m</var>). &nbsp;Лестница по 1 или 2 ступени: <var>f</var>(<var>n</var>) = <var>f</var>(<var>n</var>&nbsp;&minus;&nbsp;1) + <var>f</var>(<var>n</var>&nbsp;&minus;&nbsp;2). &nbsp;E = &sum; (значение &middot; вероятность).</div>
<p><b>Рекуррентный подсчёт.</b> Когда прямой формулы не видно, спросите: чем кончается объект? Подъём на <var>n</var> ступеней кончается шагом на 1 (до этого &mdash; любой подъём на <var>n</var>&nbsp;&minus;&nbsp;1) или шагом на 2 (подъём на <var>n</var>&nbsp;&minus;&nbsp;2): <var>f</var>(<var>n</var>) = <var>f</var>(<var>n</var>&nbsp;&minus;&nbsp;1) + <var>f</var>(<var>n</var>&nbsp;&minus;&nbsp;2) &mdash; числа Фибоначчи. Тот же скелет у замощений полосы 2&nbsp;&times;&nbsp;<var>n</var> доминошками и у слов без двух единиц подряд. Посчитайте первые значения руками (<var>f</var>(1) = 1, <var>f</var>(2) = 2 для лестницы) и раскручивайте таблицу &mdash; ошибка в старте портит всё.</p>
<p><b>Ожидание &mdash; минимум.</b> Математическое ожидание &mdash; средний выигрыш при многократном повторении: сумма произведений &laquo;значение &times; вероятность&raquo;. Для кубика: (1&nbsp;+&nbsp;2&nbsp;+&nbsp;&hellip;&nbsp;+&nbsp;6)/6 = 3,5. Ожидание суммы равно сумме ожиданий &mdash; без всяких условий независимости.</p>
<p><b>Стратегия на тесте.</b> Маленькие решётки быстрее заполнить числами прямо на картинке (в каждый узел &mdash; сумма левого и нижнего соседей), чем вспоминать формулу. Это тот же рекуррентный принцип, и он застрахован от ошибок с препятствиями: запретный узел просто получает ноль.</p>""",
  'en': f"""
<p><b>Lattice paths.</b> A path from (0,&nbsp;0) to (<var>m</var>,&nbsp;<var>n</var>) by unit steps right and up is a word of <var>m</var> letters R and <var>n</var> letters U. There are as many paths as letter arrangements: C(<var>m</var>&nbsp;+&nbsp;<var>n</var>,&nbsp;<var>m</var>). A path &ldquo;through point <var>P</var>&rdquo; is a product: (to <var>P</var>)&nbsp;&middot;&nbsp;(after <var>P</var>). A path &ldquo;avoiding <var>P</var>&rdquo; is a complement: all minus through <var>P</var>.</p>
<div class="frm">Paths from (0,&nbsp;0) to (<var>m</var>,&nbsp;<var>n</var>): C(<var>m</var>&nbsp;+&nbsp;<var>n</var>,&nbsp;<var>m</var>). &nbsp;Stairs by 1 or 2 steps: <var>f</var>(<var>n</var>) = <var>f</var>(<var>n</var>&nbsp;&minus;&nbsp;1) + <var>f</var>(<var>n</var>&nbsp;&minus;&nbsp;2). &nbsp;E = &sum; (value &middot; probability).</div>
<p><b>Recursive counting.</b> When no direct formula is in sight, ask: how does the object end? A climb of <var>n</var> steps ends with a 1-step (preceded by any climb of <var>n</var>&nbsp;&minus;&nbsp;1) or a 2-step (a climb of <var>n</var>&nbsp;&minus;&nbsp;2): <var>f</var>(<var>n</var>) = <var>f</var>(<var>n</var>&nbsp;&minus;&nbsp;1) + <var>f</var>(<var>n</var>&nbsp;&minus;&nbsp;2) &mdash; the Fibonacci numbers. The same skeleton counts domino tilings of a 2&nbsp;&times;&nbsp;<var>n</var> strip and binary words with no two adjacent ones. Compute the first values by hand (<var>f</var>(1) = 1, <var>f</var>(2) = 2 for the stairs) and unroll the table &mdash; a wrong start ruins everything.</p>
<p><b>Expected value &mdash; the minimum.</b> The expected value is the average payoff over many repetitions: the sum of value &times; probability. For a die: (1&nbsp;+&nbsp;2&nbsp;+&nbsp;&hellip;&nbsp;+&nbsp;6)/6 = 3.5. The expectation of a sum equals the sum of expectations &mdash; no independence required.</p>
<p><b>Test strategy.</b> Small grids are faster to fill with numbers right on the picture (each node = left neighbor + bottom neighbor) than to attack by formula. It is the same recursive principle, and it is immune to obstacle errors: a forbidden node simply gets a zero.</p>"""},
 'worked': [
  {'tag': {'ru': 'Разбор 1 · пути', 'en': 'Example 1 · paths'},
   'q': {'ru': 'Сколько путей из (0;&nbsp;0) в (4;&nbsp;3) шагами вправо и вверх?',
         'en': 'How many paths lead from (0,&nbsp;0) to (4,&nbsp;3) by unit steps right and up?'},
   'sol': {'ru': 'Каждый путь &mdash; слово из 4 букв П и 3 букв В: выбираем места для В среди 7 шагов, C(7;&nbsp;3) = <b>35</b>. Ловушка &laquo;порядок против выбора&raquo; наоборот: не надо ничего домножать, слово уже задаёт путь однозначно.',
          'en': 'Every path is a word of 4 R&rsquo;s and 3 U&rsquo;s: choose the places for U among 7 steps, C(7,&nbsp;3) = <b>35</b>. The order-versus-choice trap in reverse: nothing needs an extra factor &mdash; the word already determines the path uniquely.'}},
  {'tag': {'ru': 'Разбор 2 · пути мимо точки', 'en': 'Example 2 · avoiding a point'},
   'q': {'ru': 'Сколько путей из (0;&nbsp;0) в (4;&nbsp;4) не проходят через точку (2;&nbsp;2)?',
         'en': 'How many paths from (0,&nbsp;0) to (4,&nbsp;4) do not pass through (2,&nbsp;2)?'},
   'sol': {'ru': 'Дополнение. Всего C(8;&nbsp;4) = 70. Через (2;&nbsp;2): C(4;&nbsp;2)&nbsp;&middot;&nbsp;C(4;&nbsp;2) = 36 &mdash; произведение &laquo;до&raquo; и &laquo;после&raquo;. Ответ 70 &minus; 36 = <b>34</b>. Считать &laquo;мимо&raquo; напрямую &mdash; значит перебирать маршруты по краям и что-нибудь потерять.',
          'en': 'Complement. Total: C(8,&nbsp;4) = 70. Through (2,&nbsp;2): C(4,&nbsp;2)&nbsp;&middot;&nbsp;C(4,&nbsp;2) = 36 &mdash; the product of &ldquo;before&rdquo; and &ldquo;after&rdquo;. Answer: 70 &minus; 36 = <b>34</b>. Counting &ldquo;avoiding&rdquo; directly means chasing routes along the edges and losing some.'}},
  {'tag': {'ru': 'Разбор 3 · лестница', 'en': 'Example 3 · stairs'},
   'q': {'ru': 'По лестнице из 10 ступеней поднимаются шагами по 1 или по 2 ступени. Сколько существует способов подняться?',
         'en': 'A staircase of 10 steps is climbed in moves of 1 or 2 steps. How many ways are there to climb it?'},
   'sol': {'ru': 'Последний шаг: на 1 (до него подъём на 9) или на 2 (подъём на 8): <var>f</var>(10) = <var>f</var>(9) + <var>f</var>(8). Таблица от <var>f</var>(1) = 1, <var>f</var>(2) = 2: 1, 2, 3, 5, 8, 13, 21, 34, 55, <b>89</b>. Главная ошибка &mdash; фальстарт <var>f</var>(2) = 1: на две ступени есть ДВА способа (1+1 и 2).',
          'en': 'The last move: a 1-step (preceded by a climb of 9) or a 2-step (a climb of 8): <var>f</var>(10) = <var>f</var>(9) + <var>f</var>(8). The table from <var>f</var>(1) = 1, <var>f</var>(2) = 2: 1, 2, 3, 5, 8, 13, 21, 34, 55, <b>89</b>. The main error is the false start <var>f</var>(2) = 1: there are TWO ways up two steps (1+1 and 2).'}},
  {'tag': {'ru': 'Разбор 4 · ожидание', 'en': 'Example 4 · expected value'},
   'q': {'ru': 'Бросают кубик и выплачивают столько долларов, сколько выпало очков. Каков ожидаемый выигрыш?',
         'en': 'A die is rolled, and you are paid as many dollars as the number shown. What is the expected payoff?'},
   'sol': {'ru': f'Каждое значение с вероятностью 1/6: E = (1 + 2 + 3 + 4 + 5 + 6)/6 = 21/6 = <b>{F("7","2")}</b> доллара. Ожидание не обязано быть возможным исходом: 3,5 очка не выпадает никогда, но именно столько вы получаете в среднем за бросок.',
          'en': f'Each value has probability 1/6: E = (1 + 2 + 3 + 4 + 5 + 6)/6 = 21/6 = <b>{F("7","2")}</b> dollars. The expectation need not be a possible outcome: 3.5 never shows, yet that is exactly the average payoff per roll.'}},
 ],
 'selfp': [
  {'q': {'ru': 'Сколько путей из (0;&nbsp;0) в (3;&nbsp;3) шагами вправо и вверх?', 'en': 'How many paths lead from (0,&nbsp;0) to (3,&nbsp;3) by steps right and up?'},
   'hint': {'ru': 'Слово из 3 букв П и 3 букв В.', 'en': 'A word of 3 R&rsquo;s and 3 U&rsquo;s.'},
   'sol': {'ru': 'C(6;&nbsp;3) = <b>20</b>.', 'en': 'C(6,&nbsp;3) = <b>20</b>.'}},
  {'q': {'ru': 'Сколько путей из (0;&nbsp;0) в (5;&nbsp;2) шагами вправо и вверх?', 'en': 'How many paths lead from (0,&nbsp;0) to (5,&nbsp;2) by steps right and up?'},
   'hint': {'ru': 'Выберите места для двух шагов вверх.', 'en': 'Choose the places for the two up-steps.'},
   'sol': {'ru': 'C(7;&nbsp;2) = <b>21</b>.', 'en': 'C(7,&nbsp;2) = <b>21</b>.'}},
  {'q': {'ru': 'Сколькими способами можно подняться по лестнице из 8 ступеней шагами по 1 или 2?', 'en': 'In how many ways can a staircase of 8 steps be climbed in moves of 1 or 2?'},
   'hint': {'ru': 'Таблица Фибоначчи от 1, 2.', 'en': 'The Fibonacci table starting 1, 2.'},
   'sol': {'ru': '1, 2, 3, 5, 8, 13, 21, <b>34</b>.', 'en': '1, 2, 3, 5, 8, 13, 21, <b>34</b>.'}},
  {'q': {'ru': 'Сколькими способами можно замостить полосу 2&nbsp;&times;&nbsp;9 доминошками 1&nbsp;&times;&nbsp;2?', 'en': 'In how many ways can a 2&nbsp;&times;&nbsp;9 strip be tiled with 1&nbsp;&times;&nbsp;2 dominoes?'},
   'hint': {'ru': 'Конец полосы: одна вертикальная доминошка или две горизонтальные.', 'en': 'The strip&rsquo;s end: one vertical domino or two horizontal ones.'},
   'sol': {'ru': 'Та же рекуррента: <var>t</var>(<var>n</var>) = <var>t</var>(<var>n</var>&nbsp;&minus;&nbsp;1) + <var>t</var>(<var>n</var>&nbsp;&minus;&nbsp;2), старт 1, 2: получаем <b>55</b>.', 'en': 'The same recurrence: <var>t</var>(<var>n</var>) = <var>t</var>(<var>n</var>&nbsp;&minus;&nbsp;1) + <var>t</var>(<var>n</var>&nbsp;&minus;&nbsp;2), start 1, 2: we get <b>55</b>.'}},
  {'q': {'ru': 'Сколько путей из (0;&nbsp;0) в (4;&nbsp;4) проходят через точку (1;&nbsp;1)?', 'en': 'How many paths from (0,&nbsp;0) to (4,&nbsp;4) pass through the point (1,&nbsp;1)?'},
   'hint': {'ru': 'Произведение: до точки и после неё.', 'en': 'A product: to the point and after it.'},
   'sol': {'ru': 'C(2;&nbsp;1)&nbsp;&middot;&nbsp;C(6;&nbsp;3) = 2&nbsp;&middot;&nbsp;20 = <b>40</b>.', 'en': 'C(2,&nbsp;1)&nbsp;&middot;&nbsp;C(6,&nbsp;3) = 2&nbsp;&middot;&nbsp;20 = <b>40</b>.'}},
  {'q': {'ru': 'Бросают кубик и выплачивают квадрат выпавшего числа (в долларах). Каков ожидаемый выигрыш?', 'en': 'A die is rolled, and the payoff is the square of the number shown (in dollars). What is the expected payoff?'},
   'hint': {'ru': 'Сложите квадраты и поделите на 6.', 'en': 'Add the squares and divide by 6.'},
   'sol': {'ru': f'(1 + 4 + 9 + 16 + 25 + 36)/6 = <b>{F("91","6")}</b>.', 'en': f'(1 + 4 + 9 + 16 + 25 + 36)/6 = <b>{F("91","6")}</b>.'}},
  {'q': {'ru': 'Сколько путей из (0;&nbsp;0) в (3;&nbsp;3) не проходят через точку (1;&nbsp;1)?', 'en': 'How many paths from (0,&nbsp;0) to (3,&nbsp;3) avoid the point (1,&nbsp;1)?'},
   'hint': {'ru': 'Все минус проходящие через (1;&nbsp;1).', 'en': 'All minus those through (1,&nbsp;1).'},
   'sol': {'ru': '20 &minus; C(2;&nbsp;1)&nbsp;&middot;&nbsp;C(4;&nbsp;2) = 20 &minus; 12 = <b>8</b>.', 'en': '20 &minus; C(2,&nbsp;1)&nbsp;&middot;&nbsp;C(4,&nbsp;2) = 20 &minus; 12 = <b>8</b>.'}},
  {'q': {'ru': 'Сколько существует слов длины 10 из букв A и B, в которых нет двух букв B подряд?', 'en': 'How many words of length 10 over the letters A and B contain no two adjacent B&rsquo;s?'},
   'hint': {'ru': 'Чем кончается слово: буквой A (любое годное слово короче на 1) или парой AB (годное слово короче на 2)?', 'en': 'How does the word end: in A (any valid word one shorter) or in AB (any valid word two shorter)?'},
   'sol': {'ru': '<var>g</var>(<var>n</var>) = <var>g</var>(<var>n</var>&nbsp;&minus;&nbsp;1) + <var>g</var>(<var>n</var>&nbsp;&minus;&nbsp;2), старт <var>g</var>(1) = 2, <var>g</var>(2) = 3: 2, 3, 5, 8, 13, 21, 34, 55, 89, <b>144</b>.', 'en': '<var>g</var>(<var>n</var>) = <var>g</var>(<var>n</var>&nbsp;&minus;&nbsp;1) + <var>g</var>(<var>n</var>&nbsp;&minus;&nbsp;2), start <var>g</var>(1) = 2, <var>g</var>(2) = 3: 2, 3, 5, 8, 13, 21, 34, 55, 89, <b>144</b>.'}},
 ],
 'answers': {'ru': '20 · 21 · 34 · 55 · 40 · 91/6 · 8 · 144', 'en': '20, 21, 34, 55, 40, 91/6, 8, 144'},
 'routing': {'ru': 'Норма &mdash; 6 из 8. Ошибки в 1&ndash;2 &mdash; перечитать &laquo;пути по решётке&raquo;; в 3&ndash;4 и 8 &mdash; &laquo;рекуррентный подсчёт&raquo; (проверьте стартовые значения!); в 5 и 7 &mdash; пути через точку и мимо точки; в 6 &mdash; &laquo;ожидание&raquo;.',
             'en': 'Mastery bar: 6 of 8. For mistakes in 1&ndash;2, reread &ldquo;lattice paths&rdquo;; in 3&ndash;4 and 8, &ldquo;recursive counting&rdquo; (check the starting values!); in 5 and 7, paths through and avoiding a point; in 6, &ldquo;expected value&rdquo;.'},
}

T4 = {
 'problems': [
  {'q': {'ru': 'Сколько чётных четырёхзначных чисел можно составить из цифр 1, 2, 3, 4, 5, не повторяя цифры?',
         'en': 'How many even four-digit numbers can be formed from the digits 1, 2, 3, 4, 5 with no digit repeated?'},
   'opts': {'ru': ['24', '48', '60', '96', '120'], 'en': ['24', '48', '60', '96', '120']}},
  {'q': {'ru': 'Шесть человек становятся в ряд. Аня и Боря должны стоять рядом. Сколько существует расстановок?',
         'en': 'Six people line up in a row. Ann and Ben must stand next to each other. How many arrangements are there?'},
   'opts': {'ru': ['120', '144', '240', '480', '720'], 'en': ['120', '144', '240', '480', '720']}},
  {'q': {'ru': 'Из 5 мальчиков и 4 девочек выбирают команду: 3 мальчика и 2 девочки. Сколькими способами?',
         'en': 'A team of 3 boys and 2 girls is chosen from 5 boys and 4 girls. In how many ways?'},
   'opts': {'ru': ['20', '40', '54', '60', '90'], 'en': ['20', '40', '54', '60', '90']}},
  {'q': {'ru': 'Сколько диагоналей у выпуклого пятнадцатиугольника?',
         'en': 'How many diagonals does a convex 15-gon have?'},
   'opts': {'ru': ['90', '100', '105', '120', '135'], 'en': ['90', '100', '105', '120', '135']}},
  {'q': {'ru': 'Сколько чисел от 1 до 200 делятся на 6 или на 8?',
         'en': 'How many integers from 1 to 200 are divisible by 6 or by 8?'},
   'opts': {'ru': ['40', '42', '46', '48', '50'], 'en': ['40', '42', '46', '48', '50']}},
  {'q': {'ru': 'Сколько четырёхзначных чисел содержат хотя бы одну цифру 5?',
         'en': 'How many four-digit numbers contain at least one digit 5?'},
   'opts': {'ru': ['2916', '3096', '3168', '3268', '5832'], 'en': ['2916', '3096', '3168', '3268', '5832']}},
  {'q': {'ru': 'Бросают два кубика. Какова вероятность, что сумма очков не меньше 10?',
         'en': 'Two dice are rolled. What is the probability that the sum is at least 10?'},
   'opts': {'ru': [F('5','36'), F('1','6'), F('7','36'), F('2','9'), F('1','4')], 'en': [F('5','36'), F('1','6'), F('7','36'), F('2','9'), F('1','4')]}},
  {'q': {'ru': 'Из колоды 52 карты вытягивают две без возврата. Какова вероятность, что они одной масти?',
         'en': 'Two cards are drawn without replacement from a standard 52-card deck. What is the probability that they are of the same suit?'},
   'opts': {'ru': [F('4','17'), F('1','4'), F('5','17'), F('6','17'), F('1','3')], 'en': [F('4','17'), F('1','4'), F('5','17'), F('6','17'), F('1','3')]}},
  {'q': {'ru': 'Сколько путей из (0;&nbsp;0) в (5;&nbsp;4) шагами вправо и вверх?',
         'en': 'How many paths lead from (0,&nbsp;0) to (5,&nbsp;4) by unit steps right and up?'},
   'opts': {'ru': ['84', '100', '120', '126', '210'], 'en': ['84', '100', '120', '126', '210']}},
  {'q': {'ru': 'Монету бросают 5 раз. Какова вероятность, что никакие два орла не выпадут подряд?',
         'en': 'A coin is tossed 5 times. What is the probability that no two heads come up in a row?'},
   'opts': {'ru': [F('3','8'), F('13','32'), F('7','16'), F('15','32'), F('1','2')], 'en': [F('3','8'), F('13','32'), F('7','16'), F('15','32'), F('1','2')]}},
 ],
 'key': ['B', 'C', 'D', 'A', 'E', 'C', 'B', 'A', 'D', 'B'],
 'hints': {
  'ru': [
   '<b>1.</b> Последняя цифра 2 или 4: 2&nbsp;&middot;&nbsp;4&nbsp;&middot;&nbsp;3&nbsp;&middot;&nbsp;2 = 48.',
   '<b>2.</b> Склейка: 2&nbsp;&middot;&nbsp;5! = 240.',
   '<b>3.</b> C(5;&nbsp;3)&nbsp;&middot;&nbsp;C(4;&nbsp;2) = 10&nbsp;&middot;&nbsp;6 = 60.',
   '<b>4.</b> C(15,&nbsp;2) &minus; 15 = 105 &minus; 15 = 90.',
   '<b>5.</b> 33 + 25 &minus; 8 = 50 (пересечение &mdash; кратные НОК = 24).',
   '<b>6.</b> Дополнение: всего 9000, без пятёрок 8&nbsp;&middot;&nbsp;9<sup>3</sup> = 5832; ответ 9000 &minus; 5832 = 3168.',
   '<b>7.</b> Сумм 10, 11, 12 &mdash; пар 3 + 2 + 1 = 6 из 36: 1/6.',
   '<b>8.</b> Вторая карта из масти первой: 12/51 = 4/17.',
   '<b>9.</b> C(9;&nbsp;4) = 126.',
   '<b>10.</b> Без двух орлов подряд 13 последовательностей из 32 (Фибоначчи: 2, 3, 5, 8, 13): 13/32.'],
  'en': [
   '<b>1.</b> Last digit 2 or 4: 2&nbsp;&middot;&nbsp;4&nbsp;&middot;&nbsp;3&nbsp;&middot;&nbsp;2 = 48.',
   '<b>2.</b> Glue: 2&nbsp;&middot;&nbsp;5! = 240.',
   '<b>3.</b> C(5,&nbsp;3)&nbsp;&middot;&nbsp;C(4,&nbsp;2) = 10&nbsp;&middot;&nbsp;6 = 60.',
   '<b>4.</b> C(15,&nbsp;2) &minus; 15 = 105 &minus; 15 = 90.',
   '<b>5.</b> 33 + 25 &minus; 8 = 50 (the intersection is multiples of the lcm, 24).',
   '<b>6.</b> Complement: 9000 four-digit numbers in total, 8&nbsp;&middot;&nbsp;9<sup>3</sup> = 5832 with no 5; answer 9000 &minus; 5832 = 3168.',
   '<b>7.</b> Sums 10, 11, 12 give 3 + 2 + 1 = 6 pairs out of 36: 1/6.',
   '<b>8.</b> The second card from the first card&rsquo;s suit: 12/51 = 4/17.',
   '<b>9.</b> C(9,&nbsp;4) = 126.',
   '<b>10.</b> No two heads in a row: 13 sequences out of 32 (Fibonacci: 2, 3, 5, 8, 13): 13/32.'],
 },
}


STARS = {
 '4.1': {
  'q': {'ru': 'Из цифр 1, 2, 3, 4, 5 составляют пятизначные числа, используя каждую цифру ровно один раз. Сколько из них делятся на 4?',
        'en': 'Five-digit numbers are formed from the digits 1, 2, 3, 4, 5, each digit used exactly once. How many of them are divisible by 4?'},
  'hint': {'ru': 'Делимость на 4 решают две последние цифры. Выпишите двузначные кратные 4 из этих цифр без повторов.', 'en': 'Divisibility by 4 is decided by the last two digits. List the two-digit multiples of 4 made of these digits without repeats.'},
  'sol': {'ru': 'Подходящие окончания: 12, 24, 32, 52 &mdash; четыре штуки. Первые три цифры &mdash; любые из оставшихся: 3! = 6. Итого 4&nbsp;&middot;&nbsp;6 = <b>24</b>.', 'en': 'The valid endings: 12, 24, 32, 52 &mdash; four of them. The first three digits are any arrangement of the rest: 3! = 6. Total: 4&nbsp;&middot;&nbsp;6 = <b>24</b>.'}},
 '4.2': {
  'q': {'ru': 'Сколькими способами можно разбить 6 человек на 3 пары для игры в настольный теннис?',
        'en': 'In how many ways can 6 people be split into 3 pairs for table tennis?'},
  'hint': {'ru': 'C(6;&nbsp;2)&nbsp;&middot;&nbsp;C(4;&nbsp;2)&nbsp;&middot;&nbsp;C(2;&nbsp;2) пересчитывает каждое разбиение: порядок пар не важен.', 'en': 'C(6,&nbsp;2)&nbsp;&middot;&nbsp;C(4,&nbsp;2)&nbsp;&middot;&nbsp;C(2,&nbsp;2) overcounts each split: the order of the pairs does not matter.'},
  'sol': {'ru': '15&nbsp;&middot;&nbsp;6&nbsp;&middot;&nbsp;1 = 90 считает пары как &laquo;первую, вторую, третью&raquo; &mdash; каждое разбиение учтено 3! = 6 раз. Ответ 90/6 = <b>15</b>. Это ловушка двойного счёта в чистом виде: делите на перестановки неразличимых групп.', 'en': '15&nbsp;&middot;&nbsp;6&nbsp;&middot;&nbsp;1 = 90 treats the pairs as &ldquo;first, second, third&rdquo; &mdash; every split is counted 3! = 6 times. Answer: 90/6 = <b>15</b>. Overcounting in its purest form: divide by the permutations of indistinguishable groups.'}},
 '4.3': {
  'q': {'ru': 'Сколько подмножеств множества {1, 2, &hellip;, 10} содержат хотя бы одно чётное И хотя бы одно нечётное число?',
        'en': 'How many subsets of {1, 2, &hellip;, 10} contain at least one even AND at least one odd number?'},
  'hint': {'ru': 'Дополнение с двумя запретами: вычтите подмножества без чётных и подмножества без нечётных &mdash; и верните то, что вычли дважды.', 'en': 'Complement with two forbidden events: subtract the subsets with no evens and those with no odds &mdash; and add back what you subtracted twice.'},
  'sol': {'ru': 'Всего 2<sup>10</sup> = 1024. Без чётных &mdash; 2<sup>5</sup> = 32, без нечётных &mdash; 32; пустое множество вычли дважды. Ответ: 1024 &minus; 32 &minus; 32 + 1 = <b>961</b>.', 'en': 'In total 2<sup>10</sup> = 1024. With no evens: 2<sup>5</sup> = 32; with no odds: 32; the empty set was subtracted twice. Answer: 1024 &minus; 32 &minus; 32 + 1 = <b>961</b>.'}},
 '4.4': {
  'q': {'ru': 'Бросают три обычных кубика. Какова вероятность того, что значение одного из них равно сумме значений двух других?',
        'en': 'Three standard dice are rolled. What is the probability that one of the values equals the sum of the other two?'},
  'hint': {'ru': 'Зафиксируйте, какая из костей &laquo;сумма&raquo;: у неё значение <var>x</var> + <var>y</var>, где <var>x</var> + <var>y</var> &le; 6. Посчитайте упорядоченные пары и умножьте на число позиций.', 'en': 'Fix which die is the &ldquo;sum&rdquo;: it shows <var>x</var> + <var>y</var> with <var>x</var> + <var>y</var> &le; 6. Count ordered pairs, then multiply by the number of positions.'},
  'sol': {'ru': 'Упорядоченных пар (<var>x</var>;&nbsp;<var>y</var>) с <var>x</var> + <var>y</var> &le; 6 ровно 5 + 4 + 3 + 2 + 1 = 15; кость-&laquo;сумма&raquo; может стоять на любой из 3 позиций, и двойного счёта нет (две кости сразу быть суммой остальных не могут). Итого 45 исходов из 216: вероятность 45/216 = <b>5/24</b>.', 'en': 'There are 5 + 4 + 3 + 2 + 1 = 15 ordered pairs (<var>x</var>, <var>y</var>) with <var>x</var> + <var>y</var> &le; 6; the &ldquo;sum&rdquo; die can sit in any of 3 positions, and no outcome is counted twice (two dice cannot both equal the sum of the others). That is 45 outcomes out of 216: probability 45/216 = <b>5/24</b>.'}},
 '4.5': {
  'q': {'ru': 'Сколько путей из (0;&nbsp;0) в (5;&nbsp;5) шагами вправо и вверх не проходят ни через (1;&nbsp;1), ни через (4;&nbsp;4)?',
        'en': 'How many paths from (0,&nbsp;0) to (5,&nbsp;5) by unit steps right and up avoid both (1,&nbsp;1) and (4,&nbsp;4)?'},
  'hint': {'ru': 'Включения-исключения по двум запретным точкам: все &minus; через первую &minus; через вторую + через обе.', 'en': 'Inclusion-exclusion over the two forbidden points: all &minus; through the first &minus; through the second + through both.'},
  'sol': {'ru': 'Всего C(10,&nbsp;5) = 252. Через (1;&nbsp;1): 2&nbsp;&middot;&nbsp;C(8;&nbsp;4) = 140; через (4;&nbsp;4): C(8;&nbsp;4)&nbsp;&middot;&nbsp;2 = 140; через обе: 2&nbsp;&middot;&nbsp;C(6;&nbsp;3)&nbsp;&middot;&nbsp;2 = 80. Ответ: 252 &minus; 140 &minus; 140 + 80 = <b>52</b>. Урок 4.3 работает и на решётке: дважды вычтенное вернуть.', 'en': 'Total: C(10,&nbsp;5) = 252. Through (1,&nbsp;1): 2&nbsp;&middot;&nbsp;C(8,&nbsp;4) = 140; through (4,&nbsp;4): C(8,&nbsp;4)&nbsp;&middot;&nbsp;2 = 140; through both: 2&nbsp;&middot;&nbsp;C(6,&nbsp;3)&nbsp;&middot;&nbsp;2 = 80. Answer: 252 &minus; 140 &minus; 140 + 80 = <b>52</b>. Lesson 4.3 works on the grid too: give back what was subtracted twice.'}},
}
