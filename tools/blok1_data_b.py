# -*- coding: utf-8 -*-
"""Блок 1 «Алгебра»: уроки 1.3–1.4, RU+EN."""

def F(a, b):
    return f'<span class="frac"><span>{a}</span><span>{b}</span></span>'

L13 = {
 'id': '1.3', 'anchor': 'u13',
 'title': {'ru': 'Квадратный трёхчлен: корни, Виета, вершина',
           'en': 'Quadratics: Roots, Vieta&rsquo;s Formulas, the Vertex'},
 'theory': {
  'ru': f"""
<p><b>Корни.</b> Сначала пробуйте разложить: <var>x</var><sup>2</sup> &minus; 7<var>x</var> + 12 = (<var>x</var> &minus; 3)(<var>x</var> &minus; 4). Не раскладывается за десять секунд &mdash; дискриминант: <var>D</var> = <var>b</var><sup>2</sup> &minus; 4<var>ac</var>, корни ({F('&minus;<var>b</var> &plusmn; &radic;<var>D</var>','2<var>a</var>')}). <var>D</var> &gt; 0 &mdash; два корня, <var>D</var> = 0 &mdash; один (двукратный), <var>D</var> &lt; 0 &mdash; нет действительных.</p>
<div class="frm"><b>Виета</b> для <var>x</var><sup>2</sup> + <var>px</var> + <var>q</var>: сумма корней = &minus;<var>p</var>, произведение = <var>q</var>. Олимпиадный смысл: о корнях можно узнать всё, не находя их самих.</div>
<p><b>Симметричные выражения через Виета.</b> <var>r</var><sup>2</sup> + <var>s</var><sup>2</sup> = (<var>r</var> + <var>s</var>)<sup>2</sup> &minus; 2<var>rs</var>; <var>r</var><sup>3</sup> + <var>s</var><sup>3</sup> = (<var>r</var> + <var>s</var>)<sup>3</sup> &minus; 3<var>rs</var>(<var>r</var> + <var>s</var>); 1/<var>r</var> + 1/<var>s</var> = (<var>r</var> + <var>s</var>)/<var>rs</var>. Эти три закрывают большинство задач.</p>
<p><b>Вершина.</b> Парабола <var>ax</var><sup>2</sup> + <var>bx</var> + <var>c</var> имеет вершину при <var>x</var> = &minus;<var>b</var>/2<var>a</var> &mdash; это точка минимума (<var>a</var> &gt; 0) или максимума (<var>a</var> &lt; 0). Задачи &laquo;найдите наименьшее значение&raquo; &mdash; это почти всегда подстановка вершины. И знак: при <var>a</var> &gt; 0 трёхчлен отрицателен строго между корнями и положителен вне их &mdash; этого достаточно для квадратных неравенств.</p>""",
  'en': f"""
<p><b>Roots.</b> Try factoring first: <var>x</var><sup>2</sup> &minus; 7<var>x</var> + 12 = (<var>x</var> &minus; 3)(<var>x</var> &minus; 4). If it does not factor in ten seconds, use the discriminant: <var>D</var> = <var>b</var><sup>2</sup> &minus; 4<var>ac</var>, roots ({F('&minus;<var>b</var> &plusmn; &radic;<var>D</var>','2<var>a</var>')}). <var>D</var> &gt; 0 &mdash; two roots, <var>D</var> = 0 &mdash; one (a double root), <var>D</var> &lt; 0 &mdash; no real roots.</p>
<div class="frm"><b>Vieta&rsquo;s formulas</b> for <var>x</var><sup>2</sup> + <var>px</var> + <var>q</var>: sum of roots = &minus;<var>p</var>, product = <var>q</var>. The competition payoff: you can learn everything about the roots without ever finding them.</div>
<p><b>Symmetric expressions via Vieta.</b> <var>r</var><sup>2</sup> + <var>s</var><sup>2</sup> = (<var>r</var> + <var>s</var>)<sup>2</sup> &minus; 2<var>rs</var>; <var>r</var><sup>3</sup> + <var>s</var><sup>3</sup> = (<var>r</var> + <var>s</var>)<sup>3</sup> &minus; 3<var>rs</var>(<var>r</var> + <var>s</var>); 1/<var>r</var> + 1/<var>s</var> = (<var>r</var> + <var>s</var>)/<var>rs</var>. These three cover most problems.</p>
<p><b>Vertex.</b> The parabola <var>ax</var><sup>2</sup> + <var>bx</var> + <var>c</var> has its vertex at <var>x</var> = &minus;<var>b</var>/2<var>a</var> &mdash; the minimum point (<var>a</var> &gt; 0) or maximum point (<var>a</var> &lt; 0). &ldquo;Find the least value&rdquo; problems are almost always a vertex substitution. And the sign: for <var>a</var> &gt; 0, the quadratic is negative strictly between its roots and positive outside them &mdash; that is all you need for quadratic inequalities.</p>"""},
 'worked': [
  {'tag': {'ru': 'Разбор 1 · разложение', 'en': 'Example 1 · factoring'},
   'q': {'ru': 'Решите уравнение <var>x</var><sup>2</sup> &minus; 7<var>x</var> + 12 = 0.',
         'en': 'Solve <var>x</var><sup>2</sup> &minus; 7<var>x</var> + 12 = 0.'},
   'sol': {'ru': 'Ищем два числа с суммой 7 и произведением 12: это 3 и 4. Корни <b>3 и 4</b>. Дискриминант тут не нужен: разложение быстрее и без арифметических ошибок.',
          'en': 'Look for two numbers with sum 7 and product 12: these are 3 and 4. Roots: <b>3 and 4</b>. No discriminant needed: factoring is faster and avoids arithmetic slips.'}},
  {'tag': {'ru': 'Разбор 2 · Виета', 'en': 'Example 2 · Vieta'},
   'q': {'ru': 'Пусть <var>r</var> и <var>s</var> &mdash; корни <var>x</var><sup>2</sup> &minus; 5<var>x</var> + 3 = 0. Чему равно <var>r</var><sup>2</sup> + <var>s</var><sup>2</sup>?',
         'en': 'Let <var>r</var> and <var>s</var> be the roots of <var>x</var><sup>2</sup> &minus; 5<var>x</var> + 3 = 0. What is <var>r</var><sup>2</sup> + <var>s</var><sup>2</sup>?'},
   'sol': {'ru': 'Виета: <var>r</var> + <var>s</var> = 5, <var>rs</var> = 3. Тогда <var>r</var><sup>2</sup> + <var>s</var><sup>2</sup> = 25 &minus; 2&middot;3 = <b>19</b>. Сами корни иррациональны, и находить их &mdash; потеря двух минут.',
          'en': 'By Vieta&rsquo;s formulas, <var>r</var> + <var>s</var> = 5, <var>rs</var> = 3. Then <var>r</var><sup>2</sup> + <var>s</var><sup>2</sup> = 25 &minus; 2&middot;3 = <b>19</b>. The roots themselves are irrational, and finding them wastes two minutes.'}},
  {'tag': {'ru': 'Разбор 3 · вершина', 'en': 'Example 3 · vertex'},
   'q': {'ru': 'Найдите наименьшее значение выражения <var>x</var><sup>2</sup> &minus; 6<var>x</var> + 11.',
         'en': 'Find the least value of <var>x</var><sup>2</sup> &minus; 6<var>x</var> + 11.'},
   'sol': {'ru': 'Вершина при <var>x</var> = 6/2 = 3. Значение: 9 &minus; 18 + 11 = <b>2</b>. Второй способ &mdash; выделение полного квадрата: (<var>x</var> &minus; 3)<sup>2</sup> + 2 &ge; 2, и видно, что минимум равен 2 при <var>x</var> = 3.',
          'en': 'Vertex at <var>x</var> = 6/2 = 3. Value: 9 &minus; 18 + 11 = <b>2</b>. Alternatively, complete the square: (<var>x</var> &minus; 3)<sup>2</sup> + 2 &ge; 2, which shows the minimum is 2, at <var>x</var> = 3.'}},
  {'tag': {'ru': 'Разбор 4 · параметр', 'en': 'Example 4 · parameter'},
   'q': {'ru': 'При каких <var>k</var> уравнение <var>x</var><sup>2</sup> + <var>kx</var> + 9 = 0 имеет ровно один корень?',
         'en': 'For which <var>k</var> does <var>x</var><sup>2</sup> + <var>kx</var> + 9 = 0 have exactly one root?'},
   'sol': {'ru': 'Ровно один корень &hArr; <var>D</var> = 0: <var>k</var><sup>2</sup> &minus; 36 = 0, то есть <var>k</var> = <b>6 или &minus;6</b>. Классическая потеря балла &mdash; забыть отрицательное значение.',
          'en': 'Exactly one root &hArr; <var>D</var> = 0: <var>k</var><sup>2</sup> &minus; 36 = 0, so <var>k</var> = <b>6 or &minus;6</b>. The classic way to lose a point here is forgetting the negative value.'}},
 ],
 'selfp': [
  {'q': {'ru': 'Решите уравнение <var>x</var><sup>2</sup> = 5<var>x</var>. Укажите все корни.', 'en': 'Solve <var>x</var><sup>2</sup> = 5<var>x</var>. Give all roots.'},
   'hint': {'ru': 'Не делите на <var>x</var>! Перенесите и вынесите множитель.', 'en': 'Do not divide by <var>x</var>! Move everything to one side and factor.'},
   'sol': {'ru': '<var>x</var>(<var>x</var> &minus; 5) = 0: корни <b>0 и 5</b>. Деление на <var>x</var> теряет корень 0.', 'en': '<var>x</var>(<var>x</var> &minus; 5) = 0: roots <b>0 and 5</b>. Dividing by <var>x</var> loses the root 0.'}},
  {'q': {'ru': 'Найдите наибольший корень уравнения <var>x</var><sup>2</sup> &minus; 2<var>x</var> &minus; 15 = 0.', 'en': 'Find the largest root of <var>x</var><sup>2</sup> &minus; 2<var>x</var> &minus; 15 = 0.'},
   'hint': {'ru': 'Два числа: произведение &minus;15, сумма 2.', 'en': 'Two numbers: product &minus;15, sum 2.'},
   'sol': {'ru': '(<var>x</var> &minus; 5)(<var>x</var> + 3) = 0: корни 5 и &minus;3. Наибольший &mdash; <b>5</b>.', 'en': '(<var>x</var> &minus; 5)(<var>x</var> + 3) = 0: roots 5 and &minus;3. The largest is <b>5</b>.'}},
  {'q': {'ru': 'Корни <var>r</var> и <var>s</var> удовлетворяют <var>r</var> + <var>s</var> = 6 и <var>rs</var> = 4. Чему равно 1/<var>r</var> + 1/<var>s</var>?', 'en': 'Roots <var>r</var> and <var>s</var> satisfy <var>r</var> + <var>s</var> = 6 and <var>rs</var> = 4. What is 1/<var>r</var> + 1/<var>s</var>?'},
   'hint': {'ru': 'Приведите к общему знаменателю.', 'en': 'Combine over a common denominator.'},
   'sol': {'ru': '(<var>r</var> + <var>s</var>)/<var>rs</var> = 6/4 = <b>3/2</b>.', 'en': '(<var>r</var> + <var>s</var>)/<var>rs</var> = 6/4 = <b>3/2</b>.'}},
  {'q': {'ru': 'Пусть <var>r</var> и <var>s</var> &mdash; корни <var>x</var><sup>2</sup> &minus; 4<var>x</var> + 1 = 0. Чему равно <var>r</var><sup>3</sup> + <var>s</var><sup>3</sup>?', 'en': 'Let <var>r</var> and <var>s</var> be the roots of <var>x</var><sup>2</sup> &minus; 4<var>x</var> + 1 = 0. What is <var>r</var><sup>3</sup> + <var>s</var><sup>3</sup>?'},
   'hint': {'ru': '(<var>r</var> + <var>s</var>)<sup>3</sup> &minus; 3<var>rs</var>(<var>r</var> + <var>s</var>).', 'en': '(<var>r</var> + <var>s</var>)<sup>3</sup> &minus; 3<var>rs</var>(<var>r</var> + <var>s</var>).'},
   'sol': {'ru': '64 &minus; 3&nbsp;&middot;&nbsp;1&nbsp;&middot;&nbsp;4 = <b>52</b>.', 'en': '64 &minus; 3&nbsp;&middot;&nbsp;1&nbsp;&middot;&nbsp;4 = <b>52</b>.'}},
  {'q': {'ru': 'Найдите наибольшее значение выражения &minus;<var>x</var><sup>2</sup> + 8<var>x</var> &minus; 7.', 'en': 'Find the greatest value of &minus;<var>x</var><sup>2</sup> + 8<var>x</var> &minus; 7.'},
   'hint': {'ru': 'Ветви вниз: максимум в вершине <var>x</var> = &minus;<var>b</var>/2<var>a</var>.', 'en': 'The parabola opens downward: the maximum is at the vertex <var>x</var> = &minus;<var>b</var>/2<var>a</var>.'},
   'sol': {'ru': 'Вершина при <var>x</var> = 4: &minus;16 + 32 &minus; 7 = <b>9</b>.', 'en': 'Vertex at <var>x</var> = 4: &minus;16 + 32 &minus; 7 = <b>9</b>.'}},
  {'q': {'ru': 'Число 2 &mdash; корень уравнения <var>x</var><sup>2</sup> &minus; 6<var>x</var> + <var>c</var> = 0. Найдите второй корень.', 'en': 'The number 2 is a root of <var>x</var><sup>2</sup> &minus; 6<var>x</var> + <var>c</var> = 0. Find the other root.'},
   'hint': {'ru': 'Сумма корней известна из Виета.', 'en': 'The sum of the roots is known from Vieta.'},
   'sol': {'ru': 'Сумма корней 6, значит второй корень <b>4</b> (и заодно <var>c</var> = 8).', 'en': 'The sum of the roots is 6, so the other root is <b>4</b> (and incidentally <var>c</var> = 8).'}},
  {'q': {'ru': 'Сколько целых чисел удовлетворяет неравенству <var>x</var><sup>2</sup> &minus; 5<var>x</var> + 6 &lt; 0?', 'en': 'How many integers satisfy <var>x</var><sup>2</sup> &minus; 5<var>x</var> + 6 &lt; 0?'},
   'hint': {'ru': 'Разложите и посмотрите, где произведение отрицательно.', 'en': 'Factor and see where the product is negative.'},
   'sol': {'ru': '(<var>x</var> &minus; 2)(<var>x</var> &minus; 3) &lt; 0 при 2 &lt; <var>x</var> &lt; 3. Целых там <b>нет: 0</b>.', 'en': '(<var>x</var> &minus; 2)(<var>x</var> &minus; 3) &lt; 0 for 2 &lt; <var>x</var> &lt; 3. There are <b>no integers there: 0</b>.'}},
  {'q': {'ru': 'Квадратное уравнение с целыми коэффициентами имеет корни 3 + &radic;2 и 3 &minus; &radic;2. Чему равно произведение корней?', 'en': 'A quadratic with integer coefficients has roots 3 + &radic;2 and 3 &minus; &radic;2. What is the product of the roots?'},
   'hint': {'ru': '(<var>a</var> + <var>b</var>)(<var>a</var> &minus; <var>b</var>) = <var>a</var><sup>2</sup> &minus; <var>b</var><sup>2</sup>.', 'en': '(<var>a</var> + <var>b</var>)(<var>a</var> &minus; <var>b</var>) = <var>a</var><sup>2</sup> &minus; <var>b</var><sup>2</sup>.'},
   'sol': {'ru': '9 &minus; 2 = <b>7</b>. Само уравнение: <var>x</var><sup>2</sup> &minus; 6<var>x</var> + 7 = 0.', 'en': '9 &minus; 2 = <b>7</b>. The equation itself: <var>x</var><sup>2</sup> &minus; 6<var>x</var> + 7 = 0.'}},
 ],
 'answers': {'ru': '0 и 5 · 5 · 3/2 · 52 · 9 · 4 · 0 · 7', 'en': '0 and 5, 5, 3/2, 52, 9, 4, 0, 7'},
 'routing': {'ru': 'Норма &mdash; 6 из 8. Ошибки в 1&ndash;2 &mdash; &laquo;корни и разложение&raquo;; в 3&ndash;4 и 6 &mdash; &laquo;Виета&raquo;; в 5 &mdash; &laquo;вершина&raquo;; в 7 &mdash; знак трёхчлена в теории; в 8 &mdash; разбор решения целиком.',
             'en': 'Mastery bar: 6 of 8. For mistakes in 1&ndash;2, reread &ldquo;roots and factoring&rdquo;; for 3&ndash;4 and 6, &ldquo;Vieta&rsquo;s formulas&rdquo;; for 5, &ldquo;the vertex&rdquo;; for 7, the sign rule in the theory; for 8, go through the full solution.'},
}

L14 = {
 'id': '1.4', 'anchor': 'u14',
 'title': {'ru': 'Тождества и трюки: квадраты, кубы, телескопы',
           'en': 'Identities and Tricks: Squares, Cubes, Telescoping'},
 'theory': {
  'ru': f"""
<p><b>Три тождества, которые надо узнавать в лицо.</b> (<var>a</var> &plusmn; <var>b</var>)<sup>2</sup> = <var>a</var><sup>2</sup> &plusmn; 2<var>ab</var> + <var>b</var><sup>2</sup>; разность квадратов <var>a</var><sup>2</sup> &minus; <var>b</var><sup>2</sup> = (<var>a</var> &minus; <var>b</var>)(<var>a</var> + <var>b</var>); сумма и разность кубов <var>a</var><sup>3</sup> &plusmn; <var>b</var><sup>3</sup> = (<var>a</var> &plusmn; <var>b</var>)(<var>a</var><sup>2</sup> &#8723; <var>ab</var> + <var>b</var><sup>2</sup>). Разность квадратов &mdash; главный ускоритель счёта: 101<sup>2</sup> &minus; 99<sup>2</sup> = 200&nbsp;&middot;&nbsp;2.</p>
<div class="frm">Если <var>s</var> = <var>x</var> + 1/<var>x</var>, то <var>x</var><sup>2</sup> + 1/<var>x</var><sup>2</sup> = <var>s</var><sup>2</sup> &minus; 2, а <var>x</var><sup>3</sup> + 1/<var>x</var><sup>3</sup> = <var>s</var><sup>3</sup> &minus; 3<var>s</var>. Возводите известное в степень и вычитайте лишнее.</div>
<p><b>Телескопирование.</b> Длинная сумма или произведение, где соседние члены гасят друг друга: <span style="white-space:nowrap">{F('1','<var>k</var>(<var>k</var>+1)')} = {F('1','<var>k</var>')} &minus; {F('1','<var>k</var>+1')}</span> &mdash; всё внутри сокращается, остаются первый и последний. Увидели сумму из ста дробей &mdash; ищите телескоп.</p>
<p><b>Группировка.</b> <var>ab</var> + <var>a</var> + <var>b</var> + 1 = (<var>a</var> + 1)(<var>b</var> + 1). Добавить единицу и разложить &mdash; стандартный ход в задачах про целые числа.</p>""",
  'en': f"""
<p><b>Three identities to know on sight.</b> (<var>a</var> &plusmn; <var>b</var>)<sup>2</sup> = <var>a</var><sup>2</sup> &plusmn; 2<var>ab</var> + <var>b</var><sup>2</sup>; difference of squares <var>a</var><sup>2</sup> &minus; <var>b</var><sup>2</sup> = (<var>a</var> &minus; <var>b</var>)(<var>a</var> + <var>b</var>); sum and difference of cubes <var>a</var><sup>3</sup> &plusmn; <var>b</var><sup>3</sup> = (<var>a</var> &plusmn; <var>b</var>)(<var>a</var><sup>2</sup> &#8723; <var>ab</var> + <var>b</var><sup>2</sup>). The difference of squares is the biggest computational shortcut: 101<sup>2</sup> &minus; 99<sup>2</sup> = 200&nbsp;&middot;&nbsp;2.</p>
<div class="frm">If <var>s</var> = <var>x</var> + 1/<var>x</var>, then <var>x</var><sup>2</sup> + 1/<var>x</var><sup>2</sup> = <var>s</var><sup>2</sup> &minus; 2, and <var>x</var><sup>3</sup> + 1/<var>x</var><sup>3</sup> = <var>s</var><sup>3</sup> &minus; 3<var>s</var>. Raise what you know to a power and subtract the extra.</div>
<p><b>Telescoping.</b> A long sum or product where neighboring terms cancel: <span style="white-space:nowrap">{F('1','<var>k</var>(<var>k</var>+1)')} = {F('1','<var>k</var>')} &minus; {F('1','<var>k</var>+1')}</span> &mdash; everything inside collapses, leaving the first and last pieces. If you see a sum of a hundred fractions, look for telescoping.</p>
<p><b>Grouping.</b> <var>ab</var> + <var>a</var> + <var>b</var> + 1 = (<var>a</var> + 1)(<var>b</var> + 1). Adding one and factoring is a standard move in integer problems.</p>"""},
 'worked': [
  {'tag': {'ru': 'Разбор 1 · разность квадратов', 'en': 'Example 1 · difference of squares'},
   'q': {'ru': 'Вычислите 101<sup>2</sup> &minus; 99<sup>2</sup> без столбика.',
         'en': 'Compute 101<sup>2</sup> &minus; 99<sup>2</sup> without long multiplication.'},
   'sol': {'ru': '(101 &minus; 99)(101 + 99) = 2&nbsp;&middot;&nbsp;200 = <b>400</b>. На AMC такие вычисления встроены в большие задачи: узнавать разность квадратов надо мгновенно.',
          'en': '(101 &minus; 99)(101 + 99) = 2&nbsp;&middot;&nbsp;200 = <b>400</b>. On the AMC such computations are embedded in bigger problems: recognize the difference of squares instantly.'}},
  {'tag': {'ru': 'Разбор 2 · x + 1/x', 'en': 'Example 2 · x + 1/x'},
   'q': {'ru': 'Известно, что <var>x</var> + 1/<var>x</var> = 3. Найдите <var>x</var><sup>2</sup> + 1/<var>x</var><sup>2</sup> и <var>x</var><sup>4</sup> + 1/<var>x</var><sup>4</sup>.',
         'en': 'Given <var>x</var> + 1/<var>x</var> = 3, find <var>x</var><sup>2</sup> + 1/<var>x</var><sup>2</sup> and <var>x</var><sup>4</sup> + 1/<var>x</var><sup>4</sup>.'},
   'sol': {'ru': 'Квадрат: 9 = <var>x</var><sup>2</sup> + 2 + 1/<var>x</var><sup>2</sup>, значит <var>x</var><sup>2</sup> + 1/<var>x</var><sup>2</sup> = <b>7</b>. Ещё раз тот же ход: 49 = <var>x</var><sup>4</sup> + 2 + 1/<var>x</var><sup>4</sup>, значит <b>47</b>. Каждое возведение в квадрат приносит лишнюю двойку &mdash; её и вычитаем.',
          'en': 'Square it: 9 = <var>x</var><sup>2</sup> + 2 + 1/<var>x</var><sup>2</sup>, so <var>x</var><sup>2</sup> + 1/<var>x</var><sup>2</sup> = <b>7</b>. Same move again: 49 = <var>x</var><sup>4</sup> + 2 + 1/<var>x</var><sup>4</sup>, so <b>47</b>. Each squaring brings an extra 2 &mdash; subtract it.'}},
  {'tag': {'ru': 'Разбор 3 · телескоп', 'en': 'Example 3 · telescoping'},
   'q': {'ru': f'Вычислите сумму {F("1","1&middot;2")} + {F("1","2&middot;3")} + &hellip; + {F("1","99&middot;100")}.',
         'en': f'Compute the sum {F("1","1&middot;2")} + {F("1","2&middot;3")} + &hellip; + {F("1","99&middot;100")}.'},
   'sol': {'ru': f'Каждое слагаемое: {F("1","<var>k</var>(<var>k</var>+1)")} = {F("1","<var>k</var>")} &minus; {F("1","<var>k</var>+1")}. Сумма схлопывается: 1 &minus; 1/100 = <b>99/100</b>.',
          'en': f'Each term: {F("1","<var>k</var>(<var>k</var>+1)")} = {F("1","<var>k</var>")} &minus; {F("1","<var>k</var>+1")}. The sum collapses: 1 &minus; 1/100 = <b>99/100</b>.'}},
  {'tag': {'ru': 'Разбор 4 · группировка', 'en': 'Example 4 · grouping'},
   'q': {'ru': 'Натуральные <var>a</var> и <var>b</var> таковы, что <var>ab</var> + <var>a</var> + <var>b</var> = 63. Каково наименьшее возможное значение <var>a</var> + <var>b</var>?',
         'en': 'Positive integers <var>a</var> and <var>b</var> satisfy <var>ab</var> + <var>a</var> + <var>b</var> = 63. What is the least possible value of <var>a</var> + <var>b</var>?'},
   'sol': {'ru': 'Добавим 1: (<var>a</var> + 1)(<var>b</var> + 1) = 64. Разложения 64 на два множителя &ge; 2: 2&middot;32, 4&middot;16, 8&middot;8. Суммы <var>a</var> + <var>b</var>: 32, 18, 14. Наименьшая &mdash; <b>14</b> (при <var>a</var> = <var>b</var> = 7): произведение фиксировано, сумма минимальна у самых близких множителей.',
          'en': 'Add 1: (<var>a</var> + 1)(<var>b</var> + 1) = 64. Ways to write 64 as a product of two factors &ge; 2: 2&middot;32, 4&middot;16, 8&middot;8. The sums <var>a</var> + <var>b</var>: 32, 18, 14. The least is <b>14</b> (at <var>a</var> = <var>b</var> = 7): with a fixed product, the sum is smallest when the factors are closest together.'}},
 ],
 'selfp': [
  {'q': {'ru': 'Вычислите 51<sup>2</sup> &minus; 49<sup>2</sup>.', 'en': 'Compute 51<sup>2</sup> &minus; 49<sup>2</sup>.'},
   'hint': {'ru': 'Разность квадратов.', 'en': 'Difference of squares.'},
   'sol': {'ru': '2&nbsp;&middot;&nbsp;100 = <b>200</b>.', 'en': '2&nbsp;&middot;&nbsp;100 = <b>200</b>.'}},
  {'q': {'ru': 'Вычислите (&radic;7 + &radic;3)(&radic;7 &minus; &radic;3).', 'en': 'Compute (&radic;7 + &radic;3)(&radic;7 &minus; &radic;3).'},
   'hint': {'ru': 'Та же разность квадратов.', 'en': 'The same difference of squares.'},
   'sol': {'ru': '7 &minus; 3 = <b>4</b>.', 'en': '7 &minus; 3 = <b>4</b>.'}},
  {'q': {'ru': 'Известно, что <var>x</var> + 1/<var>x</var> = 6. Найдите <var>x</var><sup>3</sup> + 1/<var>x</var><sup>3</sup>.', 'en': 'Given <var>x</var> + 1/<var>x</var> = 6, find <var>x</var><sup>3</sup> + 1/<var>x</var><sup>3</sup>.'},
   'hint': {'ru': '<var>s</var><sup>3</sup> &minus; 3<var>s</var>.', 'en': '<var>s</var><sup>3</sup> &minus; 3<var>s</var>.'},
   'sol': {'ru': '216 &minus; 18 = <b>198</b>.', 'en': '216 &minus; 18 = <b>198</b>.'}},
  {'q': {'ru': 'Вычислите 999&nbsp;&middot;&nbsp;1001 без столбика.', 'en': 'Compute 999&nbsp;&middot;&nbsp;1001 without long multiplication.'},
   'hint': {'ru': '(1000 &minus; 1)(1000 + 1).', 'en': '(1000 &minus; 1)(1000 + 1).'},
   'sol': {'ru': '10<sup>6</sup> &minus; 1 = <b>999&nbsp;999</b>.', 'en': '10<sup>6</sup> &minus; 1 = <b>999,999</b>.'}},
  {'q': {'ru': f'Вычислите произведение (1 &minus; {F("1","2")})(1 &minus; {F("1","3")})&hellip;(1 &minus; {F("1","100")}).', 'en': f'Compute the product (1 &minus; {F("1","2")})(1 &minus; {F("1","3")})&hellip;(1 &minus; {F("1","100")}).'},
   'hint': {'ru': 'Запишите каждый множитель дробью и посмотрите, что сокращается.', 'en': 'Write each factor as a fraction and see what cancels.'},
   'sol': {'ru': f'{F("1","2")}&middot;{F("2","3")}&middot;&hellip;&middot;{F("99","100")}: всё сокращается до <b>1/100</b>.', 'en': f'{F("1","2")}&middot;{F("2","3")}&middot;&hellip;&middot;{F("99","100")}: everything cancels down to <b>1/100</b>.'}},
  {'q': {'ru': 'Числа <var>a</var> и <var>b</var> таковы, что <var>a</var> + <var>b</var> = 7 и <var>ab</var> = 10. Найдите <var>a</var><sup>3</sup> + <var>b</var><sup>3</sup>.', 'en': 'Numbers <var>a</var> and <var>b</var> satisfy <var>a</var> + <var>b</var> = 7 and <var>ab</var> = 10. Find <var>a</var><sup>3</sup> + <var>b</var><sup>3</sup>.'},
   'hint': {'ru': '(<var>a</var> + <var>b</var>)<sup>3</sup> &minus; 3<var>ab</var>(<var>a</var> + <var>b</var>).', 'en': '(<var>a</var> + <var>b</var>)<sup>3</sup> &minus; 3<var>ab</var>(<var>a</var> + <var>b</var>).'},
   'sol': {'ru': '343 &minus; 210 = <b>133</b>.', 'en': '343 &minus; 210 = <b>133</b>.'}},
  {'q': {'ru': f'Вычислите сумму {F("1","&radic;2 + 1")} + {F("1","&radic;3 + &radic;2")} + &hellip; + {F("1","&radic;25 + &radic;24")}.', 'en': f'Compute the sum {F("1","&radic;2 + 1")} + {F("1","&radic;3 + &radic;2")} + &hellip; + {F("1","&radic;25 + &radic;24")}.'},
   'hint': {'ru': 'Домножьте каждую дробь на сопряжённое: знаменатель станет единицей.', 'en': 'Multiply each fraction by the conjugate: the denominator becomes 1.'},
   'sol': {'ru': 'Каждое слагаемое равно &radic;(<var>k</var>+1) &minus; &radic;<var>k</var>; телескоп даёт &radic;25 &minus; 1 = <b>4</b>.', 'en': 'Each term equals &radic;(<var>k</var>+1) &minus; &radic;<var>k</var>; the telescope gives &radic;25 &minus; 1 = <b>4</b>.'}},
  {'q': {'ru': f'Вычислите {F("2<sup>10</sup> &minus; 1","2<sup>5</sup> &minus; 1")}.', 'en': f'Compute {F("2<sup>10</sup> &minus; 1","2<sup>5</sup> &minus; 1")}.'},
   'hint': {'ru': 'Разность квадратов: 2<sup>10</sup> = (2<sup>5</sup>)<sup>2</sup>.', 'en': 'Difference of squares: 2<sup>10</sup> = (2<sup>5</sup>)<sup>2</sup>.'},
   'sol': {'ru': '(2<sup>5</sup> &minus; 1)(2<sup>5</sup> + 1)/(2<sup>5</sup> &minus; 1) = 2<sup>5</sup> + 1 = <b>33</b>.', 'en': '(2<sup>5</sup> &minus; 1)(2<sup>5</sup> + 1)/(2<sup>5</sup> &minus; 1) = 2<sup>5</sup> + 1 = <b>33</b>.'}},
 ],
 'answers': {'ru': '200 · 4 · 198 · 999 999 · 1/100 · 133 · 4 · 33', 'en': '200, 4, 198, 999,999, 1/100, 133, 4, 33'},
 'routing': {'ru': 'Норма &mdash; 6 из 8. Ошибки в 1&ndash;2 и 4, 8 &mdash; &laquo;три тождества&raquo;; в 3 и 6 &mdash; формулы кубов через сумму; в 5 и 7 &mdash; &laquo;телескопирование&raquo;.',
             'en': 'Mastery bar: 6 of 8. For mistakes in 1&ndash;2, 4, and 8, reread &ldquo;three identities&rdquo;; for 3 and 6, the cube formulas; for 5 and 7, &ldquo;telescoping&rdquo;.'},
}
