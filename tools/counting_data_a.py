# -*- coding: utf-8 -*-
"""Блок 4 «Комбинаторика и вероятность»: уроки 4.1–4.2, RU+EN. HTML-фрагменты в нотации страницы курса."""

def F(a, b):
    return f'<span class="frac"><span>{a}</span><span>{b}</span></span>'

L41 = {
 'id': '4.1', 'anchor': 'u41',
 'title': {'ru': 'Правила суммы и произведения, перестановки, ограничения',
           'en': 'Sum and Product Rules, Permutations, Constraints'},
 'theory': {
  'ru': """
<p><b>Два правила решают почти всё.</b> Если выбор распадается на непересекающиеся случаи &mdash; количества <b>складываются</b> (правило суммы). Если выбор идёт по шагам и на каждом шаге число вариантов не зависит от предыдущих &mdash; количества <b>перемножаются</b> (правило произведения). Слово &laquo;или&raquo; &mdash; сигнал сложения, слово &laquo;и затем&raquo; &mdash; умножения.</p>
<p><b>Метод слотов.</b> Рисуйте пустые позиции и заполняйте их по одной, начиная с <b>самой ограниченной</b>. Трёхзначное число с различными цифрами: первый слот &mdash; 9 вариантов (без нуля), второй &mdash; 9 (любая, кроме занятой), третий &mdash; 8. Итого 9&nbsp;&middot;&nbsp;9&nbsp;&middot;&nbsp;8 = 648. Если начать не с того слота, число вариантов начнёт зависеть от предыстории &mdash; тогда режьте на случаи.</p>
<div class="frm">Перестановки <var>n</var> различных объектов в ряд: <var>n</var>! = <var>n</var>&nbsp;&middot;&nbsp;(<var>n</var>&nbsp;&minus;&nbsp;1)&nbsp;&middot;&nbsp;&hellip;&nbsp;&middot;&nbsp;1. Размещения <var>k</var> из <var>n</var>: <var>n</var>&nbsp;&middot;&nbsp;(<var>n</var>&nbsp;&minus;&nbsp;1)&nbsp;&middot;&nbsp;&hellip; (<var>k</var> множителей).</div>
<p><b>&laquo;Рядом&raquo; &mdash; склейка.</b> Двое должны стоять вместе: склейте их в один блок, переставьте блоки, потом умножьте на перестановки внутри блока (&times;2 для пары). <b>&laquo;Не рядом&raquo; &mdash; дополнение:</b> все расстановки минус те, где они вместе. Считать &laquo;не рядом&raquo; напрямую &mdash; дольше и опаснее.</p>
<p><b>Контроль ошибок.</b> Главные ловушки урока: забытый ноль в старшем разряде, слоты в неудачном порядке и двойной счёт. Помогает и симметрия: если условия для объектов симметричны (например, чётных и нечётных цифр поровну), ответы для симметричных случаев обязаны совпасть. Всегда проверяйте себя на маленьком примере: если формула верна для 2&ndash;3 объектов, где всё можно выписать руками, ей можно верить.</p>""",
  'en': """
<p><b>Two rules solve almost everything.</b> If a choice splits into non-overlapping cases, the counts <b>add</b> (sum rule). If a choice proceeds in steps and the number of options at each step does not depend on the previous ones, the counts <b>multiply</b> (product rule). The word &ldquo;or&rdquo; signals addition; &ldquo;and then&rdquo; signals multiplication.</p>
<p><b>The slot method.</b> Draw empty positions and fill them one by one, starting with the <b>most restricted</b> slot. A three-digit number with distinct digits: first slot &mdash; 9 options (no zero), second &mdash; 9 (anything except the used digit), third &mdash; 8. Total 9&nbsp;&middot;&nbsp;9&nbsp;&middot;&nbsp;8 = 648. Start with the wrong slot and the counts begin to depend on history &mdash; then split into cases.</p>
<div class="frm">Permutations of <var>n</var> distinct objects in a row: <var>n</var>! = <var>n</var>&nbsp;&middot;&nbsp;(<var>n</var>&nbsp;&minus;&nbsp;1)&nbsp;&middot;&nbsp;&hellip;&nbsp;&middot;&nbsp;1. Arrangements of <var>k</var> out of <var>n</var>: <var>n</var>&nbsp;&middot;&nbsp;(<var>n</var>&nbsp;&minus;&nbsp;1)&nbsp;&middot;&nbsp;&hellip; (<var>k</var> factors).</div>
<p><b>&ldquo;Together&rdquo; means glue.</b> Two people must stand together: glue them into one block, permute the blocks, then multiply by the arrangements inside the block (&times;2 for a pair). <b>&ldquo;Not together&rdquo; means complement:</b> all arrangements minus those where they are together. Counting &ldquo;not together&rdquo; directly is slower and riskier.</p>
<p><b>Error control.</b> The main traps of this lesson: a forgotten zero in the leading digit, slots filled in a bad order, and double counting. Symmetry helps too: when the conditions treat objects symmetrically (say, equally many even and odd digits), symmetric cases must give equal counts. Always test yourself on a tiny example: if the formula is right for 2&ndash;3 objects, where everything can be listed by hand, you can trust it.</p>"""},
 'worked': [
  {'tag': {'ru': 'Разбор 1 · метод слотов', 'en': 'Example 1 · slot method'},
   'q': {'ru': 'Сколько существует трёхзначных чисел, у которых все цифры различны?',
         'en': 'How many three-digit numbers have all digits distinct?'},
   'sol': {'ru': 'Слоты слева направо: 9 (первая цифра не ноль)&nbsp;&middot;&nbsp;9 (любая, кроме первой &mdash; ноль уже можно)&nbsp;&middot;&nbsp;8 = <b>648</b>. Ловушка &mdash; написать 9&nbsp;&middot;&nbsp;10&nbsp;&middot;&nbsp;10 и забыть про различность или 10&nbsp;&middot;&nbsp;9&nbsp;&middot;&nbsp;8 и пустить ноль в старший разряд.',
          'en': 'Slots left to right: 9 (first digit is not zero)&nbsp;&middot;&nbsp;9 (anything except the first digit &mdash; zero is now allowed)&nbsp;&middot;&nbsp;8 = <b>648</b>. The trap is writing 9&nbsp;&middot;&nbsp;10&nbsp;&middot;&nbsp;10 and forgetting distinctness, or 10&nbsp;&middot;&nbsp;9&nbsp;&middot;&nbsp;8 and letting zero lead.'}},
  {'tag': {'ru': 'Разбор 2 · «чётное» и кейсы', 'en': 'Example 2 · &ldquo;even&rdquo; and cases'},
   'q': {'ru': 'Сколько существует чётных трёхзначных чисел с различными цифрами?',
         'en': 'How many even three-digit numbers have all digits distinct?'},
   'sol': {'ru': 'Начинаем с самого ограниченного слота &mdash; последнего. Он тянет за собой ноль, поэтому два случая. Последняя цифра 0: 9&nbsp;&middot;&nbsp;8 = 72. Последняя из {2,&nbsp;4,&nbsp;6,&nbsp;8}: 4&nbsp;&middot;&nbsp;8 (первая: не ноль и не последняя)&nbsp;&middot;&nbsp;8 = 256. Итого 72 + 256 = <b>328</b>. Ловушка &mdash; посчитать 5&nbsp;&middot;&nbsp;8&nbsp;&middot;&nbsp;8 одним махом: у нуля и у 2&ndash;8 разные ограничения на первую цифру.',
          'en': 'Start with the most restricted slot &mdash; the last one. It drags zero into the picture, so two cases. Last digit 0: 9&nbsp;&middot;&nbsp;8 = 72. Last digit in {2,&nbsp;4,&nbsp;6,&nbsp;8}: 4&nbsp;&middot;&nbsp;8 (first digit: not zero and not the last digit)&nbsp;&middot;&nbsp;8 = 256. Total 72 + 256 = <b>328</b>. The trap is writing 5&nbsp;&middot;&nbsp;8&nbsp;&middot;&nbsp;8 in one stroke: zero and 2&ndash;8 impose different restrictions on the first digit.'}},
  {'tag': {'ru': 'Разбор 3 · склейка', 'en': 'Example 3 · gluing'},
   'q': {'ru': 'Пять человек становятся в ряд для фото. Аня и Боря хотят стоять рядом. Сколькими способами можно их всех расставить?',
         'en': 'Five people line up for a photo. Ann and Ben want to stand next to each other. In how many ways can everyone be arranged?'},
   'sol': {'ru': 'Склеиваем Аню и Борю в один блок: 4 объекта, 4! = 24 расстановки. Внутри блока два порядка: АБ и БА. Итого 24&nbsp;&middot;&nbsp;2 = <b>48</b>. Классическая ошибка &mdash; забыть множитель 2 за порядок внутри склейки.',
          'en': 'Glue Ann and Ben into one block: 4 objects, 4! = 24 arrangements. Inside the block there are two orders: AB and BA. Total 24&nbsp;&middot;&nbsp;2 = <b>48</b>. The classic mistake is forgetting the factor of 2 for the order inside the glued block.'}},
  {'tag': {'ru': 'Разбор 4 · «не рядом» через дополнение', 'en': 'Example 4 · &ldquo;not adjacent&rdquo; via complement'},
   'q': {'ru': 'Шесть книг ставят на полку. Два тома словаря нельзя ставить рядом. Сколько расстановок?',
         'en': 'Six books are placed on a shelf. The two dictionary volumes must not stand next to each other. How many arrangements are there?'},
   'sol': {'ru': 'Все расстановки минус &laquo;словари вместе&raquo;: 6! &minus; 2&nbsp;&middot;&nbsp;5! = 720 &minus; 240 = <b>480</b>. &laquo;Не рядом&raquo; напрямую &mdash; это возня с позициями; дополнение &mdash; одна строка. Запомните рефлекс: запрет &laquo;рядом&raquo; почти всегда считается вычитанием склейки.',
          'en': 'All arrangements minus &ldquo;dictionaries together&rdquo;: 6! &minus; 2&nbsp;&middot;&nbsp;5! = 720 &minus; 240 = <b>480</b>. Counting &ldquo;not adjacent&rdquo; directly is a mess of positions; the complement is one line. Build the reflex: a &ldquo;no-adjacency&rdquo; ban is almost always counted by subtracting the glued case.'}},
 ],
 'selfp': [
  {'q': {'ru': 'В кафе 4 супа, 5 горячих блюд и 3 напитка. Сколькими способами можно собрать обед из супа, горячего и напитка?', 'en': 'A cafe offers 4 soups, 5 mains, and 3 drinks. In how many ways can you build a lunch of one soup, one main, and one drink?'},
   'hint': {'ru': '&laquo;И затем&raquo; &mdash; перемножаем.', 'en': '&ldquo;And then&rdquo; &mdash; multiply.'},
   'sol': {'ru': '4&nbsp;&middot;&nbsp;5&nbsp;&middot;&nbsp;3 = <b>60</b>.', 'en': '4&nbsp;&middot;&nbsp;5&nbsp;&middot;&nbsp;3 = <b>60</b>.'}},
  {'q': {'ru': 'Сколько четырёхбуквенных кодов без повторов можно составить из букв A, B, C, D, E?', 'en': 'How many four-letter codes with no repeated letters can be made from the letters A, B, C, D, E?'},
   'hint': {'ru': 'Четыре слота: 5, потом 4, потом&hellip;', 'en': 'Four slots: 5, then 4, then&hellip;'},
   'sol': {'ru': '5&nbsp;&middot;&nbsp;4&nbsp;&middot;&nbsp;3&nbsp;&middot;&nbsp;2 = <b>120</b>.', 'en': '5&nbsp;&middot;&nbsp;4&nbsp;&middot;&nbsp;3&nbsp;&middot;&nbsp;2 = <b>120</b>.'}},
  {'q': {'ru': 'Пять человек становятся в ряд. Аня должна стоять с краю (любого). Сколько расстановок?', 'en': 'Five people line up in a row. Ann must stand at an end (either one). How many arrangements are there?'},
   'hint': {'ru': 'Сначала место для Ани, потом остальные.', 'en': 'Place Ann first, then everyone else.'},
   'sol': {'ru': '2 края для Ани, остальные как угодно: 2&nbsp;&middot;&nbsp;4! = <b>48</b>.', 'en': '2 ends for Ann, the rest freely: 2&nbsp;&middot;&nbsp;4! = <b>48</b>.'}},
  {'q': {'ru': 'Сколько существует трёхзначных чисел, у которых все цифры нечётные?', 'en': 'How many three-digit numbers have all digits odd?'},
   'hint': {'ru': 'Нечётных цифр пять; повторы разрешены.', 'en': 'There are five odd digits; repeats are allowed.'},
   'sol': {'ru': '5&nbsp;&middot;&nbsp;5&nbsp;&middot;&nbsp;5 = <b>125</b>. Ноль чётный, так что запрет на старший разряд здесь бесплатный.', 'en': '5&nbsp;&middot;&nbsp;5&nbsp;&middot;&nbsp;5 = <b>125</b>. Zero is even, so the leading-digit restriction costs nothing here.'}},
  {'q': {'ru': 'Сколько существует трёхзначных чисел с различными цифрами, делящихся на 5?', 'en': 'How many three-digit numbers with all digits distinct are divisible by 5?'},
   'hint': {'ru': 'Последняя цифра 0 или 5 &mdash; два случая с разными ограничениями.', 'en': 'The last digit is 0 or 5 &mdash; two cases with different restrictions.'},
   'sol': {'ru': 'Конец 0: 9&nbsp;&middot;&nbsp;8 = 72. Конец 5: 8 (первая: не ноль и не 5)&nbsp;&middot;&nbsp;8 = 64. Итого <b>136</b>.', 'en': 'Ending 0: 9&nbsp;&middot;&nbsp;8 = 72. Ending 5: 8 (first digit: not zero and not 5)&nbsp;&middot;&nbsp;8 = 64. Total <b>136</b>.'}},
  {'q': {'ru': 'Четыре мальчика и три девочки становятся в ряд так, чтобы все девочки стояли подряд. Сколько расстановок?', 'en': 'Four boys and three girls line up so that all three girls stand together. How many arrangements are there?'},
   'hint': {'ru': 'Склейте девочек в блок; не забудьте порядок внутри.', 'en': 'Glue the girls into a block; do not forget the order inside it.'},
   'sol': {'ru': 'Блок девочек + 4 мальчика = 5 объектов: 5!&nbsp;&middot;&nbsp;3! = 120&nbsp;&middot;&nbsp;6 = <b>720</b>.', 'en': 'The girls&rsquo; block + 4 boys = 5 objects: 5!&nbsp;&middot;&nbsp;3! = 120&nbsp;&middot;&nbsp;6 = <b>720</b>.'}},
  {'q': {'ru': 'Пять человек становятся в ряд. Петя и Вася поссорились и не хотят стоять рядом. Сколько расстановок?', 'en': 'Five people line up in a row. Pete and Vic had a fight and refuse to stand next to each other. How many arrangements are there?'},
   'hint': {'ru': 'Все минус &laquo;вместе&raquo;.', 'en': 'All minus &ldquo;together&rdquo;.'},
   'sol': {'ru': '5! &minus; 2&nbsp;&middot;&nbsp;4! = 120 &minus; 48 = <b>72</b>.', 'en': '5! &minus; 2&nbsp;&middot;&nbsp;4! = 120 &minus; 48 = <b>72</b>.'}},
  {'q': {'ru': 'Семь человек становятся в ряд. Сколько расстановок, в которых Аня стоит левее Бори (не обязательно рядом)?', 'en': 'Seven people line up in a row. In how many arrangements does Ann stand somewhere to the left of Ben (not necessarily adjacent)?'},
   'hint': {'ru': 'В каждой расстановке ровно один из двух порядков Аня/Боря. Симметрия!', 'en': 'Every arrangement has exactly one of the two Ann/Ben orders. Symmetry!'},
   'sol': {'ru': 'Ровно в половине всех 7! расстановок Аня левее: 5040/2 = <b>2520</b>. Никаких кейсов &mdash; чистая симметрия.', 'en': 'In exactly half of all 7! arrangements Ann is to the left: 5040/2 = <b>2520</b>. No casework &mdash; pure symmetry.'}},
 ],
 'answers': {'ru': '60 · 120 · 48 · 125 · 136 · 720 · 72 · 2520', 'en': '60, 120, 48, 125, 136, 720, 72, 2520'},
 'routing': {'ru': 'Норма урока &mdash; 6 из 8. Ошибки в 1&ndash;2 &mdash; перечитать &laquo;два правила&raquo;; в 3&ndash;5 &mdash; &laquo;метод слотов&raquo; и кейсы с нулём; в 6&ndash;7 &mdash; &laquo;склейка и дополнение&raquo;; в 8 &mdash; симметрия из &laquo;контроля ошибок&raquo;. Задачи с ошибками вернутся в начало следующей половинки B.',
             'en': 'Mastery bar: 6 of 8. For mistakes in 1&ndash;2, reread &ldquo;two rules&rdquo;; for 3&ndash;5, &ldquo;the slot method&rdquo; and the zero cases; for 6&ndash;7, &ldquo;glue and complement&rdquo;; for 8, the symmetry idea from &ldquo;error control&rdquo;. Missed problems come back at the start of the next lesson&rsquo;s B session.'},
}

L42 = {
 'id': '4.2', 'anchor': 'u42',
 'title': {'ru': 'Сочетания: выбор команды, C(n, k), звёзды и перегородки',
           'en': 'Combinations: Team Selection, C(n, k), Stars and Bars'},
 'theory': {
  'ru': f"""
<p><b>Порядок важен или нет &mdash; главный вопрос комбинаторики.</b> Выбрать капитана и вратаря &mdash; порядок важен, это размещение. Выбрать двоих дежурных &mdash; порядок не важен, это сочетание. Число способов выбрать <var>k</var> объектов из <var>n</var> без учёта порядка: C(<var>n</var>,&nbsp;<var>k</var>) = размещения, делённые на <var>k</var>! &mdash; каждую компанию мы посчитали <var>k</var>! раз и возвращаем долг делением.</p>
<div class="frm">C(<var>n</var>,&nbsp;<var>k</var>) = {F('<var>n</var>&nbsp;&middot;&nbsp;(<var>n</var>&nbsp;&minus;&nbsp;1)&nbsp;&middot;&nbsp;&hellip;&nbsp;&middot;&nbsp;(<var>n</var>&nbsp;&minus;&nbsp;<var>k</var>&nbsp;+&nbsp;1)','<var>k</var>!')} &nbsp;&middot;&nbsp; Свойства: C(<var>n</var>,&nbsp;<var>k</var>) = C(<var>n</var>,&nbsp;<var>n</var>&nbsp;&minus;&nbsp;<var>k</var>); &nbsp;C(<var>n</var>,&nbsp;0) = C(<var>n</var>,&nbsp;<var>n</var>) = 1.</div>
<p><b>Выбор по группам перемножается.</b> Команда из 2 мальчиков и 2 девочек: C(5,&nbsp;2)&nbsp;&middot;&nbsp;C(6,&nbsp;2) &mdash; выборы независимы. Симметрия C(<var>n</var>,&nbsp;<var>k</var>) = C(<var>n</var>,&nbsp;<var>n</var>&nbsp;&minus;&nbsp;<var>k</var>) экономит арифметику: C(10,&nbsp;8) считайте как C(10,&nbsp;2) = 45. Полезные образы: рукопожатия <var>n</var> человек &mdash; C(<var>n</var>,&nbsp;2); диагонали <var>n</var>-угольника &mdash; C(<var>n</var>,&nbsp;2)&nbsp;&minus;&nbsp;<var>n</var> (пары вершин минус стороны).</p>
<p><b>Звёзды и перегородки.</b> Сколькими способами раздать <var>n</var> одинаковых конфет <var>k</var> детям? Выложите конфеты в ряд и вставьте <var>k</var>&nbsp;&minus;&nbsp;1 перегородку. Если каждому хотя бы по одной &mdash; перегородки встают в промежутки между конфетами: C(<var>n</var>&nbsp;&minus;&nbsp;1,&nbsp;<var>k</var>&nbsp;&minus;&nbsp;1) способов. Если можно и по нулю &mdash; сначала выдайте каждому &laquo;виртуальную&raquo; конфету: C(<var>n</var>&nbsp;+&nbsp;<var>k</var>&nbsp;&minus;&nbsp;1,&nbsp;<var>k</var>&nbsp;&minus;&nbsp;1).</p>
<p><b>Ловушка урока &mdash; двойной счёт.</b> Если вы выбираете &laquo;сначала одного особенного, потом остальных&raquo;, проверьте: не считаете ли вы одну и ту же компанию несколько раз с разными &laquo;особенными&raquo;? Лечение стандартное: считать напрямую сочетаниями или делить на число повторов.</p>""",
  'en': f"""
<p><b>Order matters or not &mdash; the central question of counting.</b> Choosing a captain and a goalkeeper &mdash; order matters, that is an arrangement. Choosing two monitors &mdash; order does not matter, that is a combination. The number of ways to choose <var>k</var> objects out of <var>n</var> without order: C(<var>n</var>,&nbsp;<var>k</var>) = the arrangements divided by <var>k</var>! &mdash; every group was counted <var>k</var>! times, and we pay the debt back by dividing.</p>
<div class="frm">C(<var>n</var>,&nbsp;<var>k</var>) = {F('<var>n</var>&nbsp;&middot;&nbsp;(<var>n</var>&nbsp;&minus;&nbsp;1)&nbsp;&middot;&nbsp;&hellip;&nbsp;&middot;&nbsp;(<var>n</var>&nbsp;&minus;&nbsp;<var>k</var>&nbsp;+&nbsp;1)','<var>k</var>!')} &nbsp;&middot;&nbsp; Properties: C(<var>n</var>,&nbsp;<var>k</var>) = C(<var>n</var>,&nbsp;<var>n</var>&nbsp;&minus;&nbsp;<var>k</var>); &nbsp;C(<var>n</var>,&nbsp;0) = C(<var>n</var>,&nbsp;<var>n</var>) = 1.</div>
<p><b>Group choices multiply.</b> A team of 2 boys and 2 girls: C(5,&nbsp;2)&nbsp;&middot;&nbsp;C(6,&nbsp;2) &mdash; the choices are independent. The symmetry C(<var>n</var>,&nbsp;<var>k</var>) = C(<var>n</var>,&nbsp;<var>n</var>&nbsp;&minus;&nbsp;<var>k</var>) saves arithmetic: compute C(10,&nbsp;8) as C(10,&nbsp;2) = 45. Useful images: handshakes among <var>n</var> people &mdash; C(<var>n</var>,&nbsp;2); diagonals of an <var>n</var>-gon &mdash; C(<var>n</var>,&nbsp;2)&nbsp;&minus;&nbsp;<var>n</var> (pairs of vertices minus the sides).</p>
<p><b>Stars and bars.</b> In how many ways can <var>n</var> identical candies be given to <var>k</var> children? Lay the candies in a row and insert <var>k</var>&nbsp;&minus;&nbsp;1 bars. If everyone gets at least one, the bars go into the gaps between candies: C(<var>n</var>&nbsp;&minus;&nbsp;1,&nbsp;<var>k</var>&nbsp;&minus;&nbsp;1) ways. If zero is allowed, first hand each child a &ldquo;virtual&rdquo; candy: C(<var>n</var>&nbsp;+&nbsp;<var>k</var>&nbsp;&minus;&nbsp;1,&nbsp;<var>k</var>&nbsp;&minus;&nbsp;1).</p>
<p><b>The trap of this lesson is double counting.</b> If you pick &ldquo;one special member first, then the rest&rdquo;, check: are you counting the same group several times with different &ldquo;specials&rdquo;? The standard cure: count directly with combinations, or divide by the number of repeats.</p>"""},
 'worked': [
  {'tag': {'ru': 'Разбор 1 · порядок не важен', 'en': 'Example 1 · order does not matter'},
   'q': {'ru': 'Из 10 учеников выбирают троих в команду (без ролей). Сколькими способами?',
         'en': 'Three students are chosen for a team (no roles) out of 10. In how many ways?'},
   'sol': {'ru': 'Порядок не важен: C(10,&nbsp;3) = 10&nbsp;&middot;&nbsp;9&nbsp;&middot;&nbsp;8&nbsp;/&nbsp;3! = 720/6 = <b>120</b>. Ответ 720 &mdash; классическая ловушка &laquo;порядок против выбора&raquo;: 720 считает тройки с ролями, каждая команда учтена 6 раз.',
          'en': 'Order does not matter: C(10,&nbsp;3) = 10&nbsp;&middot;&nbsp;9&nbsp;&middot;&nbsp;8&nbsp;/&nbsp;3! = 720/6 = <b>120</b>. The answer 720 is the classic order-versus-choice trap: 720 counts triples with roles, so every team is counted 6 times.'}},
  {'tag': {'ru': 'Разбор 2 · выбор по группам', 'en': 'Example 2 · choosing by groups'},
   'q': {'ru': 'В кружке 5 мальчиков и 6 девочек. Сколькими способами выбрать делегацию из 2 мальчиков и 2 девочек?',
         'en': 'A club has 5 boys and 6 girls. In how many ways can a delegation of 2 boys and 2 girls be chosen?'},
   'sol': {'ru': 'Выборы независимы и перемножаются: C(5,&nbsp;2)&nbsp;&middot;&nbsp;C(6,&nbsp;2) = 10&nbsp;&middot;&nbsp;15 = <b>150</b>. Ловушка &mdash; посчитать C(11,&nbsp;4): так вы разрешите делегации из трёх мальчиков.',
          'en': 'The choices are independent and multiply: C(5,&nbsp;2)&nbsp;&middot;&nbsp;C(6,&nbsp;2) = 10&nbsp;&middot;&nbsp;15 = <b>150</b>. The trap is computing C(11,&nbsp;4): that would allow delegations with three boys.'}},
  {'tag': {'ru': 'Разбор 3 · диагонали', 'en': 'Example 3 · diagonals'},
   'q': {'ru': 'Сколько диагоналей у выпуклого десятиугольника?',
         'en': 'How many diagonals does a convex decagon have?'},
   'sol': {'ru': 'Каждая пара вершин даёт отрезок: C(10,&nbsp;2) = 45. Из них 10 &mdash; стороны, а не диагонали: 45 &minus; 10 = <b>35</b>. Забыть вычесть стороны &mdash; дежурная ошибка; вторая &mdash; считать &laquo;10&nbsp;&middot;&nbsp;7&raquo; и не поделить на 2 (каждая диагональ имеет два конца).',
          'en': 'Every pair of vertices gives a segment: C(10,&nbsp;2) = 45. Of these, 10 are sides, not diagonals: 45 &minus; 10 = <b>35</b>. Forgetting to subtract the sides is the routine error; the second one is computing 10&nbsp;&middot;&nbsp;7 and not dividing by 2 (each diagonal has two endpoints).'}},
  {'tag': {'ru': 'Разбор 4 · звёзды и перегородки', 'en': 'Example 4 · stars and bars'},
   'q': {'ru': 'Сколько решений в натуральных числах у уравнения <var>x</var> + <var>y</var> + <var>z</var> = 10?',
         'en': 'How many solutions in positive integers does <var>x</var> + <var>y</var> + <var>z</var> = 10 have?'},
   'sol': {'ru': '10 звёзд в ряд, 9 промежутков, ставим 2 перегородки: C(9,&nbsp;2) = <b>36</b>. Ловушка &mdash; перепутать режимы: для целых неотрицательных было бы C(12,&nbsp;2) = 66. Прочитайте условие дважды: &laquo;натуральные&raquo; значит каждому хотя бы по единице.',
          'en': 'Ten stars in a row, 9 gaps, place 2 bars: C(9,&nbsp;2) = <b>36</b>. The trap is mixing up the modes: for nonnegative integers it would be C(12,&nbsp;2) = 66. Read the problem twice: &ldquo;positive&rdquo; means everyone gets at least one.'}},
 ],
 'selfp': [
  {'q': {'ru': 'Сколькими способами можно выбрать 3 книги из 8?', 'en': 'In how many ways can 3 books be chosen out of 8?'},
   'hint': {'ru': 'Порядок не важен: C(8,&nbsp;3).', 'en': 'Order does not matter: C(8,&nbsp;3).'},
   'sol': {'ru': 'C(8,&nbsp;3) = 8&nbsp;&middot;&nbsp;7&nbsp;&middot;&nbsp;6&nbsp;/&nbsp;6 = <b>56</b>.', 'en': 'C(8,&nbsp;3) = 8&nbsp;&middot;&nbsp;7&nbsp;&middot;&nbsp;6&nbsp;/&nbsp;6 = <b>56</b>.'}},
  {'q': {'ru': 'На встрече 12 человек, каждый пожал руку каждому по одному разу. Сколько было рукопожатий?', 'en': 'Twelve people at a meeting each shake hands with everyone else exactly once. How many handshakes are there?'},
   'hint': {'ru': 'Рукопожатие = пара людей.', 'en': 'A handshake = a pair of people.'},
   'sol': {'ru': 'C(12,&nbsp;2) = <b>66</b>.', 'en': 'C(12,&nbsp;2) = <b>66</b>.'}},
  {'q': {'ru': 'Из 6 мужчин и 4 женщин выбирают комиссию: 3 мужчины и 2 женщины. Сколькими способами?', 'en': 'A committee of 3 men and 2 women is chosen from 6 men and 4 women. In how many ways?'},
   'hint': {'ru': 'Выборы по группам перемножаются.', 'en': 'Group choices multiply.'},
   'sol': {'ru': 'C(6,&nbsp;3)&nbsp;&middot;&nbsp;C(4,&nbsp;2) = 20&nbsp;&middot;&nbsp;6 = <b>120</b>.', 'en': 'C(6,&nbsp;3)&nbsp;&middot;&nbsp;C(4,&nbsp;2) = 20&nbsp;&middot;&nbsp;6 = <b>120</b>.'}},
  {'q': {'ru': 'Сколько диагоналей у выпуклого двенадцатиугольника?', 'en': 'How many diagonals does a convex 12-gon have?'},
   'hint': {'ru': 'Пары вершин минус стороны.', 'en': 'Pairs of vertices minus the sides.'},
   'sol': {'ru': 'C(12,&nbsp;2) &minus; 12 = 66 &minus; 12 = <b>54</b>.', 'en': 'C(12,&nbsp;2) &minus; 12 = 66 &minus; 12 = <b>54</b>.'}},
  {'q': {'ru': 'В турнире каждый сыграл с каждым по одной партии, всего партий 45. Сколько было участников?', 'en': 'In a tournament every player played every other exactly once, 45 games in total. How many players were there?'},
   'hint': {'ru': 'C(<var>n</var>,&nbsp;2) = 45.', 'en': 'C(<var>n</var>,&nbsp;2) = 45.'},
   'sol': {'ru': '<var>n</var>(<var>n</var>&nbsp;&minus;&nbsp;1)/2 = 45, значит <var>n</var>(<var>n</var>&nbsp;&minus;&nbsp;1) = 90 и <var>n</var> = <b>10</b>.', 'en': '<var>n</var>(<var>n</var>&nbsp;&minus;&nbsp;1)/2 = 45, so <var>n</var>(<var>n</var>&nbsp;&minus;&nbsp;1) = 90 and <var>n</var> = <b>10</b>.'}},
  {'q': {'ru': 'Из 9 книг выбирают 5, но два тома энциклопедии нельзя брать одновременно. Сколькими способами?', 'en': 'Five books are chosen out of 9, but the two encyclopedia volumes cannot both be taken. In how many ways?'},
   'hint': {'ru': 'Все выборы минус те, где взяты оба тома.', 'en': 'All choices minus those containing both volumes.'},
   'sol': {'ru': 'C(9,&nbsp;5) &minus; C(7,&nbsp;3) = 126 &minus; 35 = <b>91</b> (если оба тома взяты, добираем 3 из 7).', 'en': 'C(9,&nbsp;5) &minus; C(7,&nbsp;3) = 126 &minus; 35 = <b>91</b> (if both volumes are in, we pick 3 more out of 7).'}},
  {'q': {'ru': 'Сколькими способами раздать 12 одинаковых конфет четырём детям так, чтобы каждый получил хотя бы одну?', 'en': 'In how many ways can 12 identical candies be given to four children so that each gets at least one?'},
   'hint': {'ru': '11 промежутков, 3 перегородки.', 'en': 'Eleven gaps, three bars.'},
   'sol': {'ru': 'C(11,&nbsp;3) = <b>165</b>.', 'en': 'C(11,&nbsp;3) = <b>165</b>.'}},
  {'q': {'ru': 'Сетка составлена из 5&nbsp;&times;&nbsp;4 единичных клеток (6 вертикальных и 5 горизонтальных линий). Сколько всего прямоугольников можно увидеть в этой сетке?', 'en': 'A grid is made of 5&nbsp;&times;&nbsp;4 unit cells (6 vertical and 5 horizontal lines). How many rectangles in total can be seen in this grid?'},
   'hint': {'ru': 'Прямоугольник = пара вертикальных линий и пара горизонтальных.', 'en': 'A rectangle = a pair of vertical lines and a pair of horizontal lines.'},
   'sol': {'ru': 'C(6,&nbsp;2)&nbsp;&middot;&nbsp;C(5,&nbsp;2) = 15&nbsp;&middot;&nbsp;10 = <b>150</b>. Никакого перебора размеров: две пары линий однозначно задают прямоугольник.', 'en': 'C(6,&nbsp;2)&nbsp;&middot;&nbsp;C(5,&nbsp;2) = 15&nbsp;&middot;&nbsp;10 = <b>150</b>. No size-by-size enumeration: two pairs of lines determine the rectangle uniquely.'}},
 ],
 'answers': {'ru': '56 · 66 · 120 · 54 · 10 · 91 · 165 · 150', 'en': '56, 66, 120, 54, 10, 91, 165, 150'},
 'routing': {'ru': 'Норма &mdash; 6 из 8. Ошибки в 1&ndash;2 &mdash; перечитать &laquo;порядок важен или нет&raquo;; в 3&ndash;5 &mdash; &laquo;выбор по группам&raquo; и образы (рукопожатия, диагонали); в 6 и 8 &mdash; выбор с запретом и пары линий; в 7 &mdash; &laquo;звёзды и перегородки&raquo;.',
             'en': 'Mastery bar: 6 of 8. For mistakes in 1&ndash;2, reread &ldquo;order matters or not&rdquo;; for 3&ndash;5, &ldquo;group choices&rdquo; and the images (handshakes, diagonals); for 6 and 8, choice with a ban and pairs of lines; for 7, &ldquo;stars and bars&rdquo;.'},
}
