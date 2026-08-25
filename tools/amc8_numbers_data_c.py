# -*- coding: utf-8 -*-
"""AMC 8, блок 1: урок 1.5, тест Т1, звёздочки. RU+EN."""

def F(a, b):
    return f'<span class="frac"><span>{a}</span><span>{b}</span></span>'

L15 = {
 'id': '1.5', 'anchor': 'u15',
 'title': {'ru': 'Оценка, округление и последняя цифра', 'en': 'Estimation, Rounding, and the Last Digit'},
 'theory': {
  'ru': """
<p><b>Прикидка вместо точного счёта.</b> На AMC 8 варианты ответов часто далеко друг от друга: 49&middot;21 &mdash; это примерно 50&middot;20 = 1000, и этого хватает, чтобы выбрать ответ. Прикидка за десять секунд стоит дороже точного счёта за минуту.</p>
<div class="frm">Округляйте один множитель вверх, другой вниз &mdash; ошибки почти гасят друг друга: 49&middot;21 &asymp; 50&middot;20 = 1000 (точно 1029).</div>
<p><b>Последняя цифра.</b> Последняя цифра произведения зависит только от последних цифр множителей: у 7&middot;8&middot;9 последняя цифра &mdash; как у 7&middot;8 = 56, то есть 6, дальше 6&middot;9 = 54 &mdash; цифра 4. Так проверяют ответы и решают задачи, где точный счёт невозможен. У степеней последние цифры повторяются по кругу: у степеней тройки это 3, 9, 7, 1, 3, 9, &hellip; &mdash; цикл длины четыре.</p>
<p><b>Чётность и делимость как проверка.</b> Сумма двух нечётных чётна; произведение с чётным множителем чётно; сумма трёх последовательных чисел делится на 3. Одна проверка чётности ловит половину арифметических ошибок.</p>""",
  'en': """
<p><b>Estimate instead of computing.</b> On the AMC 8 the answer choices are often far apart: 49&middot;21 is about 50&middot;20 = 1000, and that is enough to pick the answer. A ten-second estimate beats a one-minute exact computation.</p>
<div class="frm">Round one factor up and the other down &mdash; the errors nearly cancel: 49&middot;21 &asymp; 50&middot;20 = 1000 (exactly 1029).</div>
<p><b>The last digit.</b> The last digit of a product depends only on the last digits of the factors: for 7&middot;8&middot;9, take 7&middot;8 = 56 &mdash; digit 6, then 6&middot;9 = 54 &mdash; digit 4. This checks answers and solves problems where exact computation is hopeless. The last digits of powers repeat in a cycle: for powers of 3 they go 3, 9, 7, 1, 3, 9, &hellip; &mdash; a cycle of length four.</p>
<p><b>Parity and divisibility as a check.</b> The sum of two odd numbers is even; a product with an even factor is even; the sum of three consecutive numbers is divisible by 3. One parity check catches half of all arithmetic slips.</p>"""},
 'worked': [
  {'tag': {'ru': 'Разбор 1 · прикидка', 'en': 'Example 1 · estimation'},
   'q': {'ru': 'Какое из чисел ближе всего к 49&middot;21: 800, 1000, 1200, 1500 или 2000?', 'en': 'Which is closest to 49&middot;21: 800, 1000, 1200, 1500, or 2000?'},
   'sol': {'ru': '49&middot;21 &asymp; 50&middot;20 = 1000; точно 1029. Ответ <b>1000</b>. Одно округление вверх, одно вниз &mdash; и оценка почти точная.',
          'en': '49&middot;21 &asymp; 50&middot;20 = 1000; exactly 1029. Answer: <b>1000</b>. One round up, one round down &mdash; and the estimate is nearly exact.'}},
  {'tag': {'ru': 'Разбор 2 · последняя цифра', 'en': 'Example 2 · last digit'},
   'q': {'ru': 'Какой цифрой оканчивается произведение 7&middot;8&middot;9?', 'en': 'What is the last digit of 7&middot;8&middot;9?'},
   'sol': {'ru': '7&middot;8 = 56 &mdash; цифра 6; 6&middot;9 = 54 &mdash; цифра <b>4</b>. (Точно: 504.) Само произведение считать не нужно.',
          'en': '7&middot;8 = 56 &mdash; digit 6; 6&middot;9 = 54 &mdash; digit <b>4</b>. (Exactly: 504.) No need to compute the product itself.'}},
  {'tag': {'ru': 'Разбор 3 · деление с прикидкой', 'en': 'Example 3 · division with an estimate'},
   'q': {'ru': 'Сколько полных недель содержится в 2026 днях?', 'en': 'How many <em>full</em> weeks are there in 2026 days?'},
   'sol': {'ru': '2026/7: прикидка 7&middot;280 = 1960, остаётся 66 &mdash; ещё 9 недель и 3 дня. Итого <b>289 полных недель</b> (289&middot;7 = 2023, остаток 3).',
          'en': '2026/7: estimate 7&middot;280 = 1960, leaving 66 &mdash; 9 more weeks and 3 days. In all, <b>289 full weeks</b> (289&middot;7 = 2023, remainder 3).'}},
  {'tag': {'ru': 'Разбор 4 · чётность', 'en': 'Example 4 · parity'},
   'q': {'ru': 'Не складывая все числа, объясните, чётна или нечётна сумма 1 + 2 + &hellip; + 10.', 'en': 'Without adding them all, decide whether 1 + 2 + &hellip; + 10 is even or odd.'},
   'sol': {'ru': 'Нечётных слагаемых пять (1, 3, 5, 7, 9) &mdash; нечётное количество нечётных даёт нечётную сумму: <b>нечётна</b> (и правда, 55).',
          'en': 'There are five odd terms (1, 3, 5, 7, 9) &mdash; an odd count of odd numbers makes the sum odd: <b>odd</b> (indeed, 55).'}},
 ],
 'selfp': [
  {'q': {'ru': 'Округлите 4872 до сотен.', 'en': 'Round 4,872 to the nearest hundred.'},
   'hint': {'ru': 'Смотрите на цифру десятков.', 'en': 'Look at the tens digit.'},
   'sol': {'ru': '<b>4900</b>.', 'en': '<b>4,900</b>.'}},
  {'q': {'ru': 'Какое число ближе всего к 68&middot;102: 600, 700, 6000, 7000 или 70 000?', 'en': 'Which is closest to 68&middot;102: 600, 700, 6,000, 7,000, or 70,000?'},
   'hint': {'ru': '68·102 — это примерно 70·100.', 'en': '68&middot;102 is about 70&middot;100.'},
   'sol': {'ru': '&asymp; 7000 (точно 6936): <b>7000</b>.', 'en': '&asymp; 7,000 (exactly 6,936): <b>7,000</b>.'}},
  {'q': {'ru': 'Какой цифрой оканчивается 3<sup>4</sup>?', 'en': 'What is the last digit of 3<sup>4</sup>?'},
   'hint': {'ru': '3, 9, 27, 81…', 'en': '3, 9, 27, 81&hellip;'},
   'sol': {'ru': '3<sup>4</sup> = 81: цифра <b>1</b>.', 'en': '3<sup>4</sup> = 81: digit <b>1</b>.'}},
  {'q': {'ru': 'Вычислите 597 + 404.', 'en': 'Compute 597 + 404.'},
   'hint': {'ru': 'Округлите до 600 и 400 и поправьте.', 'en': 'Round to 600 and 400, then correct.'},
   'sol': {'ru': '600 + 400 = 1000, поправка &minus;3 + 4 = +1: <b>1001</b>.', 'en': '600 + 400 = 1000, correction &minus;3 + 4 = +1: <b>1001</b>.'}},
  {'q': {'ru': 'Какой цифрой оканчивается 25&middot;25&middot;25?', 'en': 'What is the last digit of 25&middot;25&middot;25?'},
   'hint': {'ru': 'Посмотрите только на последние цифры множителей.', 'en': 'Look only at the last digits of the factors.'},
   'sol': {'ru': 'Произведение чисел, оканчивающихся на 5, оканчивается на <b>5</b>.', 'en': 'A product of numbers ending in 5 ends in <b>5</b>.'}},
  {'q': {'ru': 'Вычислите 7&middot;11&middot;13.', 'en': 'Compute 7&middot;11&middot;13.'},
   'hint': {'ru': '77·13 или знаменитый ответ.', 'en': '77&middot;13 &mdash; or recall the famous product.'},
   'sol': {'ru': '77&middot;13 = <b>1001</b>. Это произведение стоит запомнить: 1001 = 7&middot;11&middot;13.', 'en': '77&middot;13 = <b>1001</b>. Worth memorizing: 1001 = 7&middot;11&middot;13.'}},
  {'q': {'ru': 'На какое число всегда делится сумма трёх последовательных натуральных чисел?', 'en': 'The sum of three consecutive positive integers is always divisible by what number?'},
   'hint': {'ru': 'Запишите их как n−1, n, n+1.', 'en': 'Write them as n&minus;1, n, n+1.'},
   'sol': {'ru': 'Сумма равна 3<var>n</var>: делится на <b>3</b>.', 'en': 'The sum is 3<var>n</var>: divisible by <b>3</b>.'}},
  {'q': {'ru': 'Что больше: 2<sup>10</sup> или 10<sup>3</sup>?', 'en': 'Which is larger: 2<sup>10</sup> or 10<sup>3</sup>?'},
   'hint': {'ru': 'Обе степени невелики — вычислите их точно.', 'en': 'Both powers are small — compute them exactly.'},
   'sol': {'ru': '1024 &gt; 1000: <b>2<sup>10</sup></b>.', 'en': '1024 &gt; 1000: <b>2<sup>10</sup></b>.'}},
 ],
 'answers': {'ru': '4900 · 7000 · 1 · 1001 · 5 · 1001 · 3 · 2¹⁰', 'en': '4,900, 7,000, 1, 1001, 5, 1001, 3, 2<sup>10</sup>'},
 'routing': {'ru': 'Норма &mdash; 6 из 8. Ошибки в 1&ndash;2, 4 и 8 &mdash; &laquo;прикидка&raquo;; в 3, 5 и 6 &mdash; &laquo;последняя цифра&raquo; и точный счёт; в 7 &mdash; &laquo;чётность и делимость&raquo;.',
             'en': 'Mastery bar: 6 of 8. For mistakes in 1&ndash;2, 4, and 8, reread &ldquo;estimation&rdquo;; for 3, 5, and 6, &ldquo;the last digit&rdquo; and exact computation; for 7, &ldquo;parity and divisibility&rdquo;.'},
}

STARS = {
 '1.1': {
  'q': {'ru': f'В классе {F("3","5")} учеников &mdash; девочки. Когда в класс пришли 4 новых мальчика, девочки стали составлять ровно половину класса. Сколько учеников было в классе сначала?',
        'en': f'In a class, {F("3","5")} of the students are girls. After 4 new boys join, girls make up exactly half of the class. How many students were in the class at first?'},
  'hint': {'ru': 'Число девочек не изменилось. Запишите его двумя способами: до и после.', 'en': 'The number of girls did not change. Write it two ways: before and after.'},
  'sol': {'ru': 'Пусть было <var>N</var> учеников: девочек 3<var>N</var>/5, и они же равны (<var>N</var> + 4)/2. Тогда 6<var>N</var> = 5<var>N</var> + 20, <var>N</var> = <b>20</b>. Проверка: 12 девочек из 20; стало 24, и 12 &mdash; ровно половина.',
          'en': 'Let there be <var>N</var> students: girls are 3<var>N</var>/5, which also equals (<var>N</var> + 4)/2. Then 6<var>N</var> = 5<var>N</var> + 20, so <var>N</var> = <b>20</b>. Check: 12 girls of 20; now 24 students, and 12 is exactly half.'}},
 '1.2': {
  'q': {'ru': 'Цену товара сначала подняли на 25 %, а потом снизили на <var>p</var> % &mdash; и она вернулась ровно к исходной. Чему равно <var>p</var>?',
        'en': 'A price was first raised by 25%, then lowered by <var>p</var>% &mdash; and it returned exactly to the original. What is <var>p</var>?'},
  'hint': {'ru': 'После подъёма цена — 5/4 исходной. На какую долю её надо уменьшить?', 'en': 'After the raise the price is 5/4 of the original. By what fraction must it shrink?'},
  'sol': {'ru': 'Нужно умножить 5/4 на такое число, чтобы получить 1: это 4/5, то есть минус одна пятая. <var>p</var> = <b>20</b>. Проценты вверх и вниз не симметричны: +25 гасится &minus;20.',
          'en': 'We need to multiply 5/4 by something to get 1: that is 4/5, a drop of one fifth. <var>p</var> = <b>20</b>. Percent up and percent down are not symmetric: +25 is undone by &minus;20.'}},
 '1.3': {
  'q': {'ru': 'Два числа относятся как 5 : 3. Если из большего вычесть 10, отношение станет 5 : 4. Найдите сумму исходных чисел.',
        'en': 'Two numbers are in the ratio 5 : 3. If 10 is subtracted from the larger, the ratio becomes 5 : 4. Find the sum of the original numbers.'},
  'hint': {'ru': 'Пусть числа 5k и 3k; запишите новое отношение.', 'en': 'Let the numbers be 5k and 3k; write the new ratio.'},
  'sol': {'ru': '(5<var>k</var> &minus; 10) : 3<var>k</var> = 5 : 4, значит 20<var>k</var> &minus; 40 = 15<var>k</var> и <var>k</var> = 8. Числа 40 и 24, сумма <b>64</b>. Проверка: 30 : 24 = 5 : 4.',
          'en': '(5<var>k</var> &minus; 10) : 3<var>k</var> = 5 : 4, so 20<var>k</var> &minus; 40 = 15<var>k</var> and <var>k</var> = 8. The numbers are 40 and 24, sum <b>64</b>. Check: 30 : 24 = 5 : 4.'}},
 '1.4': {
  'q': {'ru': 'Среднее пяти различных натуральных чисел равно 10. Каково наибольшее возможное значение самого большого из этих чисел?',
        'en': 'The average of five different positive integers is 10. What is the greatest possible value of the largest of these numbers?'},
  'hint': {'ru': 'Сумма всех пяти фиксирована. Каким сделать остальные четыре, чтобы пятое стало как можно больше?', 'en': 'The total of all five is fixed. What should the other four be so the fifth is as large as possible?'},
  'sol': {'ru': 'Сумма 50. Чтобы одно число было максимальным, остальные — минимальные различные: 1 + 2 + 3 + 4 = 10. Наибольшее: 50 &minus; 10 = <b>40</b>.',
          'en': 'The sum is 50. To maximize one number, make the others the smallest possible distinct values: 1 + 2 + 3 + 4 = 10. The largest: 50 &minus; 10 = <b>40</b>.'}},
 '1.5': {
  'q': {'ru': 'Какой цифрой оканчивается 7<sup>2026</sup>?', 'en': 'What is the last digit of 7<sup>2026</sup>?'},
  'hint': {'ru': 'Выпишите последние цифры 7¹, 7², 7³, 7⁴ — они повторяются по кругу.', 'en': 'List the last digits of 7&sup1;, 7&sup2;, 7&sup3;, 7&#8308; &mdash; they cycle.'},
  'sol': {'ru': 'Цикл: 7, 9, 3, 1 (длина 4). 2026 = 4&middot;506 + 2 &mdash; вторая позиция цикла: <b>9</b>.',
          'en': 'The cycle: 7, 9, 3, 1 (length 4). 2026 = 4&middot;506 + 2 &mdash; the second position of the cycle: <b>9</b>.'}},
}

T1 = {
 'problems': [
  {'q': {'ru': f'Найдите {F("3","5")} от 40.', 'en': f'Find {F("3","5")} of 40.'},
   'opts': {'ru': ['15', '18', '24', '25', '32'], 'en': ['15', '18', '24', '25', '32']}},
  {'q': {'ru': 'Какая из дробей самая большая?', 'en': 'Which fraction is the largest?'},
   'opts': {'ru': [F(7,12), F(3,5), F(5,8), F(13,20), F(2,3)], 'en': [F(7,12), F(3,5), F(5,8), F(13,20), F(2,3)]}},
  {'q': {'ru': 'Чему равно 15 % от 60?', 'en': 'What is 15% of 60?'},
   'opts': {'ru': ['8', '9', '10', '12', '15'], 'en': ['8', '9', '10', '12', '15']}},
  {'q': {'ru': 'После скидки 30 % товар стоит 63 доллара. Какой была цена до скидки (в долларах)?', 'en': 'After a 30% discount an item costs $63. What was the original price (in dollars)?'},
   'opts': {'ru': ['84', '90', '93', '96', '110'], 'en': ['84', '90', '93', '96', '110']}},
  {'q': {'ru': 'Число 63 разделили в отношении 4 : 5. Чему равна меньшая часть?', 'en': 'The number 63 is split in the ratio 4 : 5. What is the smaller part?'},
   'opts': {'ru': ['24', '28', '32', '35', '36'], 'en': ['24', '28', '32', '35', '36']}},
  {'q': {'ru': '8 одинаковых ручек стоят 120 центов. Сколько центов стоят 5 таких ручек?', 'en': 'Eight identical pens cost 120 cents. How many cents do five of these pens cost?'},
   'opts': {'ru': ['75', '78', '80', '85', '96'], 'en': ['75', '78', '80', '85', '96']}},
  {'q': {'ru': 'Найдите среднее чисел 11, 14, 17 и 18.', 'en': 'Find the mean of 11, 14, 17, and 18.'},
   'opts': {'ru': ['12', '13', '14', '15', '16'], 'en': ['12', '13', '14', '15', '16']}},
  {'q': {'ru': 'Среднее по четырём тестам должно быть 85. Первые три: 80, 88 и 84. Сколько нужно набрать за четвёртый?', 'en': 'A four-test average of 85 is required. The first three tests: 80, 88, and 84. What must the fourth score be?'},
   'opts': {'ru': ['84', '86', '88', '90', '92'], 'en': ['84', '86', '88', '90', '92']}},
  {'q': {'ru': 'Какой цифрой оканчивается произведение 6&middot;7&middot;8&middot;9?', 'en': 'What is the last digit of 6&middot;7&middot;8&middot;9?'},
   'opts': {'ru': ['0', '2', '4', '6', '8'], 'en': ['0', '2', '4', '6', '8']}},
  {'q': {'ru': 'Какое из чисел ближе всего к произведению 52&middot;19?', 'en': 'Which of the following is closest to the product 52&middot;19?'},
   'opts': {'ru': ['900', '950', '1000', '1050', '1100'], 'en': ['900', '950', '1000', '1050', '1100']}},
 ],
 'key': ['C', 'E', 'B', 'B', 'B', 'A', 'D', 'C', 'C', 'C'],
 'hints': {
  'ru': [
   '<b>1.</b> 40/5 = 8, дальше 8&middot;3 = 24.',
   '<b>2.</b> 2/3 &asymp; 0,667 &mdash; больше, чем 13/20 = 0,65 и 5/8 = 0,625.',
   '<b>3.</b> 10 % = 6, 5 % = 3: вместе 9.',
   '<b>4.</b> 63 &mdash; это 70 %: 10 % = 9, цена 90.',
   '<b>5.</b> Часть 63/9 = 7: части 28 и 35, меньшая 28.',
   '<b>6.</b> Одна ручка 15: пять ручек 75.',
   '<b>7.</b> Сумма 60, среднее 15.',
   '<b>8.</b> Нужно 340, набрано 252: четвёртый 88.',
   '<b>9.</b> 6&middot;7 = 42 &rarr; 2; 2&middot;8 = 16 &rarr; 6; 6&middot;9 = 54 &rarr; 4.',
   '<b>10.</b> Округлите 52 вниз до 50, а 19 вверх до 20: примерно 1000 (точно 988).'],
  'en': [
   '<b>1.</b> 40/5 = 8, then 8&middot;3 = 24.',
   '<b>2.</b> 2/3 &asymp; 0.667 &mdash; more than 13/20 = 0.65 and 5/8 = 0.625.',
   '<b>3.</b> 10% = 6, 5% = 3: together 9.',
   '<b>4.</b> $63 is 70%: 10% = 9, the price was $90.',
   '<b>5.</b> One part is 63/9 = 7: the parts are 28 and 35; the smaller is 28.',
   '<b>6.</b> One pen costs 15: five pens cost 75.',
   '<b>7.</b> The sum is 60, the mean 15.',
   '<b>8.</b> 340 needed, 252 so far: the fourth is 88.',
   '<b>9.</b> 6&middot;7 = 42 &rarr; 2; 2&middot;8 = 16 &rarr; 6; 6&middot;9 = 54 &rarr; 4.',
   '<b>10.</b> Round 52 down to 50 and 19 up to 20: about 1000 (exactly 988).'],
 },
}
