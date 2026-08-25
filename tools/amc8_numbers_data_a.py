# -*- coding: utf-8 -*-
"""AMC 8, блок 1 «Числа и арифметика»: уроки 1.1–1.2, RU+EN."""

def F(a, b):
    return f'<span class="frac"><span>{a}</span><span>{b}</span></span>'

L11 = {
 'id': '1.1', 'anchor': 'u11',
 'title': {'ru': 'Дроби: сравнение и действия', 'en': 'Fractions: Comparing and Operations'},
 'theory': {
  'ru': f"""
<p><b>Сравнение дробей.</b> Три способа, от быстрого к надёжному: сравнить с половиной (у {F('5','9')} числитель больше половины знаменателя &mdash; она больше {F('1','2')}); перекрёстное умножение ({F('2','5')} против {F('3','8')}: числитель первой дроби на чужой знаменатель &mdash; 2&middot;8 = 16, числитель второй &mdash; 3&middot;5 = 15; больше произведение у первой, значит {F('2','5')} больше); общий знаменатель.</p>
<div class="frm">Дробь от числа = умножение: {F('3','5')} от 45 &mdash; это 45&nbsp;&middot;&nbsp;3/5 = 27. Сначала делите на знаменатель, потом умножайте. Обратная задача &mdash; число по его дроби: если {F('2','3')} числа равны 18, то одна треть равна 9, а всё число 27.</div>
<p><b>Сложение и вычитание.</b> Привести к общему знаменателю (наименьшему!): {F('1','2')} + {F('1','3')} = {F('3','6')} + {F('2','6')} = {F('5','6')}. Ответ всегда сокращайте.</p>
<p><b>Задачи &laquo;съели часть, потом часть остатка&raquo;.</b> Считайте по шагам и следите, ОТ ЧЕГО берётся дробь: вторая дробь почти всегда берётся от остатка, а не от исходного числа. Это главная ловушка всех задач на дроби.</p>""",
  'en': f"""
<p><b>Comparing fractions.</b> Three ways, fastest first: compare with one half (in {F('5','9')} the numerator is more than half the denominator, so it is greater than {F('1','2')}); cross-multiplication ({F('2','5')} vs {F('3','8')}: multiply each numerator by the other fraction&rsquo;s denominator &mdash; 2&middot;8 = 16 against 3&middot;5 = 15; the larger product belongs to the larger fraction, so {F('2','5')} wins); common denominators.</p>
<div class="frm">A fraction of a number means multiplication: {F('3','5')} of 45 is 45&nbsp;&middot;&nbsp;3/5 = 27. Divide by the denominator first, then multiply. The reverse problem &mdash; a number from its fraction: if {F('2','3')} of a number is 18, then one third is 9, so the number is 27.</div>
<p><b>Adding and subtracting.</b> Use the least common denominator: {F('1','2')} + {F('1','3')} = {F('3','6')} + {F('2','6')} = {F('5','6')}. Always reduce the answer.</p>
<p><b>&ldquo;Part of what&rsquo;s left&rdquo; problems.</b> Work step by step and watch WHAT each fraction is taken of: the second fraction is almost always taken of the remainder, not of the original number. That is the number one trap in fraction problems.</p>"""},
 'worked': [
  {'tag': {'ru': 'Разбор 1 · сравнение', 'en': 'Example 1 · comparing'},
   'q': {'ru': f'Что больше: {F("3","7")} или {F("4","9")}?', 'en': f'Which is larger: {F("3","7")} or {F("4","9")}?'},
   'sol': {'ru': f'Перекрёстно: 3&middot;9 = 27 и 4&middot;7 = 28. Больше та дробь, чьё произведение больше: <b>{F("4","9")}</b>. Способ работает всегда и без общего знаменателя.',
          'en': f'Cross-multiply: 3&middot;9 = 27 and 4&middot;7 = 28. The larger product marks the larger fraction: <b>{F("4","9")}</b>. The method always works, no common denominator needed.'}},
  {'tag': {'ru': 'Разбор 2 · сложение', 'en': 'Example 2 · addition'},
   'q': {'ru': f'Вычислите {F("2","3")} + {F("1","4")}.', 'en': f'Compute {F("2","3")} + {F("1","4")}.'},
   'sol': {'ru': f'Наименьший общий знаменатель 12: {F("8","12")} + {F("3","12")} = <b>{F("11","12")}</b>. Складывать числители и знаменатели по отдельности (2+1 над 3+4) &mdash; классическая ошибка.',
          'en': f'The least common denominator is 12: {F("8","12")} + {F("3","12")} = <b>{F("11","12")}</b>. Adding numerators and denominators separately (2+1 over 3+4) is the classic mistake.'}},
  {'tag': {'ru': 'Разбор 3 · дробь от числа', 'en': 'Example 3 · fraction of a number'},
   'q': {'ru': f'Найдите {F("3","8")} от 56.', 'en': f'Find {F("3","8")} of 56.'},
   'sol': {'ru': '56/8 = 7, затем 7&middot;3 = <b>21</b>. Сначала деление, потом умножение &mdash; числа остаются маленькими.',
          'en': '56/8 = 7, then 7&middot;3 = <b>21</b>. Divide first, multiply after &mdash; the numbers stay small.'}},
  {'tag': {'ru': 'Разбор 4 · часть остатка', 'en': 'Example 4 · part of the rest'},
   'q': {'ru': f'В коробке было 30 конфет. Съели {F("2","5")} всех конфет, а потом {F("1","3")} остатка. Сколько конфет осталось?',
         'en': f'A box held 30 candies. First {F("2","5")} of all the candies were eaten, then {F("1","3")} of the rest. How many candies are left?'},
   'sol': {'ru': 'Шаг 1: съели 30&middot;2/5 = 12, осталось 18. Шаг 2: съели 18&middot;1/3 = 6, осталось <b>12</b>. Ловушка &mdash; взять 1/3 от 30: вторая дробь берётся от остатка.',
          'en': 'Step 1: 30&middot;2/5 = 12 eaten, 18 left. Step 2: 18&middot;1/3 = 6 eaten, <b>12</b> left. The trap is taking 1/3 of 30: the second fraction applies to the remainder.'}},
 ],
 'selfp': [
  {'q': {'ru': f'Сократите дробь {F("18","24")}.', 'en': f'Write {F("18","24")} in lowest terms.'},
   'hint': {'ru': 'Найдите общий делитель числителя и знаменателя.', 'en': 'Find a common divisor of the numerator and denominator.'},
   'sol': {'ru': f'Делим на 6: <b>{F("3","4")}</b>.', 'en': f'Divide by 6: <b>{F("3","4")}</b>.'}},
  {'q': {'ru': f'Что больше: {F("5","8")} или {F("7","12")}?', 'en': f'Which is larger: {F("5","8")} or {F("7","12")}?'},
   'hint': {'ru': 'Перекрёстное умножение.', 'en': 'Cross-multiply.'},
   'sol': {'ru': f'5&middot;12 = 60 больше 7&middot;8 = 56: <b>{F("5","8")}</b>.', 'en': f'5&middot;12 = 60 is more than 7&middot;8 = 56: <b>{F("5","8")}</b>.'}},
  {'q': {'ru': f'Вычислите {F("5","6")} &minus; {F("1","2")}.', 'en': f'Compute {F("5","6")} &minus; {F("1","2")}.'},
   'hint': {'ru': 'Общий знаменатель 6.', 'en': 'Common denominator 6.'},
   'sol': {'ru': f'{F("5","6")} &minus; {F("3","6")} = {F("2","6")} = <b>{F("1","3")}</b>.', 'en': f'{F("5","6")} &minus; {F("3","6")} = {F("2","6")} = <b>{F("1","3")}</b>.'}},
  {'q': {'ru': f'Найдите {F("2","9")} от 63.', 'en': f'Find {F("2","9")} of 63.'},
   'hint': {'ru': 'Сначала разделите на 9.', 'en': 'Divide by 9 first.'},
   'sol': {'ru': '63/9 = 7, дальше 7&middot;2 = <b>14</b>.', 'en': '63/9 = 7, then 7&middot;2 = <b>14</b>.'}},
  {'q': {'ru': f'{F("2","7")} некоторого числа равны 10. Найдите это число.', 'en': f'{F("2","7")} of a number equals 10. Find the number.'},
   'hint': {'ru': 'Сначала узнайте, чему равна одна седьмая числа.', 'en': 'First find what one seventh of the number is.'},
   'sol': {'ru': 'Если 2/7 &mdash; это 10, то 1/7 &mdash; это 5, а всё число <b>35</b>.', 'en': 'If 2/7 is 10, then 1/7 is 5, so the number is <b>35</b>.'}},
  {'q': {'ru': f'Вычислите {F("1","2")} + {F("1","3")} + {F("1","6")}.', 'en': f'Compute {F("1","2")} + {F("1","3")} + {F("1","6")}.'},
   'hint': {'ru': 'Общий знаменатель 6.', 'en': 'Common denominator 6.'},
   'sol': {'ru': f'{F("3","6")} + {F("2","6")} + {F("1","6")} = <b>1</b>.', 'en': f'{F("3","6")} + {F("2","6")} + {F("1","6")} = <b>1</b>.'}},
  {'q': {'ru': f'На полке 24 книги, {F("5","8")} из них &mdash; сказки. Сколько книг &mdash; не сказки?', 'en': f'A shelf holds 24 books, and {F("5","8")} of them are fairy tales. How many books are not fairy tales?'},
   'hint': {'ru': 'Какая часть книг &mdash; не сказки?', 'en': 'What fraction of the books are not fairy tales?'},
   'sol': {'ru': '24&middot;3/8 = <b>9</b>.', 'en': '24&middot;3/8 = <b>9</b>.'}},
  {'q': {'ru': f'Найдите дробь со знаменателем 12, которая больше {F("1","3")}, но меньше {F("1","2")}.', 'en': f'Find a fraction with denominator 12 that is greater than {F("1","3")} but less than {F("1","2")}.'},
   'hint': {'ru': 'Переведите обе границы в двенадцатые.', 'en': 'Convert both bounds to twelfths.'},
   'sol': {'ru': f'{F("4","12")} &lt; ? &lt; {F("6","12")}: подходит <b>{F("5","12")}</b>.', 'en': f'{F("4","12")} &lt; ? &lt; {F("6","12")}: the answer is <b>{F("5","12")}</b>.'}},
 ],
 'answers': {'ru': '3/4 · 5/8 · 1/3 · 14 · 35 · 1 · 9 · 5/12', 'en': '3/4, 5/8, 1/3, 14, 35, 1, 9, 5/12'},
 'routing': {'ru': 'Норма &mdash; 6 из 8. Ошибки в 1&ndash;3 и 8 &mdash; перечитать &laquo;сравнение&raquo; и &laquo;сложение&raquo;; в 4&ndash;5 и 7 &mdash; &laquo;дробь от числа&raquo;; в 6 &mdash; общий знаменатель.',
             'en': 'Mastery bar: 6 of 8. For mistakes in 1&ndash;3 and 8, reread &ldquo;comparing&rdquo; and &ldquo;adding&rdquo;; for 4&ndash;5 and 7, &ldquo;a fraction of a number&rdquo;; for 6, common denominators.'},
}

L12 = {
 'id': '1.2', 'anchor': 'u12',
 'title': {'ru': 'Проценты', 'en': 'Percents'},
 'theory': {
  'ru': """
<p><b>Процент &mdash; это сотая часть.</b> 25&nbsp;% = 25/100 = 1/4. Полезно знать наизусть пары: 50&nbsp;% = 1/2, 25&nbsp;% = 1/4, 20&nbsp;% = 1/5, 10&nbsp;% = 1/10, 75&nbsp;% = 3/4.</p>
<div class="frm">Быстрый счёт: найдите 10&nbsp;% (разделите на 10) и собирайте из него. 15&nbsp;% от 180: 10&nbsp;% = 18, 5&nbsp;% = 9, вместе 27.</div>
<p><b>Число по его проценту.</b> Если 20&nbsp;% числа равны 12, то 10&nbsp;% &mdash; это 6, а всё число 60. Всегда спускайтесь к 10&nbsp;% или к 1&nbsp;%. И два вопроса-родственника: &laquo;сколько процентов составляет 12 от 48?&raquo; &mdash; это дробь 12/48 = 1/4, переведённая в проценты (25&nbsp;%); &laquo;на сколько процентов изменилась цена?&raquo; &mdash; изменение всегда делим на СТАРОЕ значение.</p>
<p><b>Скидки и наценки.</b> Скидка 15&nbsp;% значит: осталось 85&nbsp;% цены. Считать можно двумя способами: вычесть скидку (80 &minus; 12) или сразу взять остаток (80&middot;0,85) &mdash; ответ один.</p>""",
  'en': """
<p><b>A percent is one hundredth.</b> 25% = 25/100 = 1/4. Worth memorizing: 50% = 1/2, 25% = 1/4, 20% = 1/5, 10% = 1/10, 75% = 3/4.</p>
<div class="frm">Fast mental math: find 10% (divide by 10) and build from it. 15% of 180: 10% = 18, 5% = 9, together 27.</div>
<p><b>A number from its percent.</b> If 20% of a number is 12, then 10% is 6, so the number is 60. Always drop down to 10% or 1%. Two related questions: &ldquo;what percent of 48 is 12?&rdquo; &mdash; that is the fraction 12/48 = 1/4 written as a percent (25%); &ldquo;by what percent did the price change?&rdquo; &mdash; always divide the change by the <em>old</em> value.</p>
<p><b>Discounts and markups.</b> A 15% discount means 85% of the price remains. Two ways to compute: subtract the discount (80 &minus; 12) or take the remainder directly (80&middot;0.85) &mdash; same answer.</p>"""},
 'worked': [
  {'tag': {'ru': 'Разбор 1 · быстрый счёт', 'en': 'Example 1 · fast mental math'},
   'q': {'ru': 'Найдите 15 % от 240.', 'en': 'Find 15% of 240.'},
   'sol': {'ru': '10 % = 24, половина от этого (5 %) = 12. Вместе: 24 + 12 = <b>36</b>. Никаких столбиков: проценты собираются из 10 % как из кубиков.',
          'en': '10% = 24, half of that (5%) = 12. Together: 24 + 12 = <b>36</b>. No long multiplication: percents snap together from 10% like blocks.'}},
  {'tag': {'ru': 'Разбор 2 · число по проценту', 'en': 'Example 2 · number from a percent'},
   'q': {'ru': '30 % числа равны 45. Найдите число.', 'en': '30% of a number is 45. Find the number.'},
   'sol': {'ru': 'Если 30 % &mdash; это 45, то 10 % &mdash; это 15. Всё число (100 %) = 15&middot;10 = <b>150</b>.',
          'en': 'If 30% is 45, then 10% is 15. The whole number (100%) is 15&middot;10 = <b>150</b>.'}},
  {'tag': {'ru': 'Разбор 3 · скидка', 'en': 'Example 3 · discount'},
   'q': {'ru': 'Свитер стоил 60 долларов, его уценили на 25 %. Какова новая цена?', 'en': 'A sweater cost $60 and was marked down 25%. What is the new price?'},
   'sol': {'ru': 'Осталось 75 % цены: 60&middot;3/4 = <b>45</b>. Или: скидка 60/4 = 15, значит 60 &minus; 15 = 45.',
          'en': '75% of the price remains: 60&middot;3/4 = <b>45</b>. Or: the discount is 60/4 = 15, so 60 &minus; 15 = 45.'}},
  {'tag': {'ru': 'Разбор 4 · процент и остаток', 'en': 'Example 4 · percent and the rest'},
   'q': {'ru': 'В классе 40 % учеников &mdash; девочки, а мальчиков 18. Сколько учеников в классе?', 'en': 'In a class, 40% of the students are girls, and there are 18 boys. How many students are in the class?'},
   'sol': {'ru': 'Мальчики &mdash; это 60 %. Если 60 % = 18, то 10 % = 3, а весь класс <b>30</b>. Ключевой ход: перейти от девочек к мальчикам, ведь число дано про мальчиков.',
          'en': 'The boys are 60%. If 60% = 18, then 10% = 3, so the class has <b>30</b> students. The key move: switch from girls to boys, because the given number is about boys.'}},
 ],
 'selfp': [
  {'q': {'ru': 'Найдите 20 % от 45.', 'en': 'Find 20% of 45.'},
   'hint': {'ru': '20 % — это одна пятая.', 'en': '20% is one fifth.'},
   'sol': {'ru': '45/5 = <b>9</b>.', 'en': '45/5 = <b>9</b>.'}},
  {'q': {'ru': 'Сколько процентов составляет 12 от 48?', 'en': 'What percent of 48 is 12?'},
   'hint': {'ru': 'Какая это часть? Переведите дробь в проценты.', 'en': 'What fraction is it? Convert to a percent.'},
   'sol': {'ru': '12/48 = 1/4 = <b>25 %</b>.', 'en': '12/48 = 1/4 = <b>25%</b>.'}},
  {'q': {'ru': 'Увеличьте 80 на 15 %.', 'en': 'Increase 80 by 15%.'},
   'hint': {'ru': '10 % и 5 % от 80.', 'en': '10% and 5% of 80.'},
   'sol': {'ru': '8 + 4 = 12, значит 80 + 12 = <b>92</b>.', 'en': '8 + 4 = 12, so 80 + 12 = <b>92</b>.'}},
  {'q': {'ru': '5 % числа равны 7. Найдите число.', 'en': '5% of a number is 7. Find the number.'},
   'hint': {'ru': 'Сколько раз по 5 % в 100 %?', 'en': 'How many 5-percents make 100%?'},
   'sol': {'ru': '7&middot;20 = <b>140</b>.', 'en': '7&middot;20 = <b>140</b>.'}},
  {'q': {'ru': 'Цена упала с 250 до 200 долларов. На сколько процентов снизилась цена?', 'en': 'A price dropped from $250 to $200. By what percent did it fall?'},
   'hint': {'ru': 'Снижение 50; от чего считаем процент?', 'en': 'The drop is 50; percent of what?'},
   'sol': {'ru': '50 от 250 &mdash; это 50/250 = 1/5 = <b>20 %</b>. Процент всегда считается от СТАРОЙ цены.', 'en': '50 out of 250 is 50/250 = 1/5 = <b>20%</b>. The percent is always taken of the OLD price.'}},
  {'q': {'ru': 'У Толи было 200 долларов, он потратил 35 %. Сколько осталось?', 'en': 'Tommy had $200 and spent 35%. How much is left?'},
   'hint': {'ru': 'Осталось 65 %.', 'en': '65% remains.'},
   'sol': {'ru': '200&middot;0,65 = <b>130</b>.', 'en': '200&middot;0.65 = <b>130</b>.'}},
  {'q': {'ru': 'В школе 300 учеников, 12 % ходят в шахматный кружок. Сколько это учеников?', 'en': 'A school has 300 students, and 12% attend chess club. How many students is that?'},
   'hint': {'ru': '1 % от 300 — это 3.', 'en': '1% of 300 is 3.'},
   'sol': {'ru': '3&middot;12 = <b>36</b>.', 'en': '3&middot;12 = <b>36</b>.'}},
  {'q': {'ru': 'После скидки 20 % товар стоит 96 долларов. Какой была цена до скидки?', 'en': 'After a 20% discount an item costs $96. What was the price before the discount?'},
   'hint': {'ru': 'Сколько процентов старой цены осталось после скидки?', 'en': 'What percent of the old price remains after the discount?'},
   'sol': {'ru': 'Если 80 % = 96, то 10 % = 12, а цена <b>120</b>. Ловушка &mdash; прибавить 20 % к 96: получится 115,2, а не исходная цена.', 'en': 'If 80% = 96, then 10% = 12, so the price was <b>$120</b>. The trap is adding 20% to 96: that gives 115.20, not the original price.'}},
 ],
 'answers': {'ru': '9 · 25 % · 92 · 140 · 20 % · 130 · 36 · 120', 'en': '9, 25%, 92, 140, 20%, 130, 36, $120'},
 'routing': {'ru': 'Норма &mdash; 6 из 8. Ошибки в 1, 3, 6&ndash;7 &mdash; &laquo;быстрый счёт от 10 %&raquo;; во 2 и 5 &mdash; &laquo;процент как часть&raquo;; в 4 и 8 &mdash; &laquo;число по проценту&raquo;.',
             'en': 'Mastery bar: 6 of 8. For mistakes in 1, 3, 6&ndash;7, reread &ldquo;fast math from 10%&rdquo;; for 2 and 5, &ldquo;a percent as a fraction&rdquo;; for 4 and 8, &ldquo;a number from its percent&rdquo;.'},
}
