# -*- coding: utf-8 -*-
"""Блок 3 «Теория чисел»: уроки 3.3–3.4 + тест Т3 + задачи со звёздочкой, RU+EN."""

def F(a, b):
    return f'<span class="frac"><span>{a}</span><span>{b}</span></span>'

L33 = {
 'id': '3.3', 'anchor': 'u33',
 'title': {'ru': 'Остатки: арифметика по модулю, последние цифры, циклы степеней',
           'en': 'Remainders: Mod Arithmetic, Last Digits, Power Cycles'},
 'theory': {
  'ru': """
<p><b>Арифметика остатков.</b> Запись <var>a</var> &equiv; <var>b</var> (mod <var>n</var>) значит: <var>a</var> и <var>b</var> дают один остаток при делении на <var>n</var>. Остатки можно складывать, вычитать и перемножать ДО вычисления: остаток произведения равен остатку произведения остатков. Гигантское выражение сначала заменяют маленькими остатками, потом считают. Полезно: остаток числа по модулю 9 равен остатку суммы его цифр; по модулю 10 &mdash; последней цифре.</p>
<p><b>Последняя цифра</b> &mdash; это остаток по модулю 10. Последние цифры степеней ходят по кругу: у 7 это 7, 9, 3, 1 с периодом 4; у 2 &mdash; 2, 4, 8, 6; у 3 &mdash; 3, 9, 7, 1. Показатель делим на длину цикла и берём остаток. Ловушка: остаток 0 означает <b>последнюю</b> позицию цикла, а не первую.</p>
<div class="frm">Найти остаток степени: 1)&nbsp;выписать остатки <var>a</var><sup>1</sup>, <var>a</var><sup>2</sup>, <var>a</var><sup>3</sup>, &hellip; (mod <var>n</var>) до повтора; 2)&nbsp;показатель mod длина цикла; 3)&nbsp;остаток 0 &rarr; последний член цикла.</div>
<p><b>Две последние цифры</b> &mdash; остаток по модулю 100. Циклы длиннее, но приёмы те же; отдельно запомните бином: 11<sup><var>n</var></sup> = (10 + 1)<sup><var>n</var></sup> &equiv; 10<var>n</var> + 1 (mod 100) &mdash; все слагаемые со 100 исчезают.</p>
<p><b>Степени по модулю <var>n</var></b> тоже цикличны: у 2 по модулю 7 цикл 2, 4, 1 длины 3; у 3 по модулю 8 уже 3<sup>2</sup> &equiv; 1, и любая чётная степень тройки даёт 1. Если нашли степень с остатком 1 &mdash; всё дальнейшее сворачивается мгновенно. Это главный инструмент задач &laquo;найдите остаток 2<sup>2026</sup>&raquo;.</p>""",
  'en': """
<p><b>Mod arithmetic.</b> Writing <var>a</var> &equiv; <var>b</var> (mod <var>n</var>) means: <var>a</var> and <var>b</var> leave the same remainder upon division by <var>n</var>. Remainders may be added, subtracted, and multiplied BEFORE computing: the remainder of a product is the remainder of the product of remainders. Replace a giant expression by small remainders first, then compute. Useful: a number&rsquo;s remainder mod 9 equals the remainder of its digit sum; mod 10 &mdash; its last digit.</p>
<p><b>The last digit</b> is the remainder mod 10. Last digits of powers run in cycles: for 7 it is 7, 9, 3, 1 with period 4; for 2 &mdash; 2, 4, 8, 6; for 3 &mdash; 3, 9, 7, 1. Divide the exponent by the cycle length and take the remainder. The trap: remainder 0 means the <b>last</b> position of the cycle, not the first.</p>
<div class="frm">Remainder of a power: 1)&nbsp;list the remainders <var>a</var><sup>1</sup>, <var>a</var><sup>2</sup>, <var>a</var><sup>3</sup>, &hellip; (mod <var>n</var>) until they repeat; 2)&nbsp;exponent mod cycle length; 3)&nbsp;remainder 0 &rarr; the last term of the cycle.</div>
<p><b>The last two digits</b> are the remainder mod 100. Cycles are longer, but the tools are the same; memorize the binomial shortcut: 11<sup><var>n</var></sup> = (10 + 1)<sup><var>n</var></sup> &equiv; 10<var>n</var> + 1 (mod 100) &mdash; every term containing 100 vanishes.</p>
<p><b>Powers mod <var>n</var></b> cycle too: 2 mod 7 cycles through 2, 4, 1 with length 3; for 3 mod 8, already 3<sup>2</sup> &equiv; 1, so every even power of 3 gives 1. Once you find a power with remainder 1, everything after collapses instantly. This is the main tool for &ldquo;find the remainder of 2<sup>2026</sup>&rdquo; problems.</p>"""},
 'worked': [
  {'tag': {'ru': 'Разбор 1 · последняя цифра', 'en': 'Example 1 · last digit'},
   'q': {'ru': 'Найдите последнюю цифру числа 7<sup>2026</sup>.',
         'en': 'Find the last digit of 7<sup>2026</sup>.'},
   'sol': {'ru': 'Цикл семёрки: 7, 9, 3, 1, длина 4. Показатель: 2026 = 4&nbsp;&middot;&nbsp;506 + 2, остаток 2 &mdash; вторая позиция цикла: <b>9</b>. Ловушка: забывают поделить сам показатель на 4 и берут &laquo;последнюю цифру 2026&raquo; &mdash; цикл управляется показателем, а не основанием.',
          'en': 'The cycle of 7: 7, 9, 3, 1, length 4. Exponent: 2026 = 4&nbsp;&middot;&nbsp;506 + 2, remainder 2 &mdash; the second position of the cycle: <b>9</b>. The trap: students forget to reduce the exponent mod 4 and grab something from &ldquo;2026&rdquo; itself &mdash; the cycle is driven by the exponent, not the base.'}},
  {'tag': {'ru': 'Разбор 2 · степень с остатком 1', 'en': 'Example 2 · a power with remainder 1'},
   'q': {'ru': 'Найдите остаток от деления 3<sup>100</sup> на 8.',
         'en': 'Find the remainder when 3<sup>100</sup> is divided by 8.'},
   'sol': {'ru': '3<sup>2</sup> = 9 &equiv; 1 (mod 8). Тогда 3<sup>100</sup> = (3<sup>2</sup>)<sup>50</sup> &equiv; 1<sup>50</sup> = <b>1</b>. Одна строка: как только степень дала остаток 1, любой её кратный показатель тоже даёт 1. Искать цикл дальше не нужно.',
          'en': '3<sup>2</sup> = 9 &equiv; 1 (mod 8). Then 3<sup>100</sup> = (3<sup>2</sup>)<sup>50</sup> &equiv; 1<sup>50</sup> = <b>1</b>. One line: once some power gives remainder 1, every multiple of that exponent gives 1 too. No need to chase the cycle further.'}},
  {'tag': {'ru': 'Разбор 3 · две последние цифры', 'en': 'Example 3 · last two digits'},
   'q': {'ru': 'Найдите две последние цифры числа 7<sup>2024</sup>.',
         'en': 'Find the last two digits of 7<sup>2024</sup>.'},
   'sol': {'ru': 'По модулю 100: 7<sup>2</sup> = 49, 7<sup>3</sup> = 343 &equiv; 43, 7<sup>4</sup> = 2401 &equiv; 1. Цикл длины 4, и 2024 делится на 4 нацело &mdash; остаток 0, то есть ПОСЛЕДНЯЯ позиция цикла: 7<sup>2024</sup> &equiv; 1 (mod 100), две последние цифры <b>01</b>. Классическая ловушка: остаток 0 прочитать как первую позицию и ответить 07.',
          'en': 'Mod 100: 7<sup>2</sup> = 49, 7<sup>3</sup> = 343 &equiv; 43, 7<sup>4</sup> = 2401 &equiv; 1. The cycle has length 4, and 2024 is divisible by 4 &mdash; remainder 0, i.e. the LAST position of the cycle: 7<sup>2024</sup> &equiv; 1 (mod 100), last two digits <b>01</b>. The classic trap: reading remainder 0 as the first position and answering 07.'}},
  {'tag': {'ru': 'Разбор 4 · подстановка остатка', 'en': 'Example 4 · substituting a remainder'},
   'q': {'ru': 'Число <var>N</var> даёт остаток 3 при делении на 7. Какой остаток даёт <var>N</var><sup>2</sup> + 2<var>N</var>?',
         'en': 'A number <var>N</var> leaves remainder 3 upon division by 7. What remainder does <var>N</var><sup>2</sup> + 2<var>N</var> leave?'},
   'sol': {'ru': 'Подставляем остаток вместо числа: <var>N</var> &equiv; 3 (mod 7), значит <var>N</var><sup>2</sup> + 2<var>N</var> &equiv; 9 + 6 = 15 &equiv; <b>1</b> (mod 7). Само <var>N</var> не нужно &mdash; остатки складываются и перемножаются вместо чисел. Промежуточный итог (15) больше модуля &mdash; не забудьте привести его в конце.',
          'en': 'Substitute the remainder for the number: <var>N</var> &equiv; 3 (mod 7), so <var>N</var><sup>2</sup> + 2<var>N</var> &equiv; 9 + 6 = 15 &equiv; <b>1</b> (mod 7). We never need <var>N</var> itself &mdash; remainders add and multiply in place of numbers. The intermediate 15 exceeds the modulus &mdash; remember to reduce it at the end.'}},
 ],
 'selfp': [
  {'q': {'ru': 'Найдите остаток от деления 123&nbsp;456 на 9.', 'en': 'Find the remainder when 123,456 is divided by 9.'},
   'hint': {'ru': 'Остаток по модулю 9 равен остатку суммы цифр.', 'en': 'The remainder mod 9 equals the remainder of the digit sum.'},
   'sol': {'ru': 'Сумма цифр 1+2+3+4+5+6 = 21 &equiv; <b>3</b> (mod 9).', 'en': 'Digit sum 1+2+3+4+5+6 = 21 &equiv; <b>3</b> (mod 9).'}},
  {'q': {'ru': 'Найдите последнюю цифру числа 3<sup>2027</sup>.', 'en': 'Find the last digit of 3<sup>2027</sup>.'},
   'hint': {'ru': 'Цикл тройки: 3, 9, 7, 1. Возьмите 2027 mod 4.', 'en': 'The cycle of 3: 3, 9, 7, 1. Take 2027 mod 4.'},
   'sol': {'ru': '2027 &equiv; 3 (mod 4) &mdash; третья позиция цикла: <b>7</b>.', 'en': '2027 &equiv; 3 (mod 4) &mdash; the third position of the cycle: <b>7</b>.'}},
  {'q': {'ru': 'Найдите остаток от деления 2<sup>100</sup> на 7.', 'en': 'Find the remainder when 2<sup>100</sup> is divided by 7.'},
   'hint': {'ru': 'По модулю 7 степени двойки идут 2, 4, 1, 2, 4, 1, &hellip;', 'en': 'Mod 7 the powers of 2 go 2, 4, 1, 2, 4, 1, &hellip;'},
   'sol': {'ru': 'Цикл длины 3; 100 &equiv; 1 (mod 3) &mdash; первая позиция: <b>2</b>.', 'en': 'Cycle length 3; 100 &equiv; 1 (mod 3) &mdash; the first position: <b>2</b>.'}},
  {'q': {'ru': 'Число <var>n</var> &equiv; 5 (mod 6). Найдите остаток от деления 4<var>n</var> + 3 на 6.', 'en': 'A number satisfies <var>n</var> &equiv; 5 (mod 6). Find the remainder of 4<var>n</var> + 3 upon division by 6.'},
   'hint': {'ru': 'Подставьте остаток вместо <var>n</var> и приведите результат.', 'en': 'Substitute the remainder for <var>n</var> and reduce.'},
   'sol': {'ru': '4&nbsp;&middot;&nbsp;5 + 3 = 23 &equiv; <b>5</b> (mod 6).', 'en': '4&nbsp;&middot;&nbsp;5 + 3 = 23 &equiv; <b>5</b> (mod 6).'}},
  {'q': {'ru': 'Найдите последнюю цифру суммы 2<sup>2026</sup> + 3<sup>2026</sup>.', 'en': 'Find the last digit of 2<sup>2026</sup> + 3<sup>2026</sup>.'},
   'hint': {'ru': 'Каждое слагаемое отдельно, по своему циклу длины 4, потом сложить.', 'en': 'Each term separately, via its own length-4 cycle, then add.'},
   'sol': {'ru': '2026 &equiv; 2 (mod 4): у 2<sup>2026</sup> цифра 4, у 3<sup>2026</sup> &mdash; 9. Сумма 13, последняя цифра <b>3</b>.', 'en': '2026 &equiv; 2 (mod 4): 2<sup>2026</sup> ends in 4, 3<sup>2026</sup> in 9. Sum 13, last digit <b>3</b>.'}},
  {'q': {'ru': 'Найдите остаток от деления суммы 1 + 2 + 3 + &hellip; + 100 на 9.', 'en': 'Find the remainder when 1 + 2 + 3 + &hellip; + 100 is divided by 9.'},
   'hint': {'ru': 'Сначала сверните сумму в число, потом сумма цифр.', 'en': 'First collapse the sum into a number, then use the digit sum.'},
   'sol': {'ru': 'Сумма = 100&nbsp;&middot;&nbsp;101/2 = 5050; сумма цифр 10 &equiv; <b>1</b> (mod 9).', 'en': 'Sum = 100&nbsp;&middot;&nbsp;101/2 = 5050; digit sum 10 &equiv; <b>1</b> (mod 9).'}},
  {'q': {'ru': 'Найдите две последние цифры числа 11<sup>2025</sup>.', 'en': 'Find the last two digits of 11<sup>2025</sup>.'},
   'hint': {'ru': '(10 + 1)<sup><var>n</var></sup> &equiv; 10<var>n</var> + 1 (mod 100).', 'en': '(10 + 1)<sup><var>n</var></sup> &equiv; 10<var>n</var> + 1 (mod 100).'},
   'sol': {'ru': '10&nbsp;&middot;&nbsp;2025 + 1 = 20&nbsp;251 &equiv; <b>51</b> (mod 100).', 'en': '10&nbsp;&middot;&nbsp;2025 + 1 = 20,251 &equiv; <b>51</b> (mod 100).'}},
  {'q': {'ru': 'Найдите остаток от деления 2<sup>2026</sup> на 13.', 'en': 'Find the remainder when 2<sup>2026</sup> is divided by 13.'},
   'hint': {'ru': 'Выпишите степени двойки по модулю 13 до остатка 1 (цикл длины 12).', 'en': 'List powers of 2 mod 13 until you hit remainder 1 (the cycle has length 12).'},
   'sol': {'ru': '2<sup>12</sup> &equiv; 1 (mod 13); 2026 = 12&nbsp;&middot;&nbsp;168 + 10, значит 2<sup>2026</sup> &equiv; 2<sup>10</sup> = 1024 = 78&nbsp;&middot;&nbsp;13 + 10 &equiv; <b>10</b>.', 'en': '2<sup>12</sup> &equiv; 1 (mod 13); 2026 = 12&nbsp;&middot;&nbsp;168 + 10, so 2<sup>2026</sup> &equiv; 2<sup>10</sup> = 1024 = 78&nbsp;&middot;&nbsp;13 + 10 &equiv; <b>10</b>.'}},
 ],
 'answers': {'ru': '3 · 7 · 2 · 5 · 3 · 1 · 51 · 10', 'en': '3, 7, 2, 5, 3, 1, 51, 10'},
 'routing': {'ru': 'Норма &mdash; 6 из 8. Ошибки в 1 и 6 &mdash; перечитать &laquo;арифметику остатков&raquo; (сумма цифр и mod 9); в 2&ndash;3 и 5 &mdash; &laquo;последняя цифра&raquo; и правило остатка 0; в 4 &mdash; подстановку остатка; в 7 &mdash; &laquo;две последние цифры&raquo;; в 8 &mdash; &laquo;степени по модулю <var>n</var>&raquo;.',
             'en': 'Mastery bar: 6 of 8. For mistakes in 1 and 6, reread &ldquo;mod arithmetic&rdquo; (digit sum and mod 9); for 2&ndash;3 and 5, &ldquo;the last digit&rdquo; and the remainder-0 rule; for 4, substituting a remainder; for 7, &ldquo;the last two digits&rdquo;; for 8, &ldquo;powers mod <var>n</var>&rdquo;.'},
}

L34 = {
 'id': '3.4', 'anchor': 'u34',
 'title': {'ru': 'Факториалы и формула Лежандра, цифровые задачи, системы счисления',
           'en': 'Factorials and Legendre&rsquo;s Formula, Digit Problems, Number Bases'},
 'theory': {
  'ru': f"""
<p><b>Формула Лежандра.</b> Показатель простого <var>p</var> в разложении <var>n</var>! &mdash; это сумма целых частей: сколько чисел до <var>n</var> делится на <var>p</var>, на <var>p</var><sup>2</sup>, на <var>p</var><sup>3</sup>, &hellip; Каждый следующий член учитывает добавочный множитель <var>p</var> от кратных более высокой степени. Ловушка &mdash; остановиться на первом члене: 25 в 100! даёт не 20, а 20 + 4.</p>
<div class="frm">Показатель <var>p</var> в <var>n</var>! = {F('<var>n</var>','<var>p</var>')} + {F('<var>n</var>','<var>p</var><sup>2</sup>')} + {F('<var>n</var>','<var>p</var><sup>3</sup>')} + &hellip; (каждое слагаемое &mdash; целая часть). Нулей на конце <var>n</var>! &mdash; столько, каков показатель пятёрки.</div>
<p><b>Нули на конце.</b> Ноль рождается парой 2&nbsp;&middot;&nbsp;5, а двоек в факториале всегда больше, чем пятёрок &mdash; считаем только пятёрки. У 100!: 20 + 4 = 24 нуля. Обратная задача коварна: количество нулей прыгает на 2 у кратных 25, поэтому некоторые значения (например, ровно 5 нулей) не достигаются никогда.</p>
<p><b>Цифровые задачи.</b> Двузначное число &mdash; это 10<var>a</var> + <var>b</var>, а не &laquo;<var>ab</var>&raquo;. Ключевые тождества: <var>N</var> + перевёртыш = 11(<var>a</var> + <var>b</var>); <var>N</var> &minus; перевёртыш = 9(<var>a</var> &minus; <var>b</var>). Записали число через цифры &mdash; и задача стала уравнением.</p>
<p><b>Системы счисления &mdash; минимум.</b> Запись 132<sub>5</sub> означает 1&nbsp;&middot;&nbsp;25 + 3&nbsp;&middot;&nbsp;5 + 2 = 42. Туда &mdash; умножаем по разрядам; обратно &mdash; делим на основание и собираем остатки снизу вверх. Цифры обязаны быть меньше основания: &laquo;цифра 7 в базе 5&raquo; &mdash; сигнал ошибки.</p>""",
  'en': f"""
<p><b>Legendre&rsquo;s formula.</b> The exponent of a prime <var>p</var> in <var>n</var>! is a sum of floors: how many numbers up to <var>n</var> are divisible by <var>p</var>, by <var>p</var><sup>2</sup>, by <var>p</var><sup>3</sup>, &hellip; Each next term counts the extra factor of <var>p</var> contributed by multiples of the higher power. The trap is stopping after the first term: 25s in 100! contribute not 20 but 20 + 4.</p>
<div class="frm">Exponent of <var>p</var> in <var>n</var>! = {F('<var>n</var>','<var>p</var>')} + {F('<var>n</var>','<var>p</var><sup>2</sup>')} + {F('<var>n</var>','<var>p</var><sup>3</sup>')} + &hellip; (each term is a floor). Trailing zeros of <var>n</var>! = the exponent of 5.</div>
<p><b>Trailing zeros.</b> A zero is born from a pair 2&nbsp;&middot;&nbsp;5, and factorials always contain more 2s than 5s &mdash; so count only the 5s. For 100!: 20 + 4 = 24 zeros. The inverse problem is treacherous: the zero count jumps by 2 at multiples of 25, so some values (exactly 5 zeros, for instance) are never attained.</p>
<p><b>Digit problems.</b> A two-digit number is 10<var>a</var> + <var>b</var>, not &ldquo;<var>ab</var>&rdquo;. Key identities: <var>N</var> + reversal = 11(<var>a</var> + <var>b</var>); <var>N</var> &minus; reversal = 9(<var>a</var> &minus; <var>b</var>). Once the number is written through its digits, the problem becomes an equation.</p>
<p><b>Number bases &mdash; the minimum.</b> The string 132<sub>5</sub> means 1&nbsp;&middot;&nbsp;25 + 3&nbsp;&middot;&nbsp;5 + 2 = 42. To decimal &mdash; multiply out the place values; from decimal &mdash; divide by the base and collect remainders bottom-up. Digits must be smaller than the base: &ldquo;digit 7 in base 5&rdquo; signals an error.</p>"""},
 'worked': [
  {'tag': {'ru': 'Разбор 1 · нули на конце', 'en': 'Example 1 · trailing zeros'},
   'q': {'ru': 'Сколькими нулями оканчивается 100!?',
         'en': 'How many trailing zeros does 100! have?'},
   'sol': {'ru': 'Считаем пятёрки: &lfloor;100/5&rfloor; = 20, &lfloor;100/25&rfloor; = 4, &lfloor;100/125&rfloor; = 0. Итого 20 + 4 = <b>24</b>. Ловушка &mdash; ответить 20, забыв, что 25, 50, 75 и 100 приносят по ВТОРОЙ пятёрке: их и досчитывает член &lfloor;100/25&rfloor;.',
          'en': 'Count the 5s: &lfloor;100/5&rfloor; = 20, &lfloor;100/25&rfloor; = 4, &lfloor;100/125&rfloor; = 0. Total 20 + 4 = <b>24</b>. The trap is answering 20, forgetting that 25, 50, 75, and 100 each carry a SECOND five &mdash; exactly what the term &lfloor;100/25&rfloor; adds.'}},
  {'tag': {'ru': 'Разбор 2 · формула Лежандра', 'en': 'Example 2 · Legendre&rsquo;s formula'},
   'q': {'ru': 'Найдите показатель тройки в разложении 30! на простые.',
         'en': 'Find the exponent of 3 in the prime factorization of 30!.'},
   'sol': {'ru': '&lfloor;30/3&rfloor; + &lfloor;30/9&rfloor; + &lfloor;30/27&rfloor; = 10 + 3 + 1 = <b>14</b>. Следующий член &lfloor;30/81&rfloor; = 0 &mdash; ряд оборвался сам. Смысл слагаемых: 10 кратных тройки, из них 3 кратны девятке (вторая тройка), одно кратно 27 (третья).',
          'en': '&lfloor;30/3&rfloor; + &lfloor;30/9&rfloor; + &lfloor;30/27&rfloor; = 10 + 3 + 1 = <b>14</b>. The next term &lfloor;30/81&rfloor; = 0 &mdash; the series stops by itself. Meaning of the terms: 10 multiples of 3, of which 3 are multiples of 9 (a second three), one is a multiple of 27 (a third).'}},
  {'tag': {'ru': 'Разбор 3 · цифры и перевёртыш', 'en': 'Example 3 · digits and reversal'},
   'q': {'ru': 'Двузначное число сложили с его перевёртышем и получили 132. Чему равна сумма цифр числа?',
         'en': 'A two-digit number is added to its reversal, giving 132. What is the sum of the number&rsquo;s digits?'},
   'sol': {'ru': '(10<var>a</var> + <var>b</var>) + (10<var>b</var> + <var>a</var>) = 11(<var>a</var> + <var>b</var>) = 132, значит <var>a</var> + <var>b</var> = <b>12</b>. Само число не определено (48, 57, 66, 75, 84, 93 &mdash; подходят все), но вопрос и не про него. Не ищите лишнего: тождество отдало ответ за одну строку.',
          'en': '(10<var>a</var> + <var>b</var>) + (10<var>b</var> + <var>a</var>) = 11(<var>a</var> + <var>b</var>) = 132, so <var>a</var> + <var>b</var> = <b>12</b>. The number itself is not determined (48, 57, 66, 75, 84, 93 all work) &mdash; but that is not the question. Do not chase extras: the identity hands over the answer in one line.'}},
  {'tag': {'ru': 'Разбор 4 · перевод в базу', 'en': 'Example 4 · base conversion'},
   'q': {'ru': 'Запишите 2026 в пятеричной системе.',
         'en': 'Write 2026 in base 5.'},
   'sol': {'ru': 'Делим на 5, остатки снизу вверх: 2026 = 5&nbsp;&middot;&nbsp;405 + 1; 405 = 5&nbsp;&middot;&nbsp;81 + 0; 81 = 5&nbsp;&middot;&nbsp;16 + 1; 16 = 5&nbsp;&middot;&nbsp;3 + 1; 3 = 5&nbsp;&middot;&nbsp;0 + 3. Читаем остатки с конца: <b>31101<sub>5</sub></b>. Проверка по разрядам: 3&nbsp;&middot;&nbsp;625 + 1&nbsp;&middot;&nbsp;125 + 1&nbsp;&middot;&nbsp;25 + 0 + 1 = 2026. Верно.',
          'en': 'Divide by 5, remainders bottom-up: 2026 = 5&nbsp;&middot;&nbsp;405 + 1; 405 = 5&nbsp;&middot;&nbsp;81 + 0; 81 = 5&nbsp;&middot;&nbsp;16 + 1; 16 = 5&nbsp;&middot;&nbsp;3 + 1; 3 = 5&nbsp;&middot;&nbsp;0 + 3. Read the remainders backwards: <b>31101<sub>5</sub></b>. Check by place values: 3&nbsp;&middot;&nbsp;625 + 1&nbsp;&middot;&nbsp;125 + 1&nbsp;&middot;&nbsp;25 + 0 + 1 = 2026. Correct.'}},
 ],
 'selfp': [
  {'q': {'ru': 'Сколькими нулями оканчивается 25!?', 'en': 'How many trailing zeros does 25! have?'},
   'hint': {'ru': 'Считайте пятёрки: &lfloor;25/5&rfloor; + &lfloor;25/25&rfloor;.', 'en': 'Count the 5s: &lfloor;25/5&rfloor; + &lfloor;25/25&rfloor;.'},
   'sol': {'ru': '5 + 1 = <b>6</b>.', 'en': '5 + 1 = <b>6</b>.'}},
  {'q': {'ru': 'Найдите показатель двойки в разложении 20!.', 'en': 'Find the exponent of 2 in the factorization of 20!.'},
   'hint': {'ru': '&lfloor;20/2&rfloor; + &lfloor;20/4&rfloor; + &lfloor;20/8&rfloor; + &lfloor;20/16&rfloor;.', 'en': '&lfloor;20/2&rfloor; + &lfloor;20/4&rfloor; + &lfloor;20/8&rfloor; + &lfloor;20/16&rfloor;.'},
   'sol': {'ru': '10 + 5 + 2 + 1 = <b>18</b>.', 'en': '10 + 5 + 2 + 1 = <b>18</b>.'}},
  {'q': {'ru': 'Переведите 110110<sub>2</sub> в десятичную запись.', 'en': 'Convert 110110<sub>2</sub> to decimal.'},
   'hint': {'ru': 'Разряды двоичной записи: 32, 16, 8, 4, 2, 1.', 'en': 'Binary place values: 32, 16, 8, 4, 2, 1.'},
   'sol': {'ru': '32 + 16 + 4 + 2 = <b>54</b>.', 'en': '32 + 16 + 4 + 2 = <b>54</b>.'}},
  {'q': {'ru': 'Сколькими нулями оканчивается 130!?', 'en': 'How many trailing zeros does 130! have?'},
   'hint': {'ru': 'Три члена ряда: 5, 25 и 125 не превосходят 130.', 'en': 'Three terms: 5, 25, and 125 do not exceed 130.'},
   'sol': {'ru': '&lfloor;130/5&rfloor; + &lfloor;130/25&rfloor; + &lfloor;130/125&rfloor; = 26 + 5 + 1 = <b>32</b>.', 'en': '&lfloor;130/5&rfloor; + &lfloor;130/25&rfloor; + &lfloor;130/125&rfloor; = 26 + 5 + 1 = <b>32</b>.'}},
  {'q': {'ru': 'Сколько существует двузначных чисел, которые больше своего перевёртыша ровно на 27?', 'en': 'How many two-digit numbers exceed their reversal by exactly 27?'},
   'hint': {'ru': '<var>N</var> &minus; перевёртыш = 9(<var>a</var> &minus; <var>b</var>). Не забудьте, что <var>b</var> может быть нулём.', 'en': '<var>N</var> &minus; reversal = 9(<var>a</var> &minus; <var>b</var>). Do not forget that <var>b</var> may be zero.'},
   'sol': {'ru': '9(<var>a</var> &minus; <var>b</var>) = 27, то есть <var>a</var> &minus; <var>b</var> = 3: числа 30, 41, 52, 63, 74, 85, 96 &mdash; всего <b>7</b>.', 'en': '9(<var>a</var> &minus; <var>b</var>) = 27, so <var>a</var> &minus; <var>b</var> = 3: the numbers 30, 41, 52, 63, 74, 85, 96 &mdash; <b>7</b> in all.'}},
  {'q': {'ru': 'Найдите наибольшее <var>k</var>, при котором 12<sup><var>k</var></sup> делит 30!.', 'en': 'Find the largest <var>k</var> for which 12<sup><var>k</var></sup> divides 30!.'},
   'hint': {'ru': '12<sup><var>k</var></sup> = 2<sup>2<var>k</var></sup>&nbsp;&middot;&nbsp;3<sup><var>k</var></sup>; посчитайте запасы двоек и троек по Лежандру.', 'en': '12<sup><var>k</var></sup> = 2<sup>2<var>k</var></sup>&nbsp;&middot;&nbsp;3<sup><var>k</var></sup>; compute the stock of 2s and 3s by Legendre.'},
   'sol': {'ru': 'Двоек: 15 + 7 + 3 + 1 = 26; троек: 10 + 3 + 1 = 14. Нужно 2<var>k</var> &le; 26 и <var>k</var> &le; 14: <var>k</var> = <b>13</b>. Узкое место &mdash; двойки, хотя их &laquo;больше&raquo;: их тратится по две на каждую 12.',
          'en': '2s: 15 + 7 + 3 + 1 = 26; 3s: 10 + 3 + 1 = 14. We need 2<var>k</var> &le; 26 and <var>k</var> &le; 14: <var>k</var> = <b>13</b>. The bottleneck is the 2s, despite there being &ldquo;more&rdquo; of them: each 12 spends two.'}},
  {'q': {'ru': 'В какой системе счисления запись 132 означает десятичное число 42?', 'en': 'In which base does the string 132 represent the decimal number 42?'},
   'hint': {'ru': 'Уравнение по разрядам: <var>b</var><sup>2</sup> + 3<var>b</var> + 2 = 42.', 'en': 'Place-value equation: <var>b</var><sup>2</sup> + 3<var>b</var> + 2 = 42.'},
   'sol': {'ru': '<var>b</var><sup>2</sup> + 3<var>b</var> &minus; 40 = 0, корни 5 и &minus;8: основание <b>5</b>. Цифры 1, 3, 2 меньше пяти &mdash; запись корректна.', 'en': '<var>b</var><sup>2</sup> + 3<var>b</var> &minus; 40 = 0, roots 5 and &minus;8: base <b>5</b>. The digits 1, 3, 2 are below five &mdash; the string is legal.'}},
  {'q': {'ru': 'Найдите наименьшее <var>n</var>, при котором <var>n</var>! оканчивается ровно на 10 нулей.', 'en': 'Find the least <var>n</var> for which <var>n</var>! ends in exactly 10 zeros.'},
   'hint': {'ru': 'Нули добавляются на кратных пяти; проверьте окрестность <var>n</var> = 45.', 'en': 'Zeros are added at multiples of five; probe around <var>n</var> = 45.'},
   'sol': {'ru': 'У 44!: &lfloor;44/5&rfloor; + &lfloor;44/25&rfloor; = 8 + 1 = 9 нулей; у 45!: 9 + 1 = 10. Ответ <b>45</b>. Число нулей меняется только при переходе через кратное пяти &mdash; между ними проверять нечего.',
          'en': 'For 44!: &lfloor;44/5&rfloor; + &lfloor;44/25&rfloor; = 8 + 1 = 9 zeros; for 45!: 9 + 1 = 10. The answer is <b>45</b>. The zero count changes only when crossing a multiple of five &mdash; nothing to check in between.'}},
 ],
 'answers': {'ru': '6 · 18 · 54 · 32 · 7 · 13 · 5 · 45', 'en': '6, 18, 54, 32, 7, 13, 5, 45'},
 'routing': {'ru': 'Норма &mdash; 6 из 8. Ошибки в 1, 4 и 8 &mdash; перечитать &laquo;нули на конце&raquo;; во 2 и 6 &mdash; &laquo;формулу Лежандра&raquo;; в 5 &mdash; &laquo;цифровые задачи&raquo;; в 3 и 7 &mdash; &laquo;системы счисления&raquo;.',
             'en': 'Mastery bar: 6 of 8. For mistakes in 1, 4, and 8, reread &ldquo;trailing zeros&rdquo;; for 2 and 6, Legendre&rsquo;s formula; for 5, &ldquo;digit problems&rdquo;; for 3 and 7, &ldquo;number bases&rdquo;.'},
}

T3 = {
 'problems': [
  {'q': {'ru': 'Сколько положительных делителей у числа 540?',
         'en': 'How many positive divisors does 540 have?'},
   'opts': {'ru': ['20', '24', '27', '30', '36'], 'en': ['20', '24', '27', '30', '36']}},
  {'q': {'ru': 'Сколько натуральных чисел, не превосходящих 100, имеют ровно 12 делителей?',
         'en': 'How many positive integers not exceeding 100 have exactly 12 divisors?'},
   'opts': {'ru': ['3', '4', '5', '6', '7'], 'en': ['3', '4', '5', '6', '7']}},
  {'q': {'ru': 'Чему равен НОД(2024,&nbsp;748)?',
         'en': 'What is gcd(2024,&nbsp;748)?'},
   'opts': {'ru': ['4', '11', '22', '44', '88'], 'en': ['4', '11', '22', '44', '88']}},
  {'q': {'ru': 'Два маяка мигают: один каждые 8 секунд, другой каждые 14. Только что они мигнули одновременно. Через сколько секунд это повторится?',
         'en': 'Two lighthouses flash: one every 8 seconds, the other every 14. They just flashed together. In how many seconds will that happen again?'},
   'opts': {'ru': ['14', '22', '28', '42', '56'], 'en': ['14', '22', '28', '42', '56']}},
  {'q': {'ru': 'НОД двух чисел равен 4, НОК равен 120, одно из чисел &mdash; 24. Чему равно второе?',
         'en': 'Two numbers have gcd 4 and lcm 120; one of them is 24. What is the other?'},
   'opts': {'ru': ['10', '16', '20', '24', '30'], 'en': ['10', '16', '20', '24', '30']}},
  {'q': {'ru': 'Каков остаток от деления 5<sup>2026</sup> на 7?',
         'en': 'What is the remainder when 5<sup>2026</sup> is divided by 7?'},
   'opts': {'ru': ['0', '1', '2', '4', '6'], 'en': ['0', '1', '2', '4', '6']}},
  {'q': {'ru': 'Какова последняя цифра числа 7<sup>2023</sup>?',
         'en': 'What is the last digit of 7<sup>2023</sup>?'},
   'opts': {'ru': ['1', '3', '5', '7', '9'], 'en': ['1', '3', '5', '7', '9']}},
  {'q': {'ru': 'Каковы две последние цифры числа 11<sup>25</sup>?',
         'en': 'What are the last two digits of 11<sup>25</sup>?'},
   'opts': {'ru': ['01', '21', '31', '51', '71'], 'en': ['01', '21', '31', '51', '71']}},
  {'q': {'ru': 'Сколькими нулями оканчивается 60!?',
         'en': 'How many trailing zeros does 60! have?'},
   'opts': {'ru': ['14', '15', '16', '18', '20'], 'en': ['14', '15', '16', '18', '20']}},
  {'q': {'ru': 'Чему равен показатель семёрки в разложении 100! на простые?',
         'en': 'What is the exponent of 7 in the prime factorization of 100!?'},
   'opts': {'ru': ['9', '12', '14', '15', '16'], 'en': ['9', '12', '14', '15', '16']}},
 ],
 'key': ['B', 'C', 'D', 'E', 'C', 'C', 'B', 'D', 'A', 'E'],
 'hints': {
  'ru': [
   '<b>1.</b> 540 = 2<sup>2</sup>&middot;3<sup>3</sup>&middot;5: (2+1)(3+1)(1+1) = 24.',
   '<b>2.</b> 12 = 12&middot;1 = 6&middot;2 = 4&middot;3 = 3&middot;2&middot;2: формы <var>p</var><sup>5</sup><var>q</var>, <var>p</var><sup>3</sup><var>q</var><sup>2</sup>, <var>p</var><sup>2</sup><var>qr</var>. До 100 подходят 60, 72, 84, 90, 96 &mdash; ровно 5.',
   '<b>3.</b> Евклид: 2024 = 2&middot;748 + 528; 748 = 528 + 220; 528 = 2&middot;220 + 88; 220 = 2&middot;88 + 44; 88 = 2&middot;44. НОД = 44.',
   '<b>4.</b> НОК(8,&nbsp;14) = 8&middot;14/2 = 56.',
   '<b>5.</b> Произведение = 4&middot;120 = 480; второе число 480/24 = 20.',
   '<b>6.</b> Цикл пятёрки mod 7 имеет длину 6; 2026 &equiv; 4 (mod 6), 5<sup>4</sup> = 625 = 89&middot;7 + 2: остаток 2.',
   '<b>7.</b> Цикл 7, 9, 3, 1; 2023 &equiv; 3 (mod 4): цифра 3.',
   '<b>8.</b> 11<sup><var>n</var></sup> &equiv; 10<var>n</var> + 1 (mod 100): 250 + 1 &equiv; 51.',
   '<b>9.</b> &lfloor;60/5&rfloor; + &lfloor;60/25&rfloor; = 12 + 2 = 14.',
   '<b>10.</b> &lfloor;100/7&rfloor; + &lfloor;100/49&rfloor; = 14 + 2 = 16.'],
  'en': [
   '<b>1.</b> 540 = 2<sup>2</sup>&middot;3<sup>3</sup>&middot;5: (2+1)(3+1)(1+1) = 24.',
   '<b>2.</b> 12 = 12&middot;1 = 6&middot;2 = 4&middot;3 = 3&middot;2&middot;2: shapes <var>p</var><sup>5</sup><var>q</var>, <var>p</var><sup>3</sup><var>q</var><sup>2</sup>, <var>p</var><sup>2</sup><var>qr</var>. Up to 100 this gives 60, 72, 84, 90, 96 &mdash; exactly 5.',
   '<b>3.</b> Euclid: 2024 = 2&middot;748 + 528; 748 = 528 + 220; 528 = 2&middot;220 + 88; 220 = 2&middot;88 + 44; 88 = 2&middot;44. Gcd = 44.',
   '<b>4.</b> Lcm(8,&nbsp;14) = 8&middot;14/2 = 56.',
   '<b>5.</b> Product = 4&middot;120 = 480; the other number is 480/24 = 20.',
   '<b>6.</b> The cycle of 5 mod 7 has length 6; 2026 &equiv; 4 (mod 6), 5<sup>4</sup> = 625 = 89&middot;7 + 2: remainder 2.',
   '<b>7.</b> Cycle 7, 9, 3, 1; 2023 &equiv; 3 (mod 4): digit 3.',
   '<b>8.</b> 11<sup><var>n</var></sup> &equiv; 10<var>n</var> + 1 (mod 100): 250 + 1 &equiv; 51.',
   '<b>9.</b> &lfloor;60/5&rfloor; + &lfloor;60/25&rfloor; = 12 + 2 = 14.',
   '<b>10.</b> &lfloor;100/7&rfloor; + &lfloor;100/49&rfloor; = 14 + 2 = 16.'],
 },
}


STARS = {
 '3.1': {
  'q': {'ru': 'Сколько делителей числа 1&nbsp;000&nbsp;000 не являются ни точными квадратами, ни точными кубами?',
        'en': 'How many divisors of 1,000,000 are neither perfect squares nor perfect cubes?'},
  'hint': {'ru': '10<sup>6</sup> = 2<sup>6</sup>&middot;5<sup>6</sup>. Посчитайте квадраты, кубы и включение-исключение: пересечение &mdash; шестые степени.', 'en': '10<sup>6</sup> = 2<sup>6</sup>&middot;5<sup>6</sup>. Count squares, cubes, and use inclusion-exclusion: the overlap is the sixth powers.'},
  'sol': {'ru': 'Всего делителей 7&nbsp;&middot;&nbsp;7 = 49. Квадраты (чётные показатели 0, 2, 4, 6): 4&nbsp;&middot;&nbsp;4 = 16. Кубы (показатели 0, 3, 6): 3&nbsp;&middot;&nbsp;3 = 9. Шестые степени (0, 6): 2&nbsp;&middot;&nbsp;2 = 4. Ответ: 49 &minus; 16 &minus; 9 + 4 = <b>28</b>.', 'en': 'Total divisors: 7&nbsp;&middot;&nbsp;7 = 49. Squares (even exponents 0, 2, 4, 6): 4&nbsp;&middot;&nbsp;4 = 16. Cubes (exponents 0, 3, 6): 3&nbsp;&middot;&nbsp;3 = 9. Sixth powers (0, 6): 2&nbsp;&middot;&nbsp;2 = 4. Answer: 49 &minus; 16 &minus; 9 + 4 = <b>28</b>.'}},
 '3.2': {
  'q': {'ru': 'Найдите сумму всех натуральных <var>n</var> &le; 60, для которых НОД(<var>n</var>,&nbsp;18) = 6.',
        'en': 'Find the sum of all positive integers <var>n</var> &le; 60 with gcd(<var>n</var>,&nbsp;18) = 6.'},
  'hint': {'ru': '18 = 2&middot;3<sup>2</sup>. Условие: <var>n</var> кратно 6, но не кратно 9.', 'en': '18 = 2&middot;3<sup>2</sup>. The condition: <var>n</var> is a multiple of 6 but not of 9.'},
  'sol': {'ru': 'НОД(<var>n</var>,&nbsp;18) = 6 = 2&middot;3 требует: <var>n</var> чётно и делится на 3 ровно в первой степени. Кратные 6 до 60: их 10; вычёркиваем кратные 18 (18, 36, 54). Остаются 6, 12, 24, 30, 42, 48, 60; сумма <b>222</b>.', 'en': 'Gcd(<var>n</var>,&nbsp;18) = 6 = 2&middot;3 requires: <var>n</var> even and divisible by 3 exactly once. Multiples of 6 up to 60: ten of them; strike out the multiples of 18 (18, 36, 54). Left: 6, 12, 24, 30, 42, 48, 60; the sum is <b>222</b>.'}},
 '3.3': {
  'q': {'ru': 'Найдите остаток от деления 2<sup>2026</sup> + 2026<sup>2</sup> на 7.',
        'en': 'Find the remainder when 2<sup>2026</sup> + 2026<sup>2</sup> is divided by 7.'},
  'hint': {'ru': 'Два разных модульных хода: цикл степеней двойки длины 3 и остаток самого 2026 по модулю 7.', 'en': 'Two different mod moves: the length-3 cycle of powers of 2, and the remainder of 2026 itself mod 7.'},
  'sol': {'ru': 'Степени двойки mod 7: 2, 4, 1 (цикл 3); 2026 &equiv; 1 (mod 3), значит 2<sup>2026</sup> &equiv; 2. Далее 2026 = 7&nbsp;&middot;&nbsp;289 + 3, то есть 2026 &equiv; 3 и 2026<sup>2</sup> &equiv; 9 &equiv; 2. Сумма: 2 + 2 = <b>4</b>. Замечание-ловушка: показатель приводим по длине цикла (mod 3), основание &mdash; по модулю 7; перепутать &mdash; типовая ошибка.', 'en': 'Powers of 2 mod 7: 2, 4, 1 (cycle 3); 2026 &equiv; 1 (mod 3), so 2<sup>2026</sup> &equiv; 2. Next, 2026 = 7&nbsp;&middot;&nbsp;289 + 3, so 2026 &equiv; 3 and 2026<sup>2</sup> &equiv; 9 &equiv; 2. Sum: 2 + 2 = <b>4</b>. The trap: the exponent is reduced by the cycle length (mod 3), the base mod 7; mixing these up is the standard error.'}},
 '3.4': {
  'q': {'ru': 'Найдите наименьшее натуральное <var>m</var>, для которого НИ ОДИН факториал <var>n</var>! не оканчивается ровно на <var>m</var> нулей.',
        'en': 'Find the least positive integer <var>m</var> such that NO factorial <var>n</var>! ends in exactly <var>m</var> zeros.'},
  'hint': {'ru': 'Число нулей растёт скачками на кратных пяти; сколько их у 24! и у 25!?', 'en': 'The zero count grows in jumps at multiples of five; what is it for 24! and for 25!?'},
  'sol': {'ru': 'На каждом кратном пяти счётчик нулей прибавляет показатель пятёрки этого числа. У 24!: &lfloor;24/5&rfloor; = 4 нуля; 25 приносит сразу ДВЕ пятёрки, и у 25! уже 6 нулей. Значение 5 перепрыгнуто и не достигается никогда: <var>m</var> = <b>5</b>. Дальше пропуски идут у каждого кратного 25 (например, 11 &mdash; между 49! и 50!).', 'en': 'At each multiple of five the zero counter increases by that number&rsquo;s exponent of 5. For 24!: &lfloor;24/5&rfloor; = 4 zeros; 25 brings TWO fives at once, and 25! already has 6 zeros. The value 5 is jumped over and never attained: <var>m</var> = <b>5</b>. Further skips occur at every multiple of 25 (for instance 11, between 49! and 50!).'}},
}
