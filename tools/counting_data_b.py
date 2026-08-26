# -*- coding: utf-8 -*-
"""Блок 4 «Комбинаторика и вероятность»: уроки 4.3–4.4, RU+EN."""

def F(a, b):
    return f'<span class="frac"><span>{a}</span><span>{b}</span></span>'

L43 = {
 'id': '4.3', 'anchor': 'u43',
 'title': {'ru': 'Кейсворк, дополнение, включения-исключения',
           'en': 'Casework, Complementary Counting, Inclusion-Exclusion'},
 'theory': {
  'ru': """
<p><b>Кейсворк &mdash; честный труд.</b> Если единой формулы нет, режьте задачу на непересекающиеся случаи и складывайте. Два требования к разрезу: случаи не пересекаются и вместе покрывают всё. Выбирайте параметр разреза так, чтобы случаев было мало: резать &laquo;по последней цифре&raquo; обычно лучше, чем &laquo;по первой&raquo;.</p>
<p><b>&laquo;Хотя бы один&raquo; &mdash; сигнал дополнения.</b> Считать &laquo;хотя бы один&raquo; напрямую &mdash; значит складывать десяток случаев и почти наверняка что-то посчитать дважды. Переверните: (хотя бы один) = (всего) &minus; (ни одного). &laquo;Ни одного&raquo; почти всегда считается одним произведением. Это самый прибыльный рефлекс всей комбинаторики.</p>
<div class="frm">|<var>A</var> &cup; <var>B</var>| = |<var>A</var>| + |<var>B</var>| &minus; |<var>A</var> &cap; <var>B</var>|. &nbsp;Для трёх: |<var>A</var> &cup; <var>B</var> &cup; <var>C</var>| = |<var>A</var>| + |<var>B</var>| + |<var>C</var>| &minus; |<var>A</var>&cap;<var>B</var>| &minus; |<var>A</var>&cap;<var>C</var>| &minus; |<var>B</var>&cap;<var>C</var>| + |<var>A</var>&cap;<var>B</var>&cap;<var>C</var>|.</div>
<p><b>Включения-исключения.</b> Сложили два множества &mdash; пересечение посчитано дважды, вычтите его один раз. С тремя множествами: сложить по одному, вычесть попарные, вернуть тройное. Для кратности: чисел от 1 до <var>N</var>, кратных <var>d</var>, ровно &lfloor;<var>N</var>/<var>d</var>&rfloor;; пересечение &laquo;кратно 3 и 5&raquo; &mdash; это кратно 15, НОК, а не произведению, если числа не взаимно просты.</p>
<p><b>Комбинируйте инструменты.</b> Запрет &laquo;<var>A</var> на первом месте&raquo; и &laquo;<var>B</var> на последнем&raquo; &mdash; это дополнение плюс включения-исключения: всего &minus; (плохие по <var>A</var>) &minus; (плохие по <var>B</var>) + (плохие по обоим). Прибавка в конце обязательна: дважды вычтенное надо вернуть.</p>""",
  'en': """
<p><b>Casework is honest labor.</b> When no single formula applies, cut the problem into non-overlapping cases and add. Two requirements for the cut: the cases must not overlap and together must cover everything. Choose the cutting parameter so that there are few cases: cutting &ldquo;by the last digit&rdquo; usually beats cutting &ldquo;by the first&rdquo;.</p>
<p><b>&ldquo;At least one&rdquo; is the signal for the complement.</b> Counting &ldquo;at least one&rdquo; directly means adding up a dozen cases and almost surely double-counting something. Flip it: (at least one) = (total) &minus; (none). &ldquo;None&rdquo; is almost always a single product. This is the most profitable reflex in all of counting.</p>
<div class="frm">|<var>A</var> &cup; <var>B</var>| = |<var>A</var>| + |<var>B</var>| &minus; |<var>A</var> &cap; <var>B</var>|. &nbsp;For three sets: |<var>A</var> &cup; <var>B</var> &cup; <var>C</var>| = |<var>A</var>| + |<var>B</var>| + |<var>C</var>| &minus; |<var>A</var>&cap;<var>B</var>| &minus; |<var>A</var>&cap;<var>C</var>| &minus; |<var>B</var>&cap;<var>C</var>| + |<var>A</var>&cap;<var>B</var>&cap;<var>C</var>|.</div>
<p><b>Inclusion-exclusion.</b> Add two sets and the intersection is counted twice &mdash; subtract it once. With three sets: add the singles, subtract the pairwise intersections, add the triple back. For divisibility: the count of numbers from 1 to <var>N</var> divisible by <var>d</var> is exactly &lfloor;<var>N</var>/<var>d</var>&rfloor;; the intersection &ldquo;divisible by 3 and 5&rdquo; means divisible by 15 &mdash; the LCM, not the product, when the numbers are not coprime.</p>
<p><b>Combine the tools.</b> The ban &ldquo;<var>A</var> not first&rdquo; and &ldquo;<var>B</var> not last&rdquo; is complement plus inclusion-exclusion: total &minus; (bad by <var>A</var>) &minus; (bad by <var>B</var>) + (bad by both). The final addition is mandatory: what was subtracted twice must be given back.</p>"""},
 'worked': [
  {'tag': {'ru': 'Разбор 1 · дополнение', 'en': 'Example 1 · complement'},
   'q': {'ru': 'Сколько трёхзначных чисел содержат хотя бы одну цифру 7?',
         'en': 'How many three-digit numbers contain at least one digit 7?'},
   'sol': {'ru': '&laquo;Хотя бы одна&raquo; &mdash; переворачиваем. Без семёрок: 8&nbsp;&middot;&nbsp;9&nbsp;&middot;&nbsp;9 = 648. Всего трёхзначных 900. Ответ: 900 &minus; 648 = <b>252</b>. Прямой подсчёт (7 на первом месте, на втором, на третьем&hellip;) утонет в двойном счёте чисел вроде 774.',
          'en': '&ldquo;At least one&rdquo; &mdash; flip it. No sevens at all: 8&nbsp;&middot;&nbsp;9&nbsp;&middot;&nbsp;9 = 648. Total three-digit numbers: 900. Answer: 900 &minus; 648 = <b>252</b>. A direct count (7 in the first place, in the second, in the third&hellip;) drowns in double-counting numbers like 774.'}},
  {'tag': {'ru': 'Разбор 2 · два множества', 'en': 'Example 2 · two sets'},
   'q': {'ru': 'Сколько чисел от 1 до 100 делятся на 3 или на 5?',
         'en': 'How many integers from 1 to 100 are divisible by 3 or by 5?'},
   'sol': {'ru': 'Кратных 3 &mdash; 33, кратных 5 &mdash; 20, кратных 15 &mdash; 6. По формуле: 33 + 20 &minus; 6 = <b>47</b>. Не вычесть пересечение &mdash; главный провал: числа 15, 30, &hellip; посчитаны в обоих списках.',
          'en': 'Divisible by 3: 33; by 5: 20; by 15: 6. By the formula: 33 + 20 &minus; 6 = <b>47</b>. Skipping the subtraction is the main failure: 15, 30, &hellip; are counted in both lists.'}},
  {'tag': {'ru': 'Разбор 3 · кейсворк', 'en': 'Example 3 · casework'},
   'q': {'ru': 'Сколько трёхзначных чисел имеют сумму цифр 5?',
         'en': 'How many three-digit numbers have digit sum 5?'},
   'sol': {'ru': 'Кейсворк по первой цифре <var>a</var> = 1, 2, 3, 4, 5: остаток 5&nbsp;&minus;&nbsp;<var>a</var> раскладывается на две цифры соответственно 5, 4, 3, 2, 1 способами. Сумма 5 + 4 + 3 + 2 + 1 = <b>15</b>. Проверка разреза: случаи не пересекаются и покрывают всё. (Знаток заметит здесь звёзды и перегородки &mdash; ответ тот же.)',
          'en': 'Casework on the first digit <var>a</var> = 1, 2, 3, 4, 5: the remainder 5&nbsp;&minus;&nbsp;<var>a</var> splits into two digits in 5, 4, 3, 2, 1 ways respectively. Sum: 5 + 4 + 3 + 2 + 1 = <b>15</b>. Check the cut: the cases do not overlap and cover everything. (A connoisseur will spot stars and bars here &mdash; same answer.)'}},
  {'tag': {'ru': 'Разбор 4 · три множества', 'en': 'Example 4 · three sets'},
   'q': {'ru': 'Из 100 школьников 60 ходят на математику, 50 на физику, 40 на химию; 30 &mdash; на математику и физику, 25 &mdash; на математику и химию, 20 &mdash; на физику и химию, 10 &mdash; на все три. Сколько школьников не ходят никуда?',
         'en': 'Of 100 students, 60 take math, 50 physics, 40 chemistry; 30 take math and physics, 25 math and chemistry, 20 physics and chemistry, and 10 take all three. How many students take none of the subjects?'},
   'sol': {'ru': 'Объединение: 60 + 50 + 40 &minus; 30 &minus; 25 &minus; 20 + 10 = 85. Никуда не ходят 100 &minus; 85 = <b>15</b>. Ловушка &mdash; забыть вернуть тройное пересечение: те, кто ходит на все три, трижды прибавлены и трижды вычтены, их надо вернуть.',
          'en': 'The union: 60 + 50 + 40 &minus; 30 &minus; 25 &minus; 20 + 10 = 85. Taking none: 100 &minus; 85 = <b>15</b>. The trap is forgetting to add the triple intersection back: students taking all three were added three times and subtracted three times, so they must be restored.'}},
 ],
 'selfp': [
  {'q': {'ru': 'Сколько двузначных чисел имеют сумму цифр 9?', 'en': 'How many two-digit numbers have digit sum 9?'},
   'hint': {'ru': 'Переберите первую цифру: от 1 до 9.', 'en': 'Run through the first digit: 1 to 9.'},
   'sol': {'ru': '18, 27, &hellip;, 90: по одному на каждую первую цифру, всего <b>9</b>.', 'en': '18, 27, &hellip;, 90: one for each first digit, <b>9</b> in total.'}},
  {'q': {'ru': 'Монету бросают 5 раз. Сколько последовательностей исходов содержат хотя бы одного орла?', 'en': 'A coin is tossed 5 times. How many outcome sequences contain at least one head?'},
   'hint': {'ru': '&laquo;Хотя бы один&raquo; &mdash; через &laquo;ни одного&raquo;.', 'en': '&ldquo;At least one&rdquo; &mdash; via &ldquo;none&rdquo;.'},
   'sol': {'ru': '2<sup>5</sup> &minus; 1 = <b>31</b>: без орлов только одна последовательность, все решки.', 'en': '2<sup>5</sup> &minus; 1 = <b>31</b>: only one sequence has no heads &mdash; all tails.'}},
  {'q': {'ru': 'Сколько чисел от 1 до 60 делятся на 4 или на 6?', 'en': 'How many integers from 1 to 60 are divisible by 4 or by 6?'},
   'hint': {'ru': 'Пересечение &mdash; кратные НОК(4,&nbsp;6) = 12, а не 24.', 'en': 'The intersection is multiples of lcm(4,&nbsp;6) = 12, not 24.'},
   'sol': {'ru': '15 + 10 &minus; 5 = <b>20</b>.', 'en': '15 + 10 &minus; 5 = <b>20</b>.'}},
  {'q': {'ru': 'В классе 25 человек: 17 любят математику, 15 &mdash; английский, и каждый любит хотя бы один из предметов. Сколько человек любят оба?', 'en': 'A class has 25 students: 17 like math, 15 like English, and every student likes at least one of the two. How many like both?'},
   'hint': {'ru': 'Объединение известно: 25.', 'en': 'The union is known: 25.'},
   'sol': {'ru': '17 + 15 &minus; <var>x</var> = 25, значит <var>x</var> = <b>7</b>.', 'en': '17 + 15 &minus; <var>x</var> = 25, so <var>x</var> = <b>7</b>.'}},
  {'q': {'ru': 'Сколько четырёхзначных чисел содержат хотя бы один ноль?', 'en': 'How many four-digit numbers contain at least one digit 0?'},
   'hint': {'ru': 'Всего минус &laquo;без нулей&raquo;.', 'en': 'Total minus &ldquo;no zeros&rdquo;.'},
   'sol': {'ru': '9000 &minus; 9<sup>4</sup> = 9000 &minus; 6561 = <b>2439</b>.', 'en': '9000 &minus; 9<sup>4</sup> = 9000 &minus; 6561 = <b>2439</b>.'}},
  {'q': {'ru': 'Из 5 мужчин и 4 женщин выбирают комиссию из трёх человек, в которой есть хотя бы одна женщина. Сколькими способами?', 'en': 'A committee of three with at least one woman is chosen from 5 men and 4 women. In how many ways?'},
   'hint': {'ru': 'Дополнение: все тройки минус чисто мужские.', 'en': 'Complement: all triples minus the all-male ones.'},
   'sol': {'ru': 'C(9,&nbsp;3) &minus; C(5,&nbsp;3) = 84 &minus; 10 = <b>74</b>.', 'en': 'C(9,&nbsp;3) &minus; C(5,&nbsp;3) = 84 &minus; 10 = <b>74</b>.'}},
  {'q': {'ru': 'Сколько чисел от 1 до 1000 делятся хотя бы на одно из чисел 2, 3, 5?', 'en': 'How many integers from 1 to 1000 are divisible by at least one of 2, 3, 5?'},
   'hint': {'ru': 'Три множества: 500 + 333 + 200, потом попарные и тройное.', 'en': 'Three sets: 500 + 333 + 200, then the pairwise and triple terms.'},
   'sol': {'ru': '500 + 333 + 200 &minus; 166 &minus; 100 &minus; 66 + 33 = <b>734</b>.', 'en': '500 + 333 + 200 &minus; 166 &minus; 100 &minus; 66 + 33 = <b>734</b>.'}},
  {'q': {'ru': 'Сколько перестановок букв A, B, C, D, E таких, что A не стоит первой, а B не стоит последней?', 'en': 'How many permutations of the letters A, B, C, D, E have A not in the first position and B not in the last?'},
   'hint': {'ru': 'Всего &minus; (A первая) &minus; (B последняя) + (обе беды сразу).', 'en': 'Total &minus; (A first) &minus; (B last) + (both at once).'},
   'sol': {'ru': '120 &minus; 24 &minus; 24 + 6 = <b>78</b>. Слагаемое +6 обязательно: перестановки с обеими бедами вычтены дважды.', 'en': '120 &minus; 24 &minus; 24 + 6 = <b>78</b>. The +6 term is mandatory: permutations with both offenses were subtracted twice.'}},
 ],
 'answers': {'ru': '9 · 31 · 20 · 7 · 2439 · 74 · 734 · 78', 'en': '9, 31, 20, 7, 2439, 74, 734, 78'},
 'routing': {'ru': 'Норма &mdash; 6 из 8. Ошибки в 1 &mdash; перечитать &laquo;кейсворк&raquo;; во 2, 5, 6 &mdash; &laquo;хотя бы один через дополнение&raquo;; в 3&ndash;4 и 7 &mdash; &laquo;включения-исключения&raquo; (и НОК!); в 8 &mdash; &laquo;комбинируйте инструменты&raquo;.',
             'en': 'Mastery bar: 6 of 8. For mistakes in 1, reread &ldquo;casework&rdquo;; in 2, 5, 6, &ldquo;at least one via the complement&rdquo;; in 3&ndash;4 and 7, &ldquo;inclusion-exclusion&rdquo; (and the LCM!); in 8, &ldquo;combine the tools&rdquo;.'},
}

L44 = {
 'id': '4.4', 'anchor': 'u44',
 'title': {'ru': 'Вероятность через подсчёт: кубики, монеты, карты',
           'en': 'Probability via Counting: Dice, Coins, Cards'},
 'theory': {
  'ru': f"""
<p><b>Вероятность = дробь из двух подсчётов.</b> Если все исходы равновозможны, то P = (благоприятные)&nbsp;/&nbsp;(все). Вся трудность &mdash; в комбинаторике числителя и знаменателя, поэтому уроки 4.1&ndash;4.3 работают и здесь. Железное правило: числитель и знаменатель считайте <b>в одной и той же модели</b> &mdash; либо оба с учётом порядка, либо оба без.</p>
<div class="frm">P(<var>A</var>) = {F('число благоприятных исходов','число всех исходов')} &nbsp;&middot;&nbsp; P(хотя бы один) = 1 &minus; P(ни одного).</div>
<p><b>Стандартные полигоны.</b> Два кубика: 36 упорядоченных пар, и держите их упорядоченными &mdash; сумма 8 набирается пятью парами (2;&nbsp;6), (3;&nbsp;5), (4;&nbsp;4), (5;&nbsp;3), (6;&nbsp;2), а не тремя. Монеты: <var>n</var> бросков &mdash; 2<sup><var>n</var></sup> последовательностей, ровно <var>k</var> орлов &mdash; C(<var>n</var>,&nbsp;<var>k</var>) из них. Колода 52 карты: 4 масти по 13 рангов; две карты без возврата удобно считать по шагам: P(обе черви) = 13/52&nbsp;&middot;&nbsp;12/51 &mdash; вторая дробь уже &laquo;знает&raquo; про первую карту.</p>
<p><b>Геометрическая вероятность.</b> Когда исходов бесконечно много (точка на отрезке, пара чисел), вероятность = (длина или площадь благоприятной области)&nbsp;/&nbsp;(длина или площадь всей). Рисуйте картинку: квадрат возможностей и область условия в нём.</p>
<p><b>Ответ &mdash; несократимая дробь.</b> На AMC вероятность почти всегда дана в виде дроби, и неверно сокращённая дробь стоит среди вариантов. И проверка здравым смыслом обязательна: вероятность &laquo;хотя бы один&raquo; не меньше, чем &laquo;ровно один&raquo;, а любая вероятность живёт между 0 и 1.</p>""",
  'en': f"""
<p><b>Probability = a fraction made of two counts.</b> When all outcomes are equally likely, P = (favorable)&nbsp;/&nbsp;(total). All the difficulty lives in the counting of numerator and denominator, so lessons 4.1&ndash;4.3 keep working here. The iron rule: count numerator and denominator <b>in the same model</b> &mdash; either both ordered, or both unordered.</p>
<div class="frm">P(<var>A</var>) = {F('number of favorable outcomes','number of all outcomes')} &nbsp;&middot;&nbsp; P(at least one) = 1 &minus; P(none).</div>
<p><b>The standard playgrounds.</b> Two dice: 36 ordered pairs &mdash; keep them ordered: the sum 8 comes from five pairs (2, 6), (3, 5), (4, 4), (5, 3), (6, 2), not three. Coins: <var>n</var> tosses give 2<sup><var>n</var></sup> sequences, and exactly <var>k</var> heads happens in C(<var>n</var>,&nbsp;<var>k</var>) of them. A standard 52-card deck: 4 suits of 13 ranks; two cards without replacement are best handled step by step: P(both hearts) = 13/52&nbsp;&middot;&nbsp;12/51 &mdash; the second fraction already &ldquo;knows&rdquo; about the first card.</p>
<p><b>Geometric probability.</b> When there are infinitely many outcomes (a point on a segment, a pair of numbers), probability = (length or area of the favorable region)&nbsp;/&nbsp;(length or area of the whole). Draw the picture: the square of possibilities and the condition&rsquo;s region inside it.</p>
<p><b>The answer is a fraction in lowest terms.</b> On the AMC a probability is almost always a fraction, and a wrongly reduced fraction sits among the choices. Sanity checks are mandatory: &ldquo;at least one&rdquo; is at least as likely as &ldquo;exactly one&rdquo;, and every probability lives between 0 and 1.</p>"""},
 'worked': [
  {'tag': {'ru': 'Разбор 1 · два кубика', 'en': 'Example 1 · two dice'},
   'q': {'ru': 'Бросают два кубика. Какова вероятность, что сумма равна 8?',
         'en': 'Two dice are rolled. What is the probability that the sum is 8?'},
   'sol': {'ru': f'Упорядоченных пар 36. Сумма 8: (2;&nbsp;6), (3;&nbsp;5), (4;&nbsp;4), (5;&nbsp;3), (6;&nbsp;2) &mdash; пять пар. P = {F("5","36")}. Ловушка &mdash; счесть (2;&nbsp;6) и (6;&nbsp;2) одним исходом: тогда исходы перестают быть равновозможными, ведь (4;&nbsp;4) встречается вдвое реже, чем &laquo;2 и 6 в каком-то порядке&raquo;.',
          'en': f'There are 36 ordered pairs. Sum 8: (2, 6), (3, 5), (4, 4), (5, 3), (6, 2) &mdash; five pairs. P = {F("5","36")}. The trap is treating (2, 6) and (6, 2) as one outcome: then the outcomes stop being equally likely, since (4, 4) occurs half as often as &ldquo;2 and 6 in some order&rdquo;.'}},
  {'tag': {'ru': 'Разбор 2 · монеты', 'en': 'Example 2 · coins'},
   'q': {'ru': 'Монету бросают три раза. Какова вероятность ровно двух орлов?',
         'en': 'A coin is tossed three times. What is the probability of exactly two heads?'},
   'sol': {'ru': f'Последовательностей 2<sup>3</sup> = 8; ровно два орла &mdash; C(3,&nbsp;2) = 3 из них (ООР, ОРО, РОО). P = {F("3","8")}. Ошибка &laquo;исходов четыре: 0, 1, 2, 3 орла&raquo; забывает, что эти четыре исхода не равновозможны.',
          'en': f'There are 2<sup>3</sup> = 8 sequences; exactly two heads &mdash; C(3,&nbsp;2) = 3 of them (HHT, HTH, THH). P = {F("3","8")}. The error &ldquo;four outcomes: 0, 1, 2, 3 heads&rdquo; forgets that those four outcomes are not equally likely.'}},
  {'tag': {'ru': 'Разбор 3 · карты', 'en': 'Example 3 · cards'},
   'q': {'ru': 'Из колоды 52 карты вытягивают две без возврата. Какова вероятность, что обе &mdash; черви?',
         'en': 'Two cards are drawn without replacement from a standard 52-card deck. What is the probability that both are hearts?'},
   'sol': {'ru': f'По шагам: {F("13","52")}&nbsp;&middot;&nbsp;{F("12","51")} = {F("1","4")}&nbsp;&middot;&nbsp;{F("4","17")} = {F("1","17")}. Вторая дробь &mdash; 12/51, не 13/52: одна черва уже ушла. Тот же ответ через сочетания: C(13,&nbsp;2)/C(52,&nbsp;2) &mdash; модель без порядка в числителе И в знаменателе.',
          'en': f'Step by step: {F("13","52")}&nbsp;&middot;&nbsp;{F("12","51")} = {F("1","4")}&nbsp;&middot;&nbsp;{F("4","17")} = {F("1","17")}. The second fraction is 12/51, not 13/52: one heart is already gone. The same answer via combinations: C(13,&nbsp;2)/C(52,&nbsp;2) &mdash; the unordered model in the numerator AND the denominator.'}},
  {'tag': {'ru': 'Разбор 4 · геометрическая', 'en': 'Example 4 · geometric'},
   'q': {'ru': 'Числа <var>x</var> и <var>y</var> выбирают независимо и равномерно из отрезка [0;&nbsp;1]. Какова вероятность, что <var>x</var> + <var>y</var> &lt; 1/2?',
         'en': 'Numbers <var>x</var> and <var>y</var> are chosen independently and uniformly from [0,&nbsp;1]. What is the probability that <var>x</var> + <var>y</var> &lt; 1/2?'},
   'sol': {'ru': f'Пара (<var>x</var>,&nbsp;<var>y</var>) &mdash; точка единичного квадрата площади 1. Условие вырезает треугольник с катетами 1/2: площадь (1/2)&nbsp;&middot;&nbsp;(1/2)&nbsp;&middot;&nbsp;(1/2) = {F("1","8")}. Ответ <b>{F("1","8")}</b>. Перебор исходов здесь невозможен в принципе &mdash; только площадь.',
          'en': f'The pair (<var>x</var>,&nbsp;<var>y</var>) is a point of the unit square of area 1. The condition cuts off a right triangle with legs 1/2: area (1/2)&nbsp;&middot;&nbsp;(1/2)&nbsp;&middot;&nbsp;(1/2) = {F("1","8")}. Answer: <b>{F("1","8")}</b>. Enumerating outcomes is impossible here in principle &mdash; only area works.'}},
 ],
 'selfp': [
  {'q': {'ru': 'Бросают один кубик. Какова вероятность выпадения простого числа?', 'en': 'A die is rolled once. What is the probability of rolling a prime number?'},
   'hint': {'ru': 'Простые на кубике: 2, 3, 5.', 'en': 'The primes on a die: 2, 3, 5.'},
   'sol': {'ru': f'3 из 6: <b>{F("1","2")}</b>. Единица не простое!', 'en': f'3 out of 6: <b>{F("1","2")}</b>. One is not prime!'}},
  {'q': {'ru': 'Монету бросают 4 раза. Какова вероятность ровно двух орлов?', 'en': 'A coin is tossed 4 times. What is the probability of exactly two heads?'},
   'hint': {'ru': 'C(4,&nbsp;2) благоприятных из 2<sup>4</sup>.', 'en': 'C(4,&nbsp;2) favorable out of 2<sup>4</sup>.'},
   'sol': {'ru': f'6/16 = <b>{F("3","8")}</b>.', 'en': f'6/16 = <b>{F("3","8")}</b>.'}},
  {'q': {'ru': 'Бросают два кубика. Какова вероятность, что сумма равна 7?', 'en': 'Two dice are rolled. What is the probability that the sum is 7?'},
   'hint': {'ru': 'Сколько упорядоченных пар дают 7?', 'en': 'How many ordered pairs give 7?'},
   'sol': {'ru': f'Шесть пар из 36: <b>{F("1","6")}</b>. Сумма 7 &mdash; самая вероятная на двух кубиках.', 'en': f'Six pairs out of 36: <b>{F("1","6")}</b>. Seven is the most likely sum on two dice.'}},
  {'q': {'ru': 'Из колоды 52 карты берут одну. Какова вероятность, что это картинка (валет, дама или король)?', 'en': 'One card is drawn from a standard 52-card deck. What is the probability that it is a face card (jack, queen, or king)?'},
   'hint': {'ru': 'По три картинки в каждой из четырёх мастей.', 'en': 'Three face cards in each of the four suits.'},
   'sol': {'ru': f'12/52 = <b>{F("3","13")}</b>.', 'en': f'12/52 = <b>{F("3","13")}</b>.'}},
  {'q': {'ru': 'Бросают два кубика. Какова вероятность, что выпадет хотя бы одна шестёрка?', 'en': 'Two dice are rolled. What is the probability that at least one six appears?'},
   'hint': {'ru': '1 &minus; P(ни одной шестёрки).', 'en': '1 &minus; P(no sixes).'},
   'sol': {'ru': f'1 &minus; (5/6)<sup>2</sup> = 1 &minus; 25/36 = <b>{F("11","36")}</b>.', 'en': f'1 &minus; (5/6)<sup>2</sup> = 1 &minus; 25/36 = <b>{F("11","36")}</b>.'}},
  {'q': {'ru': 'В мешке 5 красных и 3 синих шара. Наугад вынимают два. Какова вероятность, что они разного цвета?', 'en': 'A bag holds 5 red and 3 blue marbles. Two are drawn at random. What is the probability that they are different colors?'},
   'hint': {'ru': 'Пар &laquo;красный + синий&raquo; ровно 5&nbsp;&middot;&nbsp;3.', 'en': 'There are exactly 5&nbsp;&middot;&nbsp;3 red-blue pairs.'},
   'sol': {'ru': f'5&nbsp;&middot;&nbsp;3 = 15 разноцветных пар из C(8,&nbsp;2) = 28: <b>{F("15","28")}</b>.', 'en': f'5&nbsp;&middot;&nbsp;3 = 15 mixed pairs out of C(8,&nbsp;2) = 28: <b>{F("15","28")}</b>.'}},
  {'q': {'ru': 'Из колоды 52 карты вытягивают две без возврата. Какова вероятность, что обе &mdash; тузы?', 'en': 'Two cards are drawn without replacement from a standard 52-card deck. What is the probability that both are aces?'},
   'hint': {'ru': 'По шагам: 4/52, затем 3/51.', 'en': 'Step by step: 4/52, then 3/51.'},
   'sol': {'ru': f'{F("4","52")}&nbsp;&middot;&nbsp;{F("3","51")} = <b>{F("1","221")}</b>.', 'en': f'{F("4","52")}&nbsp;&middot;&nbsp;{F("3","51")} = <b>{F("1","221")}</b>.'}},
  {'q': {'ru': 'Числа <var>x</var> и <var>y</var> выбирают независимо и равномерно из отрезка [0;&nbsp;3]. Какова вероятность, что <var>x</var> &gt; <var>y</var> + 1?', 'en': 'Numbers <var>x</var> and <var>y</var> are chosen independently and uniformly from [0,&nbsp;3]. What is the probability that <var>x</var> &gt; <var>y</var> + 1?'},
   'hint': {'ru': 'Квадрат 3&nbsp;&times;&nbsp;3; условие вырезает треугольник.', 'en': 'A 3&nbsp;&times;&nbsp;3 square; the condition cuts off a triangle.'},
   'sol': {'ru': f'Область <var>x</var> &minus; <var>y</var> &gt; 1 &mdash; треугольник с катетами 2, площадь 2. Вероятность 2/9: <b>{F("2","9")}</b>.', 'en': f'The region <var>x</var> &minus; <var>y</var> &gt; 1 is a right triangle with legs 2, area 2. Probability 2/9: <b>{F("2","9")}</b>.'}},
 ],
 'answers': {'ru': '1/2 · 3/8 · 1/6 · 3/13 · 11/36 · 15/28 · 1/221 · 2/9', 'en': '1/2, 3/8, 1/6, 3/13, 11/36, 15/28, 1/221, 2/9'},
 'routing': {'ru': 'Норма &mdash; 6 из 8. Ошибки в 1&ndash;3 &mdash; перечитать &laquo;дробь из двух подсчётов&raquo; и &laquo;стандартные полигоны&raquo;; в 4 и 7 &mdash; карты без возврата; в 5 &mdash; &laquo;хотя бы один&raquo; через дополнение; в 6 &mdash; одна модель в числителе и знаменателе; в 8 &mdash; &laquo;геометрическая вероятность&raquo;.',
             'en': 'Mastery bar: 6 of 8. For mistakes in 1&ndash;3, reread &ldquo;a fraction made of two counts&rdquo; and &ldquo;the standard playgrounds&rdquo;; in 4 and 7, cards without replacement; in 5, &ldquo;at least one&rdquo; via the complement; in 6, one model for numerator and denominator; in 8, &ldquo;geometric probability&rdquo;.'},
}
