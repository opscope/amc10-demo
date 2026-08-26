# -*- coding: utf-8 -*-
"""Блок 3 «Теория чисел»: уроки 3.1–3.2, RU+EN. HTML-фрагменты в нотации страницы курса."""

def F(a, b):
    return f'<span class="frac"><span>{a}</span><span>{b}</span></span>'

L31 = {
 'id': '3.1', 'anchor': 'u31',
 'title': {'ru': 'Делимость, разложение на простые, число и сумма делителей',
           'en': 'Divisibility, Prime Factorization, Number and Sum of Divisors'},
 'theory': {
  'ru': f"""
<p><b>Признаки делимости.</b> На 3 и 9 &mdash; по сумме цифр; на 11 &mdash; по знакопеременной сумме цифр (справа налево, с чередованием знаков); на 4 &mdash; по двум последним цифрам, на 8 &mdash; по трём. Составные признаки собираются из взаимно простых частей: делимость на 12 &mdash; это делимость на 3 <b>и</b> на 4 одновременно; проверить только одну часть &mdash; классическая ошибка.</p>
<p><b>Разложение на простые</b> &mdash; паспорт числа: 720 = 2<sup>4</sup>&nbsp;&middot;&nbsp;3<sup>2</sup>&nbsp;&middot;&nbsp;5. Почти каждый вопрос о делителях, НОД, НОК и степенях читается прямо с показателей. Первый рефлекс в задаче о числе &mdash; разложить его.</p>
<div class="frm">Если <var>n</var> = <var>p</var><sup><var>a</var></sup><var>q</var><sup><var>b</var></sup><var>r</var><sup><var>c</var></sup>&hellip;, то число делителей = (<var>a</var>+1)(<var>b</var>+1)(<var>c</var>+1)&hellip;, а сумма делителей = (1 + <var>p</var> + &hellip; + <var>p</var><sup><var>a</var></sup>)(1 + <var>q</var> + &hellip; + <var>q</var><sup><var>b</var></sup>)&hellip;, где каждая скобка равна {F('<var>p</var><sup><var>a</var>+1</sup> &minus; 1','<var>p</var> &minus; 1')}.</div>
<p><b>Число делителей.</b> Делитель &mdash; это выбор показателя по каждому простому: от 0 до <var>a</var>, всего <var>a</var>+1 вариантов, и варианты перемножаются. Отсюда же считаются делители с условием: делители-точные квадраты &mdash; это выбор чётных показателей; делители, кратные 6 &mdash; показатели при 2 и 3 не ниже единицы.</p>
<p><b>Сумма делителей</b> &mdash; те же скобки, но с суммой степеней вместо количества. Полезный контроль: у числа делителей нечётное значение бывает только у точных квадратов &mdash; делители разбиваются на пары <var>d</var> и <var>n</var>/<var>d</var>, и лишь квадрат имеет непарный делитель &radic;<var>n</var>.</p>""",
  'en': f"""
<p><b>Divisibility rules.</b> For 3 and 9 &mdash; the digit sum; for 11 &mdash; the alternating digit sum (right to left, alternating signs); for 4 &mdash; the last two digits, for 8 &mdash; the last three. Composite rules are built from coprime parts: divisibility by 12 means divisibility by 3 <b>and</b> by 4 at once; checking only one part is a classic mistake.</p>
<p><b>Prime factorization</b> is a number&rsquo;s passport: 720 = 2<sup>4</sup>&nbsp;&middot;&nbsp;3<sup>2</sup>&nbsp;&middot;&nbsp;5. Nearly every question about divisors, GCD, LCM, or powers is read straight off the exponents. In any problem about a specific number, factoring it is reflex number one.</p>
<div class="frm">If <var>n</var> = <var>p</var><sup><var>a</var></sup><var>q</var><sup><var>b</var></sup><var>r</var><sup><var>c</var></sup>&hellip;, then the number of divisors = (<var>a</var>+1)(<var>b</var>+1)(<var>c</var>+1)&hellip;, and the sum of divisors = (1 + <var>p</var> + &hellip; + <var>p</var><sup><var>a</var></sup>)(1 + <var>q</var> + &hellip; + <var>q</var><sup><var>b</var></sup>)&hellip;, each bracket equal to {F('<var>p</var><sup><var>a</var>+1</sup> &minus; 1','<var>p</var> &minus; 1')}.</div>
<p><b>Number of divisors.</b> A divisor is a choice of exponent for each prime: from 0 to <var>a</var>, that is <var>a</var>+1 options, and the options multiply. Conditional counts work the same way: perfect-square divisors are choices of even exponents; divisors that are multiples of 6 keep the exponents of 2 and 3 at least 1.</p>
<p><b>Sum of divisors</b> &mdash; the same brackets, but with sums of powers instead of counts. A useful check: the number of divisors is odd only for perfect squares &mdash; divisors pair up as <var>d</var> and <var>n</var>/<var>d</var>, and only a square has the unpaired divisor &radic;<var>n</var>.</p>"""},
 'worked': [
  {'tag': {'ru': 'Разбор 1 · признаки', 'en': 'Example 1 · divisibility rules'},
   'q': {'ru': 'При какой цифре <var>a</var> число 4<var>a</var>16 делится на 36?',
         'en': 'For which digit <var>a</var> is the number 4<var>a</var>16 divisible by 36?'},
   'sol': {'ru': '36 = 4&nbsp;&middot;&nbsp;9, части взаимно просты &mdash; проверяем обе. На 4: последние две цифры 16, делятся при любом <var>a</var>. На 9: сумма цифр 4 + <var>a</var> + 1 + 6 = 11 + <var>a</var> должна делиться на 9, значит <var>a</var> = <b>7</b>. Проверка: 4716 / 36 = 131. Ловушка &mdash; проверить только девятку и забыть четвёрку (здесь она бесплатна, но проверить обязаны).',
          'en': '36 = 4&nbsp;&middot;&nbsp;9, the parts are coprime &mdash; check both. By 4: the last two digits are 16, divisible for every <var>a</var>. By 9: the digit sum 4 + <var>a</var> + 1 + 6 = 11 + <var>a</var> must be divisible by 9, so <var>a</var> = <b>7</b>. Check: 4716 / 36 = 131. The trap is checking only the 9 and forgetting the 4 (free here, but you must check it).'}},
  {'tag': {'ru': 'Разбор 2 · число делителей', 'en': 'Example 2 · number of divisors'},
   'q': {'ru': 'Сколько положительных делителей у числа 720?',
         'en': 'How many positive divisors does 720 have?'},
   'sol': {'ru': '720 = 2<sup>4</sup>&nbsp;&middot;&nbsp;3<sup>2</sup>&nbsp;&middot;&nbsp;5. Число делителей: (4+1)(2+1)(1+1) = 5&nbsp;&middot;&nbsp;3&nbsp;&middot;&nbsp;2 = <b>30</b>. Ловушка &mdash; перемножить сами показатели (4&middot;2&middot;1 = 8): забытые &laquo;+1&raquo; &mdash; самая частая ошибка формулы. Показатель 0 &mdash; тоже выбор.',
          'en': '720 = 2<sup>4</sup>&nbsp;&middot;&nbsp;3<sup>2</sup>&nbsp;&middot;&nbsp;5. Number of divisors: (4+1)(2+1)(1+1) = 5&nbsp;&middot;&nbsp;3&nbsp;&middot;&nbsp;2 = <b>30</b>. The trap is multiplying the exponents themselves (4&middot;2&middot;1 = 8): forgetting the &ldquo;+1&rdquo; is the most common error with this formula. Exponent 0 is a choice too.'}},
  {'tag': {'ru': 'Разбор 3 · сумма делителей', 'en': 'Example 3 · sum of divisors'},
   'q': {'ru': 'Найдите сумму всех положительных делителей числа 200.',
         'en': 'Find the sum of all positive divisors of 200.'},
   'sol': {'ru': '200 = 2<sup>3</sup>&nbsp;&middot;&nbsp;5<sup>2</sup>. Сумма = (1 + 2 + 4 + 8)(1 + 5 + 25) = 15&nbsp;&middot;&nbsp;31 = <b>465</b>. Скобки перемножаются, потому что каждый делитель &mdash; ровно одно произведение &laquo;степень двойки на степень пятёрки&raquo;, и раскрытие скобок перечисляет их все по одному разу.',
          'en': '200 = 2<sup>3</sup>&nbsp;&middot;&nbsp;5<sup>2</sup>. Sum = (1 + 2 + 4 + 8)(1 + 5 + 25) = 15&nbsp;&middot;&nbsp;31 = <b>465</b>. The brackets multiply because every divisor is exactly one product &ldquo;power of 2 times power of 5&rdquo;, and expanding the brackets lists each of them exactly once.'}},
  {'tag': {'ru': 'Разбор 4 · делители с условием', 'en': 'Example 4 · divisors with a condition'},
   'q': {'ru': 'Сколько делителей числа 360 кратны 6?',
         'en': 'How many divisors of 360 are multiples of 6?'},
   'sol': {'ru': '360 = 2<sup>3</sup>&nbsp;&middot;&nbsp;3<sup>2</sup>&nbsp;&middot;&nbsp;5. Делитель кратен 6, когда показатель при 2 равен 1, 2 или 3 (три варианта), при 3 &mdash; 1 или 2 (два), при 5 &mdash; 0 или 1 (два): 3&nbsp;&middot;&nbsp;2&nbsp;&middot;&nbsp;2 = <b>12</b>. Эквивалентный ход: делители, кратные 6, &mdash; это 6<var>d</var>, где <var>d</var> пробегает делители числа 360/6 = 60, а их (2+1)(1+1)(1+1) = 12.',
          'en': '360 = 2<sup>3</sup>&nbsp;&middot;&nbsp;3<sup>2</sup>&nbsp;&middot;&nbsp;5. A divisor is a multiple of 6 when the exponent of 2 is 1, 2, or 3 (three options), of 3 &mdash; 1 or 2 (two), of 5 &mdash; 0 or 1 (two): 3&nbsp;&middot;&nbsp;2&nbsp;&middot;&nbsp;2 = <b>12</b>. Equivalent move: multiples of 6 among the divisors are 6<var>d</var> where <var>d</var> runs over divisors of 360/6 = 60, and there are (2+1)(1+1)(1+1) = 12 of those.'}},
 ],
 'selfp': [
  {'q': {'ru': 'При какой цифре <var>a</var> число 73<var>a</var>5 делится на 9?', 'en': 'For which digit <var>a</var> is the number 73<var>a</var>5 divisible by 9?'},
   'hint': {'ru': 'Сумма цифр должна делиться на 9.', 'en': 'The digit sum must be divisible by 9.'},
   'sol': {'ru': '7 + 3 + 5 = 15; нужно 15 + <var>a</var> &equiv; 0 (mod 9), значит <var>a</var> = <b>3</b> (сумма 18).', 'en': '7 + 3 + 5 = 15; we need 15 + <var>a</var> &equiv; 0 (mod 9), so <var>a</var> = <b>3</b> (sum 18).'}},
  {'q': {'ru': 'При какой цифре <var>a</var> число 6<var>a</var>352 делится на 11?', 'en': 'For which digit <var>a</var> is the number 6<var>a</var>352 divisible by 11?'},
   'hint': {'ru': 'Знакопеременная сумма цифр справа налево: 2 &minus; 5 + 3 &minus; <var>a</var> + 6.', 'en': 'Alternating digit sum from the right: 2 &minus; 5 + 3 &minus; <var>a</var> + 6.'},
   'sol': {'ru': '2 &minus; 5 + 3 &minus; <var>a</var> + 6 = 6 &minus; <var>a</var> должно делиться на 11: <var>a</var> = <b>6</b>. Проверка: 66&nbsp;352 = 11&nbsp;&middot;&nbsp;6032.', 'en': '2 &minus; 5 + 3 &minus; <var>a</var> + 6 = 6 &minus; <var>a</var> must be divisible by 11: <var>a</var> = <b>6</b>. Check: 66,352 = 11&nbsp;&middot;&nbsp;6032.'}},
  {'q': {'ru': 'Сколько положительных делителей у числа 200?', 'en': 'How many positive divisors does 200 have?'},
   'hint': {'ru': 'Разложите: 200 = 2<sup>3</sup>&nbsp;&middot;&nbsp;5<sup>2</sup>.', 'en': 'Factor: 200 = 2<sup>3</sup>&nbsp;&middot;&nbsp;5<sup>2</sup>.'},
   'sol': {'ru': '(3+1)(2+1) = <b>12</b>.', 'en': '(3+1)(2+1) = <b>12</b>.'}},
  {'q': {'ru': 'Найдите сумму всех положительных делителей числа 72.', 'en': 'Find the sum of all positive divisors of 72.'},
   'hint': {'ru': '72 = 2<sup>3</sup>&nbsp;&middot;&nbsp;3<sup>2</sup>; перемножьте скобки-суммы.', 'en': '72 = 2<sup>3</sup>&nbsp;&middot;&nbsp;3<sup>2</sup>; multiply the bracket sums.'},
   'sol': {'ru': '(1 + 2 + 4 + 8)(1 + 3 + 9) = 15&nbsp;&middot;&nbsp;13 = <b>195</b>.', 'en': '(1 + 2 + 4 + 8)(1 + 3 + 9) = 15&nbsp;&middot;&nbsp;13 = <b>195</b>.'}},
  {'q': {'ru': 'Сколько чётных делителей у числа 2<sup>5</sup>&nbsp;&middot;&nbsp;3<sup>4</sup>?', 'en': 'How many even divisors does 2<sup>5</sup>&nbsp;&middot;&nbsp;3<sup>4</sup> have?'},
   'hint': {'ru': 'Чётный делитель &mdash; показатель при 2 не меньше 1. Или: все минус нечётные.', 'en': 'An even divisor has exponent of 2 at least 1. Or: all minus the odd ones.'},
   'sol': {'ru': 'Всего делителей 6&nbsp;&middot;&nbsp;5 = 30, нечётных (степень двойки 0) &mdash; 5. Чётных 30 &minus; 5 = <b>25</b>.', 'en': 'Total divisors: 6&nbsp;&middot;&nbsp;5 = 30; odd ones (exponent of 2 equal to 0): 5. Even: 30 &minus; 5 = <b>25</b>.'}},
  {'q': {'ru': 'Найдите наименьшее натуральное число, у которого ровно 10 делителей.', 'en': 'Find the least positive integer with exactly 10 divisors.'},
   'hint': {'ru': '10 = 10 или 2&nbsp;&middot;&nbsp;5: наборы показателей (9) или (4, 1).', 'en': '10 = 10 or 2&nbsp;&middot;&nbsp;5: exponent patterns (9) or (4, 1).'},
   'sol': {'ru': 'Кандидаты: 2<sup>9</sup> = 512 и 2<sup>4</sup>&nbsp;&middot;&nbsp;3 = 48. Большие показатели вешаем на маленькие простые: ответ <b>48</b>.', 'en': 'Candidates: 2<sup>9</sup> = 512 and 2<sup>4</sup>&nbsp;&middot;&nbsp;3 = 48. Put the large exponents on the small primes: the answer is <b>48</b>.'}},
  {'q': {'ru': 'Сколько делителей числа 3600 являются точными квадратами?', 'en': 'How many divisors of 3600 are perfect squares?'},
   'hint': {'ru': '3600 = 2<sup>4</sup>&nbsp;&middot;&nbsp;3<sup>2</sup>&nbsp;&middot;&nbsp;5<sup>2</sup>; у квадрата все показатели чётные.', 'en': '3600 = 2<sup>4</sup>&nbsp;&middot;&nbsp;3<sup>2</sup>&nbsp;&middot;&nbsp;5<sup>2</sup>; a square has all exponents even.'},
   'sol': {'ru': 'Чётные показатели: при 2 &mdash; 0, 2, 4 (три варианта), при 3 и при 5 &mdash; 0 или 2 (по два): 3&nbsp;&middot;&nbsp;2&nbsp;&middot;&nbsp;2 = <b>12</b>.', 'en': 'Even exponents: for 2 &mdash; 0, 2, 4 (three options), for 3 and for 5 &mdash; 0 or 2 (two each): 3&nbsp;&middot;&nbsp;2&nbsp;&middot;&nbsp;2 = <b>12</b>.'}},
  {'q': {'ru': 'У скольких чисел от 1 до 60 нечётное число делителей?', 'en': 'How many integers from 1 to 60 have an odd number of divisors?'},
   'hint': {'ru': 'Делители разбиваются на пары <var>d</var> и <var>n</var>/<var>d</var>. Когда пара склеивается в один делитель?', 'en': 'Divisors pair up as <var>d</var> and <var>n</var>/<var>d</var>. When does a pair collapse into one divisor?'},
   'sol': {'ru': 'Нечётное число делителей &mdash; только у точных квадратов. От 1 до 60: 1, 4, 9, 16, 25, 36, 49 &mdash; <b>7 чисел</b>.', 'en': 'Only perfect squares have an odd number of divisors. From 1 to 60: 1, 4, 9, 16, 25, 36, 49 &mdash; <b>7 numbers</b>.'}},
 ],
 'answers': {'ru': '3 · 6 · 12 · 195 · 25 · 48 · 12 · 7', 'en': '3, 6, 12, 195, 25, 48, 12, 7'},
 'routing': {'ru': 'Норма урока &mdash; 6 из 8. Ошибки в 1&ndash;2 &mdash; перечитать &laquo;признаки делимости&raquo;; в 3 и 6 &mdash; &laquo;число делителей&raquo;; в 4 &mdash; &laquo;сумма делителей&raquo;; в 5, 7&ndash;8 &mdash; &laquo;делители с условием&raquo; и абзац о квадратах.',
             'en': 'Mastery bar: 6 of 8. For mistakes in 1&ndash;2, reread &ldquo;divisibility rules&rdquo;; for 3 and 6, &ldquo;number of divisors&rdquo;; for 4, &ldquo;sum of divisors&rdquo;; for 5 and 7&ndash;8, conditional divisor counts and the paragraph on squares.'},
}

L32 = {
 'id': '3.2', 'anchor': 'u32',
 'title': {'ru': 'НОД и НОК, алгоритм Евклида, взаимная простота',
           'en': 'GCD and LCM, the Euclidean Algorithm, Coprimality'},
 'theory': {
  'ru': f"""
<p><b>Через разложение.</b> НОД берёт по каждому простому <b>меньший</b> показатель, НОК &mdash; <b>больший</b>: для 2<sup>3</sup>&middot;3<sup>2</sup>&middot;5 и 2<sup>2</sup>&middot;3<sup>3</sup>&middot;7 НОД = 2<sup>2</sup>&middot;3<sup>2</sup> = 36, НОК = 2<sup>3</sup>&middot;3<sup>3</sup>&middot;5&middot;7 = 7560. Так как min + max = сумма показателей, получаем главное тождество ниже.</p>
<div class="frm">НОД(<var>a</var>,&nbsp;<var>b</var>)&nbsp;&middot;&nbsp;НОК(<var>a</var>,&nbsp;<var>b</var>) = <var>a</var>&nbsp;&middot;&nbsp;<var>b</var>. &nbsp;Евклид: НОД(<var>a</var>,&nbsp;<var>b</var>) = НОД(<var>b</var>,&nbsp;<var>a</var> mod <var>b</var>).</div>
<p><b>Алгоритм Евклида</b> &mdash; когда раскладывать долго: заменяем большее число остатком от деления на меньшее и повторяем; последний ненулевой остаток и есть НОД. Работает и с буквами: НОД(<var>a</var>,&nbsp;<var>b</var>) = НОД(<var>b</var>,&nbsp;<var>a</var> &minus; <var>kb</var>) для любого целого <var>k</var> &mdash; так добиваются НОД выражений вроде 6<var>n</var>&nbsp;+&nbsp;5 и 3<var>n</var>&nbsp;+&nbsp;2.</p>
<p><b>Взаимная простота:</b> НОД = 1, общих простых нет. Соседние числа <var>n</var> и <var>n</var>&nbsp;+&nbsp;1 всегда взаимно просты. Стандартная замена в задачах: <var>a</var> = <var>gx</var>, <var>b</var> = <var>gy</var>, где <var>g</var> &mdash; НОД и НОД(<var>x</var>,&nbsp;<var>y</var>) = 1; тогда НОК = <var>gxy</var>.</p>
<p><b>Смысловой словарь.</b> &laquo;Разрезать на одинаковые наибольшие куски&raquo;, &laquo;поровну без остатка&raquo; &mdash; НОД. &laquo;Снова совпадут, встретятся, зажгутся вместе&raquo;, &laquo;наименьшее общее кратное расписаний&raquo; &mdash; НОК. Перепутать их &mdash; ловушка номер один в текстовых задачах; НОД не больше каждого из чисел, НОК не меньше.</p>""",
  'en': f"""
<p><b>Via factorization.</b> The GCD takes the <b>smaller</b> exponent of each prime, the LCM the <b>larger</b>: for 2<sup>3</sup>&middot;3<sup>2</sup>&middot;5 and 2<sup>2</sup>&middot;3<sup>3</sup>&middot;7, GCD = 2<sup>2</sup>&middot;3<sup>2</sup> = 36 and LCM = 2<sup>3</sup>&middot;3<sup>3</sup>&middot;5&middot;7 = 7560. Since min + max = sum of the exponents, we get the key identity below.</p>
<div class="frm">gcd(<var>a</var>,&nbsp;<var>b</var>)&nbsp;&middot;&nbsp;lcm(<var>a</var>,&nbsp;<var>b</var>) = <var>a</var>&nbsp;&middot;&nbsp;<var>b</var>. &nbsp;Euclid: gcd(<var>a</var>,&nbsp;<var>b</var>) = gcd(<var>b</var>,&nbsp;<var>a</var> mod <var>b</var>).</div>
<p><b>The Euclidean algorithm</b> &mdash; for when factoring is slow: replace the larger number by its remainder upon division by the smaller, and repeat; the last nonzero remainder is the GCD. It works with letters too: gcd(<var>a</var>,&nbsp;<var>b</var>) = gcd(<var>b</var>,&nbsp;<var>a</var> &minus; <var>kb</var>) for any integer <var>k</var> &mdash; that is how you tame gcds of expressions like 6<var>n</var>&nbsp;+&nbsp;5 and 3<var>n</var>&nbsp;+&nbsp;2.</p>
<p><b>Coprimality:</b> gcd = 1, no common primes. Consecutive integers <var>n</var> and <var>n</var>&nbsp;+&nbsp;1 are always coprime. The standard substitution: <var>a</var> = <var>gx</var>, <var>b</var> = <var>gy</var>, where <var>g</var> is the gcd and gcd(<var>x</var>,&nbsp;<var>y</var>) = 1; then lcm = <var>gxy</var>.</p>
<p><b>Word-problem dictionary.</b> &ldquo;Cut into equal largest pieces&rdquo;, &ldquo;share evenly with nothing left&rdquo; &mdash; GCD. &ldquo;Meet again, flash together, coincide&rdquo;, &ldquo;the schedules line up&rdquo; &mdash; LCM. Mixing them up is trap number one in word problems; the GCD is at most each number, the LCM at least.</p>"""},
 'worked': [
  {'tag': {'ru': 'Разбор 1 · алгоритм Евклида', 'en': 'Example 1 · Euclidean algorithm'},
   'q': {'ru': 'Найдите НОД(1071,&nbsp;462).',
         'en': 'Find gcd(1071,&nbsp;462).'},
   'sol': {'ru': '1071 = 2&nbsp;&middot;&nbsp;462 + 147; далее 462 = 3&nbsp;&middot;&nbsp;147 + 21; далее 147 = 7&nbsp;&middot;&nbsp;21 + 0. Последний ненулевой остаток: НОД = <b>21</b>. Три строки вместо разложения на простые &mdash; на больших числах Евклид всегда быстрее.',
          'en': '1071 = 2&nbsp;&middot;&nbsp;462 + 147; then 462 = 3&nbsp;&middot;&nbsp;147 + 21; then 147 = 7&nbsp;&middot;&nbsp;21 + 0. The last nonzero remainder: gcd = <b>21</b>. Three lines instead of factoring &mdash; on large numbers Euclid is always faster.'}},
  {'tag': {'ru': 'Разбор 2 · gcd&middot;lcm = ab', 'en': 'Example 2 · gcd&middot;lcm = ab'},
   'q': {'ru': 'НОД двух чисел равен 6, НОК равен 180, одно из чисел &mdash; 30. Найдите второе.',
         'en': 'Two numbers have gcd 6 and lcm 180; one of the numbers is 30. Find the other.'},
   'sol': {'ru': 'Произведение чисел равно НОД&nbsp;&middot;&nbsp;НОК = 6&nbsp;&middot;&nbsp;180 = 1080. Второе число: 1080 / 30 = <b>36</b>. Проверка: НОД(30,&nbsp;36) = 6, НОК = 180. Тождество избавляет от перебора полностью.',
          'en': 'The product of the numbers equals gcd&nbsp;&middot;&nbsp;lcm = 6&nbsp;&middot;&nbsp;180 = 1080. The other number: 1080 / 30 = <b>36</b>. Check: gcd(30,&nbsp;36) = 6, lcm = 180. The identity removes all guesswork.'}},
  {'tag': {'ru': 'Разбор 3 · по показателям', 'en': 'Example 3 · via exponents'},
   'q': {'ru': 'Найдите НОД и НОК чисел 2<sup>3</sup>&nbsp;&middot;&nbsp;3<sup>2</sup>&nbsp;&middot;&nbsp;5 и 2<sup>2</sup>&nbsp;&middot;&nbsp;3<sup>3</sup>&nbsp;&middot;&nbsp;7.',
         'en': 'Find the gcd and lcm of 2<sup>3</sup>&nbsp;&middot;&nbsp;3<sup>2</sup>&nbsp;&middot;&nbsp;5 and 2<sup>2</sup>&nbsp;&middot;&nbsp;3<sup>3</sup>&nbsp;&middot;&nbsp;7.'},
   'sol': {'ru': 'По каждому простому: минимум в НОД, максимум в НОК. НОД = 2<sup>2</sup>&nbsp;&middot;&nbsp;3<sup>2</sup> = <b>36</b>; НОК = 2<sup>3</sup>&nbsp;&middot;&nbsp;3<sup>3</sup>&nbsp;&middot;&nbsp;5&nbsp;&middot;&nbsp;7 = <b>7560</b>. Простые 5 и 7 входят в НОК, но не в НОД: минимум их показателей равен нулю. Контроль: 36&nbsp;&middot;&nbsp;7560 = 360&nbsp;&middot;&nbsp;756 &mdash; произведение исходных чисел.',
          'en': 'For each prime: minimum into the gcd, maximum into the lcm. Gcd = 2<sup>2</sup>&nbsp;&middot;&nbsp;3<sup>2</sup> = <b>36</b>; lcm = 2<sup>3</sup>&nbsp;&middot;&nbsp;3<sup>3</sup>&nbsp;&middot;&nbsp;5&nbsp;&middot;&nbsp;7 = <b>7560</b>. The primes 5 and 7 enter the lcm but not the gcd: the minimum of their exponents is zero. Control: 36&nbsp;&middot;&nbsp;7560 = 360&nbsp;&middot;&nbsp;756, the product of the numbers.'}},
  {'tag': {'ru': 'Разбор 4 · текстовая задача', 'en': 'Example 4 · word problem'},
   'q': {'ru': 'Две верёвки, 84 м и 60 м, режут на равные куски наибольшей возможной длины. Сколько получится кусков?',
         'en': 'Two ropes, 84 m and 60 m, are cut into equal pieces of the greatest possible length. How many pieces result?'},
   'sol': {'ru': '&laquo;Равные наибольшие куски&raquo; &mdash; это НОД(84,&nbsp;60) = 12 м. Кусков: 84/12 + 60/12 = 7 + 5 = <b>12</b>. Ловушка &mdash; схватить НОК: 420-метровых кусков из этих верёвок не нарезать. НОД &le; каждой длины &mdash; быстрая проверка на здравый смысл.',
          'en': '&ldquo;Equal largest pieces&rdquo; means gcd(84,&nbsp;60) = 12 m. Pieces: 84/12 + 60/12 = 7 + 5 = <b>12</b>. The trap is grabbing the lcm: you cannot cut 420-meter pieces from these ropes. Gcd &le; each length &mdash; a quick sanity check.'}},
 ],
 'selfp': [
  {'q': {'ru': 'Найдите НОД(48,&nbsp;180).', 'en': 'Find gcd(48,&nbsp;180).'},
   'hint': {'ru': '48 = 2<sup>4</sup>&middot;3, 180 = 2<sup>2</sup>&middot;3<sup>2</sup>&middot;5: минимальные показатели.', 'en': '48 = 2<sup>4</sup>&middot;3, 180 = 2<sup>2</sup>&middot;3<sup>2</sup>&middot;5: take minimal exponents.'},
   'sol': {'ru': '2<sup>2</sup>&nbsp;&middot;&nbsp;3 = <b>12</b>.', 'en': '2<sup>2</sup>&nbsp;&middot;&nbsp;3 = <b>12</b>.'}},
  {'q': {'ru': 'Найдите НОК(24,&nbsp;36).', 'en': 'Find lcm(24,&nbsp;36).'},
   'hint': {'ru': 'Максимальные показатели, или 24&nbsp;&middot;&nbsp;36 / НОД.', 'en': 'Maximal exponents, or 24&nbsp;&middot;&nbsp;36 / gcd.'},
   'sol': {'ru': 'НОД = 12, значит НОК = 24&nbsp;&middot;&nbsp;36 / 12 = <b>72</b>.', 'en': 'Gcd = 12, so lcm = 24&nbsp;&middot;&nbsp;36 / 12 = <b>72</b>.'}},
  {'q': {'ru': 'Алгоритмом Евклида найдите НОД(391,&nbsp;323).', 'en': 'Use the Euclidean algorithm to find gcd(391,&nbsp;323).'},
   'hint': {'ru': '391 = 323 + 68; продолжайте с парой (323,&nbsp;68).', 'en': '391 = 323 + 68; continue with the pair (323,&nbsp;68).'},
   'sol': {'ru': '323 = 4&nbsp;&middot;&nbsp;68 + 51; 68 = 51 + 17; 51 = 3&nbsp;&middot;&nbsp;17. НОД = <b>17</b> (и правда: 391 = 17&middot;23, 323 = 17&middot;19).', 'en': '323 = 4&nbsp;&middot;&nbsp;68 + 51; 68 = 51 + 17; 51 = 3&nbsp;&middot;&nbsp;17. Gcd = <b>17</b> (indeed 391 = 17&middot;23, 323 = 17&middot;19).'}},
  {'q': {'ru': 'НОД двух чисел равен 8, их произведение равно 1920. Найдите их НОК.', 'en': 'Two numbers have gcd 8 and product 1920. Find their lcm.'},
   'hint': {'ru': 'НОД&nbsp;&middot;&nbsp;НОК = произведение чисел.', 'en': 'Gcd&nbsp;&middot;&nbsp;lcm = the product of the numbers.'},
   'sol': {'ru': 'НОК = 1920 / 8 = <b>240</b>.', 'en': 'Lcm = 1920 / 8 = <b>240</b>.'}},
  {'q': {'ru': 'Два автобуса отходят от вокзала каждые 12 и 18 минут; в полдень они отошли вместе. Когда они в следующий раз отойдут одновременно?', 'en': 'Two buses leave a station every 12 and every 18 minutes; at noon they left together. When do they next leave at the same time?'},
   'hint': {'ru': '&laquo;Снова вместе&raquo; &mdash; это НОК.', 'en': '&ldquo;Together again&rdquo; means the lcm.'},
   'sol': {'ru': 'НОК(12,&nbsp;18) = 36: в <b>12:36</b>.', 'en': 'Lcm(12,&nbsp;18) = 36: at <b>12:36</b>.'}},
  {'q': {'ru': 'Сколько чисел от 1 до 100 взаимно просты со 100?', 'en': 'How many integers from 1 to 100 are coprime with 100?'},
   'hint': {'ru': '100 = 2<sup>2</sup>&middot;5<sup>2</sup>: нужны числа, не делящиеся ни на 2, ни на 5. Включение-исключение.', 'en': '100 = 2<sup>2</sup>&middot;5<sup>2</sup>: count numbers divisible by neither 2 nor 5. Inclusion-exclusion.'},
   'sol': {'ru': '100 &minus; 50 (чётные) &minus; 20 (кратные 5) + 10 (кратные 10 вычлись дважды) = <b>40</b>.', 'en': '100 &minus; 50 (even) &minus; 20 (multiples of 5) + 10 (multiples of 10, subtracted twice) = <b>40</b>.'}},
  {'q': {'ru': 'Найдите НОД чисел 6<var>n</var> + 5 и 3<var>n</var> + 2 (для произвольного натурального <var>n</var>).', 'en': 'Find the gcd of 6<var>n</var> + 5 and 3<var>n</var> + 2 (for an arbitrary positive integer <var>n</var>).'},
   'hint': {'ru': 'Евклид с буквами: вычтите из первого удвоенное второе.', 'en': 'Euclid with letters: subtract twice the second from the first.'},
   'sol': {'ru': '(6<var>n</var> + 5) &minus; 2(3<var>n</var> + 2) = 1, значит НОД делит 1: он равен <b>1</b> при любом <var>n</var>.', 'en': '(6<var>n</var> + 5) &minus; 2(3<var>n</var> + 2) = 1, so the gcd divides 1: it equals <b>1</b> for every <var>n</var>.'}},
  {'q': {'ru': 'Сколько упорядоченных пар (<var>a</var>,&nbsp;<var>b</var>) натуральных чисел имеют НОД(<var>a</var>,&nbsp;<var>b</var>) = 5 и НОК(<var>a</var>,&nbsp;<var>b</var>) = 60?', 'en': 'How many ordered pairs (<var>a</var>,&nbsp;<var>b</var>) of positive integers have gcd(<var>a</var>,&nbsp;<var>b</var>) = 5 and lcm(<var>a</var>,&nbsp;<var>b</var>) = 60?'},
   'hint': {'ru': 'Замена <var>a</var> = 5<var>x</var>, <var>b</var> = 5<var>y</var>: НОД(<var>x</var>,&nbsp;<var>y</var>) = 1, НОК(<var>x</var>,&nbsp;<var>y</var>) = 12 = 2<sup>2</sup>&middot;3.', 'en': 'Substitute <var>a</var> = 5<var>x</var>, <var>b</var> = 5<var>y</var>: gcd(<var>x</var>,&nbsp;<var>y</var>) = 1, lcm(<var>x</var>,&nbsp;<var>y</var>) = 12 = 2<sup>2</sup>&middot;3.'},
   'sol': {'ru': 'Из взаимной простоты каждая степень простого (4 и 3) целиком уходит к <var>x</var> или к <var>y</var>: 2&nbsp;&middot;&nbsp;2 = <b>4</b> пары. Это (5,&nbsp;60), (60,&nbsp;5), (15,&nbsp;20), (20,&nbsp;15).', 'en': 'By coprimality each prime power (4 and 3) goes wholly to <var>x</var> or to <var>y</var>: 2&nbsp;&middot;&nbsp;2 = <b>4</b> pairs. They are (5,&nbsp;60), (60,&nbsp;5), (15,&nbsp;20), (20,&nbsp;15).'}},
 ],
 'answers': {'ru': '12 · 72 · 17 · 240 · 12:36 · 40 · 1 · 4', 'en': '12, 72, 17, 240, 12:36, 40, 1, 4'},
 'routing': {'ru': 'Норма &mdash; 6 из 8. Ошибки в 1&ndash;2 &mdash; перечитать &laquo;через разложение&raquo;; в 3 и 7 &mdash; &laquo;алгоритм Евклида&raquo;; в 4 и 8 &mdash; тождество gcd&middot;lcm = ab и замену <var>a</var> = <var>gx</var>; в 5 &mdash; &laquo;смысловой словарь&raquo;; в 6 &mdash; &laquo;взаимная простота&raquo;.',
             'en': 'Mastery bar: 6 of 8. For mistakes in 1&ndash;2, reread &ldquo;via factorization&rdquo;; for 3 and 7, the Euclidean algorithm; for 4 and 8, the identity gcd&middot;lcm = ab and the substitution <var>a</var> = <var>gx</var>; for 5, the word-problem dictionary; for 6, coprimality.'},
}
