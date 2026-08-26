# -*- coding: utf-8 -*-
"""Блок 2 «Геометрия»: уроки 2.1–2.2, RU+EN. HTML-фрагменты в нотации страницы курса."""

def F(a, b):
    return f'<span class="frac"><span>{a}</span><span>{b}</span></span>'

L21 = {
 'id': '2.1', 'anchor': 'u21',
 'title': {'ru': 'Углы: параллельные прямые, треугольники, многоугольники',
           'en': 'Angles: Parallel Lines, Triangles, Polygons'},
 'theory': {
  'ru': """
<p><b>Параллельные прямые.</b> Секущая при двух параллельных прямых даёт три пары равных или дополняющих углов: соответственные равны, накрест лежащие равны, односторонние дают в сумме 180&deg;. На контесте это работает в одну сторону мысли: увидели параллельность &mdash; переносите угол вдоль секущей, не пересчитывая заново. Если точка висит МЕЖДУ параллельными прямыми, проведите через неё вспомогательную параллель: любой ломаный угол распадётся на два простых.</p>
<div class="frm">Сумма углов треугольника = <b>180&deg;</b>. Внешний угол = сумме двух не смежных внутренних. Сумма углов <var>n</var>-угольника = <b>(<var>n</var> &minus; 2)&nbsp;&middot;&nbsp;180&deg;</b>; сумма внешних углов любого выпуклого многоугольника = <b>360&deg;</b>.</div>
<p><b>Треугольник.</b> 180&deg; &mdash; главная валюта. Внешний угол экономит ход: он сразу равен сумме двух дальних внутренних, без вычисления третьего угла. В равнобедренном треугольнике углы при основании равны &mdash; половина всех угловых погонь на AMC держится на этом факте плюс 180&deg;.</p>
<p><b>Многоугольники.</b> Для правильных многоугольников считайте через ВНЕШНИЙ угол: он равен 360&deg;/<var>n</var>, а внутренний = 180&deg; &minus; 360&deg;/<var>n</var>. Дан внутренний угол 156&deg;? Не решайте уравнение с (<var>n</var> &minus; 2): внешний равен 24&deg;, и <var>n</var> = 360/24 = 15. Быстрее и без арифметических ям.</p>
<p><b>Биссектрисы.</b> Биссектрисы внутренних углов часто встречаются в угловых погонях: выражайте их половинки через сумму углов треугольника &mdash; одна строчка честной арифметики надёжнее полузабытой готовой формулы.</p>""",
  'en': """
<p><b>Parallel lines.</b> A transversal across two parallel lines produces three families of angle pairs: corresponding angles are equal, alternate interior angles are equal, and same-side interior angles add to 180&deg;. On a contest this should work in one mental move: see parallel lines &mdash; slide the angle along the transversal instead of recomputing. If a point sits BETWEEN two parallel lines, draw an auxiliary parallel line through it: any bent angle splits into two simple ones.</p>
<div class="frm">Angle sum of a triangle = <b>180&deg;</b>. An exterior angle = the sum of the two remote interior angles. Angle sum of an <var>n</var>-gon = <b>(<var>n</var> &minus; 2)&nbsp;&middot;&nbsp;180&deg;</b>; the exterior angles of any convex polygon sum to <b>360&deg;</b>.</div>
<p><b>Triangles.</b> 180&deg; is the main currency. The exterior angle saves a step: it directly equals the sum of the two remote interior angles, no need to find the third one. In an isosceles triangle the base angles are equal &mdash; half of all AMC angle chases run on this fact plus 180&deg;.</p>
<p><b>Polygons.</b> For regular polygons, compute through the EXTERIOR angle: it equals 360&deg;/<var>n</var>, and the interior angle is 180&deg; &minus; 360&deg;/<var>n</var>. Given an interior angle of 156&deg;? Do not solve an equation with (<var>n</var> &minus; 2): the exterior angle is 24&deg;, so <var>n</var> = 360/24 = 15. Faster, and no arithmetic potholes.</p>
<p><b>Bisectors.</b> Angle bisectors appear in angle chases all the time: express their half-angles through the 180&deg; sum instead of memorizing ready-made facts &mdash; one clean line of arithmetic beats a misremembered formula.</p>"""},
 'worked': [
  {'tag': {'ru': 'Разбор 1 · параллельные прямые', 'en': 'Example 1 · parallel lines'},
   'q': {'ru': 'Прямые <var>a</var> и <var>b</var> параллельны. Секущая образует с прямой <var>a</var> угол 65&deg;. Найдите односторонний с ним внутренний угол при прямой <var>b</var>.',
         'en': 'Lines <var>a</var> and <var>b</var> are parallel. A transversal makes a 65&deg; angle with line <var>a</var>. Find the same-side interior angle at line <var>b</var>.'},
   'sol': {'ru': 'Односторонние углы дают в сумме 180&deg;: искомый угол равен 180&deg; &minus; 65&deg; = <b>115&deg;</b>. Ловушка &mdash; спутать пары: накрест лежащий был бы равен 65&deg;. Перед ответом на секунду проверьте, РАВЕНСТВО или ДОПОЛНЕНИЕ даёт ваша пара углов.',
          'en': 'Same-side interior angles add to 180&deg;: the angle is 180&deg; &minus; 65&deg; = <b>115&deg;</b>. The trap is mixing up the pairs: the alternate interior angle would be 65&deg;. Before answering, take one second to check whether your pair gives EQUALITY or a SUPPLEMENT.'}},
  {'tag': {'ru': 'Разбор 2 · внешний угол', 'en': 'Example 2 · exterior angle'},
   'q': {'ru': 'В треугольнике <var>ABC</var> угол <var>A</var> = 50&deg;, а внешний угол при вершине <var>B</var> равен 120&deg;. Найдите угол <var>C</var>.',
         'en': 'In triangle <var>ABC</var>, angle <var>A</var> = 50&deg; and the exterior angle at vertex <var>B</var> is 120&deg;. Find angle <var>C</var>.'},
   'sol': {'ru': 'Внешний угол при <var>B</var> равен сумме дальних внутренних: 120&deg; = <var>A</var> + <var>C</var> = 50&deg; + <var>C</var>, значит <var>C</var> = <b>70&deg;</b>. Медленный путь &mdash; сначала найти <var>B</var> = 60&deg;, потом вычитать из 180&deg;: результат тот же, но ходов вдвое больше.',
          'en': 'The exterior angle at <var>B</var> equals the sum of the remote interior angles: 120&deg; = <var>A</var> + <var>C</var> = 50&deg; + <var>C</var>, so <var>C</var> = <b>70&deg;</b>. The slow route &mdash; first find <var>B</var> = 60&deg;, then subtract from 180&deg; &mdash; gives the same answer in twice as many moves.'}},
  {'tag': {'ru': 'Разбор 3 · правильный многоугольник', 'en': 'Example 3 · regular polygon'},
   'q': {'ru': 'Внутренний угол правильного многоугольника равен 156&deg;. Сколько у него сторон?',
         'en': 'The interior angle of a regular polygon is 156&deg;. How many sides does it have?'},
   'sol': {'ru': 'Внешний угол: 180&deg; &minus; 156&deg; = 24&deg;. Все внешние в сумме дают 360&deg;, значит <var>n</var> = 360/24 = <b>15</b>. Проверка через (<var>n</var> &minus; 2)&nbsp;&middot;&nbsp;180: 13&nbsp;&middot;&nbsp;180 = 2340 и 2340/15 = 156. Верно. Внешний угол &mdash; всегда короче.',
          'en': 'Exterior angle: 180&deg; &minus; 156&deg; = 24&deg;. All exterior angles sum to 360&deg;, so <var>n</var> = 360/24 = <b>15</b>. Check via (<var>n</var> &minus; 2)&nbsp;&middot;&nbsp;180: 13&nbsp;&middot;&nbsp;180 = 2340 and 2340/15 = 156. Correct. The exterior angle is always the shorter road.'}},
  {'tag': {'ru': 'Разбор 4 · угловая погоня', 'en': 'Example 4 · angle chase'},
   'q': {'ru': 'В треугольнике <var>ABC</var> стороны <var>AB</var> = <var>AC</var> и угол <var>A</var> = 36&deg;. Биссектриса угла <var>B</var> пересекает сторону <var>AC</var> в точке <var>D</var>. Найдите угол <var>BDC</var>.',
         'en': 'In triangle <var>ABC</var>, <var>AB</var> = <var>AC</var> and angle <var>A</var> = 36&deg;. The bisector of angle <var>B</var> meets side <var>AC</var> at point <var>D</var>. Find angle <var>BDC</var>.'},
   'sol': {'ru': 'Углы при основании: (180&deg; &minus; 36&deg;)/2 = 72&deg;. Биссектриса делит угол <var>B</var> пополам: угол <var>ABD</var> = 36&deg;. В треугольнике <var>ABD</var>: угол <var>ADB</var> = 180&deg; &minus; 36&deg; &minus; 36&deg; = 108&deg;, значит смежный угол <var>BDC</var> = <b>72&deg;</b>. Метод один для всех погонь: ставьте числа на КАЖДЫЙ угол по мере вычисления, ничего не держите в голове.',
          'en': 'Base angles: (180&deg; &minus; 36&deg;)/2 = 72&deg;. The bisector halves angle <var>B</var>: angle <var>ABD</var> = 36&deg;. In triangle <var>ABD</var>: angle <var>ADB</var> = 180&deg; &minus; 36&deg; &minus; 36&deg; = 108&deg;, so the supplementary angle <var>BDC</var> = <b>72&deg;</b>. One method for every chase: write a number on EVERY angle as you find it; keep nothing in your head.'}},
 ],
 'selfp': [
  {'q': {'ru': 'Углы треугольника относятся как 2&nbsp;:&nbsp;3&nbsp;:&nbsp;4. Найдите наибольший угол.', 'en': 'The angles of a triangle are in the ratio 2&nbsp;:&nbsp;3&nbsp;:&nbsp;4. Find the largest angle.'},
   'hint': {'ru': 'Девять частей на 180&deg;.', 'en': 'Nine parts make 180&deg;.'},
   'sol': {'ru': 'Часть = 180/9 = 20&deg;: углы 40&deg;, 60&deg;, 80&deg;. Наибольший <b>80&deg;</b>.', 'en': 'One part = 180/9 = 20&deg;: the angles are 40&deg;, 60&deg;, 80&deg;. The largest is <b>80&deg;</b>.'}},
  {'q': {'ru': 'Прямые <var>a</var> и <var>b</var> параллельны. Односторонние внутренние углы при секущей равны (3<var>x</var> + 20)&deg; и (2<var>x</var> &minus; 10)&deg;. Найдите <var>x</var>.', 'en': 'Lines <var>a</var> and <var>b</var> are parallel. The same-side interior angles at a transversal are (3<var>x</var> + 20)&deg; and (2<var>x</var> &minus; 10)&deg;. Find <var>x</var>.'},
   'hint': {'ru': 'Односторонние углы дают в сумме 180&deg;.', 'en': 'Same-side interior angles add to 180&deg;.'},
   'sol': {'ru': '5<var>x</var> + 10 = 180, значит <var>x</var> = <b>34</b> (углы 122&deg; и 58&deg;).', 'en': '5<var>x</var> + 10 = 180, so <var>x</var> = <b>34</b> (the angles are 122&deg; and 58&deg;).'}},
  {'q': {'ru': 'Внешний угол правильного многоугольника равен 24&deg;. Сколько у него сторон?', 'en': 'The exterior angle of a regular polygon is 24&deg;. How many sides does it have?'},
   'hint': {'ru': 'Внешние углы в сумме дают 360&deg;.', 'en': 'The exterior angles sum to 360&deg;.'},
   'sol': {'ru': '360/24 = <b>15</b> сторон.', 'en': '360/24 = <b>15</b> sides.'}},
  {'q': {'ru': 'В равнобедренном треугольнике угол при вершине равен 40&deg;. Найдите угол при основании.', 'en': 'The apex angle of an isosceles triangle is 40&deg;. Find a base angle.'},
   'hint': {'ru': 'Два равных угла делят остаток от 180&deg;.', 'en': 'Two equal angles share what is left of 180&deg;.'},
   'sol': {'ru': '(180 &minus; 40)/2 = <b>70&deg;</b>.', 'en': '(180 &minus; 40)/2 = <b>70&deg;</b>.'}},
  {'q': {'ru': 'Сумма внутренних углов выпуклого многоугольника равна 1440&deg;. Сколько у него сторон?', 'en': 'The interior angles of a convex polygon sum to 1440&deg;. How many sides does it have?'},
   'hint': {'ru': '(<var>n</var> &minus; 2)&nbsp;&middot;&nbsp;180 = 1440.', 'en': '(<var>n</var> &minus; 2)&nbsp;&middot;&nbsp;180 = 1440.'},
   'sol': {'ru': '<var>n</var> &minus; 2 = 8, значит <var>n</var> = <b>10</b>.', 'en': '<var>n</var> &minus; 2 = 8, so <var>n</var> = <b>10</b>.'}},
  {'q': {'ru': 'Внешний угол треугольника равен 110&deg;, один из не смежных с ним внутренних углов равен 45&deg;. Найдите второй не смежный внутренний угол.', 'en': 'An exterior angle of a triangle is 110&deg;, and one of the remote interior angles is 45&deg;. Find the other remote interior angle.'},
   'hint': {'ru': 'Внешний угол = сумме двух дальних внутренних.', 'en': 'An exterior angle equals the sum of the two remote interior angles.'},
   'sol': {'ru': '110 &minus; 45 = <b>65&deg;</b>.', 'en': '110 &minus; 45 = <b>65&deg;</b>.'}},
  {'q': {'ru': 'В правильном многоугольнике внутренний угол в 5 раз больше внешнего. Сколько у многоугольника сторон?', 'en': 'In a regular polygon, each interior angle is 5 times the exterior angle. How many sides does the polygon have?'},
   'hint': {'ru': 'Внутренний и внешний в сумме дают 180&deg;.', 'en': 'Interior and exterior angles add to 180&deg;.'},
   'sol': {'ru': '6 частей = 180&deg;, внешний угол 30&deg;: <var>n</var> = 360/30 = <b>12</b>.', 'en': '6 parts = 180&deg;, so the exterior angle is 30&deg;: <var>n</var> = 360/30 = <b>12</b>.'}},
  {'q': {'ru': 'Точка <var>P</var> лежит между параллельными прямыми <var>a</var> и <var>b</var>. Отрезок из точки <var>A</var> на прямой <var>a</var> идёт в <var>P</var>, отрезок из <var>P</var> идёт в точку <var>B</var> на прямой <var>b</var>. Угол между <var>AP</var> и прямой <var>a</var> равен 35&deg;, угол между <var>PB</var> и прямой <var>b</var> равен 45&deg; (оба угла открыты в сторону точки <var>P</var>). Найдите угол <var>APB</var>.', 'en': 'Point <var>P</var> lies between parallel lines <var>a</var> and <var>b</var>. A segment runs from point <var>A</var> on line <var>a</var> to <var>P</var>, and a segment runs from <var>P</var> to point <var>B</var> on line <var>b</var>. The angle between <var>AP</var> and line <var>a</var> is 35&deg;, and the angle between <var>PB</var> and line <var>b</var> is 45&deg; (both angles open toward <var>P</var>). Find angle <var>APB</var>.'},
   'hint': {'ru': 'Проведите через <var>P</var> вспомогательную прямую, параллельную <var>a</var> и <var>b</var>.', 'en': 'Draw an auxiliary line through <var>P</var> parallel to <var>a</var> and <var>b</var>.'},
   'sol': {'ru': 'Вспомогательная параллель через <var>P</var> разбивает угол <var>APB</var> на два накрест лежащих: 35&deg; + 45&deg; = <b>80&deg;</b>.', 'en': 'The auxiliary parallel through <var>P</var> splits angle <var>APB</var> into two alternate interior angles: 35&deg; + 45&deg; = <b>80&deg;</b>.'}},
 ],
 'answers': {'ru': '80° · 34 · 15 · 70° · 10 · 65° · 12 · 80°', 'en': '80&deg;, 34, 15, 70&deg;, 10, 65&deg;, 12, 80&deg;'},
 'routing': {'ru': 'Норма урока &mdash; 6 из 8. Ошибки во 2 и 8 &mdash; перечитать &laquo;параллельные прямые&raquo;; в 1, 4 и 6 &mdash; &laquo;треугольник&raquo; и внешний угол; в 3, 5 и 7 &mdash; &laquo;многоугольники&raquo;. Задачи с ошибками вернутся в начало следующей половинки B.',
             'en': 'Mastery bar: 6 of 8. For mistakes in 2 and 8, reread &ldquo;parallel lines&rdquo;; for 1, 4, and 6, &ldquo;triangles&rdquo; and the exterior angle; for 3, 5, and 7, &ldquo;polygons&rdquo;. Missed problems come back at the start of the next lesson&rsquo;s B session.'},
}

L22 = {
 'id': '2.2', 'anchor': 'u22',
 'title': {'ru': 'Подобие и Пифагор: особые треугольники, высота к гипотенузе, тройки',
           'en': 'Similarity and Pythagoras: Special Triangles, Altitude to the Hypotenuse, Triples'},
 'theory': {
  'ru': """
<p><b>Подобие.</b> Два равных угла &mdash; и треугольники подобны (третий угол бесплатный). Все линейные размеры подобных фигур связаны одним коэффициентом <var>k</var>: стороны, высоты, периметры. Площади &mdash; коэффициентом <var>k</var><sup>2</sup>. Прямая, параллельная стороне треугольника, отрезает подобный треугольник: из <var>DE</var>&nbsp;&#8741;&nbsp;<var>BC</var> сразу следует <var>AD</var>/<var>AB</var> = <var>AE</var>/<var>AC</var> = <var>DE</var>/<var>BC</var>.</p>
<p><b>Пифагор и тройки.</b> В прямоугольном треугольнике <var>a</var><sup>2</sup> + <var>b</var><sup>2</sup> = <var>c</var><sup>2</sup>. Выучите тройки: 3-4-5, 5-12-13, 7-24-25, 8-15-17 &mdash; и их кратные (6-8-10, 9-12-15, 10-24-26). На AMC тройка узнаётся быстрее, чем извлекается корень; увидели катет 7 и гипотенузу 25 &mdash; второй катет 24 без вычислений.</p>
<div class="frm">45-45-90: стороны <b><var>x</var> : <var>x</var> : <var>x</var>&radic;2</b>. &nbsp;30-60-90: стороны <b><var>x</var> : <var>x</var>&radic;3 : 2<var>x</var></b> (против 30&deg; лежит <var>x</var>, против 60&deg; &mdash; <var>x</var>&radic;3).</div>
<p><b>Особые треугольники.</b> Половина квадрата &mdash; это 45-45-90: диагональ = сторона&nbsp;&middot;&nbsp;&radic;2. Половина равностороннего треугольника &mdash; это 30-60-90. Главная ошибка &mdash; приставить &radic;3 не к той стороне: &radic;3 всегда у СРЕДНЕЙ стороны, лежащей против 60&deg;.</p>
<p><b>Высота к гипотенузе.</b> Она рассекает прямоугольный треугольник на два, подобных исходному. Отсюда три формулы: <var>h</var> = <var>ab</var>/<var>c</var> (из двух выражений площади), <var>h</var><sup>2</sup> = <var>mn</var> и катет<sup>2</sup> = <var>c</var>&nbsp;&middot;&nbsp;(своя проекция), где <var>m</var>, <var>n</var> &mdash; отрезки гипотенузы. Эти три равенства закрывают целый класс задач AMC.</p>""",
  'en': """
<p><b>Similarity.</b> Two equal angles &mdash; and the triangles are similar (the third angle comes free). All linear measurements of similar figures share one ratio <var>k</var>: sides, altitudes, perimeters. Areas scale by <var>k</var><sup>2</sup>. A line parallel to a side of a triangle cuts off a similar triangle: <var>DE</var>&nbsp;&#8741;&nbsp;<var>BC</var> immediately gives <var>AD</var>/<var>AB</var> = <var>AE</var>/<var>AC</var> = <var>DE</var>/<var>BC</var>.</p>
<p><b>Pythagoras and triples.</b> In a right triangle, <var>a</var><sup>2</sup> + <var>b</var><sup>2</sup> = <var>c</var><sup>2</sup>. Memorize the triples: 3-4-5, 5-12-13, 7-24-25, 8-15-17 &mdash; and their multiples (6-8-10, 9-12-15, 10-24-26). On the AMC, recognizing a triple is faster than computing the root; see a leg of 7 and a hypotenuse of 25 &mdash; the other leg is 24, no computation.</p>
<div class="frm">45-45-90: sides <b><var>x</var> : <var>x</var> : <var>x</var>&radic;2</b>. &nbsp;30-60-90: sides <b><var>x</var> : <var>x</var>&radic;3 : 2<var>x</var></b> (<var>x</var> is opposite 30&deg;, and <var>x</var>&radic;3 is opposite 60&deg;).</div>
<p><b>Special triangles.</b> Half a square is a 45-45-90: diagonal = side&nbsp;&middot;&nbsp;&radic;2. Half an equilateral triangle is a 30-60-90. The classic mistake is attaching &radic;3 to the wrong side: &radic;3 always belongs to the MIDDLE side, the one opposite 60&deg;.</p>
<p><b>Altitude to the hypotenuse.</b> It cuts a right triangle into two triangles similar to the original. Hence three formulas: <var>h</var> = <var>ab</var>/<var>c</var> (two expressions for the area), <var>h</var><sup>2</sup> = <var>mn</var>, and leg<sup>2</sup> = <var>c</var>&nbsp;&middot;&nbsp;(its own projection), where <var>m</var>, <var>n</var> are the segments of the hypotenuse. These three identities close out an entire class of AMC problems.</p>"""},
 'worked': [
  {'tag': {'ru': 'Разбор 1 · 30-60-90', 'en': 'Example 1 · 30-60-90'},
   'q': {'ru': 'В прямоугольном треугольнике острый угол равен 30&deg;, гипотенуза равна 10. Найдите оба катета.',
         'en': 'A right triangle has an acute angle of 30&deg; and a hypotenuse of 10. Find both legs.'},
   'sol': {'ru': 'Схема <var>x</var> : <var>x</var>&radic;3 : 2<var>x</var>. Гипотенуза 2<var>x</var> = 10, значит <var>x</var> = 5: катеты <b>5 и 5&radic;3</b>. Проверка Пифагором: 25 + 75 = 100. Верно. Ловушка &mdash; написать 5&radic;3 против угла 30&deg;: против меньшего угла лежит меньшая сторона.',
          'en': 'The pattern is <var>x</var> : <var>x</var>&radic;3 : 2<var>x</var>. The hypotenuse 2<var>x</var> = 10, so <var>x</var> = 5: the legs are <b>5 and 5&radic;3</b>. Pythagorean check: 25 + 75 = 100. Correct. The trap is placing 5&radic;3 opposite the 30&deg; angle: the smaller angle faces the smaller side.'}},
  {'tag': {'ru': 'Разбор 2 · подобие', 'en': 'Example 2 · similarity'},
   'q': {'ru': 'В треугольнике <var>ABC</var> точка <var>D</var> на стороне <var>AB</var>, точка <var>E</var> на стороне <var>AC</var>, причём <var>DE</var>&nbsp;&#8741;&nbsp;<var>BC</var>. Известно: <var>AD</var> = 4, <var>DB</var> = 6, <var>DE</var> = 6. Найдите <var>BC</var>.',
         'en': 'In triangle <var>ABC</var>, point <var>D</var> is on side <var>AB</var> and point <var>E</var> is on side <var>AC</var>, with <var>DE</var>&nbsp;&#8741;&nbsp;<var>BC</var>. Given: <var>AD</var> = 4, <var>DB</var> = 6, <var>DE</var> = 6. Find <var>BC</var>.'},
   'sol': {'ru': 'Треугольники <var>ADE</var> и <var>ABC</var> подобны с коэффициентом <var>AD</var>/<var>AB</var> = 4/10 = 2/5. Значит <var>BC</var> = <var>DE</var>&nbsp;&middot;&nbsp;5/2 = <b>15</b>. Классическая ловушка &mdash; взять отношение <var>AD</var>/<var>DB</var> = 4/6: коэффициент подобия считается к ЦЕЛОЙ стороне, не к её куску.',
          'en': 'Triangles <var>ADE</var> and <var>ABC</var> are similar with ratio <var>AD</var>/<var>AB</var> = 4/10 = 2/5. So <var>BC</var> = <var>DE</var>&nbsp;&middot;&nbsp;5/2 = <b>15</b>. The classic trap is taking <var>AD</var>/<var>DB</var> = 4/6: the similarity ratio compares to the WHOLE side, not to its piece.'}},
  {'tag': {'ru': 'Разбор 3 · высота к гипотенузе', 'en': 'Example 3 · altitude to the hypotenuse'},
   'q': {'ru': 'Катеты прямоугольного треугольника равны 6 и 8. Найдите высоту, опущенную на гипотенузу, и отрезки, на которые она делит гипотенузу.',
         'en': 'The legs of a right triangle are 6 and 8. Find the altitude to the hypotenuse and the segments into which it divides the hypotenuse.'},
   'sol': {'ru': 'Тройка 6-8-10: гипотенуза 10. Высота из площади: <var>h</var> = 6&nbsp;&middot;&nbsp;8/10 = <b>4,8</b>. Проекции катетов: 6<sup>2</sup>/10 = 3,6 и 8<sup>2</sup>/10 = 6,4. Проверка: 3,6 + 6,4 = 10 и <var>h</var><sup>2</sup> = 3,6&nbsp;&middot;&nbsp;6,4 = 23,04 = 4,8<sup>2</sup>. Всё сходится.',
          'en': 'The 6-8-10 triple: the hypotenuse is 10. Altitude from the area: <var>h</var> = 6&nbsp;&middot;&nbsp;8/10 = <b>4.8</b>. Projections of the legs: 6<sup>2</sup>/10 = 3.6 and 8<sup>2</sup>/10 = 6.4. Check: 3.6 + 6.4 = 10 and <var>h</var><sup>2</sup> = 3.6&nbsp;&middot;&nbsp;6.4 = 23.04 = 4.8<sup>2</sup>. Everything agrees.'}},
  {'tag': {'ru': 'Разбор 4 · тройки', 'en': 'Example 4 · triples'},
   'q': {'ru': 'В прямоугольном треугольнике гипотенуза равна 25, один из катетов равен 7. Найдите периметр.',
         'en': 'A right triangle has hypotenuse 25 and one leg equal to 7. Find the perimeter.'},
   'sol': {'ru': 'Это тройка 7-24-25: второй катет <b>24</b>, периметр 7 + 24 + 25 = <b>56</b>. Без тройки пришлось бы считать &radic;(625 &minus; 49) = &radic;576 &mdash; посильно, но на минуту дольше. Выученные тройки &mdash; это купленное время.',
          'en': 'This is the 7-24-25 triple: the other leg is <b>24</b>, and the perimeter is 7 + 24 + 25 = <b>56</b>. Without the triple you would compute &radic;(625 &minus; 49) = &radic;576 &mdash; doable, but a minute slower. Memorized triples are purchased time.'}},
 ],
 'selfp': [
  {'q': {'ru': 'Катеты прямоугольного треугольника равны 9 и 12. Найдите гипотенузу.', 'en': 'The legs of a right triangle are 9 and 12. Find the hypotenuse.'},
   'hint': {'ru': 'Это кратная тройка 3-4-5.', 'en': 'A multiple of the 3-4-5 triple.'},
   'sol': {'ru': '3-4-5, умноженная на 3: гипотенуза <b>15</b>.', 'en': '3-4-5 scaled by 3: the hypotenuse is <b>15</b>.'}},
  {'q': {'ru': 'Диагональ квадрата равна 10. Найдите его площадь.', 'en': 'The diagonal of a square is 10. Find its area.'},
   'hint': {'ru': 'Сторона = диагональ/&radic;2; а можно взять половину произведения диагоналей.', 'en': 'Side = diagonal/&radic;2; or take half the product of the diagonals.'},
   'sol': {'ru': 'Площадь = <var>d</var><sup>2</sup>/2 = 100/2 = <b>50</b>.', 'en': 'Area = <var>d</var><sup>2</sup>/2 = 100/2 = <b>50</b>.'}},
  {'q': {'ru': 'В треугольнике 30-60-90 меньший катет равен 7. Найдите гипотенузу.', 'en': 'In a 30-60-90 triangle the shorter leg is 7. Find the hypotenuse.'},
   'hint': {'ru': 'Гипотенуза &mdash; удвоенный меньший катет.', 'en': 'The hypotenuse is twice the shorter leg.'},
   'sol': {'ru': '2&nbsp;&middot;&nbsp;7 = <b>14</b> (а больший катет 7&radic;3).', 'en': '2&nbsp;&middot;&nbsp;7 = <b>14</b> (and the longer leg is 7&radic;3).'}},
  {'q': {'ru': 'Стороны треугольника равны 6, 8, 10. Подобный ему треугольник имеет периметр 60. Найдите его наибольшую сторону.', 'en': 'A triangle has sides 6, 8, 10. A similar triangle has perimeter 60. Find its longest side.'},
   'hint': {'ru': 'Сравните периметры: 24 против 60.', 'en': 'Compare the perimeters: 24 versus 60.'},
   'sol': {'ru': 'Коэффициент 60/24 = 2,5: стороны 15, 20, 25. Наибольшая <b>25</b>.', 'en': 'Ratio 60/24 = 2.5: the sides are 15, 20, 25. The longest is <b>25</b>.'}},
  {'q': {'ru': 'В треугольнике <var>ABC</var> отрезок <var>DE</var>&nbsp;&#8741;&nbsp;<var>BC</var>, точка <var>D</var> на <var>AB</var>, <var>AD</var>&nbsp;:&nbsp;<var>DB</var> = 2&nbsp;:&nbsp;3, <var>BC</var> = 20. Найдите <var>DE</var>.', 'en': 'In triangle <var>ABC</var>, segment <var>DE</var>&nbsp;&#8741;&nbsp;<var>BC</var> with <var>D</var> on <var>AB</var>, <var>AD</var>&nbsp;:&nbsp;<var>DB</var> = 2&nbsp;:&nbsp;3, and <var>BC</var> = 20. Find <var>DE</var>.'},
   'hint': {'ru': 'Коэффициент подобия &mdash; <var>AD</var>/<var>AB</var>, а не <var>AD</var>/<var>DB</var>.', 'en': 'The similarity ratio is <var>AD</var>/<var>AB</var>, not <var>AD</var>/<var>DB</var>.'},
   'sol': {'ru': '<var>AD</var>/<var>AB</var> = 2/5, значит <var>DE</var> = 20&nbsp;&middot;&nbsp;2/5 = <b>8</b>.', 'en': '<var>AD</var>/<var>AB</var> = 2/5, so <var>DE</var> = 20&nbsp;&middot;&nbsp;2/5 = <b>8</b>.'}},
  {'q': {'ru': 'Катеты прямоугольного треугольника равны 5 и 12. Найдите высоту, опущенную на гипотенузу.', 'en': 'The legs of a right triangle are 5 and 12. Find the altitude to the hypotenuse.'},
   'hint': {'ru': 'Две записи площади: катеты и гипотенуза с высотой.', 'en': 'Two expressions for the area: the legs, and the hypotenuse with the altitude.'},
   'sol': {'ru': 'Гипотенуза 13 (тройка 5-12-13): <var>h</var> = 5&nbsp;&middot;&nbsp;12/13 = <b>60/13</b>.', 'en': 'The hypotenuse is 13 (the 5-12-13 triple): <var>h</var> = 5&nbsp;&middot;&nbsp;12/13 = <b>60/13</b>.'}},
  {'q': {'ru': 'Диагональ прямоугольника равна 17, одна из сторон равна 8. Найдите площадь прямоугольника.', 'en': 'The diagonal of a rectangle is 17, and one side is 8. Find the area of the rectangle.'},
   'hint': {'ru': 'Диагональ и стороны &mdash; прямоугольный треугольник. Узнайте тройку.', 'en': 'The diagonal and the sides form a right triangle. Recognize the triple.'},
   'sol': {'ru': 'Тройка 8-15-17: вторая сторона 15, площадь 8&nbsp;&middot;&nbsp;15 = <b>120</b>.', 'en': 'The 8-15-17 triple: the other side is 15, so the area is 8&nbsp;&middot;&nbsp;15 = <b>120</b>.'}},
  {'q': {'ru': 'Лестница длиной 25 приставлена к стене: её основание в 7 от стены. Верх лестницы сполз вниз на 4. На сколько отъехало от стены основание?', 'en': 'A 25-foot ladder leans against a wall with its foot 7 feet from the wall. The top slides down 4 feet. How far does the foot slide away from the wall?'},
   'hint': {'ru': 'Две тройки Пифагора с одной и той же гипотенузой 25.', 'en': 'Two Pythagorean triples with the same hypotenuse 25.'},
   'sol': {'ru': 'Сначала высота &radic;(625 &minus; 49) = 24 (тройка 7-24-25). Новая высота 20, новое основание &radic;(625 &minus; 400) = 15 (тройка 15-20-25). Сдвиг: 15 &minus; 7 = <b>8</b>.', 'en': 'First the height: &radic;(625 &minus; 49) = 24 (the 7-24-25 triple). New height 20, new base &radic;(625 &minus; 400) = 15 (the 15-20-25 triple). The slide: 15 &minus; 7 = <b>8</b>.'}},
 ],
 'answers': {'ru': '15 · 50 · 14 · 25 · 8 · 60/13 · 120 · 8', 'en': '15, 50, 14, 25, 8, 60/13, 120, 8'},
 'routing': {'ru': 'Норма &mdash; 6 из 8. Ошибки в 1, 7 и 8 &mdash; &laquo;Пифагор и тройки&raquo;; во 2&ndash;3 &mdash; &laquo;особые треугольники&raquo;; в 4&ndash;5 &mdash; &laquo;подобие&raquo;; в 6 &mdash; &laquo;высота к гипотенузе&raquo;.',
             'en': 'Mastery bar: 6 of 8. For mistakes in 1, 7, and 8, reread &ldquo;Pythagoras and triples&rdquo;; for 2&ndash;3, &ldquo;special triangles&rdquo;; for 4&ndash;5, &ldquo;similarity&rdquo;; for 6, &ldquo;altitude to the hypotenuse&rdquo;.'},
}
