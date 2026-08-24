# -*- coding: utf-8 -*-
"""Блок 1 «Алгебра»: урок 1.5 + тест Т1, RU+EN."""

def F(a, b):
    return f'<span class="frac"><span>{a}</span><span>{b}</span></span>'

L15 = {
 'id': '1.5', 'anchor': 'u15',
 'title': {'ru': 'Модуль: уравнения, неравенства, расстояния',
           'en': 'Absolute Value: Equations, Inequalities, Distances'},
 'theory': {
  'ru': """
<p><b>Модуль &mdash; это расстояние.</b> |<var>x</var>| &mdash; расстояние от <var>x</var> до нуля; |<var>x</var> &minus; <var>a</var>| &mdash; расстояние от <var>x</var> до точки <var>a</var>. Половина задач с модулем решается картинкой на числовой прямой быстрее, чем разбором случаев.</p>
<div class="frm">|<var>f</var>| = <var>c</var> (при <var>c</var> &gt; 0) &hArr; <var>f</var> = <var>c</var> или <var>f</var> = &minus;<var>c</var>. &nbsp;При <var>a</var> &gt; 0: |<var>x</var>| &lt; <var>a</var> &hArr; &minus;<var>a</var> &lt; <var>x</var> &lt; <var>a</var>; &nbsp;|<var>x</var>| &gt; <var>a</var> &hArr; <var>x</var> &lt; &minus;<var>a</var> или <var>x</var> &gt; <var>a</var>.</div>
<p><b>Сумма расстояний.</b> |<var>x</var> &minus; <var>a</var>| + |<var>x</var> &minus; <var>b</var>| &mdash; это суммарное расстояние от <var>x</var> до двух точек. Между точками она постоянна и равна |<var>a</var> &minus; <var>b</var>|; вне &mdash; растёт. Для нечётного числа точек минимум суммы расстояний достигается в средней (медианной) точке.</p>
<p><b>Вложенные модули.</b> ||<var>x</var>| &minus; 4| = 2 раскрывается послойно, снаружи внутрь: сначала |<var>x</var>| &minus; 4 = &plusmn;2, потом каждый случай отдельно. Аккуратность важнее скорости: считайте корни в конце.</p>""",
  'en': """
<p><b>Absolute value is distance.</b> |<var>x</var>| is the distance from <var>x</var> to zero; |<var>x</var> &minus; <var>a</var>| is the distance from <var>x</var> to the point <var>a</var>. Half of all absolute-value problems are solved faster by a number-line picture than by case analysis.</p>
<div class="frm">|<var>f</var>| = <var>c</var> (for <var>c</var> &gt; 0) &hArr; <var>f</var> = <var>c</var> or <var>f</var> = &minus;<var>c</var>. &nbsp;For <var>a</var> &gt; 0: |<var>x</var>| &lt; <var>a</var> &hArr; &minus;<var>a</var> &lt; <var>x</var> &lt; <var>a</var>; &nbsp;|<var>x</var>| &gt; <var>a</var> &hArr; <var>x</var> &lt; &minus;<var>a</var> or <var>x</var> &gt; <var>a</var>.</div>
<p><b>Sum of distances.</b> |<var>x</var> &minus; <var>a</var>| + |<var>x</var> &minus; <var>b</var>| is the total distance from <var>x</var> to two points. Between the points it is constant and equals |<var>a</var> &minus; <var>b</var>|; outside, it grows. For an odd number of points, the minimum of the sum of distances is at the middle (median) point.</p>
<p><b>Nested absolute values.</b> ||<var>x</var>| &minus; 4| = 2 unwraps layer by layer, outside in: first |<var>x</var>| &minus; 4 = &plusmn;2, then each case separately. Care beats speed: count the roots at the end.</p>"""},
 'worked': [
  {'tag': {'ru': 'Разбор 1 · уравнение', 'en': 'Example 1 · equation'},
   'q': {'ru': 'Решите уравнение |2<var>x</var> &minus; 3| = 7.',
         'en': 'Solve |2<var>x</var> &minus; 3| = 7.'},
   'sol': {'ru': '2<var>x</var> &minus; 3 = 7 или 2<var>x</var> &minus; 3 = &minus;7: корни <b>5 и &minus;2</b>. Проверка подстановкой: |7| = 7, |&minus;7| = 7. Верно.',
          'en': '2<var>x</var> &minus; 3 = 7 or 2<var>x</var> &minus; 3 = &minus;7: roots <b>5 and &minus;2</b>. Check by substitution: |7| = 7, |&minus;7| = 7. Correct.'}},
  {'tag': {'ru': 'Разбор 2 · сумма расстояний', 'en': 'Example 2 · sum of distances'},
   'q': {'ru': 'Каково наименьшее значение выражения |<var>x</var> &minus; 1| + |<var>x</var> &minus; 5|, и при каких <var>x</var> оно достигается?',
         'en': 'What is the least value of |<var>x</var> &minus; 1| + |<var>x</var> &minus; 5|, and for which <var>x</var> is it attained?'},
   'sol': {'ru': 'Это сумма расстояний от <var>x</var> до точек 1 и 5. Между ними она постоянна и равна расстоянию между точками: <b>4</b>, при любом <var>x</var> из отрезка [1;&nbsp;5]. Никакого разбора случаев: одна картинка.',
          'en': 'This is the total distance from <var>x</var> to the points 1 and 5. Between them it is constant and equals the distance between the points: <b>4</b>, for every <var>x</var> in [1,&nbsp;5]. No case analysis: one picture.'}},
  {'tag': {'ru': 'Разбор 3 · неравенство', 'en': 'Example 3 · inequality'},
   'q': {'ru': 'Сколько целых чисел удовлетворяет неравенству |<var>x</var> &minus; 2| &lt; 3?',
         'en': 'How many integers satisfy |<var>x</var> &minus; 2| &lt; 3?'},
   'sol': {'ru': '&minus;3 &lt; <var>x</var> &minus; 2 &lt; 3, то есть &minus;1 &lt; <var>x</var> &lt; 5. Целые: 0, 1, 2, 3, 4 &mdash; <b>пять</b>. Частая ошибка &mdash; посчитать концы: при строгом неравенстве &minus;1 и 5 не входят.',
          'en': '&minus;3 &lt; <var>x</var> &minus; 2 &lt; 3, that is &minus;1 &lt; <var>x</var> &lt; 5. Integers: 0, 1, 2, 3, 4 &mdash; <b>five</b>. A frequent mistake is counting the endpoints: with a strict inequality, &minus;1 and 5 are not included.'}},
  {'tag': {'ru': 'Разбор 4 · вложенные модули', 'en': 'Example 4 · nested absolute values'},
   'q': {'ru': 'Сколько корней у уравнения ||<var>x</var>| &minus; 4| = 2?',
         'en': 'How many solutions does ||<var>x</var>| &minus; 4| = 2 have?'},
   'sol': {'ru': 'Слой первый: |<var>x</var>| &minus; 4 = 2 или &minus;2, то есть |<var>x</var>| = 6 или |<var>x</var>| = 2. Слой второй: <var>x</var> = &plusmn;6 и <var>x</var> = &plusmn;2. Итого <b>4 корня</b>.',
          'en': 'First layer: |<var>x</var>| &minus; 4 = 2 or &minus;2, so |<var>x</var>| = 6 or |<var>x</var>| = 2. Second layer: <var>x</var> = &plusmn;6 and <var>x</var> = &plusmn;2. In total, <b>4 solutions</b>.'}},
 ],
 'selfp': [
  {'q': {'ru': 'Решите уравнение |<var>x</var> + 4| = 9 и найдите сумму корней.', 'en': 'Solve |<var>x</var> + 4| = 9 and find the sum of the roots.'},
   'hint': {'ru': 'Два случая: <var>x</var> + 4 = &plusmn;9.', 'en': 'Two cases: <var>x</var> + 4 = &plusmn;9.'},
   'sol': {'ru': 'Корни 5 и &minus;13: они симметричны относительно точки &minus;4, поэтому сумма равна <b>&minus;8</b>.', 'en': 'The solutions are 5 and &minus;13: they are symmetric about &minus;4, so the sum is <b>&minus;8</b>.'}},
  {'q': {'ru': 'Сколько корней у уравнения |3<var>x</var> &minus; 6| = 0?', 'en': 'How many solutions does |3<var>x</var> &minus; 6| = 0 have?'},
   'hint': {'ru': 'Модуль равен нулю только в одной ситуации.', 'en': 'An absolute value is zero in only one situation.'},
   'sol': {'ru': 'Только 3<var>x</var> &minus; 6 = 0: <b>один корень</b>, <var>x</var> = 2.', 'en': 'Only 3<var>x</var> &minus; 6 = 0: <b>one solution</b>, <var>x</var> = 2.'}},
  {'q': {'ru': 'Сколько целых чисел удовлетворяет неравенству |<var>x</var> &minus; 3| &le; 5?', 'en': 'How many integers satisfy |<var>x</var> &minus; 3| &le; 5?'},
   'hint': {'ru': 'Отрезок от &minus;2 до 8, концы входят.', 'en': 'The segment from &minus;2 to 8, endpoints included.'},
   'sol': {'ru': 'От &minus;2 до 8 включительно: <b>11 чисел</b>.', 'en': 'From &minus;2 to 8 inclusive: <b>11 integers</b>.'}},
  {'q': {'ru': 'Сколько целых решений у уравнения |<var>x</var> + 2| + |<var>x</var> &minus; 4| = 6?', 'en': 'How many integer solutions does |<var>x</var> + 2| + |<var>x</var> &minus; 4| = 6 have?'},
   'hint': {'ru': 'Сравните 6 с расстоянием между точками &minus;2 и 4.', 'en': 'Compare 6 with the distance between the points &minus;2 and 4.'},
   'sol': {'ru': 'Расстояние между &minus;2 и 4 равно 6, значит равенство выполняется на всём отрезке [&minus;2;&nbsp;4]. Целых решений <b>7</b>.', 'en': 'The distance between &minus;2 and 4 is 6, so the equation holds on the whole segment [&minus;2,&nbsp;4]. Integer solutions: <b>7</b>.'}},
  {'q': {'ru': 'Решите уравнение |<var>x</var> &minus; 1| = |<var>x</var> &minus; 7|.', 'en': 'Solve |<var>x</var> &minus; 1| = |<var>x</var> &minus; 7|.'},
   'hint': {'ru': 'Точка, равноудалённая от 1 и 7.', 'en': 'The point equidistant from 1 and 7.'},
   'sol': {'ru': 'Середина: <var>x</var> = <b>4</b>.', 'en': 'The midpoint: <var>x</var> = <b>4</b>.'}},
  {'q': {'ru': 'Каково наименьшее значение выражения |<var>x</var> &minus; 2| + |<var>x</var> &minus; 6| + |<var>x</var> &minus; 9|?', 'en': 'What is the least value of |<var>x</var> &minus; 2| + |<var>x</var> &minus; 6| + |<var>x</var> &minus; 9|?'},
   'hint': {'ru': 'Три точки: минимум в средней.', 'en': 'Three points: the minimum is at the middle one.'},
   'sol': {'ru': 'При <var>x</var> = 6: 4 + 0 + 3 = <b>7</b>.', 'en': 'At <var>x</var> = 6: 4 + 0 + 3 = <b>7</b>.'}},
  {'q': {'ru': 'Найдите наименьшее натуральное решение неравенства |5 &minus; 2<var>x</var>| &gt; 3.', 'en': 'Find the least positive integer solution of |5 &minus; 2<var>x</var>| &gt; 3.'},
   'hint': {'ru': '&laquo;Модуль больше 3&raquo; значит: выражение под модулем больше 3 или меньше &minus;3.', 'en': '&ldquo;Absolute value greater than 3&rdquo; means: the expression inside is greater than 3 or less than &minus;3.'},
   'sol': {'ru': 'Натуральные из <var>x</var> &gt; 4 начинаются с <b>5</b> (числа 1&ndash;4 не подходят: подставьте и проверьте).', 'en': 'Positive integers with <var>x</var> &gt; 4 start at <b>5</b> (1 through 4 fail: substitute and check).'}},
  {'q': {'ru': 'Сколько корней у уравнения ||<var>x</var> &minus; 1| &minus; 3| = 2?', 'en': 'How many solutions does ||<var>x</var> &minus; 1| &minus; 3| = 2 have?'},
   'hint': {'ru': 'Раскрывайте снаружи внутрь, слой за слоем.', 'en': 'Unwrap from the outside in, one layer at a time.'},
   'sol': {'ru': '|<var>x</var> &minus; 1| = 5 даёт 6 и &minus;4; |<var>x</var> &minus; 1| = 1 даёт 2 и 0. Всего <b>4 корня</b>.', 'en': '|<var>x</var> &minus; 1| = 5 gives 6 and &minus;4; |<var>x</var> &minus; 1| = 1 gives 2 and 0. In total, <b>4 solutions</b>.'}},
 ],
 'answers': {'ru': '−8 · 1 корень · 11 · 7 · 4 · 7 · 5 · 4 корня', 'en': '−8, 1 solution, 11, 7, 4, 7, 5, 4 solutions'},
 'routing': {'ru': 'Норма &mdash; 6 из 8. Ошибки в 1&ndash;2 &mdash; &laquo;модуль как два случая&raquo;; в 3 и 7 &mdash; неравенства и концы; в 4&ndash;6 &mdash; &laquo;расстояния на прямой&raquo;; в 8 &mdash; &laquo;вложенные модули&raquo;.',
             'en': 'Mastery bar: 6 of 8. For mistakes in 1&ndash;2, reread &ldquo;two cases&rdquo;; for 3 and 7, inequalities and endpoints; for 4&ndash;6, &ldquo;distances on the line&rdquo;; for 8, &ldquo;nested absolute values&rdquo;.'},
}

T1 = {
 'problems': [
  {'q': {'ru': 'Цену дважды повышали на 20&nbsp;%, после чего она стала 144 доллара. Какой была исходная цена (в долларах)?',
         'en': 'A price was increased by 20% twice in succession, after which it was $144. What was the original price (in dollars)?'},
   'opts': {'ru': ['96', '100', '104', '110', '120'], 'en': ['96', '100', '104', '110', '120']}},
  {'q': {'ru': 'Числа <var>a</var> и <var>b</var> относятся как 3&nbsp;:&nbsp;5, и <var>a</var> + <var>b</var> = 64. Чему равно <var>b</var> &minus; <var>a</var>?',
         'en': 'Numbers <var>a</var> and <var>b</var> are in the ratio 3&nbsp;:&nbsp;5, and <var>a</var> + <var>b</var> = 64. What is <var>b</var> &minus; <var>a</var>?'},
   'opts': {'ru': ['8', '12', '16', '24', '40'], 'en': ['8', '12', '16', '24', '40']}},
  {'q': {'ru': 'Половину пути велосипедист ехал со скоростью 20 км/ч, другую половину &mdash; 30 км/ч. Какова его средняя скорость (км/ч)?',
         'en': 'A cyclist rides half of a route at 20 mph and the other half at 30 mph. What is the average speed (mph)?'},
   'opts': {'ru': ['24', '25', '26', '27', '28'], 'en': ['24', '25', '26', '27', '28']}},
  {'q': {'ru': 'Числа <var>x</var> и <var>y</var> таковы, что <var>x</var> + <var>y</var> = 10 и <var>x</var><sup>2</sup> &minus; <var>y</var><sup>2</sup> = 40. Чему равно <var>x</var>?',
         'en': 'Numbers <var>x</var> and <var>y</var> satisfy <var>x</var> + <var>y</var> = 10 and <var>x</var><sup>2</sup> &minus; <var>y</var><sup>2</sup> = 40. What is <var>x</var>?'},
   'opts': {'ru': ['4', '5', '6', '7', '8'], 'en': ['4', '5', '6', '7', '8']}},
  {'q': {'ru': 'Одна труба наполняет бак за 2 часа, другая &mdash; за 3. За сколько часов они наполнят бак вместе?',
         'en': 'One pipe fills a tank in 2 hours, another in 3. How many hours do they need together?'},
   'opts': {'ru': ['1', '1,2', '1,5', '2,5', '5'], 'en': ['1', '1.2', '1.5', '2.5', '5']}},
  {'q': {'ru': 'Пусть <var>r</var> и <var>s</var> &mdash; корни уравнения <var>x</var><sup>2</sup> &minus; 9<var>x</var> + 14 = 0. Чему равно <var>r</var><sup>2</sup> + <var>s</var><sup>2</sup>?',
         'en': 'Let <var>r</var> and <var>s</var> be the roots of <var>x</var><sup>2</sup> &minus; 9<var>x</var> + 14 = 0. What is <var>r</var><sup>2</sup> + <var>s</var><sup>2</sup>?'},
   'opts': {'ru': ['25', '39', '45', '49', '53'], 'en': ['25', '39', '45', '49', '53']}},
  {'q': {'ru': 'Каково наименьшее значение выражения <var>x</var><sup>2</sup> &minus; 8<var>x</var> + 3?',
         'en': 'What is the least value of <var>x</var><sup>2</sup> &minus; 8<var>x</var> + 3?'},
   'opts': {'ru': ['&minus;16', '&minus;13', '&minus;8', '3', '13'], 'en': ['&minus;16', '&minus;13', '&minus;8', '3', '13']}},
  {'q': {'ru': 'Действительное число <var>x</var> удовлетворяет равенству <var>x</var> + 1/<var>x</var> = 6. Чему равно <var>x</var><sup>2</sup> + 1/<var>x</var><sup>2</sup>?',
         'en': 'A real number <var>x</var> satisfies <var>x</var> + 1/<var>x</var> = 6. What is <var>x</var><sup>2</sup> + 1/<var>x</var><sup>2</sup>?'},
   'opts': {'ru': ['30', '32', '34', '36', '38'], 'en': ['30', '32', '34', '36', '38']}},
  {'q': {'ru': f'Чему равна сумма {F("1","1&middot;2")} + {F("1","2&middot;3")} + &hellip; + {F("1","19&middot;20")}?',
         'en': f'What is the sum {F("1","1&middot;2")} + {F("1","2&middot;3")} + &hellip; + {F("1","19&middot;20")}?'},
   'opts': {'ru': [F('9','10'), F('18','19'), F('19','20'), '1', F('20','19')], 'en': [F('9','10'), F('18','19'), F('19','20'), '1', F('20','19')]}},
  {'q': {'ru': 'Чему равна сумма корней уравнения |2<var>x</var> &minus; 5| = 9?',
         'en': 'What is the sum of the solutions of |2<var>x</var> &minus; 5| = 9?'},
   'opts': {'ru': ['&minus;14', '&minus;5', '2', '5', '14'], 'en': ['&minus;14', '&minus;5', '2', '5', '14']}},
 ],
 'key': ['B', 'C', 'A', 'D', 'B', 'E', 'B', 'C', 'C', 'D'],
 'hints': {
  'ru': [
   '<b>1.</b> 144 = <var>x</var>&nbsp;&middot;&nbsp;1,2&nbsp;&middot;&nbsp;1,2, значит <var>x</var> = 144/1,44 = 100.',
   '<b>2.</b> Часть <var>k</var> = 64/8 = 8: числа 24 и 40, разность 16.',
   '<b>3.</b> 2&middot;20&middot;30/(20+30) = 24. Не 25: на медленной половине уходит больше времени.',
   '<b>4.</b> <var>x</var><sup>2</sup> &minus; <var>y</var><sup>2</sup> = (<var>x</var>+<var>y</var>)(<var>x</var>&minus;<var>y</var>) = 40, значит <var>x</var> &minus; <var>y</var> = 4 и <var>x</var> = 7.',
   '<b>5.</b> 1/2 + 1/3 = 5/6 бака в час: 6/5 = 1,2 часа.',
   '<b>6.</b> Виета: 81 &minus; 2&middot;14 = 53.',
   '<b>7.</b> Вершина при <var>x</var> = 4: 16 &minus; 32 + 3 = &minus;13.',
   '<b>8.</b> 36 &minus; 2 = 34.',
   '<b>9.</b> Телескоп: 1 &minus; 1/20 = 19/20.',
   '<b>10.</b> Корни 7 и &minus;2, сумма 5.'],
  'en': [
   '<b>1.</b> 144 = <var>x</var>&nbsp;&middot;&nbsp;1.2&nbsp;&middot;&nbsp;1.2, so <var>x</var> = 144/1.44 = 100.',
   '<b>2.</b> One part <var>k</var> = 64/8 = 8: the numbers are 24 and 40, difference 16.',
   '<b>3.</b> 2&middot;20&middot;30/(20+30) = 24. Not 25: the slower half takes more time.',
   '<b>4.</b> <var>x</var><sup>2</sup> &minus; <var>y</var><sup>2</sup> = (<var>x</var>+<var>y</var>)(<var>x</var>&minus;<var>y</var>) = 40, so <var>x</var> &minus; <var>y</var> = 4 and <var>x</var> = 7.',
   '<b>5.</b> 1/2 + 1/3 = 5/6 of the tank per hour: 6/5 = 1.2 hours.',
   '<b>6.</b> Vieta: 81 &minus; 2&middot;14 = 53.',
   '<b>7.</b> Vertex at <var>x</var> = 4: 16 &minus; 32 + 3 = &minus;13.',
   '<b>8.</b> 36 &minus; 2 = 34.',
   '<b>9.</b> Telescoping: 1 &minus; 1/20 = 19/20.',
   '<b>10.</b> The solutions are 7 and &minus;2; their sum is 5.'],
 },
}


STARS = {
 '1.1': {
  'q': {'ru': 'В сосуде 40-процентный раствор кислоты. Четверть содержимого отлили и долили водой; затем ещё раз отлили четверть и долили водой. Какова теперь концентрация?',
        'en': 'A container holds a 40% acid solution. A quarter of the contents is removed and replaced with water; then a quarter is removed and replaced with water again. What is the concentration now?'},
  'hint': {'ru': 'После каждой замены кислоты остаётся 3/4 от прежней.', 'en': 'After each replacement, 3/4 of the acid remains.'},
  'sol': {'ru': 'Каждая замена умножает количество кислоты на 3/4: 40&nbsp;%&nbsp;&middot;&nbsp;(3/4)<sup>2</sup> = <b>22,5&nbsp;%</b>.', 'en': 'Each replacement multiplies the amount of acid by 3/4: 40%&nbsp;&middot;&nbsp;(3/4)<sup>2</sup> = <b>22.5%</b>.'}},
 '1.2': {
  'q': {'ru': 'Сумма первых <var>n</var> членов последовательности равна <var>S</var><sub><var>n</var></sub> = 3<var>n</var><sup>2</sup> + 2<var>n</var>. Найдите десятый член.',
        'en': 'The sum of the first <var>n</var> terms of a sequence is <var>S</var><sub><var>n</var></sub> = 3<var>n</var><sup>2</sup> + 2<var>n</var>. Find the tenth term.'},
  'hint': {'ru': 'Десятый член = <var>S</var><sub>10</sub> &minus; <var>S</var><sub>9</sub>.', 'en': 'The tenth term = <var>S</var><sub>10</sub> &minus; <var>S</var><sub>9</sub>.'},
  'sol': {'ru': '<var>S</var><sub>10</sub> = 320, <var>S</var><sub>9</sub> = 261: десятый член равен <b>59</b>. Приём работает для любой суммы: член = разность соседних сумм.', 'en': '<var>S</var><sub>10</sub> = 320, <var>S</var><sub>9</sub> = 261: the tenth term is <b>59</b>. The trick works for any sum formula: a term is the difference of consecutive sums.'}},
 '1.3': {
  'q': {'ru': 'Пусть <var>r</var> и <var>s</var> &mdash; корни уравнения <var>x</var><sup>2</sup> &minus; 3<var>x</var> &minus; 2 = 0. Квадратное уравнение вида <var>x</var><sup>2</sup> + <var>px</var> + <var>q</var> = 0 имеет корни <var>r</var> + 1 и <var>s</var> + 1. Чему равно <var>q</var>?',
        'en': 'Let <var>r</var> and <var>s</var> be the roots of <var>x</var><sup>2</sup> &minus; 3<var>x</var> &minus; 2 = 0. A quadratic of the form <var>x</var><sup>2</sup> + <var>px</var> + <var>q</var> = 0 has roots <var>r</var> + 1 and <var>s</var> + 1. What is <var>q</var>?'},
  'hint': {'ru': '<var>q</var> &mdash; произведение новых корней; раскройте (<var>r</var> + 1)(<var>s</var> + 1).', 'en': '<var>q</var> is the product of the new roots; expand (<var>r</var> + 1)(<var>s</var> + 1).'},
  'sol': {'ru': '(<var>r</var> + 1)(<var>s</var> + 1) = <var>rs</var> + <var>r</var> + <var>s</var> + 1 = &minus;2 + 3 + 1 = <b>2</b>. Корни искать не нужно: всё даёт Виета.', 'en': '(<var>r</var> + 1)(<var>s</var> + 1) = <var>rs</var> + <var>r</var> + <var>s</var> + 1 = &minus;2 + 3 + 1 = <b>2</b>. No need to find the roots: Vieta&rsquo;s formulas give everything.'}},
 '1.4': {
  'q': {'ru': 'Вычислите (2 + 1)(2<sup>2</sup> + 1)(2<sup>4</sup> + 1)(2<sup>8</sup> + 1) + 1.',
        'en': 'Compute (2 + 1)(2<sup>2</sup> + 1)(2<sup>4</sup> + 1)(2<sup>8</sup> + 1) + 1.'},
  'hint': {'ru': 'Домножьте произведение на (2 &minus; 1) &mdash; оно не изменится, а разности квадратов начнут схлопываться.', 'en': 'Multiply the product by (2 &minus; 1) &mdash; it changes nothing, and differences of squares start collapsing.'},
  'sol': {'ru': '(2&minus;1)(2+1)(2<sup>2</sup>+1)(2<sup>4</sup>+1)(2<sup>8</sup>+1) = 2<sup>16</sup> &minus; 1, значит выражение равно 2<sup>16</sup> = <b>65&nbsp;536</b>.', 'en': '(2&minus;1)(2+1)(2<sup>2</sup>+1)(2<sup>4</sup>+1)(2<sup>8</sup>+1) = 2<sup>16</sup> &minus; 1, so the expression equals 2<sup>16</sup> = <b>65,536</b>.'}},
 '1.5': {
  'q': {'ru': 'Сколько решений у уравнения |<var>x</var> &minus; 1| + |<var>x</var> &minus; 3| = <var>x</var>?',
        'en': 'How many solutions does |<var>x</var> &minus; 1| + |<var>x</var> &minus; 3| = <var>x</var> have?'},
  'hint': {'ru': 'Три промежутка: <var>x</var> &lt; 1, от 1 до 3, <var>x</var> &gt; 3. На каждом раскройте модули и проверьте, попал ли корень в промежуток.', 'en': 'Three intervals: <var>x</var> &lt; 1, from 1 to 3, <var>x</var> &gt; 3. Open the absolute values on each and check whether the root lands in its interval.'},
  'sol': {'ru': 'При <var>x</var> &lt; 1: 4 &minus; 2<var>x</var> = <var>x</var>, <var>x</var> = 4/3 &mdash; не в промежутке. При 1 &le; <var>x</var> &le; 3: 2 = <var>x</var> &mdash; подходит. При <var>x</var> &gt; 3: 2<var>x</var> &minus; 4 = <var>x</var>, <var>x</var> = 4 &mdash; подходит. Итого <b>2 решения</b> (2 и 4).', 'en': 'For <var>x</var> &lt; 1: 4 &minus; 2<var>x</var> = <var>x</var>, <var>x</var> = 4/3 &mdash; not in the interval. For 1 &le; <var>x</var> &le; 3: 2 = <var>x</var> &mdash; works. For <var>x</var> &gt; 3: 2<var>x</var> &minus; 4 = <var>x</var>, <var>x</var> = 4 &mdash; works. In total, <b>2 solutions</b> (2 and 4).'}},
}
