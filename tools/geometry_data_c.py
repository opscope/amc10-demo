# -*- coding: utf-8 -*-
"""Блок 2 «Геометрия»: уроки 2.5–2.6, RU+EN. HTML-фрагменты в нотации страницы курса."""

def F(a, b):
    return f'<span class="frac"><span>{a}</span><span>{b}</span></span>'

L25 = {
 'id': '2.5', 'anchor': 'u25',
 'title': {'ru': 'Координатная геометрия: расстояние, прямые, окружность, шнуровка',
           'en': 'Coordinate Geometry: Distance, Lines, Circles, Shoelace'},
 'theory': {
  'ru': f"""
<p><b>Расстояние и середина.</b> Расстояние между точками &mdash; Пифагор по разностям координат: &radic;((<var>x</var><sub>2</sub> &minus; <var>x</var><sub>1</sub>)<sup>2</sup> + (<var>y</var><sub>2</sub> &minus; <var>y</var><sub>1</sub>)<sup>2</sup>). Середина &mdash; полусуммы координат. Разности 6 и 8, 5 и 12, 8 и 15 &mdash; узнавайте тройки и не извлекайте корень честно.</p>
<p><b>Прямые.</b> Угловой коэффициент <var>k</var> = &Delta;<var>y</var>/&Delta;<var>x</var>: подъём на шаг вправо. Параллельные прямые: равные <var>k</var>; перпендикулярные: <var>k</var><sub>1</sub><var>k</var><sub>2</sub> = &minus;1. Прямая по точке и наклону: <var>y</var> &minus; <var>y</var><sub>0</sub> = <var>k</var>(<var>x</var> &minus; <var>x</var><sub>0</sub>). Пересечения с осями ищутся подстановкой нуля &mdash; не по памяти, а подстановкой.</p>
<div class="frm">Шнуровка для треугольника (<var>x</var><sub>1</sub>,&nbsp;<var>y</var><sub>1</sub>), (<var>x</var><sub>2</sub>,&nbsp;<var>y</var><sub>2</sub>), (<var>x</var><sub>3</sub>,&nbsp;<var>y</var><sub>3</sub>): <var>S</var> = {F('1','2')}|<var>x</var><sub>1</sub><var>y</var><sub>2</sub> &minus; <var>x</var><sub>2</sub><var>y</var><sub>1</sub> + <var>x</var><sub>2</sub><var>y</var><sub>3</sub> &minus; <var>x</var><sub>3</sub><var>y</var><sub>2</sub> + <var>x</var><sub>3</sub><var>y</var><sub>1</sub> &minus; <var>x</var><sub>1</sub><var>y</var><sub>3</sub>|. Окружность: (<var>x</var> &minus; <var>a</var>)<sup>2</sup> + (<var>y</var> &minus; <var>b</var>)<sup>2</sup> = <var>r</var><sup>2</sup>.</div>
<p><b>Окружность.</b> Уравнение с <var>x</var><sup>2</sup> + <var>y</var><sup>2</sup> и линейными членами приводится выделением полных квадратов: из <var>x</var><sup>2</sup> &minus; 6<var>x</var> получаем (<var>x</var> &minus; 3)<sup>2</sup> &minus; 9. Центр и радиус читаются из канонического вида; не забудьте перенести &laquo;хвосты&raquo; от квадратов в правую часть.</p>
<p><b>Шнуровка.</b> Обход вершин &mdash; строго по контуру (по или против часовой стрелки, но без прыжков через фигуру), модуль в конце спасает от знака. Ставьте вершину с нулями первой: слагаемые с нулём выгорают, и счёт укорачивается вдвое. Для многоугольника формула та же: пары соседних вершин по кругу.</p>""",
  'en': f"""
<p><b>Distance and midpoint.</b> The distance between points is Pythagoras on coordinate differences: &radic;((<var>x</var><sub>2</sub> &minus; <var>x</var><sub>1</sub>)<sup>2</sup> + (<var>y</var><sub>2</sub> &minus; <var>y</var><sub>1</sub>)<sup>2</sup>). The midpoint takes half-sums of the coordinates. Differences of 6 and 8, 5 and 12, 8 and 15 &mdash; recognize the triples instead of grinding out the square root.</p>
<p><b>Lines.</b> Slope <var>k</var> = &Delta;<var>y</var>/&Delta;<var>x</var>: the rise per step right. Parallel lines: equal slopes; perpendicular: <var>k</var><sub>1</sub><var>k</var><sub>2</sub> = &minus;1. A line from a point and a slope: <var>y</var> &minus; <var>y</var><sub>0</sub> = <var>k</var>(<var>x</var> &minus; <var>x</var><sub>0</sub>). Axis intercepts come from substituting zero &mdash; by substitution, not from memory.</p>
<div class="frm">Shoelace for a triangle (<var>x</var><sub>1</sub>,&nbsp;<var>y</var><sub>1</sub>), (<var>x</var><sub>2</sub>,&nbsp;<var>y</var><sub>2</sub>), (<var>x</var><sub>3</sub>,&nbsp;<var>y</var><sub>3</sub>): <var>S</var> = {F('1','2')}|<var>x</var><sub>1</sub><var>y</var><sub>2</sub> &minus; <var>x</var><sub>2</sub><var>y</var><sub>1</sub> + <var>x</var><sub>2</sub><var>y</var><sub>3</sub> &minus; <var>x</var><sub>3</sub><var>y</var><sub>2</sub> + <var>x</var><sub>3</sub><var>y</var><sub>1</sub> &minus; <var>x</var><sub>1</sub><var>y</var><sub>3</sub>|. Circle: (<var>x</var> &minus; <var>a</var>)<sup>2</sup> + (<var>y</var> &minus; <var>b</var>)<sup>2</sup> = <var>r</var><sup>2</sup>.</div>
<p><b>Circles.</b> An equation with <var>x</var><sup>2</sup> + <var>y</var><sup>2</sup> and linear terms is tamed by completing the square: from <var>x</var><sup>2</sup> &minus; 6<var>x</var> we get (<var>x</var> &minus; 3)<sup>2</sup> &minus; 9. The center and radius read off the standard form; do not forget to carry the leftover constants to the right-hand side.</p>
<p><b>Shoelace.</b> Walk the vertices strictly along the boundary (clockwise or counterclockwise, but never jumping across the figure); the absolute value at the end fixes the sign. Put a vertex with zeros first: zero terms burn away and the computation halves. For any polygon the formula is the same: consecutive vertex pairs around the loop.</p>"""},
 'worked': [
  {'tag': {'ru': 'Разбор 1 · расстояние и середина', 'en': 'Example 1 · distance and midpoint'},
   'q': {'ru': 'Даны точки <var>A</var>(&minus;2;&nbsp;3) и <var>B</var>(4;&nbsp;11). Найдите длину отрезка <var>AB</var> и его середину.',
         'en': 'Given points <var>A</var>(&minus;2,&nbsp;3) and <var>B</var>(4,&nbsp;11), find the length of segment <var>AB</var> and its midpoint.'},
   'sol': {'ru': 'Разности: &Delta;<var>x</var> = 6, &Delta;<var>y</var> = 8 &mdash; тройка 6-8-10, длина <b>10</b> без корня. Середина: ((&minus;2 + 4)/2;&nbsp;(3 + 11)/2) = <b>(1;&nbsp;7)</b>. Частая ошибка в середине &mdash; полуразность вместо полусуммы: середина &mdash; это СРЕДНЕЕ координат.',
          'en': 'Differences: &Delta;<var>x</var> = 6, &Delta;<var>y</var> = 8 &mdash; the 6-8-10 triple, so the length is <b>10</b> with no root. Midpoint: ((&minus;2 + 4)/2,&nbsp;(3 + 11)/2) = <b>(1,&nbsp;7)</b>. The common midpoint error is a half-difference instead of a half-sum: the midpoint is the AVERAGE of the coordinates.'}},
  {'tag': {'ru': 'Разбор 2 · уравнение прямой', 'en': 'Example 2 · equation of a line'},
   'q': {'ru': 'Прямая проходит через точки (2;&nbsp;3) и (6;&nbsp;11). Найдите её уравнение и угловой коэффициент перпендикулярной ей прямой.',
         'en': 'A line passes through (2,&nbsp;3) and (6,&nbsp;11). Find its equation and the slope of a line perpendicular to it.'},
   'sol': {'ru': 'Наклон: (11 &minus; 3)/(6 &minus; 2) = 2. Через точку (2;&nbsp;3): <var>y</var> &minus; 3 = 2(<var>x</var> &minus; 2), то есть <b><var>y</var> = 2<var>x</var> &minus; 1</b>. Проверка второй точкой: 2&nbsp;&middot;&nbsp;6 &minus; 1 = 11. Верно. Перпендикулярный наклон: <var>k</var> = <b>&minus;1/2</b> (произведение наклонов равно &minus;1).',
          'en': 'Slope: (11 &minus; 3)/(6 &minus; 2) = 2. Through (2,&nbsp;3): <var>y</var> &minus; 3 = 2(<var>x</var> &minus; 2), that is <b><var>y</var> = 2<var>x</var> &minus; 1</b>. Check with the second point: 2&nbsp;&middot;&nbsp;6 &minus; 1 = 11. Correct. Perpendicular slope: <var>k</var> = <b>&minus;1/2</b> (the product of slopes is &minus;1).'}},
  {'tag': {'ru': 'Разбор 3 · шнуровка', 'en': 'Example 3 · Shoelace'},
   'q': {'ru': 'Найдите площадь треугольника с вершинами (0;&nbsp;0), (8;&nbsp;2), (3;&nbsp;7).',
         'en': 'Find the area of the triangle with vertices (0,&nbsp;0), (8,&nbsp;2), (3,&nbsp;7).'},
   'sol': {'ru': 'Нулевая вершина первая &mdash; выживает одно перекрёстное произведение: <var>S</var> = |8&nbsp;&middot;&nbsp;7 &minus; 3&nbsp;&middot;&nbsp;2|/2 = |56 &minus; 6|/2 = <b>25</b>. Полная шнуровка дала бы то же: 0&nbsp;&middot;&nbsp;2 &minus; 8&nbsp;&middot;&nbsp;0 + 8&nbsp;&middot;&nbsp;7 &minus; 3&nbsp;&middot;&nbsp;2 + 3&nbsp;&middot;&nbsp;0 &minus; 0&nbsp;&middot;&nbsp;7 = 50, половина 25.',
          'en': 'With the zero vertex first, a single cross product survives: <var>S</var> = |8&nbsp;&middot;&nbsp;7 &minus; 3&nbsp;&middot;&nbsp;2|/2 = |56 &minus; 6|/2 = <b>25</b>. The full Shoelace gives the same: 0&nbsp;&middot;&nbsp;2 &minus; 8&nbsp;&middot;&nbsp;0 + 8&nbsp;&middot;&nbsp;7 &minus; 3&nbsp;&middot;&nbsp;2 + 3&nbsp;&middot;&nbsp;0 &minus; 0&nbsp;&middot;&nbsp;7 = 50, half of which is 25.'}},
  {'tag': {'ru': 'Разбор 4 · окружность', 'en': 'Example 4 · circle'},
   'q': {'ru': 'Найдите центр и радиус окружности <var>x</var><sup>2</sup> + <var>y</var><sup>2</sup> &minus; 6<var>x</var> + 4<var>y</var> &minus; 12 = 0.',
         'en': 'Find the center and radius of the circle <var>x</var><sup>2</sup> + <var>y</var><sup>2</sup> &minus; 6<var>x</var> + 4<var>y</var> &minus; 12 = 0.'},
   'sol': {'ru': 'Полные квадраты: (<var>x</var> &minus; 3)<sup>2</sup> &minus; 9 + (<var>y</var> + 2)<sup>2</sup> &minus; 4 = 12, значит (<var>x</var> &minus; 3)<sup>2</sup> + (<var>y</var> + 2)<sup>2</sup> = 25. Центр <b>(3;&nbsp;&minus;2)</b>, радиус <b>5</b>. Два капкана: знак центра противоположен знаку в скобке, а 25 &mdash; это <var>r</var><sup>2</sup>, не радиус.',
          'en': 'Complete the squares: (<var>x</var> &minus; 3)<sup>2</sup> &minus; 9 + (<var>y</var> + 2)<sup>2</sup> &minus; 4 = 12, so (<var>x</var> &minus; 3)<sup>2</sup> + (<var>y</var> + 2)<sup>2</sup> = 25. Center <b>(3,&nbsp;&minus;2)</b>, radius <b>5</b>. Two snares: the center&rsquo;s sign is opposite to the sign inside the parentheses, and 25 is <var>r</var><sup>2</sup>, not the radius.'}},
 ],
 'selfp': [
  {'q': {'ru': 'Найдите расстояние между точками (1;&nbsp;2) и (7;&nbsp;10).', 'en': 'Find the distance between (1,&nbsp;2) and (7,&nbsp;10).'},
   'hint': {'ru': 'Разности 6 и 8.', 'en': 'The differences are 6 and 8.'},
   'sol': {'ru': 'Тройка 6-8-10: расстояние <b>10</b>.', 'en': 'The 6-8-10 triple: distance <b>10</b>.'}},
  {'q': {'ru': 'Найдите середину отрезка с концами (&minus;3;&nbsp;5) и (9;&nbsp;&minus;1).', 'en': 'Find the midpoint of the segment with endpoints (&minus;3,&nbsp;5) and (9,&nbsp;&minus;1).'},
   'hint': {'ru': 'Полусуммы координат.', 'en': 'Half-sums of the coordinates.'},
   'sol': {'ru': '((&minus;3 + 9)/2;&nbsp;(5 &minus; 1)/2) = <b>(3;&nbsp;2)</b>.', 'en': '((&minus;3 + 9)/2,&nbsp;(5 &minus; 1)/2) = <b>(3,&nbsp;2)</b>.'}},
  {'q': {'ru': 'Найдите угловой коэффициент прямой, проходящей через точки (2;&nbsp;&minus;1) и (5;&nbsp;8).', 'en': 'Find the slope of the line through (2,&nbsp;&minus;1) and (5,&nbsp;8).'},
   'hint': {'ru': '&Delta;<var>y</var>/&Delta;<var>x</var>; следите за знаком при вычитании &minus;1.', 'en': '&Delta;<var>y</var>/&Delta;<var>x</var>; watch the sign when subtracting &minus;1.'},
   'sol': {'ru': '(8 &minus; (&minus;1))/(5 &minus; 2) = 9/3 = <b>3</b>.', 'en': '(8 &minus; (&minus;1))/(5 &minus; 2) = 9/3 = <b>3</b>.'}},
  {'q': {'ru': 'Прямая 3<var>x</var> + 4<var>y</var> = 12 отсекает от осей координат треугольник. Найдите его площадь.', 'en': 'The line 3<var>x</var> + 4<var>y</var> = 12 cuts a triangle off the coordinate axes. Find its area.'},
   'hint': {'ru': 'Подставьте <var>y</var> = 0 и <var>x</var> = 0.', 'en': 'Substitute <var>y</var> = 0 and <var>x</var> = 0.'},
   'sol': {'ru': 'Пересечения (4;&nbsp;0) и (0;&nbsp;3): прямоугольный треугольник, площадь 4&nbsp;&middot;&nbsp;3/2 = <b>6</b>.', 'en': 'Intercepts (4,&nbsp;0) and (0,&nbsp;3): a right triangle of area 4&nbsp;&middot;&nbsp;3/2 = <b>6</b>.'}},
  {'q': {'ru': 'Прямая перпендикулярна прямой <var>y</var> = 2<var>x</var> + 3 и проходит через точку (4;&nbsp;1). Найдите её пересечение с осью <var>y</var>.', 'en': 'A line is perpendicular to <var>y</var> = 2<var>x</var> + 3 and passes through (4,&nbsp;1). Find its <var>y</var>-intercept.'},
   'hint': {'ru': 'Перпендикулярный наклон: &minus;1/2.', 'en': 'The perpendicular slope is &minus;1/2.'},
   'sol': {'ru': '<var>y</var> &minus; 1 = &minus;(<var>x</var> &minus; 4)/2, то есть <var>y</var> = &minus;<var>x</var>/2 + 3: пересечение <b>(0;&nbsp;3)</b>.', 'en': '<var>y</var> &minus; 1 = &minus;(<var>x</var> &minus; 4)/2, that is <var>y</var> = &minus;<var>x</var>/2 + 3: the intercept is <b>(0,&nbsp;3)</b>.'}},
  {'q': {'ru': 'Найдите радиус окружности <var>x</var><sup>2</sup> + <var>y</var><sup>2</sup> &minus; 4<var>x</var> + 6<var>y</var> &minus; 3 = 0.', 'en': 'Find the radius of the circle <var>x</var><sup>2</sup> + <var>y</var><sup>2</sup> &minus; 4<var>x</var> + 6<var>y</var> &minus; 3 = 0.'},
   'hint': {'ru': 'Выделите полные квадраты и соберите константы справа.', 'en': 'Complete the squares and collect the constants on the right.'},
   'sol': {'ru': '(<var>x</var> &minus; 2)<sup>2</sup> + (<var>y</var> + 3)<sup>2</sup> = 3 + 4 + 9 = 16: радиус <b>4</b>.', 'en': '(<var>x</var> &minus; 2)<sup>2</sup> + (<var>y</var> + 3)<sup>2</sup> = 3 + 4 + 9 = 16: radius <b>4</b>.'}},
  {'q': {'ru': 'Найдите площадь четырёхугольника с вершинами (0;&nbsp;0), (5;&nbsp;0), (6;&nbsp;4), (1;&nbsp;3), перечисленными по контуру.', 'en': 'Find the area of the quadrilateral with vertices (0,&nbsp;0), (5,&nbsp;0), (6,&nbsp;4), (1,&nbsp;3), listed along the boundary.'},
   'hint': {'ru': 'Шнуровка по четырём парам соседних вершин.', 'en': 'Shoelace over the four consecutive vertex pairs.'},
   'sol': {'ru': 'Сумма перекрёстных произведений: 0 + (5&nbsp;&middot;&nbsp;4 &minus; 6&nbsp;&middot;&nbsp;0) + (6&nbsp;&middot;&nbsp;3 &minus; 1&nbsp;&middot;&nbsp;4) + 0 = 20 + 14 = 34. Площадь 34/2 = <b>17</b>.', 'en': 'The cross-product sum: 0 + (5&nbsp;&middot;&nbsp;4 &minus; 6&nbsp;&middot;&nbsp;0) + (6&nbsp;&middot;&nbsp;3 &minus; 1&nbsp;&middot;&nbsp;4) + 0 = 20 + 14 = 34. Area 34/2 = <b>17</b>.'}},
  {'q': {'ru': 'Точка на оси <var>x</var> равноудалена от точек <var>A</var>(1;&nbsp;2) и <var>B</var>(7;&nbsp;4). Найдите её абсциссу.', 'en': 'A point on the <var>x</var>-axis is equidistant from <var>A</var>(1,&nbsp;2) and <var>B</var>(7,&nbsp;4). Find its <var>x</var>-coordinate.'},
   'hint': {'ru': 'Приравняйте КВАДРАТЫ расстояний от точки (<var>x</var>;&nbsp;0): корни не понадобятся.', 'en': 'Set the SQUARES of the distances from (<var>x</var>,&nbsp;0) equal: no roots needed.'},
   'sol': {'ru': '(<var>x</var> &minus; 1)<sup>2</sup> + 4 = (<var>x</var> &minus; 7)<sup>2</sup> + 16: &minus;2<var>x</var> + 5 = &minus;14<var>x</var> + 65, откуда 12<var>x</var> = 60 и <var>x</var> = <b>5</b>. Проверка: обе дистанции &radic;20.', 'en': '(<var>x</var> &minus; 1)<sup>2</sup> + 4 = (<var>x</var> &minus; 7)<sup>2</sup> + 16: &minus;2<var>x</var> + 5 = &minus;14<var>x</var> + 65, so 12<var>x</var> = 60 and <var>x</var> = <b>5</b>. Check: both distances are &radic;20.'}},
 ],
 'answers': {'ru': '10 · (3; 2) · 3 · 6 · (0; 3) · 4 · 17 · 5', 'en': '10, (3, 2), 3, 6, (0, 3), 4, 17, 5'},
 'routing': {'ru': 'Норма &mdash; 6 из 8. Ошибки в 1&ndash;2 и 8 &mdash; &laquo;расстояние и середина&raquo;; в 3&ndash;5 &mdash; &laquo;прямые&raquo;; в 6 &mdash; &laquo;окружность&raquo;; в 7 &mdash; &laquo;шнуровка&raquo;.',
             'en': 'Mastery bar: 6 of 8. For mistakes in 1&ndash;2 and 8, reread &ldquo;distance and midpoint&rdquo;; for 3&ndash;5, &ldquo;lines&rdquo;; for 6, &ldquo;circles&rdquo;; for 7, &ldquo;Shoelace&rdquo;.'},
}

L26 = {
 'id': '2.6', 'anchor': 'u26',
 'title': {'ru': 'Стереометрия-минимум: объёмы, поверхности, развёртки, диагональ',
           'en': 'Minimal Solid Geometry: Volumes, Surfaces, Nets, the Box Diagonal'},
 'theory': {
  'ru': f"""
<p><b>Призма и цилиндр.</b> Всё, что &laquo;вытянуто&raquo; из основания на высоту: объём = площадь основания &times; высота. Цилиндр: <var>V</var> = &pi;<var>r</var><sup>2</sup><var>h</var>, боковая поверхность &mdash; развёрнутый прямоугольник 2&pi;<var>r</var> на <var>h</var>, полная поверхность 2&pi;<var>r</var><var>h</var> + 2&pi;<var>r</var><sup>2</sup>. Куб с ребром <var>a</var>: объём <var>a</var><sup>3</sup>, поверхность 6<var>a</var><sup>2</sup>.</p>
<p><b>Конус, пирамида, шар.</b> Всё &laquo;острое&raquo; берёт треть от своей призмы: <var>V</var> = {F('1','3')}&nbsp;&middot;&nbsp;основание&nbsp;&middot;&nbsp;высота. У конуса радиус, высота и образующая <var>l</var> связаны Пифагором: <var>l</var><sup>2</sup> = <var>r</var><sup>2</sup> + <var>h</var><sup>2</sup>; боковая поверхность &pi;<var>rl</var>. Шар: <var>V</var> = {F('4','3')}&pi;<var>r</var><sup>3</sup>, поверхность 4&pi;<var>r</var><sup>2</sup>.</p>
<div class="frm">Диагональ прямоугольного параллелепипеда <var>a</var>&nbsp;&times;&nbsp;<var>b</var>&nbsp;&times;&nbsp;<var>c</var>: <b><var>d</var> = &radic;(<var>a</var><sup>2</sup> + <var>b</var><sup>2</sup> + <var>c</var><sup>2</sup>)</b>. Куб: <var>d</var> = <var>a</var>&radic;3.</div>
<p><b>Развёртки.</b> Боковая поверхность цилиндра разворачивается в прямоугольник со сторонами 2&pi;<var>r</var> и <var>h</var>; боковая поверхность конуса &mdash; в сектор радиуса <var>l</var>, длина дуги которого равна 2&pi;<var>r</var>. Кратчайший путь по поверхности ищется на развёртке отрезком &mdash; в объёме он выглядит кривым, на развёртке он прямой.</p>
<p><b>Диагональ и уровень воды.</b> Диагональ параллелепипеда &mdash; двойной Пифагор одной формулой. Задачи о погружении и переливании держатся на одном законе: объём не исчезает. Тело, полностью ушедшее под воду в цилиндре, поднимает уровень ровно на свой объём, делённый на площадь основания.</p>""",
  'en': f"""
<p><b>Prism and cylinder.</b> Anything &ldquo;extruded&rdquo; from a base along a height: volume = base area &times; height. Cylinder: <var>V</var> = &pi;<var>r</var><sup>2</sup><var>h</var>, the lateral surface unrolls into a 2&pi;<var>r</var>-by-<var>h</var> rectangle, and the total surface is 2&pi;<var>r</var><var>h</var> + 2&pi;<var>r</var><sup>2</sup>. A cube of edge <var>a</var>: volume <var>a</var><sup>3</sup>, surface 6<var>a</var><sup>2</sup>.</p>
<p><b>Cone, pyramid, sphere.</b> Everything &ldquo;pointed&rdquo; takes a third of its prism: <var>V</var> = {F('1','3')}&nbsp;&middot;&nbsp;base&nbsp;&middot;&nbsp;height. In a cone, the radius, height, and slant <var>l</var> are tied by Pythagoras: <var>l</var><sup>2</sup> = <var>r</var><sup>2</sup> + <var>h</var><sup>2</sup>; the lateral surface is &pi;<var>rl</var>. Sphere: <var>V</var> = {F('4','3')}&pi;<var>r</var><sup>3</sup>, surface 4&pi;<var>r</var><sup>2</sup>.</p>
<div class="frm">Diagonal of an <var>a</var>&nbsp;&times;&nbsp;<var>b</var>&nbsp;&times;&nbsp;<var>c</var> box: <b><var>d</var> = &radic;(<var>a</var><sup>2</sup> + <var>b</var><sup>2</sup> + <var>c</var><sup>2</sup>)</b>. Cube: <var>d</var> = <var>a</var>&radic;3.</div>
<p><b>Nets.</b> A cylinder&rsquo;s lateral surface unrolls into a rectangle with sides 2&pi;<var>r</var> and <var>h</var>; a cone&rsquo;s lateral surface unrolls into a sector of radius <var>l</var> whose arc length is 2&pi;<var>r</var>. The shortest path along a surface is a straight segment on the net &mdash; it looks curved in 3D, but it is straight once unrolled.</p>
<p><b>The diagonal and water levels.</b> The box diagonal is a double Pythagoras in one formula. Submersion and pouring problems rest on one law: volume does not vanish. A body fully submerged in a cylinder raises the level by exactly its volume divided by the base area.</p>"""},
 'worked': [
  {'tag': {'ru': 'Разбор 1 · диагональ', 'en': 'Example 1 · box diagonal'},
   'q': {'ru': 'Найдите диагональ прямоугольного параллелепипеда с рёбрами 3, 4 и 12.',
         'en': 'Find the diagonal of a 3-by-4-by-12 rectangular box.'},
   'sol': {'ru': '<var>d</var> = &radic;(9 + 16 + 144) = &radic;169 = <b>13</b>. Внутри спрятаны две тройки: 3-4-5 по дну и 5-12-13 в вертикальном сечении &mdash; формула просто склеивает два Пифагора в один.',
          'en': '<var>d</var> = &radic;(9 + 16 + 144) = &radic;169 = <b>13</b>. Two triples hide inside: 3-4-5 across the bottom and 5-12-13 in the vertical cross-section &mdash; the formula just glues two Pythagorean steps into one.'}},
  {'tag': {'ru': 'Разбор 2 · цилиндр', 'en': 'Example 2 · cylinder'},
   'q': {'ru': 'Радиус цилиндра равен 3, высота равна 5. Найдите объём и полную поверхность.',
         'en': 'A cylinder has radius 3 and height 5. Find its volume and total surface area.'},
   'sol': {'ru': 'Объём: &pi;&nbsp;&middot;&nbsp;9&nbsp;&middot;&nbsp;5 = <b>45&pi;</b>. Поверхность: бок 2&pi;&nbsp;&middot;&nbsp;3&nbsp;&middot;&nbsp;5 = 30&pi; плюс две крышки 2&nbsp;&middot;&nbsp;9&pi; = 18&pi;, итого <b>48&pi;</b>. Ответы на AMC часто оставляют с &pi; &mdash; не спешите умножать на 3,14.',
          'en': 'Volume: &pi;&nbsp;&middot;&nbsp;9&nbsp;&middot;&nbsp;5 = <b>45&pi;</b>. Surface: the side 2&pi;&nbsp;&middot;&nbsp;3&nbsp;&middot;&nbsp;5 = 30&pi; plus two lids 2&nbsp;&middot;&nbsp;9&pi; = 18&pi;, total <b>48&pi;</b>. AMC answers usually stay in terms of &pi; &mdash; do not rush to multiply by 3.14.'}},
  {'tag': {'ru': 'Разбор 3 · конус', 'en': 'Example 3 · cone'},
   'q': {'ru': 'Радиус основания конуса равен 6, высота равна 8. Найдите объём и боковую поверхность.',
         'en': 'A cone has base radius 6 and height 8. Find its volume and lateral surface area.'},
   'sol': {'ru': 'Объём: (1/3)&pi;&nbsp;&middot;&nbsp;36&nbsp;&middot;&nbsp;8 = <b>96&pi;</b>. Образующая: &radic;(36 + 64) = 10 (тройка 6-8-10), боковая поверхность &pi;<var>rl</var> = <b>60&pi;</b>. Ловушка &mdash; подставить в &pi;<var>rl</var> высоту вместо образующей: в формуле поверхности живёт именно <var>l</var>.',
          'en': 'Volume: (1/3)&pi;&nbsp;&middot;&nbsp;36&nbsp;&middot;&nbsp;8 = <b>96&pi;</b>. Slant: &radic;(36 + 64) = 10 (the 6-8-10 triple), so the lateral surface is &pi;<var>rl</var> = <b>60&pi;</b>. The trap is plugging the height into &pi;<var>rl</var> instead of the slant: the surface formula runs on <var>l</var>.'}},
  {'tag': {'ru': 'Разбор 4 · шар', 'en': 'Example 4 · sphere'},
   'q': {'ru': 'Радиус шара равен 3. Найдите объём и площадь поверхности.',
         'en': 'A sphere has radius 3. Find its volume and surface area.'},
   'sol': {'ru': 'Объём: (4/3)&pi;&nbsp;&middot;&nbsp;27 = <b>36&pi;</b>. Поверхность: 4&pi;&nbsp;&middot;&nbsp;9 = <b>36&pi;</b>. Числа совпали &mdash; это особенность именно радиуса 3, а не закон природы. Держите обе формулы раздельно: (4/3)&pi;<var>r</var><sup>3</sup> и 4&pi;<var>r</var><sup>2</sup> путают чаще всех остальных пар.',
          'en': 'Volume: (4/3)&pi;&nbsp;&middot;&nbsp;27 = <b>36&pi;</b>. Surface: 4&pi;&nbsp;&middot;&nbsp;9 = <b>36&pi;</b>. The numbers match &mdash; a quirk of radius 3, not a law of nature. Keep the formulas separate: (4/3)&pi;<var>r</var><sup>3</sup> and 4&pi;<var>r</var><sup>2</sup> get confused more than any other pair.'}},
 ],
 'selfp': [
  {'q': {'ru': 'Ребро куба равно 4. Найдите площадь его поверхности.', 'en': 'A cube has edge 4. Find its surface area.'},
   'hint': {'ru': 'Шесть одинаковых граней.', 'en': 'Six identical faces.'},
   'sol': {'ru': '6&nbsp;&middot;&nbsp;16 = <b>96</b>.', 'en': '6&nbsp;&middot;&nbsp;16 = <b>96</b>.'}},
  {'q': {'ru': 'Найдите диагональ прямоугольного параллелепипеда с рёбрами 2, 3 и 6.', 'en': 'Find the diagonal of a 2-by-3-by-6 rectangular box.'},
   'hint': {'ru': 'Сумма квадратов рёбер.', 'en': 'The sum of the squares of the edges.'},
   'sol': {'ru': '&radic;(4 + 9 + 36) = &radic;49 = <b>7</b>.', 'en': '&radic;(4 + 9 + 36) = &radic;49 = <b>7</b>.'}},
  {'q': {'ru': 'Прямая призма: в основании прямоугольный треугольник с катетами 3 и 4, высота призмы равна 10. Найдите площадь полной поверхности.', 'en': 'A right prism has a right-triangle base with legs 3 and 4, and the prism&rsquo;s height is 10. Find the total surface area.'},
   'hint': {'ru': 'Гипотенуза основания &mdash; 5. Боковая поверхность призмы = периметр основания &times; высота.', 'en': 'The base hypotenuse is 5. The lateral surface of a prism = base perimeter &times; height.'},
   'sol': {'ru': 'Основание: 3-4-5, площадь 6, периметр 12. Полная поверхность: 2&nbsp;&middot;&nbsp;6 + 12&nbsp;&middot;&nbsp;10 = <b>132</b>.', 'en': 'The base is a 3-4-5 triangle: area 6, perimeter 12. Total surface: 2&nbsp;&middot;&nbsp;6 + 12&nbsp;&middot;&nbsp;10 = <b>132</b>.'}},
  {'q': {'ru': 'Площадь поверхности шара равна 100&pi;. Найдите его объём.', 'en': 'A sphere has surface area 100&pi;. Find its volume.'},
   'hint': {'ru': 'Сначала радиус из 4&pi;<var>r</var><sup>2</sup> = 100&pi;.', 'en': 'First get the radius from 4&pi;<var>r</var><sup>2</sup> = 100&pi;.'},
   'sol': {'ru': '<var>r</var> = 5: объём (4/3)&pi;&nbsp;&middot;&nbsp;125 = <b>500&pi;/3</b>.', 'en': '<var>r</var> = 5: volume (4/3)&pi;&nbsp;&middot;&nbsp;125 = <b>500&pi;/3</b>.'}},
  {'q': {'ru': 'Радиус основания конуса равен 5, образующая равна 13. Найдите объём.', 'en': 'A cone has base radius 5 and slant height 13. Find its volume.'},
   'hint': {'ru': 'Высота &mdash; из тройки 5-12-13.', 'en': 'The height comes from the 5-12-13 triple.'},
   'sol': {'ru': '<var>h</var> = 12: объём (1/3)&pi;&nbsp;&middot;&nbsp;25&nbsp;&middot;&nbsp;12 = <b>100&pi;</b>.', 'en': '<var>h</var> = 12: volume (1/3)&pi;&nbsp;&middot;&nbsp;25&nbsp;&middot;&nbsp;12 = <b>100&pi;</b>.'}},
  {'q': {'ru': 'Объём куба равен 27. Найдите его диагональ (от вершины до противоположной вершины).', 'en': 'A cube has volume 27. Find its space diagonal (vertex to opposite vertex).'},
   'hint': {'ru': 'Сначала ребро; диагональ куба = ребро&nbsp;&middot;&nbsp;&radic;3.', 'en': 'First the edge; the cube diagonal = edge&nbsp;&middot;&nbsp;&radic;3.'},
   'sol': {'ru': 'Ребро 3: диагональ <b>3&radic;3</b>.', 'en': 'Edge 3: diagonal <b>3&radic;3</b>.'}},
  {'q': {'ru': 'Боковую поверхность цилиндра с радиусом 4 и высотой 10 развернули в прямоугольник. Найдите его площадь.', 'en': 'The lateral surface of a cylinder with radius 4 and height 10 is unrolled into a rectangle. Find its area.'},
   'hint': {'ru': 'Стороны прямоугольника: длина окружности и высота.', 'en': 'The rectangle&rsquo;s sides: the base circumference and the height.'},
   'sol': {'ru': '2&pi;&nbsp;&middot;&nbsp;4&nbsp;&middot;&nbsp;10 = <b>80&pi;</b>.', 'en': '2&pi;&nbsp;&middot;&nbsp;4&nbsp;&middot;&nbsp;10 = <b>80&pi;</b>.'}},
  {'q': {'ru': 'В цилиндрический бак с радиусом основания 6 полностью погрузили шар радиуса 3 (вода накрыла его целиком и не перелилась). На сколько поднялся уровень воды?', 'en': 'A sphere of radius 3 is fully submerged in a cylindrical tank of base radius 6 (the water covers it completely and does not overflow). By how much does the water level rise?'},
   'hint': {'ru': 'Объём шара распределяется по площади основания цилиндра.', 'en': 'The sphere&rsquo;s volume spreads over the cylinder&rsquo;s base area.'},
   'sol': {'ru': 'Объём шара 36&pi;, площадь основания 36&pi;: подъём 36&pi;/36&pi; = <b>1</b>.', 'en': 'Sphere volume 36&pi;, base area 36&pi;: the rise is 36&pi;/36&pi; = <b>1</b>.'}},
 ],
 'answers': {'ru': '96 · 7 · 132 · 500π/3 · 100π · 3√3 · 80π · 1', 'en': '96, 7, 132, 500&pi;/3, 100&pi;, 3&radic;3, 80&pi;, 1'},
 'routing': {'ru': 'Норма &mdash; 6 из 8. Ошибки в 1, 3 и 8 &mdash; &laquo;призма и цилиндр&raquo;; в 4&ndash;5 &mdash; &laquo;конус, пирамида, шар&raquo;; во 2 и 6 &mdash; &laquo;диагональ&raquo;; в 7 &mdash; &laquo;развёртки&raquo;.',
             'en': 'Mastery bar: 6 of 8. For mistakes in 1, 3, and 8, reread &ldquo;prism and cylinder&rdquo;; for 4&ndash;5, &ldquo;cone, pyramid, sphere&rdquo;; for 2 and 6, &ldquo;the diagonal&rdquo;; for 7, &ldquo;nets&rdquo;.'},
}
