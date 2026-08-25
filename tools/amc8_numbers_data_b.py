# -*- coding: utf-8 -*-
"""AMC 8, блок 1: уроки 1.3–1.4, RU+EN."""

def F(a, b):
    return f'<span class="frac"><span>{a}</span><span>{b}</span></span>'

L13 = {
 'id': '1.3', 'anchor': 'u13',
 'title': {'ru': 'Отношения и пропорции', 'en': 'Ratios and Proportions'},
 'theory': {
  'ru': """
<p><b>Отношение &mdash; это части.</b> Если числа относятся как 3&nbsp;:&nbsp;5, представьте 3 части и 5 частей одинакового размера. Сумма &mdash; 8 частей: зная сумму, находим размер одной части делением.</p>
<div class="frm">Деление в отношении: сумму делим на общее число частей. 56 в отношении 3&nbsp;:&nbsp;4 &mdash; часть 56/7 = 8, числа 24 и 32.</div>
<p><b>Пропорция &mdash; равенство отношений.</b> Рецепты, карты, цены: если 3 стакана риса варят в 4 стаканах воды, то на 9 стаканов риса нужно втрое больше воды. Найдите, во сколько раз выросла одна величина, и умножьте вторую на то же. А если отношения сцеплены через общую величину (<var>a</var>:<var>b</var> и <var>b</var>:<var>c</var>), приведите <var>b</var> к одному числу в обоих &mdash; и цепочка склеится.</p>
<p><b>Цена за штуку (unit rate).</b> Сравнивать и пересчитывать удобнее всего через &laquo;цену одной штуки&raquo;: 6 наклеек стоят 42 цента &mdash; значит одна стоит 7, а десять стоят 70.</p>""",
  'en': """
<p><b>A ratio means parts.</b> If two numbers are in the ratio 3&nbsp;:&nbsp;5, picture 3 parts and 5 parts of the same size. The total is 8 parts: knowing the total, divide to get one part.</p>
<div class="frm">Splitting in a ratio: divide the total by the number of parts. 56 in the ratio 3&nbsp;:&nbsp;4 &mdash; one part is 56/7 = 8, the numbers are 24 and 32.</div>
<p><b>A proportion is an equality of ratios.</b> Recipes, maps, prices: if 3 cups of rice cook in 4 cups of water, then 9 cups of rice need three times the water. Find how many times one quantity grew and multiply the other by the same factor. And when ratios are chained through a shared quantity (<var>a</var>:<var>b</var> and <var>b</var>:<var>c</var>), scale <var>b</var> to the same number in both &mdash; and the chain links up.</p>
<p><b>Unit rate.</b> The easiest way to compare and rescale is the price of one item: 6 stickers cost 42 cents, so one costs 7, and ten cost 70.</p>"""},
 'worked': [
  {'tag': {'ru': 'Разбор 1 · деление в отношении', 'en': 'Example 1 · splitting in a ratio'},
   'q': {'ru': 'Разделите 72 в отношении 3 : 5.', 'en': 'Split 72 in the ratio 3 : 5.'},
   'sol': {'ru': 'Всего 8 частей, часть = 72/8 = 9. Числа: 27 и 45. Проверка: 27 + 45 = 72. <b>27 и 45</b>.',
          'en': '8 parts in all, one part = 72/8 = 9. The numbers: 27 and 45. Check: 27 + 45 = 72. <b>27 and 45</b>.'}},
  {'tag': {'ru': 'Разбор 2 · рецепт', 'en': 'Example 2 · recipe'},
   'q': {'ru': 'На 2 чашки муки кладут 3 ложки сахара. Сколько ложек сахара нужно на 8 чашек муки?', 'en': 'A recipe uses 3 tablespoons of sugar for every 2 cups of flour. How many tablespoons of sugar are needed for 8 cups of flour?'},
   'sol': {'ru': 'Муки стало вчетверо больше (8/2 = 4), значит и сахара вчетверо: 3&middot;4 = <b>12</b>.',
          'en': 'The flour grew fourfold (8/2 = 4), so the sugar does too: 3&middot;4 = <b>12</b>.'}},
  {'tag': {'ru': 'Разбор 3 · карта', 'en': 'Example 3 · map'},
   'q': {'ru': 'Масштаб карты 1 : 50 000. Какому расстоянию на местности отвечают 4 см на карте?', 'en': 'A map has scale 1 : 50,000. What real distance corresponds to 4 cm on the map?'},
   'sol': {'ru': '4 см на карте &mdash; это 4&middot;50 000 = 200 000 см = <b>2 км</b>. Главная работа тут &mdash; перевод единиц, делайте его в конце.',
          'en': '4 cm on the map is 4&middot;50,000 = 200,000 cm = <b>2 km</b>. The real work is the unit conversion; do it last.'}},
  {'tag': {'ru': 'Разбор 4 · цена за штуку', 'en': 'Example 4 · unit rate'},
   'q': {'ru': '6 карандашей стоят 90 центов. Сколько стоят 10 таких карандашей?', 'en': 'Six pencils cost 90 cents. How much do 10 such pencils cost?'},
   'sol': {'ru': 'Один карандаш: 90/6 = 15 центов. Десять: <b>150 центов</b> (доллар пятьдесят).',
          'en': 'One pencil: 90/6 = 15 cents. Ten: <b>150 cents</b> ($1.50).'}},
 ],
 'selfp': [
  {'q': {'ru': 'Разделите 45 в отношении 2 : 7. Чему равна большая часть?', 'en': 'Split 45 in the ratio 2 : 7. What is the larger part?'},
   'hint': {'ru': 'Всего 9 частей.', 'en': '9 parts in all.'},
   'sol': {'ru': 'Часть 45/9 = 5: части 10 и <b>35</b>.', 'en': 'One part is 45/9 = 5: the parts are 10 and <b>35</b>.'}},
  {'q': {'ru': 'Упростите отношение 12 : 18.', 'en': 'Simplify the ratio 12 : 18.'},
   'hint': {'ru': 'Разделите обе части на общий делитель.', 'en': 'Divide both sides by a common divisor.'},
   'sol': {'ru': 'Делим на 6: <b>2 : 3</b>.', 'en': 'Divide by 6: <b>2 : 3</b>.'}},
  {'q': {'ru': '5 одинаковых яблок весят 400 граммов. Сколько весят 8 таких яблок?', 'en': 'Five identical apples weigh 400 grams. How much do 8 such apples weigh?'},
   'hint': {'ru': 'Сначала вес одного яблока.', 'en': 'Find the weight of one apple first.'},
   'sol': {'ru': 'Одно яблоко 80 г, восемь &mdash; <b>640 г</b>.', 'en': 'One apple is 80 g, eight are <b>640 g</b>.'}},
  {'q': {'ru': '<var>a</var> : <var>b</var> = 3 : 4 и <var>b</var> : <var>c</var> = 2 : 5. Найдите <var>a</var> : <var>c</var>.', 'en': '<var>a</var> : <var>b</var> = 3 : 4 and <var>b</var> : <var>c</var> = 2 : 5. Find <var>a</var> : <var>c</var>.'},
   'hint': {'ru': 'Приведите b к одному числу в обоих отношениях (к 8).', 'en': 'Scale b to the same number in both ratios (to 8).'},
   'sol': {'ru': '<var>a</var> : <var>b</var> = 6 : 8, <var>b</var> : <var>c</var> = 8 : 20, значит <var>a</var> : <var>c</var> = 6 : 20 = <b>3 : 10</b>.', 'en': '<var>a</var> : <var>b</var> = 6 : 8 and <var>b</var> : <var>c</var> = 8 : 20, so <var>a</var> : <var>c</var> = 6 : 20 = <b>3 : 10</b>.'}},
  {'q': {'ru': 'Диктор прочитал 180 слов за 3 минуты. Какова его скорость в словах в минуту?', 'en': 'An audiobook narrator reads 180 words in 3 minutes. What is the rate in words per minute?'},
   'hint': {'ru': 'Слова разделить на минуты.', 'en': 'Words divided by minutes.'},
   'sol': {'ru': '180/3 = <b>60 слов в минуту</b>.', 'en': '180/3 = <b>60 words per minute</b>.'}},
  {'q': {'ru': 'Найдите <var>x</var>, если 3 : 4 = <var>x</var> : 20.', 'en': 'Find <var>x</var> if 3 : 4 = <var>x</var> : 20.'},
   'hint': {'ru': 'Во сколько раз 20 больше 4?', 'en': 'How many times larger than 4 is 20?'},
   'sol': {'ru': 'В 5 раз: <var>x</var> = 3&middot;5 = <b>15</b>.', 'en': 'Five times: <var>x</var> = 3&middot;5 = <b>15</b>.'}},
  {'q': {'ru': 'В сплаве медь и цинк в отношении 2 : 3. Меди 14 кг. Сколько весит весь сплав?', 'en': 'A trail mix has raisins and peanuts in the ratio 2:3. There are 14 ounces of raisins. How many ounces does the whole mix weigh?'},
   'hint': {'ru': 'Скольким частям отвечает изюм?', 'en': 'How many parts do the raisins account for?'},
   'sol': {'ru': 'Часть 7 кг, всего 5 частей: <b>35 кг</b>.', 'en': 'One part is 7 oz, five parts in all: <b>35 oz</b>.'}},
  {'q': {'ru': 'Отношение мальчиков к девочкам в классе 4 : 5, девочек на 3 больше. Сколько всего учеников?', 'en': 'The ratio of boys to girls in a class is 4 : 5, and there are 3 more girls than boys. How many students are there in all?'},
   'hint': {'ru': 'Скольким частям равна разница между девочками и мальчиками?', 'en': 'How many parts is the difference between girls and boys?'},
   'sol': {'ru': 'Часть = 3: всего 9 частей, то есть <b>27</b>.', 'en': 'One part = 3: nine parts in all, so <b>27</b>.'}},
 ],
 'answers': {'ru': '35 · 2:3 · 640 г · 3:10 · 60 · 15 · 35 кг · 27', 'en': '35, 2:3, 640 g, 3:10, 60, 15, 35 oz, 27'},
 'routing': {'ru': 'Норма &mdash; 6 из 8. Ошибки в 1&ndash;2 и 7&ndash;8 &mdash; &laquo;отношение как части&raquo;; в 3, 5&ndash;6 &mdash; &laquo;цена за штуку&raquo; и пропорции; в 4 &mdash; сшивание отношений.',
             'en': 'Mastery bar: 6 of 8. For mistakes in 1&ndash;2 and 7&ndash;8, reread &ldquo;a ratio means parts&rdquo;; for 3, 5&ndash;6, unit rate and proportions; for 4, chaining ratios.'},
}

L14 = {
 'id': '1.4', 'anchor': 'u14',
 'title': {'ru': 'Средние', 'en': 'Averages'},
 'theory': {
  'ru': """
<p><b>Среднее = сумма, делённая на количество.</b> Но решать задачи удобнее наоборот: <b>сумма = среднее &times; количество</b>. Почти каждая задача о среднем &mdash; это задача о сумме.</p>
<div class="frm">Узнайте сумму до и после изменения &mdash; и задача решится сама. Добавили число? Новая сумма минус старая. Убрали? Старая минус новая.</div>
<p><b>Недостающее число.</b> Нужно среднее 90 по трём контрольным, а первые две дали 88 и 86? Нужная сумма 270, набрано 174 &mdash; на третью остаётся 96. И полезный сдвиг: если каждое число выросло на 3, среднее тоже выросло ровно на 3.</p>
<p><b>Медиана</b> &mdash; середина упорядоченного списка. При нечётном количестве это средний элемент; при чётном &mdash; среднее двух средних: у набора 3, 5, 9, 11 медиана (5 + 9)/2 = 7. Сортировка обязательна. На AMC 8 медиану спрашивают не реже среднего.</p>""",
  'en': """
<p><b>The mean is the sum divided by the count.</b> But problems are easier the other way round: <b>sum = mean &times; count</b>. Nearly every average problem is really a sum problem.</p>
<div class="frm">Find the sum before and after the change &mdash; and the problem solves itself. A number added? New sum minus old. Removed? Old minus new.</div>
<p><b>The missing number.</b> Need an average of 90 across three quizzes, and the first two gave 88 and 86? The required sum is 270, you have 174 &mdash; the third must be 96. A useful shift: if every number grows by 3, the mean grows by exactly 3.</p>
<p><b>The median</b> is the middle value of the sorted list. With an odd count it is the middle element; with an even count, the average of the two middle ones: for 3, 5, 9, 11 the median is (5 + 9)/2 = 7. Sorting is mandatory. On the AMC 8 the median comes up as often as the mean.</p>"""},
 'worked': [
  {'tag': {'ru': 'Разбор 1 · через сумму', 'en': 'Example 1 · via the sum'},
   'q': {'ru': 'Среднее пяти чисел равно 14. Одно число, равное 26, убрали. Чему равно среднее оставшихся четырёх?', 'en': 'The mean of five numbers is 14. The number 26 is removed. What is the mean of the remaining four?'},
   'sol': {'ru': 'Сумма была 5&middot;14 = 70. Стала 70 &minus; 26 = 44. Среднее: 44/4 = <b>11</b>.',
          'en': 'The sum was 5&middot;14 = 70. It became 70 &minus; 26 = 44. Mean: 44/4 = <b>11</b>.'}},
  {'tag': {'ru': 'Разбор 2 · прямой счёт', 'en': 'Example 2 · direct computation'},
   'q': {'ru': 'Оценки за три контрольные: 78, 85, 92. Каково среднее?', 'en': 'Test scores: 78, 85, 92. What is the mean?'},
   'sol': {'ru': '(78 + 85 + 92)/3 = 255/3 = <b>85</b>. Быстрее заметить: 78 и 92 симметричны вокруг 85.',
          'en': '(78 + 85 + 92)/3 = 255/3 = <b>85</b>. Faster: notice 78 and 92 are symmetric around 85.'}},
  {'tag': {'ru': 'Разбор 3 · недостающий тест', 'en': 'Example 3 · the missing test'},
   'q': {'ru': 'За три теста набрано 74, 82 и 79. Сколько нужно набрать за четвёртый, чтобы среднее по четырём стало 80?', 'en': 'Three tests scored 74, 82, and 79. What must the fourth score be for the four-test average to equal 80?'},
   'sol': {'ru': 'Нужна сумма 4&middot;80 = 320. Набрано 235. Четвёртый тест: 320 &minus; 235 = <b>85</b>.',
          'en': 'The required sum is 4&middot;80 = 320. So far 235. The fourth test: 320 &minus; 235 = <b>85</b>.'}},
  {'tag': {'ru': 'Разбор 4 · медиана', 'en': 'Example 4 · median'},
   'q': {'ru': 'Найдите медиану набора 12, 3, 14, 7, 8.', 'en': 'Find the median of 12, 3, 14, 7, 8.'},
   'sol': {'ru': 'Упорядочим: 3, 7, 8, 12, 14. Средний элемент &mdash; <b>8</b>. Сортировка обязательна: медиана &laquo;как есть&raquo; (14) &mdash; типовая ошибка.',
          'en': 'Sort: 3, 7, 8, 12, 14. The middle element is <b>8</b>. Sorting is mandatory: taking the middle of the unsorted list (14) is the standard mistake.'}},
 ],
 'selfp': [
  {'q': {'ru': 'Найдите среднее чисел 7, 9 и 14.', 'en': 'Find the mean of 7, 9, and 14.'},
   'hint': {'ru': 'Сумма, потом деление.', 'en': 'Sum, then divide.'},
   'sol': {'ru': '30/3 = <b>10</b>.', 'en': '30/3 = <b>10</b>.'}},
  {'q': {'ru': 'Среднее шести чисел равно 12. Чему равна их сумма?', 'en': 'The mean of six numbers is 12. What is their sum?'},
   'hint': {'ru': 'Сумма = среднее × количество.', 'en': 'Sum = mean × count.'},
   'sol': {'ru': '6&middot;12 = <b>72</b>.', 'en': '6&middot;12 = <b>72</b>.'}},
  {'q': {'ru': 'Среднее четырёх чисел равно 9. Три из них: 6, 8 и 10. Найдите четвёртое.', 'en': 'The mean of four numbers is 9. Three of them are 6, 8, and 10. Find the fourth.'},
   'hint': {'ru': 'Какова должна быть сумма?', 'en': 'What must the sum be?'},
   'sol': {'ru': 'Сумма 36, набрано 24: четвёртое <b>12</b>.', 'en': 'The sum must be 36; we have 24: the fourth is <b>12</b>.'}},
  {'q': {'ru': 'К пяти числам добавили число 25, и среднее шести чисел стало 15. Каким было среднее исходных пяти?', 'en': 'The number 25 was added to five numbers, and the mean of the six became 15. What was the mean of the original five?'},
   'hint': {'ru': 'Сумму шести чисел даёт их среднее.', 'en': 'The mean of the six numbers gives you their sum.'},
   'sol': {'ru': 'Было 90 &minus; 25 = 65, среднее 65/5 = <b>13</b>.', 'en': 'The old sum is 90 &minus; 25 = 65, mean 65/5 = <b>13</b>.'}},
  {'q': {'ru': 'Найдите медиану набора 5, 12, 9, 3, 11, 7.', 'en': 'Find the median of 5, 12, 9, 3, 11, 7.'},
   'hint': {'ru': 'Сначала упорядочите; чисел чётное количество.', 'en': 'Sort first; the count is even.'},
   'sol': {'ru': 'По порядку: 3, 5, 7, 9, 11, 12. Медиана &mdash; среднее двух средних: (7 + 9)/2 = <b>8</b>.', 'en': 'Sorted: 3, 5, 7, 9, 11, 12. The median is the average of the two middle values: (7 + 9)/2 = <b>8</b>.'}},
  {'q': {'ru': 'Средний возраст четырёх детей 9 лет. Каким будет их средний возраст через 3 года?', 'en': 'The average age of four children is 9. What will their average age be in 3 years?'},
   'hint': {'ru': 'Каждый станет старше на 3.', 'en': 'Everyone gets 3 years older.'},
   'sol': {'ru': 'Среднее тоже вырастет на 3: <b>12</b>.', 'en': 'The mean grows by 3 as well: <b>12</b>.'}},
  {'q': {'ru': 'Маме 36 лет, папе 38, детям 4 и 6. Каков средний возраст семьи?', 'en': 'Mom is 36, Dad is 38, and the kids are 4 and 6. What is the average age of the family?'},
   'hint': {'ru': 'Сложите и разделите на четыре.', 'en': 'Add and divide by four.'},
   'sol': {'ru': '(36 + 38 + 4 + 6)/4 = 84/4 = <b>21</b>.', 'en': '(36 + 38 + 4 + 6)/4 = 84/4 = <b>21</b>.'}},
  {'q': {'ru': 'Среднее двадцати чисел равно 10. Одно число, равное 29, заменили на 9. Каким стало среднее?', 'en': 'The mean of twenty numbers is 10. One number equal to 29 is replaced by 9. What is the new mean?'},
   'hint': {'ru': 'Как изменилась сумма?', 'en': 'How did the sum change?'},
   'sol': {'ru': 'Сумма упала на 20: с 200 до 180. Среднее: 180/20 = <b>9</b>.', 'en': 'The sum dropped by 20: from 200 to 180. Mean: 180/20 = <b>9</b>.'}},
 ],
 'answers': {'ru': '10 · 72 · 12 · 13 · 8 · 12 · 21 · 9', 'en': '10, 72, 12, 13, 8, 12, 21, 9'},
 'routing': {'ru': 'Норма &mdash; 6 из 8. Ошибки в 1&ndash;2 и 7 &mdash; определение среднего; в 3&ndash;4 и 8 &mdash; &laquo;через сумму&raquo;; в 5 &mdash; медиана; в 6 &mdash; сдвиг всех чисел.',
             'en': 'Mastery bar: 6 of 8. For mistakes in 1&ndash;2 and 7, the definition; for 3&ndash;4 and 8, &ldquo;via the sum&rdquo;; for 5, the median; for 6, shifting every number.'},
}
