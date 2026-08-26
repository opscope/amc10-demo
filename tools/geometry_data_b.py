# -*- coding: utf-8 -*-
"""Блок 2 «Геометрия»: уроки 2.3–2.4, RU+EN. HTML-фрагменты в нотации страницы курса."""

def F(a, b):
    return f'<span class="frac"><span>{a}</span><span>{b}</span></span>'

L23 = {
 'id': '2.3', 'anchor': 'u23',
 'title': {'ru': 'Площади: треугольник, трапеция, «достроить и вычесть», отношения',
           'en': 'Areas: Triangle, Trapezoid, Complete-and-Subtract, Ratios'},
 'theory': {
  'ru': f"""
<p><b>Треугольник.</b> Базовая формула &mdash; полупроизведение основания на высоту: <var>S</var> = {F('1','2')}<var>ah</var>. Основанием можно объявить ЛЮБУЮ сторону &mdash; выбирайте ту, к которой высота видна сразу. У прямоугольного треугольника площадь &mdash; половина произведения катетов, без поиска высоты.</p>
<div class="frm">Герон: <var>S</var> = &radic;(<var>p</var>(<var>p</var> &minus; <var>a</var>)(<var>p</var> &minus; <var>b</var>)(<var>p</var> &minus; <var>c</var>)), где <var>p</var> &mdash; полупериметр. Трапеция: <var>S</var> = {F('<var>a</var> + <var>b</var>','2')}&nbsp;&middot;&nbsp;<var>h</var>.</div>
<p><b>Герон и дежурные треугольники.</b> Треугольник 13-14-15 (площадь 84) и его родня 5-5-6, 9-10-17 живут в задачах десятилетиями. Часто Герон не нужен: высота равнобедренного треугольника считается Пифагором за один ход. Ромб и любой четырёхугольник с перпендикулярными диагоналями: <var>S</var> = половина произведения диагоналей.</p>
<p><b>&laquo;Достроить и вычесть&raquo;.</b> Кривой многоугольник не считают в лоб: достройте его до прямоугольника и вычтите лишние прямоугольные треугольники по углам. Метод обгоняет любые формулы на фигурах с вершинами в узлах сетки и готовит руку к шнуровке из урока 2.5.</p>
<p><b>Отношения площадей.</b> Треугольники с общей высотой относятся как основания: чевиана <var>AD</var> с <var>BD</var>&nbsp;:&nbsp;<var>DC</var> = <var>m</var>&nbsp;:&nbsp;<var>n</var> делит площадь в отношении <var>m</var>&nbsp;:&nbsp;<var>n</var>. Медиана делит площадь пополам; треугольник из средних линий занимает {F('1','4')} площади (как и каждый из трёх угловых). Два отношения подряд перемножаются &mdash; это главный рычаг задач AMC #10&ndash;15 о площадях.</p>""",
  'en': f"""
<p><b>Triangle.</b> The base formula is half of base times height: <var>S</var> = {F('1','2')}<var>ah</var>. ANY side can serve as the base &mdash; pick the one whose altitude you can see immediately. For a right triangle, the area is half the product of the legs, no altitude hunting needed.</p>
<div class="frm">Heron: <var>S</var> = &radic;(<var>p</var>(<var>p</var> &minus; <var>a</var>)(<var>p</var> &minus; <var>b</var>)(<var>p</var> &minus; <var>c</var>)), where <var>p</var> is the semiperimeter. Trapezoid: <var>S</var> = {F('<var>a</var> + <var>b</var>','2')}&nbsp;&middot;&nbsp;<var>h</var>.</div>
<p><b>Heron and the usual suspects.</b> The 13-14-15 triangle (area 84) and its relatives 5-5-6 and 9-10-17 have lived in contest problems for decades. Often Heron is overkill: the altitude of an isosceles triangle falls out of Pythagoras in one move. A rhombus, or any quadrilateral with perpendicular diagonals: <var>S</var> = half the product of the diagonals.</p>
<p><b>Complete-and-subtract.</b> Do not attack a crooked polygon head-on: complete it to a rectangle and subtract the extra right triangles at the corners. This method beats any formula on figures with lattice-point vertices, and it trains your hand for the Shoelace formula of Lesson 2.5.</p>
<p><b>Area ratios.</b> Triangles with a shared altitude compare as their bases: a cevian <var>AD</var> with <var>BD</var>&nbsp;:&nbsp;<var>DC</var> = <var>m</var>&nbsp;:&nbsp;<var>n</var> splits the area in the ratio <var>m</var>&nbsp;:&nbsp;<var>n</var>. A median halves the area; the midsegment triangle takes {F('1','4')} of it. Two successive ratios multiply &mdash; the main lever of AMC #10&ndash;15 area problems.</p>"""},
 'worked': [
  {'tag': {'ru': 'Разбор 1 · Герон', 'en': 'Example 1 · Heron'},
   'q': {'ru': 'Найдите площадь треугольника со сторонами 13, 14, 15.',
         'en': 'Find the area of the triangle with sides 13, 14, 15.'},
   'sol': {'ru': 'Полупериметр <var>p</var> = 21. <var>S</var> = &radic;(21&nbsp;&middot;&nbsp;8&nbsp;&middot;&nbsp;7&nbsp;&middot;&nbsp;6) = &radic;7056 = <b>84</b>. Считать корень удобнее группами: 21&nbsp;&middot;&nbsp;7 = 147 = 49&nbsp;&middot;&nbsp;3 и 8&nbsp;&middot;&nbsp;6 = 48 = 16&nbsp;&middot;&nbsp;3, значит <var>S</var> = 7&nbsp;&middot;&nbsp;4&nbsp;&middot;&nbsp;3 = 84. Бонус: высота к стороне 14 равна 2&nbsp;&middot;&nbsp;84/14 = 12.',
          'en': 'Semiperimeter <var>p</var> = 21. <var>S</var> = &radic;(21&nbsp;&middot;&nbsp;8&nbsp;&middot;&nbsp;7&nbsp;&middot;&nbsp;6) = &radic;7056 = <b>84</b>. Take the root by grouping: 21&nbsp;&middot;&nbsp;7 = 147 = 49&nbsp;&middot;&nbsp;3 and 8&nbsp;&middot;&nbsp;6 = 48 = 16&nbsp;&middot;&nbsp;3, so <var>S</var> = 7&nbsp;&middot;&nbsp;4&nbsp;&middot;&nbsp;3 = 84. Bonus: the altitude to the side of 14 is 2&nbsp;&middot;&nbsp;84/14 = 12.'}},
  {'tag': {'ru': 'Разбор 2 · трапеция', 'en': 'Example 2 · trapezoid'},
   'q': {'ru': 'Основания трапеции равны 8 и 14, высота равна 5. Найдите площадь.',
         'en': 'A trapezoid has bases 8 and 14 and height 5. Find its area.'},
   'sol': {'ru': '<var>S</var> = (8 + 14)/2&nbsp;&middot;&nbsp;5 = 11&nbsp;&middot;&nbsp;5 = <b>55</b>. Полусумма оснований 11 &mdash; это средняя линия: трапеция равновелика прямоугольнику со сторонами 11 и 5. Ловушка &mdash; забыть деление на 2 и получить 110: ответ-приманка такого вида почти всегда есть среди вариантов.',
          'en': '<var>S</var> = (8 + 14)/2&nbsp;&middot;&nbsp;5 = 11&nbsp;&middot;&nbsp;5 = <b>55</b>. The half-sum 11 is the midsegment: the trapezoid has the same area as an 11-by-5 rectangle. The trap is dropping the division by 2 and getting 110: a decoy of exactly that shape is almost always among the choices.'}},
  {'tag': {'ru': 'Разбор 3 · достроить и вычесть', 'en': 'Example 3 · complete-and-subtract'},
   'q': {'ru': 'Из прямоугольника 12 на 9 отрезали один угол: прямоугольный треугольник с катетами 4 и 3, идущими по сторонам прямоугольника. Найдите площадь оставшегося пятиугольника.',
         'en': 'One corner is cut off a 12-by-9 rectangle: a right triangle with legs 4 and 3 lying along the sides of the rectangle. Find the area of the remaining pentagon.'},
   'sol': {'ru': 'Целое минус лишнее: 12&nbsp;&middot;&nbsp;9 &minus; 4&nbsp;&middot;&nbsp;3/2 = 108 &minus; 6 = <b>102</b>. Тот же приём работает в обратную сторону: невыпуклую фигуру достраиваем до прямоугольника и вычитаем добавленные куски. Одна большая простая фигура минус простые куски &mdash; вместо одной сложной.',
          'en': 'The whole minus the extra: 12&nbsp;&middot;&nbsp;9 &minus; 4&nbsp;&middot;&nbsp;3/2 = 108 &minus; 6 = <b>102</b>. The same move runs in reverse: complete a nonconvex figure to a rectangle and subtract the added pieces. One big simple figure minus simple pieces &mdash; instead of one complicated figure.'}},
  {'tag': {'ru': 'Разбор 4 · отношения площадей', 'en': 'Example 4 · area ratios'},
   'q': {'ru': 'Площадь треугольника <var>ABC</var> равна 60. Точка <var>D</var> на стороне <var>BC</var>, причём <var>BD</var>&nbsp;:&nbsp;<var>DC</var> = 2&nbsp;:&nbsp;3; точка <var>E</var> &mdash; середина отрезка <var>AD</var>. Найдите площадь треугольника <var>ABE</var>.',
         'en': 'Triangle <var>ABC</var> has area 60. Point <var>D</var> lies on side <var>BC</var> with <var>BD</var>&nbsp;:&nbsp;<var>DC</var> = 2&nbsp;:&nbsp;3; point <var>E</var> is the midpoint of segment <var>AD</var>. Find the area of triangle <var>ABE</var>.'},
   'sol': {'ru': 'Шаг 1: общая высота из <var>A</var>, значит [<var>ABD</var>] = 60&nbsp;&middot;&nbsp;2/5 = 24. Шаг 2: <var>BE</var> &mdash; медиана треугольника <var>ABD</var>, она делит его площадь пополам: [<var>ABE</var>] = <b>12</b>. Два отношения перемножились &mdash; ни одной высоты считать не пришлось.',
          'en': 'Step 1: shared altitude from <var>A</var>, so [<var>ABD</var>] = 60&nbsp;&middot;&nbsp;2/5 = 24. Step 2: <var>BE</var> is a median of triangle <var>ABD</var> and halves its area: [<var>ABE</var>] = <b>12</b>. Two ratios multiplied &mdash; and not a single altitude was computed.'}},
 ],
 'selfp': [
  {'q': {'ru': 'Основание треугольника равно 10, высота к нему равна 7. Найдите площадь.', 'en': 'A triangle has base 10 and the altitude to it equal to 7. Find the area.'},
   'hint': {'ru': 'Полупроизведение.', 'en': 'Half the product.'},
   'sol': {'ru': '10&nbsp;&middot;&nbsp;7/2 = <b>35</b>.', 'en': '10&nbsp;&middot;&nbsp;7/2 = <b>35</b>.'}},
  {'q': {'ru': 'Основания трапеции равны 6 и 10, высота равна 4. Найдите площадь.', 'en': 'A trapezoid has bases 6 and 10 and height 4. Find its area.'},
   'hint': {'ru': 'Полусумма оснований на высоту.', 'en': 'The average of the bases times the height.'},
   'sol': {'ru': '(6 + 10)/2&nbsp;&middot;&nbsp;4 = <b>32</b>.', 'en': '(6 + 10)/2&nbsp;&middot;&nbsp;4 = <b>32</b>.'}},
  {'q': {'ru': 'Найдите площадь треугольника со сторонами 5, 5, 6.', 'en': 'Find the area of the triangle with sides 5, 5, 6.'},
   'hint': {'ru': 'Высота к основанию 6 &mdash; из Пифагора; Герон не нужен.', 'en': 'The altitude to the base of 6 comes from Pythagoras; no Heron needed.'},
   'sol': {'ru': 'Высота &radic;(25 &minus; 9) = 4: площадь 6&nbsp;&middot;&nbsp;4/2 = <b>12</b>.', 'en': 'Altitude &radic;(25 &minus; 9) = 4: area 6&nbsp;&middot;&nbsp;4/2 = <b>12</b>.'}},
  {'q': {'ru': 'Найдите площадь треугольника со сторонами 9, 10, 17.', 'en': 'Find the area of the triangle with sides 9, 10, 17.'},
   'hint': {'ru': 'Герон; полупериметр 18.', 'en': 'Heron; the semiperimeter is 18.'},
   'sol': {'ru': '&radic;(18&nbsp;&middot;&nbsp;9&nbsp;&middot;&nbsp;8&nbsp;&middot;&nbsp;1) = &radic;1296 = <b>36</b>.', 'en': '&radic;(18&nbsp;&middot;&nbsp;9&nbsp;&middot;&nbsp;8&nbsp;&middot;&nbsp;1) = &radic;1296 = <b>36</b>.'}},
  {'q': {'ru': 'Диагонали ромба равны 10 и 24. Найдите его площадь.', 'en': 'The diagonals of a rhombus are 10 and 24. Find its area.'},
   'hint': {'ru': 'Диагонали ромба перпендикулярны.', 'en': 'The diagonals of a rhombus are perpendicular.'},
   'sol': {'ru': '10&nbsp;&middot;&nbsp;24/2 = <b>120</b> (а сторона ромба &mdash; 13, тройка 5-12-13).', 'en': '10&nbsp;&middot;&nbsp;24/2 = <b>120</b> (and the side of the rhombus is 13, the 5-12-13 triple).'}},
  {'q': {'ru': 'Площадь треугольника <var>ABC</var> равна 54. Точка <var>D</var> на стороне <var>BC</var>, причём <var>BD</var>&nbsp;:&nbsp;<var>DC</var> = 4&nbsp;:&nbsp;5. Найдите площадь треугольника <var>ABD</var>.', 'en': 'Triangle <var>ABC</var> has area 54. Point <var>D</var> lies on side <var>BC</var> with <var>BD</var>&nbsp;:&nbsp;<var>DC</var> = 4&nbsp;:&nbsp;5. Find the area of triangle <var>ABD</var>.'},
   'hint': {'ru': 'Общая высота из вершины <var>A</var>: площади относятся как основания.', 'en': 'Shared altitude from <var>A</var>: areas compare as the bases.'},
   'sol': {'ru': '54&nbsp;&middot;&nbsp;4/9 = <b>24</b>.', 'en': '54&nbsp;&middot;&nbsp;4/9 = <b>24</b>.'}},
  {'q': {'ru': 'Площадь треугольника равна 40. Найдите площадь треугольника, образованного серединами его сторон.', 'en': 'A triangle has area 40. Find the area of the triangle formed by the midpoints of its sides.'},
   'hint': {'ru': 'Средний треугольник подобен исходному с коэффициентом 1/2.', 'en': 'The midpoint triangle is similar to the original with ratio 1/2.'},
   'sol': {'ru': 'Коэффициент площадей (1/2)<sup>2</sup> = 1/4: площадь <b>10</b>.', 'en': 'The area ratio is (1/2)<sup>2</sup> = 1/4: area <b>10</b>.'}},
  {'q': {'ru': 'Площадь треугольника <var>ABC</var> равна 81. Точка <var>M</var> на стороне <var>AB</var>, точка <var>N</var> на стороне <var>AC</var>, причём <var>AM</var>&nbsp;:&nbsp;<var>MB</var> = 1&nbsp;:&nbsp;2 и <var>AN</var>&nbsp;:&nbsp;<var>NC</var> = 1&nbsp;:&nbsp;2. Найдите площадь четырёхугольника <var>BMNC</var>.', 'en': 'Triangle <var>ABC</var> has area 81. Point <var>M</var> is on side <var>AB</var> and point <var>N</var> is on side <var>AC</var>, with <var>AM</var>&nbsp;:&nbsp;<var>MB</var> = 1&nbsp;:&nbsp;2 and <var>AN</var>&nbsp;:&nbsp;<var>NC</var> = 1&nbsp;:&nbsp;2. Find the area of quadrilateral <var>BMNC</var>.'},
   'hint': {'ru': 'Сначала площадь <var>AMN</var>: два отношения 1/3 перемножаются.', 'en': 'First find the area of <var>AMN</var>: two ratios of 1/3 multiply.'},
   'sol': {'ru': '[<var>AMN</var>] = 81&nbsp;&middot;&nbsp;(1/3)(1/3) = 9, значит [<var>BMNC</var>] = 81 &minus; 9 = <b>72</b>. Вычесть &mdash; быстрее, чем считать четырёхугольник напрямую.', 'en': '[<var>AMN</var>] = 81&nbsp;&middot;&nbsp;(1/3)(1/3) = 9, so [<var>BMNC</var>] = 81 &minus; 9 = <b>72</b>. Subtracting beats computing the quadrilateral directly.'}},
 ],
 'answers': {'ru': '35 · 32 · 12 · 36 · 120 · 24 · 10 · 72', 'en': '35, 32, 12, 36, 120, 24, 10, 72'},
 'routing': {'ru': 'Норма &mdash; 6 из 8. Ошибки в 1&ndash;3 и 5 &mdash; перечитать &laquo;треугольник&raquo; и формулы в рамке; в 4 &mdash; &laquo;Герон&raquo;; в 6&ndash;8 &mdash; &laquo;отношения площадей&raquo;.',
             'en': 'Mastery bar: 6 of 8. For mistakes in 1&ndash;3 and 5, reread &ldquo;triangle&rdquo; and the formula box; for 4, &ldquo;Heron&rdquo;; for 6&ndash;8, &ldquo;area ratios&rdquo;.'},
}

L24 = {
 'id': '2.4', 'anchor': 'u24',
 'title': {'ru': 'Окружность: вписанные углы, касательные, r = S/p',
           'en': 'Circles: Inscribed Angles, Tangents, r = S/p'},
 'theory': {
  'ru': f"""
<p><b>Вписанные и центральные углы.</b> Вписанный угол равен половине центрального, опирающегося на ту же дугу; все вписанные углы на одной дуге равны. Частный случай, решающий сотни задач: угол, опирающийся на диаметр, &mdash; прямой (Фалес). Во вписанном четырёхугольнике противоположные углы дают в сумме 180&deg;.</p>
<p><b>Касательные.</b> Касательная перпендикулярна радиусу в точке касания &mdash; увидели касательную, ставьте прямой угол и готовьте Пифагора. Два отрезка касательных из одной внешней точки равны; длина касательной из точки на расстоянии <var>d</var> от центра: &radic;(<var>d</var><sup>2</sup> &minus; <var>r</var><sup>2</sup>).</p>
<div class="frm">Вписанный угол = {F('центральный','2')}. Вписанная окружность: <b><var>r</var> = <var>S</var>/<var>p</var></b> (<var>p</var> &mdash; полупериметр). Прямоугольный треугольник: <var>r</var> = {F('<var>a</var> + <var>b</var> &minus; <var>c</var>','2')}, &nbsp;<var>R</var> = <var>c</var>/2.</div>
<p><b>Вписанная и описанная окружности.</b> Разрежьте треугольник на три треугольника с вершиной в центре вписанной окружности: высота каждого равна <var>r</var>, отсюда <var>S</var> = <var>pr</var> и <var>r</var> = <var>S</var>/<var>p</var>. У прямоугольного треугольника центр описанной окружности &mdash; середина гипотенузы: <var>R</var> = <var>c</var>/2, и это мгновенно даёт медиану к гипотенузе.</p>
<p><b>Хорды.</b> Перпендикуляр из центра делит хорду пополам: половина хорды, радиус и расстояние до центра образуют прямоугольный треугольник. Хорда 8 в окружности радиуса 5 лежит на расстоянии 3 от центра &mdash; та же тройка 3-4-5 в новом костюме.</p>""",
  'en': f"""
<p><b>Inscribed and central angles.</b> An inscribed angle is half the central angle on the same arc; all inscribed angles on one arc are equal. The special case that settles hundreds of problems: an angle subtending a diameter is right (Thales). In a cyclic quadrilateral, opposite angles sum to 180&deg;.</p>
<p><b>Tangents.</b> A tangent is perpendicular to the radius at the point of tangency &mdash; see a tangent, drop a right angle and ready Pythagoras. Two tangent segments from one external point are equal; the tangent length from a point at distance <var>d</var> from the center is &radic;(<var>d</var><sup>2</sup> &minus; <var>r</var><sup>2</sup>).</p>
<div class="frm">Inscribed angle = {F('central angle','2')}. Incircle: <b><var>r</var> = <var>S</var>/<var>p</var></b> (<var>p</var> is the semiperimeter). Right triangle: <var>r</var> = {F('<var>a</var> + <var>b</var> &minus; <var>c</var>','2')}, &nbsp;<var>R</var> = <var>c</var>/2.</div>
<p><b>Incircle and circumcircle.</b> Cut the triangle into three triangles with a common vertex at the incenter: each has height <var>r</var>, whence <var>S</var> = <var>pr</var> and <var>r</var> = <var>S</var>/<var>p</var>. In a right triangle, the circumcenter is the midpoint of the hypotenuse: <var>R</var> = <var>c</var>/2, which instantly gives the median to the hypotenuse.</p>
<p><b>Chords.</b> The perpendicular from the center bisects a chord: half the chord, the radius, and the distance to the center form a right triangle. A chord of 8 in a circle of radius 5 sits at distance 3 from the center &mdash; the same 3-4-5 triple in a new costume.</p>"""},
 'worked': [
  {'tag': {'ru': 'Разбор 1 · вписанный угол', 'en': 'Example 1 · inscribed angle'},
   'q': {'ru': 'Хорда <var>AB</var> стягивает центральный угол 100&deg;. Точка <var>C</var> лежит на большей дуге <var>AB</var>. Найдите угол <var>ACB</var>.',
         'en': 'Chord <var>AB</var> subtends a central angle of 100&deg;. Point <var>C</var> lies on the major arc <var>AB</var>. Find angle <var>ACB</var>.'},
   'sol': {'ru': 'Вписанный угол <var>ACB</var> опирается на ту же дугу, что и центральный: 100&deg;/2 = <b>50&deg;</b>. Ловушка &mdash; точка на МЕНЬШЕЙ дуге: там угол опирался бы на дугу 260&deg; и был бы равен 130&deg;. Всегда проверяйте, на какую дугу смотрит вершина.',
          'en': 'Inscribed angle <var>ACB</var> stands on the same arc as the central angle: 100&deg;/2 = <b>50&deg;</b>. The trap is a point on the MINOR arc: there the angle would stand on the 260&deg; arc and equal 130&deg;. Always check which arc the vertex faces.'}},
  {'tag': {'ru': 'Разбор 2 · касательная', 'en': 'Example 2 · tangent'},
   'q': {'ru': 'Точка <var>P</var> находится на расстоянии 13 от центра окружности радиуса 5. Найдите длину касательной из точки <var>P</var>.',
         'en': 'Point <var>P</var> is at distance 13 from the center of a circle of radius 5. Find the length of the tangent from <var>P</var>.'},
   'sol': {'ru': 'Радиус в точку касания перпендикулярен касательной: прямоугольный треугольник с гипотенузой 13 и катетом 5. Касательная = &radic;(169 &minus; 25) = <b>12</b> &mdash; тройка 5-12-13. Каждая задача о касательной начинается с этого прямого угла.',
          'en': 'The radius to the point of tangency is perpendicular to the tangent: a right triangle with hypotenuse 13 and leg 5. Tangent = &radic;(169 &minus; 25) = <b>12</b> &mdash; the 5-12-13 triple. Every tangent problem starts with this right angle.'}},
  {'tag': {'ru': 'Разбор 3 · вписанная окружность', 'en': 'Example 3 · incircle'},
   'q': {'ru': 'Найдите радиус окружности, вписанной в прямоугольный треугольник с катетами 6 и 8.',
         'en': 'Find the radius of the circle inscribed in a right triangle with legs 6 and 8.'},
   'sol': {'ru': 'Гипотенуза 10. Через формулу <var>r</var> = <var>S</var>/<var>p</var>: площадь 24, полупериметр 12, значит <var>r</var> = 24/12 = <b>2</b>. Быстрая проверка формулой для прямоугольного треугольника: (6 + 8 &minus; 10)/2 = 2. Сошлось. Обе формулы держите наготове: первая универсальна, вторая мгновенна.',
          'en': 'The hypotenuse is 10. Via <var>r</var> = <var>S</var>/<var>p</var>: area 24, semiperimeter 12, so <var>r</var> = 24/12 = <b>2</b>. Quick check with the right-triangle formula: (6 + 8 &minus; 10)/2 = 2. Agreed. Keep both formulas ready: the first is universal, the second instantaneous.'}},
  {'tag': {'ru': 'Разбор 4 · вписанный четырёхугольник', 'en': 'Example 4 · cyclic quadrilateral'},
   'q': {'ru': 'Четырёхугольник <var>ABCD</var> вписан в окружность, угол <var>A</var> = 70&deg;, угол <var>B</var> = 85&deg;. Найдите углы <var>C</var> и <var>D</var>.',
         'en': 'Quadrilateral <var>ABCD</var> is inscribed in a circle, with angle <var>A</var> = 70&deg; and angle <var>B</var> = 85&deg;. Find angles <var>C</var> and <var>D</var>.'},
   'sol': {'ru': 'Противоположные углы дают 180&deg;: <var>C</var> = 180&deg; &minus; 70&deg; = <b>110&deg;</b>, <var>D</var> = 180&deg; &minus; 85&deg; = <b>95&deg;</b>. Проверка: 70 + 85 + 110 + 95 = 360. Верно. Пары &mdash; именно ПРОТИВОПОЛОЖНЫЕ углы: <var>A</var> с <var>C</var>, <var>B</var> с <var>D</var>, не соседние.',
          'en': 'Opposite angles sum to 180&deg;: <var>C</var> = 180&deg; &minus; 70&deg; = <b>110&deg;</b>, <var>D</var> = 180&deg; &minus; 85&deg; = <b>95&deg;</b>. Check: 70 + 85 + 110 + 95 = 360. Correct. The pairs are the OPPOSITE angles: <var>A</var> with <var>C</var>, <var>B</var> with <var>D</var>, not adjacent ones.'}},
 ],
 'selfp': [
  {'q': {'ru': 'Центральный угол равен 80&deg;. Найдите вписанный угол, опирающийся на ту же дугу.', 'en': 'A central angle is 80&deg;. Find the inscribed angle on the same arc.'},
   'hint': {'ru': 'Половина центрального.', 'en': 'Half the central angle.'},
   'sol': {'ru': '80/2 = <b>40&deg;</b>.', 'en': '80/2 = <b>40&deg;</b>.'}},
  {'q': {'ru': 'Отрезок <var>AB</var> &mdash; диаметр окружности, точка <var>C</var> лежит на окружности, угол <var>CAB</var> = 35&deg;. Найдите угол <var>CBA</var>.', 'en': 'Segment <var>AB</var> is a diameter of a circle, point <var>C</var> lies on the circle, and angle <var>CAB</var> = 35&deg;. Find angle <var>CBA</var>.'},
   'hint': {'ru': 'Угол <var>ACB</var> опирается на диаметр.', 'en': 'Angle <var>ACB</var> subtends the diameter.'},
   'sol': {'ru': 'Угол <var>C</var> = 90&deg; (Фалес), значит <var>CBA</var> = 90 &minus; 35 = <b>55&deg;</b>.', 'en': 'Angle <var>C</var> = 90&deg; (Thales), so <var>CBA</var> = 90 &minus; 35 = <b>55&deg;</b>.'}},
  {'q': {'ru': 'Точка <var>P</var> удалена от центра окружности радиуса 6 на расстояние 10. Найдите длину касательной из <var>P</var>.', 'en': 'Point <var>P</var> is at distance 10 from the center of a circle of radius 6. Find the tangent length from <var>P</var>.'},
   'hint': {'ru': 'Прямой угол между радиусом и касательной.', 'en': 'The right angle between the radius and the tangent.'},
   'sol': {'ru': '&radic;(100 &minus; 36) = <b>8</b> (тройка 6-8-10).', 'en': '&radic;(100 &minus; 36) = <b>8</b> (the 6-8-10 triple).'}},
  {'q': {'ru': 'Четырёхугольник вписан в окружность, один из его углов равен 100&deg;. Найдите противоположный угол.', 'en': 'A quadrilateral is inscribed in a circle, and one of its angles is 100&deg;. Find the opposite angle.'},
   'hint': {'ru': 'Противоположные углы вписанного четырёхугольника.', 'en': 'Opposite angles of a cyclic quadrilateral.'},
   'sol': {'ru': '180 &minus; 100 = <b>80&deg;</b>.', 'en': '180 &minus; 100 = <b>80&deg;</b>.'}},
  {'q': {'ru': 'Найдите радиус окружности, вписанной в треугольник со сторонами 13, 14, 15.', 'en': 'Find the radius of the circle inscribed in the triangle with sides 13, 14, 15.'},
   'hint': {'ru': 'Площадь этого треугольника уже считали в уроке 2.3: 84.', 'en': 'The area of this triangle was computed in Lesson 2.3: 84.'},
   'sol': {'ru': '<var>r</var> = <var>S</var>/<var>p</var> = 84/21 = <b>4</b>.', 'en': '<var>r</var> = <var>S</var>/<var>p</var> = 84/21 = <b>4</b>.'}},
  {'q': {'ru': 'Катеты прямоугольного треугольника равны 9 и 12. Найдите радиус описанной окружности.', 'en': 'The legs of a right triangle are 9 and 12. Find the circumradius.'},
   'hint': {'ru': 'Гипотенуза &mdash; диаметр.', 'en': 'The hypotenuse is a diameter.'},
   'sol': {'ru': 'Гипотенуза 15 (тройка 9-12-15), значит <var>R</var> = <b>7,5</b>.', 'en': 'The hypotenuse is 15 (the 9-12-15 triple), so <var>R</var> = <b>7.5</b>.'}},
  {'q': {'ru': 'Из точки <var>P</var> проведены касательные <var>PA</var> и <var>PB</var> к окружности с центром <var>O</var>; угол <var>APB</var> = 40&deg;. Найдите центральный угол <var>AOB</var>.', 'en': 'Tangents <var>PA</var> and <var>PB</var> are drawn from point <var>P</var> to a circle with center <var>O</var>; angle <var>APB</var> = 40&deg;. Find central angle <var>AOB</var>.'},
   'hint': {'ru': 'В четырёхугольнике <var>PAOB</var> два прямых угла.', 'en': 'Quadrilateral <var>PAOB</var> has two right angles.'},
   'sol': {'ru': '360 &minus; 90 &minus; 90 &minus; 40 = <b>140&deg;</b>.', 'en': '360 &minus; 90 &minus; 90 &minus; 40 = <b>140&deg;</b>.'}},
  {'q': {'ru': 'В окружности радиуса 5 проведены две параллельные хорды длиной 6 и 8, лежащие по одну сторону от центра. Найдите расстояние между ними.', 'en': 'In a circle of radius 5, two parallel chords of lengths 6 and 8 lie on the same side of the center. Find the distance between them.'},
   'hint': {'ru': 'Расстояние от центра до каждой хорды &mdash; из тройки 3-4-5.', 'en': 'The distance from the center to each chord comes from the 3-4-5 triple.'},
   'sol': {'ru': 'Хорда 6 лежит на расстоянии &radic;(25 &minus; 9) = 4, хорда 8 &mdash; на расстоянии &radic;(25 &minus; 16) = 3. По одну сторону: 4 &minus; 3 = <b>1</b>. Ловушка &mdash; сложить и получить 7: это ответ для хорд по РАЗНЫЕ стороны.', 'en': 'The chord of 6 sits at distance &radic;(25 &minus; 9) = 4, the chord of 8 at &radic;(25 &minus; 16) = 3. Same side: 4 &minus; 3 = <b>1</b>. The trap is adding to get 7: that answers the OPPOSITE-sides version.'}},
 ],
 'answers': {'ru': '40° · 55° · 8 · 80° · 4 · 7,5 · 140° · 1', 'en': '40&deg;, 55&deg;, 8, 80&deg;, 4, 7.5, 140&deg;, 1'},
 'routing': {'ru': 'Норма &mdash; 6 из 8. Ошибки в 1&ndash;2 и 4 &mdash; &laquo;вписанные и центральные углы&raquo;; в 3 и 7 &mdash; &laquo;касательные&raquo;; в 5&ndash;6 &mdash; &laquo;вписанная и описанная окружности&raquo;; в 8 &mdash; &laquo;хорды&raquo;.',
             'en': 'Mastery bar: 6 of 8. For mistakes in 1&ndash;2 and 4, reread &ldquo;inscribed and central angles&rdquo;; for 3 and 7, &ldquo;tangents&rdquo;; for 5&ndash;6, &ldquo;incircle and circumcircle&rdquo;; for 8, &ldquo;chords&rdquo;.'},
}
