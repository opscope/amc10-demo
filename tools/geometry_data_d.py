# -*- coding: utf-8 -*-
"""Блок 2 «Геометрия»: тест Т2 + задачи-звёздочки, RU+EN."""

def F(a, b):
    return f'<span class="frac"><span>{a}</span><span>{b}</span></span>'

T2 = {
 'problems': [
  {'q': {'ru': 'Внешний угол правильного многоугольника равен 30&deg;. Сколько у многоугольника сторон?',
         'en': 'The exterior angle of a regular polygon is 30&deg;. How many sides does the polygon have?'},
   'opts': {'ru': ['8', '9', '10', '12', '15'], 'en': ['8', '9', '10', '12', '15']}},
  {'q': {'ru': 'Углы треугольника относятся как 3&nbsp;:&nbsp;4&nbsp;:&nbsp;5. Чему равен наибольший угол (в градусах)?',
         'en': 'The angles of a triangle are in the ratio 3&nbsp;:&nbsp;4&nbsp;:&nbsp;5. What is the largest angle (in degrees)?'},
   'opts': {'ru': ['60', '70', '75', '80', '90'], 'en': ['60', '70', '75', '80', '90']}},
  {'q': {'ru': 'В прямоугольном треугольнике с острым углом 30&deg; гипотенуза равна 12. Найдите катет, лежащий против угла 60&deg;.',
         'en': 'A right triangle has a 30&deg; acute angle and hypotenuse 12. Find the leg opposite the 60&deg; angle.'},
   'opts': {'ru': ['3&radic;3', '6', '6&radic;2', '9', '6&radic;3'], 'en': ['3&radic;3', '6', '6&radic;2', '9', '6&radic;3']}},
  {'q': {'ru': 'Катеты прямоугольного треугольника равны 6 и 8. Найдите высоту, опущенную на гипотенузу.',
         'en': 'The legs of a right triangle are 6 and 8. Find the altitude to the hypotenuse.'},
   'opts': {'ru': ['3,6', '4,8', '5', '6,4', '7'], 'en': ['3.6', '4.8', '5', '6.4', '7']}},
  {'q': {'ru': 'Найдите площадь треугольника со сторонами 10, 10 и 12.',
         'en': 'Find the area of the triangle with sides 10, 10, and 12.'},
   'opts': {'ru': ['36', '44', '48', '54', '60'], 'en': ['36', '44', '48', '54', '60']}},
  {'q': {'ru': 'В треугольнике <var>ABC</var> точка <var>M</var> лежит на стороне <var>AB</var>, а точка <var>N</var> &mdash; на стороне <var>AC</var>, причём <var>AM</var>&nbsp;:&nbsp;<var>AB</var> = 2&nbsp;:&nbsp;3 и <var>AN</var>&nbsp;:&nbsp;<var>AC</var> = 3&nbsp;:&nbsp;4. Площадь треугольника <var>ABC</var> равна 96. Найдите площадь четырёхугольника <var>BMNC</var>.',
         'en': 'In triangle <var>ABC</var>, point <var>M</var> lies on side <var>AB</var> and point <var>N</var> on side <var>AC</var>, with <var>AM</var>&nbsp;:&nbsp;<var>AB</var> = 2&nbsp;:&nbsp;3 and <var>AN</var>&nbsp;:&nbsp;<var>AC</var> = 3&nbsp;:&nbsp;4. The area of triangle <var>ABC</var> is 96. Find the area of quadrilateral <var>BMNC</var>.'},
   'opts': {'ru': ['40', '44', '48', '52', '56'], 'en': ['40', '44', '48', '52', '56']}},
  {'q': {'ru': 'Точка <var>P</var> находится на расстоянии 17 от центра окружности радиуса 8. Найдите длину касательной, проведённой из <var>P</var> к окружности.',
         'en': 'Point <var>P</var> is at distance 17 from the center of a circle of radius 8. Find the length of the tangent from <var>P</var> to the circle.'},
   'opts': {'ru': ['9', '12', '13', '15', '25'], 'en': ['9', '12', '13', '15', '25']}},
  {'q': {'ru': 'Стороны треугольника <var>ABC</var> равны <var>AB</var> = 13, <var>BC</var> = 14, <var>CA</var> = 15. Вписанная окружность касается стороны <var>BC</var> в точке <var>T</var>. Найдите <var>BT</var>.',
         'en': 'Triangle <var>ABC</var> has sides <var>AB</var> = 13, <var>BC</var> = 14, <var>CA</var> = 15. The incircle touches side <var>BC</var> at point <var>T</var>. Find <var>BT</var>.'},
   'opts': {'ru': ['5', '6', '7', '8', '9'], 'en': ['5', '6', '7', '8', '9']}},
  {'q': {'ru': 'Найдите площадь треугольника с вершинами (0;&nbsp;0), (10;&nbsp;4) и (2;&nbsp;6).',
         'en': 'Find the area of the triangle with vertices (0,&nbsp;0), (10,&nbsp;4), and (2,&nbsp;6).'},
   'opts': {'ru': ['18', '20', '22', '24', '26'], 'en': ['18', '20', '22', '24', '26']}},
  {'q': {'ru': 'Найдите диагональ прямоугольного параллелепипеда с рёбрами 4, 4 и 7.',
         'en': 'Find the space diagonal of a 4-by-4-by-7 rectangular box.'},
   'opts': {'ru': ['9', '10', '11', '12', '15'], 'en': ['9', '10', '11', '12', '15']}},
 ],
 'key': ['D', 'C', 'E', 'B', 'C', 'C', 'D', 'B', 'E', 'A'],
 'hints': {
  'ru': [
   '<b>1.</b> Внешние углы дают 360&deg;: <var>n</var> = 360/30 = 12.',
   '<b>2.</b> Часть = 180/12 = 15&deg;: наибольший угол 5&nbsp;&middot;&nbsp;15 = 75&deg;.',
   '<b>3.</b> Схема <var>x</var> : <var>x</var>&radic;3 : 2<var>x</var>: <var>x</var> = 6, против 60&deg; лежит 6&radic;3.',
   '<b>4.</b> Гипотенуза 10, высота = 6&nbsp;&middot;&nbsp;8/10 = 4,8 (а 3,6 и 6,4 &mdash; отрезки гипотенузы, ловушки).',
   '<b>5.</b> Высота к стороне 12: &radic;(100 &minus; 36) = 8, площадь 12&nbsp;&middot;&nbsp;8/2 = 48.',
   '<b>6.</b> [<var>AMN</var>] = (2/3)&middot;(3/4)&middot;96 = 48; четырёхугольник: 96 &minus; 48 = 48. Отношение площадей при общем угле = произведение отношений сторон.',
   '<b>7.</b> &radic;(17<sup>2</sup> &minus; 8<sup>2</sup>) = &radic;225 = 15 (тройка 8-15-17).',
   '<b>8.</b> Отрезки касательных: <var>x</var>+<var>y</var> = 13, <var>y</var>+<var>z</var> = 14, <var>x</var>+<var>z</var> = 15; сложить и вычесть: <var>y</var> = <var>BT</var> = 6 (= <var>p</var> &minus; <var>CA</var> = 21 &minus; 15).',
   '<b>9.</b> Шнуровка с нулевой вершиной: |10&nbsp;&middot;&nbsp;6 &minus; 2&nbsp;&middot;&nbsp;4|/2 = 52/2 = 26.',
   '<b>10.</b> &radic;(16 + 16 + 49) = &radic;81 = 9.'],
  'en': [
   '<b>1.</b> Exterior angles sum to 360&deg;: <var>n</var> = 360/30 = 12.',
   '<b>2.</b> One part = 180/12 = 15&deg;: the largest angle is 5&nbsp;&middot;&nbsp;15 = 75&deg;.',
   '<b>3.</b> The pattern <var>x</var> : <var>x</var>&radic;3 : 2<var>x</var>: <var>x</var> = 6, and 6&radic;3 lies opposite 60&deg;.',
   '<b>4.</b> Hypotenuse 10, altitude = 6&nbsp;&middot;&nbsp;8/10 = 4.8 (while 3.6 and 6.4 are the hypotenuse segments &mdash; traps).',
   '<b>5.</b> The altitude to the side of 12: &radic;(100 &minus; 36) = 8, so the area is 12&nbsp;&middot;&nbsp;8/2 = 48.',
   '<b>6.</b> [<var>AMN</var>] = (2/3)&middot;(3/4)&middot;96 = 48; quadrilateral: 96 &minus; 48 = 48. With a shared angle, the area ratio is the product of the side ratios.',
   '<b>7.</b> &radic;(17<sup>2</sup> &minus; 8<sup>2</sup>) = &radic;225 = 15 (the 8-15-17 triple).',
   '<b>8.</b> Tangent segments: <var>x</var>+<var>y</var> = 13, <var>y</var>+<var>z</var> = 14, <var>x</var>+<var>z</var> = 15; add and subtract: <var>y</var> = <var>BT</var> = 6 (= <var>s</var> &minus; <var>CA</var> = 21 &minus; 15).',
   '<b>9.</b> Shoelace with the zero vertex first: |10&nbsp;&middot;&nbsp;6 &minus; 2&nbsp;&middot;&nbsp;4|/2 = 52/2 = 26.',
   '<b>10.</b> &radic;(16 + 16 + 49) = &radic;81 = 9.'],
 },
}


STARS = {
 '2.1': {
  'q': {'ru': 'В треугольнике <var>ABC</var> угол <var>A</var> = 40&deg;. Биссектрисы углов <var>B</var> и <var>C</var> пересекаются в точке <var>I</var>. Найдите угол <var>BIC</var>.',
        'en': 'In triangle <var>ABC</var>, angle <var>A</var> = 40&deg;. The bisectors of angles <var>B</var> and <var>C</var> meet at point <var>I</var>. Find angle <var>BIC</var>.'},
  'hint': {'ru': 'В треугольнике <var>BIC</var> сумма углов при <var>B</var> и <var>C</var> равна половине суммы углов <var>B</var> и <var>C</var> исходного треугольника.', 'en': 'In triangle <var>BIC</var>, the angles at <var>B</var> and <var>C</var> add to half the sum of angles <var>B</var> and <var>C</var> of the original triangle.'},
  'sol': {'ru': 'Углы <var>B</var> + <var>C</var> = 140&deg;, их половины дают 70&deg;, значит угол <var>BIC</var> = 180&deg; &minus; 70&deg; = <b>110&deg;</b>. Общий факт: угол между биссектрисами равен 90&deg; + <var>A</var>/2.', 'en': 'Angles <var>B</var> + <var>C</var> = 140&deg;, and their halves give 70&deg;, so angle <var>BIC</var> = 180&deg; &minus; 70&deg; = <b>110&deg;</b>. The general fact: the angle between the bisectors is 90&deg; + <var>A</var>/2.'}},
 '2.2': {
  'q': {'ru': 'В прямоугольном треугольнике катеты равны 15 и 20. Из вершины прямого угла на гипотенузу опущена высота; <var>D</var> &mdash; её основание. Найдите расстояние от точки <var>D</var> до катета длины 15.',
        'en': 'A right triangle has legs 15 and 20. The altitude from the right angle meets the hypotenuse at point <var>D</var>. Find the distance from <var>D</var> to the leg of length 15.'},
  'hint': {'ru': 'Сначала найдите отрезок гипотенузы у катета 15: <var>AD</var> = <var>b</var><sup>2</sup>/<var>c</var>. Потом ещё одно подобие: искомое расстояние &mdash; катет маленького треугольника с гипотенузой <var>AD</var>.', 'en': 'First find the hypotenuse segment next to the leg 15: <var>AD</var> = <var>b</var><sup>2</sup>/<var>c</var>. Then one more similarity: the distance is a leg of a small triangle whose hypotenuse is <var>AD</var>.'},
  'sol': {'ru': 'Гипотенуза 25. Отрезок у катета 15: <var>AD</var> = 15<sup>2</sup>/25 = 9. Перпендикуляр из <var>D</var> на катет создаёт треугольник, подобный исходному: расстояние = <var>AD</var>&nbsp;&middot;&nbsp;20/25 = 9&nbsp;&middot;&nbsp;0,8 = <b>7,2</b>. Две ступени подобия подряд &mdash; фирменный ход задач №11&ndash;15.', 'en': 'The hypotenuse is 25. The segment next to the leg 15: <var>AD</var> = 15<sup>2</sup>/25 = 9. The perpendicular from <var>D</var> to that leg creates a triangle similar to the original: distance = <var>AD</var>&nbsp;&middot;&nbsp;20/25 = 9&nbsp;&middot;&nbsp;0.8 = <b>7.2</b>. Two similarity steps in a row is the signature move of problems #11&ndash;15.'}},
 '2.3': {
  'q': {'ru': 'В трапеции <var>ABCD</var> основания <var>BC</var> = 5 и <var>AD</var> = 15, диагонали пересекаются в точке <var>O</var>. Площадь треугольника <var>BOC</var> равна 3. Найдите площадь трапеции.',
        'en': 'In trapezoid <var>ABCD</var>, the bases are <var>BC</var> = 5 and <var>AD</var> = 15, and the diagonals meet at point <var>O</var>. The area of triangle <var>BOC</var> is 3. Find the area of the trapezoid.'},
  'hint': {'ru': 'Треугольники <var>BOC</var> и <var>DOA</var> подобны с коэффициентом 1&nbsp;:&nbsp;3; боковые треугольники сравните с <var>BOC</var> через общую высоту.', 'en': 'Triangles <var>BOC</var> and <var>DOA</var> are similar with ratio 1&nbsp;:&nbsp;3; compare the side triangles to <var>BOC</var> via a shared altitude.'},
  'sol': {'ru': 'Подобие 1&nbsp;:&nbsp;3 даёт [<var>DOA</var>] = 9&nbsp;&middot;&nbsp;3 = 27. Далее <var>OA</var>&nbsp;:&nbsp;<var>OC</var> = 3&nbsp;:&nbsp;1, значит [<var>AOB</var>] = 3&nbsp;&middot;&nbsp;[<var>BOC</var>] = 9, и так же [<var>COD</var>] = 9. Итого 3 + 27 + 9 + 9 = <b>48</b>.', 'en': 'The 1&nbsp;:&nbsp;3 similarity gives [<var>DOA</var>] = 9&nbsp;&middot;&nbsp;3 = 27. Then <var>OA</var>&nbsp;:&nbsp;<var>OC</var> = 3&nbsp;:&nbsp;1, so [<var>AOB</var>] = 3&nbsp;&middot;&nbsp;[<var>BOC</var>] = 9, and likewise [<var>COD</var>] = 9. Total: 3 + 27 + 9 + 9 = <b>48</b>.'}},
 '2.4': {
  'q': {'ru': 'Окружность, вписанная в прямоугольный треугольник, касается гипотенузы в точке, делящей её на отрезки 6 и 4. Найдите площадь треугольника.',
        'en': 'The circle inscribed in a right triangle touches the hypotenuse at a point dividing it into segments of lengths 6 and 4. Find the area of the triangle.'},
  'hint': {'ru': 'Отрезки касательных из одной вершины равны: катеты равны 6 + <var>r</var> и 4 + <var>r</var>.', 'en': 'Tangent segments from one vertex are equal: the legs are 6 + <var>r</var> and 4 + <var>r</var>.'},
  'sol': {'ru': 'Пифагор: (6 + <var>r</var>)<sup>2</sup> + (4 + <var>r</var>)<sup>2</sup> = 100, то есть <var>r</var><sup>2</sup> + 10<var>r</var> &minus; 24 = 0 и <var>r</var> = 2. Катеты 8 и 6: площадь 8&nbsp;&middot;&nbsp;6/2 = <b>24</b>. Проверка: тройка 6-8-10.', 'en': 'Pythagoras: (6 + <var>r</var>)<sup>2</sup> + (4 + <var>r</var>)<sup>2</sup> = 100, that is <var>r</var><sup>2</sup> + 10<var>r</var> &minus; 24 = 0, so <var>r</var> = 2. The legs are 8 and 6: area 8&nbsp;&middot;&nbsp;6/2 = <b>24</b>. Check: the 6-8-10 triple.'}},
 '2.5': {
  'q': {'ru': 'Точки <var>A</var>(2;&nbsp;3) и <var>B</var>(10;&nbsp;9) лежат по одну сторону от оси <var>x</var>. Точка <var>P</var> выбирается на оси <var>x</var> так, чтобы сумма <var>AP</var> + <var>PB</var> была наименьшей. Найдите абсциссу точки <var>P</var>.',
        'en': 'Points <var>A</var>(2, 3) and <var>B</var>(10, 9) lie on the same side of the <var>x</var>-axis. Point <var>P</var> is chosen on the <var>x</var>-axis so that <var>AP</var> + <var>PB</var> is as small as possible. Find the <var>x</var>-coordinate of <var>P</var>.'},
  'hint': {'ru': 'Отразите <var>A</var> относительно оси: кратчайший путь через ось &mdash; это прямая от <var>A</var>&prime;(2;&nbsp;&minus;3) до <var>B</var>.', 'en': 'Reflect <var>A</var> across the axis: the shortest path through the axis is the straight segment from <var>A</var>&prime;(2, &minus;3) to <var>B</var>.'},
  'sol': {'ru': 'Отражение: <var>A</var>&prime;(2;&nbsp;&minus;3). Прямая <var>A</var>&prime;<var>B</var> имеет наклон 12/8 = 3/2 и пересекает ось <var>x</var> при &minus;3 + (3/2)(<var>x</var> &minus; 2) = 0, то есть <var>x</var> = <b>4</b>. Любой другой путь длиннее ломаной, распрямлённой отражением &mdash; это и есть трюк задач о кратчайшем пути.', 'en': 'Reflect: <var>A</var>&prime;(2, &minus;3). Line <var>A</var>&prime;<var>B</var> has slope 12/8 = 3/2 and crosses the <var>x</var>-axis where &minus;3 + (3/2)(<var>x</var> &minus; 2) = 0, i.e. <var>x</var> = <b>4</b>. Every other path is longer than the reflection-straightened one &mdash; the signature shortest-path trick.'}},
 '2.6': {
  'q': {'ru': 'Из сектора круга радиуса 10 с центральным углом 216&deg; свернули боковую поверхность конуса. Найдите объём конуса.',
        'en': 'A 216&deg; sector of a circle of radius 10 is rolled into the lateral surface of a cone. Find the volume of the cone.'},
  'hint': {'ru': 'Дуга сектора становится окружностью основания, радиус сектора &mdash; образующей.', 'en': 'The arc of the sector becomes the base circle, and the sector&rsquo;s radius becomes the slant height.'},
  'sol': {'ru': 'Дуга: (216/360)&nbsp;&middot;&nbsp;2&pi;&nbsp;&middot;&nbsp;10 = 12&pi;, значит радиус основания 6. Образующая 10, высота &radic;(100 &minus; 36) = 8. Объём: (1/3)&pi;&nbsp;&middot;&nbsp;36&nbsp;&middot;&nbsp;8 = <b>96&pi;</b>.', 'en': 'Arc: (216/360)&nbsp;&middot;&nbsp;2&pi;&nbsp;&middot;&nbsp;10 = 12&pi;, so the base radius is 6. The slant is 10, and the height is &radic;(100 &minus; 36) = 8. Volume: (1/3)&pi;&nbsp;&middot;&nbsp;36&nbsp;&middot;&nbsp;8 = <b>96&pi;</b>.'}},
}
