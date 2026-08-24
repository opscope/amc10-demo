# -*- coding: utf-8 -*-
"""Блок 1 «Алгебра»: уроки 1.1–1.2, RU+EN. HTML-фрагменты в нотации страницы курса."""

def F(a, b):
    return f'<span class="frac"><span>{a}</span><span>{b}</span></span>'

L11 = {
 'id': '1.1', 'anchor': 'u11',
 'title': {'ru': 'Проценты, отношения, средние, движение',
           'en': 'Percents, Ratios, Averages, Motion'},
 'theory': {
  'ru': f"""
<p><b>Проценты через множители.</b> Рост на 20&nbsp;% &mdash; это умножение на 1,2; падение на 25&nbsp;% &mdash; умножение на 0,75. Последовательные изменения перемножаются: +20&nbsp;% и затем &minus;25&nbsp;% дают 1,2&nbsp;&middot;&nbsp;0,75&nbsp;=&nbsp;0,9, то есть &minus;10&nbsp;%. Никогда не складывайте проценты от разных баз.</p>
<div class="frm">Изменение на <b>p&nbsp;%</b> = умножение на <b>(1 + p/100)</b>. Цепочка изменений = произведение множителей.</div>
<p><b>Отношения через части.</b> Если величины относятся как 3&nbsp;:&nbsp;4, введите размер одной части <var>k</var>: величины равны 3<var>k</var> и 4<var>k</var>. Составные отношения сшиваются через общий член: из <var>a</var>&nbsp;:&nbsp;<var>b</var> = 2&nbsp;:&nbsp;3 и <var>b</var>&nbsp;:&nbsp;<var>c</var> = 4&nbsp;:&nbsp;5 приводим <var>b</var> к 12 и получаем <var>a</var>&nbsp;:&nbsp;<var>b</var>&nbsp;:&nbsp;<var>c</var> = 8&nbsp;:&nbsp;12&nbsp;:&nbsp;15.</p>
<p><b>Средние.</b> Среднее арифметическое = сумма / количество; почти все задачи о среднем решаются через <b>сумму</b>: узнайте сумму до и после изменения. Взвешенное среднее лежит между групповыми средними, ближе к большей группе.</p>
<p><b>Движение.</b> Путь = скорость &times; время. Средняя скорость &mdash; это ВЕСЬ путь на ВСЁ время, а не среднее скоростей: на равных отрезках пути она равна {F('2<var>v</var><sub>1</sub><var>v</var><sub>2</sub>','<var>v</var><sub>1</sub> + <var>v</var><sub>2</sub>')} и всегда меньше среднего арифметического. Перевод единиц: 1&nbsp;м/с = 3,6&nbsp;км/ч.</p>""",
  'en': f"""
<p><b>Percents as multipliers.</b> A 20% increase means multiplying by 1.2; a 25% decrease means multiplying by 0.75. Successive changes multiply: +20% followed by &minus;25% gives 1.2&nbsp;&middot;&nbsp;0.75&nbsp;=&nbsp;0.9, that is &minus;10%. Never add percents taken of different bases.</p>
<div class="frm">A change of <b>p%</b> = multiplication by <b>(1 + p/100)</b>. A chain of changes = the product of the multipliers.</div>
<p><b>Ratios via parts.</b> If two quantities are in the ratio 3&nbsp;:&nbsp;4, let <var>k</var> be the size of one part: the quantities are 3<var>k</var> and 4<var>k</var>. Chained ratios are linked through the common quantity: from <var>a</var>&nbsp;:&nbsp;<var>b</var> = 2&nbsp;:&nbsp;3 and <var>b</var>&nbsp;:&nbsp;<var>c</var> = 4&nbsp;:&nbsp;5, scale <var>b</var> to 12 to get <var>a</var>&nbsp;:&nbsp;<var>b</var>&nbsp;:&nbsp;<var>c</var> = 8&nbsp;:&nbsp;12&nbsp;:&nbsp;15.</p>
<p><b>Averages.</b> Mean = sum / count; nearly every average problem is solved by working with the <b>sum</b>: find the sum before and after the change. A weighted average lies between the group means, closer to the larger group.</p>
<p><b>Motion.</b> Distance = speed &times; time. Average speed is the TOTAL distance over the TOTAL time, not the average of speeds: over equal distances it equals {F('2<var>v</var><sub>1</sub><var>v</var><sub>2</sub>','<var>v</var><sub>1</sub> + <var>v</var><sub>2</sub>')} and is always less than the arithmetic mean.</p>"""},
 'worked': [
  {'tag': {'ru': 'Разбор 1 · проценты', 'en': 'Example 1 · percents'},
   'q': {'ru': 'Цена сначала выросла на 25&nbsp;%, потом снизилась на 20&nbsp;%. Как итог соотносится с началом?',
         'en': 'A price first rose by 25%, then fell by 20%. How does the final price compare to the original?'},
   'sol': {'ru': 'Множители: 1,25&nbsp;&middot;&nbsp;0,8 = 1. Цена не изменилась. Обратите внимание: +25 и &minus;20 &laquo;не сокращаются&raquo; в голове, но сокращаются в множителях: 5/4&nbsp;&middot;&nbsp;4/5 = 1. Дроби здесь быстрее десятичных.',
          'en': 'Multipliers: 1.25&nbsp;&middot;&nbsp;0.8 = 1. The price is unchanged. +25 and &minus;20 look like they should not cancel &mdash; but as multipliers they do: 5/4&nbsp;&middot;&nbsp;4/5 = 1. Fractions are faster than decimals here.'}},
  {'tag': {'ru': 'Разбор 2 · отношения', 'en': 'Example 2 · ratios'},
   'q': {'ru': 'В классе отношение мальчиков к девочкам 3&nbsp;:&nbsp;4. Пришли 6 мальчиков, и отношение стало 9&nbsp;:&nbsp;8. Сколько человек теперь в классе?',
         'en': 'In a class the ratio of boys to girls is 3&nbsp;:&nbsp;4. After 6 more boys join, the ratio becomes 9&nbsp;:&nbsp;8. How many students are in the class now?'},
   'sol': {'ru': f'Было 3<var>k</var> и 4<var>k</var>. Стало: {F("3<var>k</var> + 6","4<var>k</var>")} = {F("9","8")}. Перемножаем крест-накрест: 24<var>k</var> + 48 = 36<var>k</var>, откуда <var>k</var> = 4. Теперь в классе (12 + 6) + 16 = <b>34</b>. Проверка: 18&nbsp;:&nbsp;16 = 9&nbsp;:&nbsp;8. Верно.',
          'en': f'Originally 3<var>k</var> and 4<var>k</var>. Now: {F("3<var>k</var> + 6","4<var>k</var>")} = {F("9","8")}. Cross-multiply: 24<var>k</var> + 48 = 36<var>k</var>, so <var>k</var> = 4. The class now has (12 + 6) + 16 = <b>34</b> students. Check: 18&nbsp;:&nbsp;16 = 9&nbsp;:&nbsp;8. Correct.'}},
  {'tag': {'ru': 'Разбор 3 · средняя скорость', 'en': 'Example 3 · average speed'},
   'q': {'ru': 'Туда ехали со скоростью 60 км/ч, обратно той же дорогой &mdash; 40 км/ч. Какова средняя скорость за всю поездку?',
         'en': 'You drive to a town at 60 mph and return along the same road at 40 mph. What is the average speed for the whole trip?'},
   'sol': {'ru': 'Пусть путь в одну сторону <var>d</var>. Время: <var>d</var>/60 + <var>d</var>/40 = <var>d</var>&nbsp;&middot;&nbsp;5/120 = <var>d</var>/24. Средняя = 2<var>d</var> &divide; (<var>d</var>/24) = <b>48 км/ч</b>. Не 50! Формула 2&middot;60&middot;40/(60+40) даёт то же мгновенно. На AMC ответ &laquo;среднее арифметическое скоростей&raquo; почти всегда стоит среди вариантов как ловушка.',
          'en': 'Let the one-way distance be <var>d</var>. Time: <var>d</var>/60 + <var>d</var>/40 = <var>d</var>&nbsp;&middot;&nbsp;5/120 = <var>d</var>/24. Average = 2<var>d</var> &divide; (<var>d</var>/24) = <b>48 mph</b>. Not 50! The formula 2&middot;60&middot;40/(60+40) gives the same instantly. On the AMC, the arithmetic mean of the speeds almost always appears among the choices as a trap.'}},
  {'tag': {'ru': 'Разбор 4 · взвешенное среднее', 'en': 'Example 4 · weighted average'},
   'q': {'ru': 'Средний балл девочек 90, мальчиков 80, средний по классу 84. Какая доля класса &mdash; мальчики?',
         'en': 'The girls&rsquo; average score is 90, the boys&rsquo; is 80, and the class average is 84. What fraction of the class are boys?'},
   'sol': {'ru': 'Пусть доля мальчиков <var>m</var>. Тогда 80<var>m</var> + 90(1&nbsp;&minus;&nbsp;<var>m</var>) = 84, то есть 90 &minus; 10<var>m</var> = 84, <var>m</var> = 0,6: <b>60&nbsp;%</b>. Быстрая проверка рычагом: 84 отстоит от 80 на 4, от 90 на 6; веса обратны расстояниям, 6&nbsp;:&nbsp;4 = 3&nbsp;:&nbsp;2 в пользу мальчиков.',
          'en': 'Let the boys&rsquo; fraction be <var>m</var>. Then 80<var>m</var> + 90(1&nbsp;&minus;&nbsp;<var>m</var>) = 84, so 90 &minus; 10<var>m</var> = 84 and <var>m</var> = 0.6: <b>60%</b>. Quick lever check: 84 is 4 away from 80 and 6 away from 90; weights are inverse to distances, 6&nbsp;:&nbsp;4 = 3&nbsp;:&nbsp;2 in favor of the boys.'}},
 ],
 'selfp': [
  {'q': {'ru': '20&nbsp;% от 30&nbsp;% числа равны 12. Найдите число.', 'en': '20% of 30% of a number equals 12. Find the number.'},
   'hint': {'ru': '20&nbsp;% от 30&nbsp;% &mdash; это один множитель: 0,2&nbsp;&middot;&nbsp;0,3.', 'en': '20% of 30% is a single multiplier: 0.2&nbsp;&middot;&nbsp;0.3.'},
   'sol': {'ru': '0,06<var>x</var> = 12, значит <var>x</var> = <b>200</b>.', 'en': '0.06<var>x</var> = 12, so <var>x</var> = <b>200</b>.'}},
  {'q': {'ru': 'Товар подешевел на 50&nbsp;%. На сколько процентов он должен подорожать, чтобы вернуться к прежней цене?', 'en': 'An item&rsquo;s price dropped by 50%. By what percent must it rise to return to the original price?'},
   'hint': {'ru': 'Новая база меньше старой. Ищите множитель, который вернёт 0,5 к единице.', 'en': 'The new base is smaller. Find the multiplier that brings 0.5 back to 1.'},
   'sol': {'ru': '0,5&nbsp;&middot;&nbsp;<var>t</var> = 1, значит <var>t</var> = 2: подорожать на <b>100&nbsp;%</b>. Проценты вниз и вверх не симметричны, потому что базы разные.', 'en': '0.5&nbsp;&middot;&nbsp;<var>t</var> = 1, so <var>t</var> = 2: a rise of <b>100%</b>. Percents down and up are not symmetric, because the bases differ.'}},
  {'q': {'ru': 'Смешали 2 литра 10-процентного сока с 3 литрами 20-процентного. Какова концентрация смеси?', 'en': 'Two liters of a 10% acid solution are mixed with three liters of a 20% solution. What is the concentration of the mixture?'},
   'hint': {'ru': 'Считайте чистый сок в литрах, отдельно от воды.', 'en': 'Count the pure acid in liters, separately from the water.'},
   'sol': {'ru': 'Чистого сока 0,2 + 0,6 = 0,8 л на 5 л смеси: <b>16&nbsp;%</b>. Это взвешенное среднее 10 и 20 с весами 2&nbsp;:&nbsp;3.', 'en': 'Pure acid: 0.2 + 0.6 = 0.8 L out of 5 L: <b>16%</b>. This is the weighted average of 10 and 20 with weights 2&nbsp;:&nbsp;3.'}},
  {'q': {'ru': '<var>a</var>&nbsp;:&nbsp;<var>b</var> = 2&nbsp;:&nbsp;3 и <var>b</var>&nbsp;:&nbsp;<var>c</var> = 4&nbsp;:&nbsp;5. Найдите <var>a</var>&nbsp;:&nbsp;<var>c</var>.', 'en': '<var>a</var>&nbsp;:&nbsp;<var>b</var> = 2&nbsp;:&nbsp;3 and <var>b</var>&nbsp;:&nbsp;<var>c</var> = 4&nbsp;:&nbsp;5. Find <var>a</var>&nbsp;:&nbsp;<var>c</var>.'},
   'hint': {'ru': 'Приведите <var>b</var> к общему значению в обоих отношениях.', 'en': 'Scale <var>b</var> to a common value in both ratios.'},
   'sol': {'ru': '<var>b</var> = 12: тогда <var>a</var> = 8, <var>c</var> = 15. Ответ <b>8&nbsp;:&nbsp;15</b>.', 'en': '<var>b</var> = 12: then <var>a</var> = 8, <var>c</var> = 15. Answer: <b>8&nbsp;:&nbsp;15</b>.'}},
  {'q': {'ru': 'Среднее семи чисел равно 15. Добавили восьмое число, и среднее стало 16. Какое число добавили?', 'en': 'The average of seven numbers is 15. An eighth number is added, and the average becomes 16. What number was added?'},
   'hint': {'ru': 'Работайте с суммами: сумма до и сумма после.', 'en': 'Work with sums: the sum before and the sum after.'},
   'sol': {'ru': 'Было 105, стало 16&nbsp;&middot;&nbsp;8 = 128. Добавили <b>23</b>.', 'en': 'Before: 105; after: 16&nbsp;&middot;&nbsp;8 = 128. The number added is <b>23</b>.'}},
  {'q': {'ru': 'Первую половину пути автомобиль ехал со скоростью 30 км/ч, вторую половину &mdash; 60 км/ч. Какова средняя скорость?', 'en': 'A car drives the first half of a route at 30 mph and the second half at 60 mph. What is its average speed?'},
   'hint': {'ru': 'Половины равны по ПУТИ, значит время на них разное.', 'en': 'The halves are equal in DISTANCE, so the times are different.'},
   'sol': {'ru': '2&nbsp;&middot;&nbsp;30&nbsp;&middot;&nbsp;60 / (30 + 60) = <b>40 км/ч</b>.', 'en': '2&nbsp;&middot;&nbsp;30&nbsp;&middot;&nbsp;60 / (30 + 60) = <b>40 mph</b>.'}},
  {'q': {'ru': 'Поезд длиной 200 метров проезжает мимо столба за 10 секунд. Какова его скорость в км/ч?', 'en': 'A train 880 feet long passes a pole in 10 seconds. What is its speed in miles per hour?'},
   'hint': {'ru': '&laquo;Мимо столба&raquo; значит: поезд проходит расстояние, равное собственной длине.', 'en': '&ldquo;Passes a pole&rdquo; means the train covers a distance equal to its own length. A useful fact: 60 mph = 88 ft/s.'},
   'sol': {'ru': '20 м/с. Перевод: &times;3,6, то есть <b>72 км/ч</b>.', 'en': '88 ft/s. Since 60 mph = 88 ft/s, the speed is <b>60 mph</b>.'}},
  {'q': {'ru': 'Зарплату повысили на 10&nbsp;%, а через год ещё на 10&nbsp;%. На сколько процентов она выросла за два года?', 'en': 'A salary was raised by 10%, and a year later by another 10%. By what percent did it grow over the two years?'},
   'hint': {'ru': 'Множители, не сложение.', 'en': 'Multipliers, not addition.'},
   'sol': {'ru': '1,1&nbsp;&middot;&nbsp;1,1 = 1,21: на <b>21&nbsp;%</b>. Лишний 1&nbsp;% &mdash; это &laquo;процент на процент&raquo;, десять процентов от десяти.', 'en': '1.1&nbsp;&middot;&nbsp;1.1 = 1.21: by <b>21%</b>. The extra 1% is &ldquo;percent on percent&rdquo;: ten percent of ten.'}},
 ],
 'answers': {'ru': '200 · 100 % · 16 % · 8:15 · 23 · 40 км/ч · 72 км/ч · 21 %', 'en': '200, 100%, 16%, 8 : 15, 23, 40 mph, 60 mph, 21%'},
 'routing': {'ru': 'Норма урока &mdash; 6 из 8. Ошибки в 1&ndash;2 и 8 &mdash; перечитать &laquo;проценты через множители&raquo;; в 3 и 5 &mdash; &laquo;средние&raquo;; в 4 &mdash; &laquo;отношения через части&raquo;; в 6&ndash;7 &mdash; &laquo;движение&raquo;. Задачи с ошибками вернутся в начало следующей половинки B.',
             'en': 'Mastery bar: 6 of 8. For mistakes in 1&ndash;2 and 8, reread &ldquo;percents as multipliers&rdquo;; for 3 and 5, &ldquo;averages&rdquo;; for 4, &ldquo;ratios via parts&rdquo;; for 6&ndash;7, &ldquo;motion&rdquo;. Missed problems come back at the start of the next lesson&rsquo;s B session.'},
}

L12 = {
 'id': '1.2', 'anchor': 'u12',
 'title': {'ru': 'Уравнения и системы, работа и смеси, прогрессии',
           'en': 'Equations and Systems, Work and Mixtures, Sequences'},
 'theory': {
  'ru': f"""
<p><b>Линейные уравнения и системы.</b> Раскрыть скобки, собрать <var>x</var> слева, числа справа, поделить. В системе из двух уравнений выражайте ту переменную, у которой коэффициент 1, и подставляйте во второе. Каждый найденный ответ подставляйте обратно: проверка стоит десять секунд и ловит половину ошибок.</p>
<p><b>Задачи на работу.</b> Ключ &mdash; производительность: доля работы в час. Кран, наполняющий бассейн за 6 часов, делает 1/6 работы в час. Производительности складываются: вместе кран &laquo;за 6&raquo; и кран &laquo;за 3&raquo; дают 1/6 + 1/3 = 1/2 работы в час, то есть 2 часа на всё.</p>
<div class="frm">Работа за час = {F('1','время в одиночку')}. Совместное время = {F('1','сумма производительностей')}.</div>
<p><b>Смеси.</b> Следите за чистым веществом, а не за процентами: сколько литров чистого сока/кислоты было и стало. Вода при доливании добавляет объём, но не вещество.</p>
<p><b>Прогрессии.</b> Арифметическая: <var>a</var><sub><var>n</var></sub> = <var>a</var><sub>1</sub> + (<var>n</var>&nbsp;&minus;&nbsp;1)<var>d</var>; сумма = {F('<var>a</var><sub>1</sub> + <var>a</var><sub><var>n</var></sub>','2')}&nbsp;&middot;&nbsp;<var>n</var> (среднее первого и последнего на количество). Геометрическая: <var>b</var><sub><var>n</var></sub> = <var>b</var><sub>1</sub><var>r</var><sup><var>n</var>&minus;1</sup>; сумма = <var>b</var><sub>1</sub>{F('<var>r</var><sup><var>n</var></sup> &minus; 1','<var>r</var> &minus; 1')} (при <var>r</var> &ne; 1).</p>""",
  'en': f"""
<p><b>Linear equations and systems.</b> Expand, collect <var>x</var> on the left and numbers on the right, divide. In a two-equation system, solve for the variable whose coefficient is 1 and substitute into the other equation. Plug every answer back in: the check takes ten seconds and catches half of all mistakes.</p>
<p><b>Work problems.</b> The key is the rate: the fraction of the job done per hour. A pipe that fills a pool in 6 hours does 1/6 of the job per hour. Rates add: a &ldquo;6-hour&rdquo; pipe and a &ldquo;3-hour&rdquo; pipe together do 1/6 + 1/3 = 1/2 of the job per hour, i.e. 2 hours for the whole job.</p>
<div class="frm">Work per hour = {F('1','time alone')}. Joint time = {F('1','sum of rates')}.</div>
<p><b>Mixtures.</b> Track the pure substance, not the percents: how many liters of pure juice/acid there were and there are. Added water increases the volume but not the substance.</p>
<p><b>Sequences.</b> Arithmetic: <var>a</var><sub><var>n</var></sub> = <var>a</var><sub>1</sub> + (<var>n</var>&nbsp;&minus;&nbsp;1)<var>d</var>; sum = {F('<var>a</var><sub>1</sub> + <var>a</var><sub><var>n</var></sub>','2')}&nbsp;&middot;&nbsp;<var>n</var> (the mean of the first and last, times the count). Geometric: <var>a</var><sub><var>n</var></sub> = <var>a</var><sub>1</sub><var>r</var><sup><var>n</var>&minus;1</sup>; sum = <var>a</var><sub>1</sub>{F('<var>r</var><sup><var>n</var></sup> &minus; 1','<var>r</var> &minus; 1')} (for <var>r</var> &ne; 1).</p>"""},
 'worked': [
  {'tag': {'ru': 'Разбор 1 · система', 'en': 'Example 1 · system'},
   'q': {'ru': '3 ручки и 2 тетради стоят 240 рублей; 1 ручка и 4 тетради &mdash; 180. Сколько стоит ручка?',
         'en': 'Three pens and two notebooks cost $24; one pen and four notebooks cost $18. How much does a pen cost?'},
   'sol': {'ru': 'Из второго уравнения <var>p</var> = 180 &minus; 4<var>t</var>. Подставляем: 3(180 &minus; 4<var>t</var>) + 2<var>t</var> = 240, то есть 540 &minus; 10<var>t</var> = 240, <var>t</var> = 30 и <var>p</var> = <b>60</b>. Проверка: 3&middot;60 + 2&middot;30 = 240. Верно.',
          'en': 'From the second equation, <var>p</var> = 18 &minus; 4<var>n</var>. Substitute: 3(18 &minus; 4<var>n</var>) + 2<var>n</var> = 24, so 54 &minus; 10<var>n</var> = 24, <var>n</var> = 3 and <var>p</var> = <b>$6</b>. Check: 3&middot;6 + 2&middot;3 = 24. Correct.'}},
  {'tag': {'ru': 'Разбор 2 · работа', 'en': 'Example 2 · work'},
   'q': {'ru': 'Одна труба наполняет бассейн за 10 часов, другая &mdash; за 15. За сколько наполнят вместе?',
         'en': 'One pipe fills a pool in 10 hours, another in 15. How long do they take together?'},
   'sol': {'ru': 'Производительности: 1/10 + 1/15 = 1/6 бассейна в час. Значит, вместе &mdash; <b>6 часов</b>. Типовая ловушка &laquo;(10+15)/2&raquo; неверна: вместе всегда быстрее, чем самая быстрая труба в одиночку.',
          'en': 'Rates: 1/10 + 1/15 = 1/6 of the pool per hour. Together: <b>6 hours</b>. The common trap &ldquo;(10+15)/2&rdquo; is wrong: together is always faster than the faster pipe alone.'}},
  {'tag': {'ru': 'Разбор 3 · смесь', 'en': 'Example 3 · mixture'},
   'q': {'ru': 'В 5 литрах сока концентрация 12&nbsp;%. Сколько воды долить, чтобы стало 8&nbsp;%?',
         'en': 'Five liters of juice have concentration 12%. How much water must be added to get 8%?'},
   'sol': {'ru': 'Чистого сока 0,12&nbsp;&middot;&nbsp;5 = 0,6 л, и он не меняется. Новый объём: 0,6 / 0,08 = 7,5 л. Долить <b>2,5 литра</b>. Вся задача &mdash; одно деление, если следить за веществом, а не за процентами.',
          'en': 'Pure juice: 0.12&nbsp;&middot;&nbsp;5 = 0.6 L, and it does not change. New volume: 0.6 / 0.08 = 7.5 L. Add <b>2.5 liters</b>. The whole problem is one division if you track the substance, not the percents.'}},
  {'tag': {'ru': 'Разбор 4 · прогрессии', 'en': 'Example 4 · sequences'},
   'q': {'ru': 'Найдите сумму 3 + 6 + 12 + &hellip; + 384.',
         'en': 'Find the sum 3 + 6 + 12 + &hellip; + 384.'},
   'sol': {'ru': 'Это геометрическая прогрессия: <var>b</var><sub>1</sub> = 3, <var>r</var> = 2. Последний член 384 = 3&nbsp;&middot;&nbsp;2<sup>7</sup>, значит членов 8. Сумма = 3(2<sup>8</sup> &minus; 1)/(2 &minus; 1) = 3&nbsp;&middot;&nbsp;255 = <b>765</b>. Быстрая проверка для <var>r</var> = 2: сумма = удвоенный последний член минус первый: 768 &minus; 3 = 765.',
          'en': 'A geometric sequence: <var>a</var><sub>1</sub> = 3, <var>r</var> = 2. The last term is 384 = 3&nbsp;&middot;&nbsp;2<sup>7</sup>, so there are 8 terms. Sum = 3(2<sup>8</sup> &minus; 1)/(2 &minus; 1) = 3&nbsp;&middot;&nbsp;255 = <b>765</b>. Quick check for <var>r</var> = 2: the sum is twice the last term minus the first: 768 &minus; 3 = 765.'}},
 ],
 'selfp': [
  {'q': {'ru': 'Решите уравнение 5(<var>x</var> &minus; 2) = 3<var>x</var> + 8.', 'en': 'Solve the equation 5(<var>x</var> &minus; 2) = 3<var>x</var> + 8.'},
   'hint': {'ru': 'Раскройте скобки и соберите <var>x</var> слева.', 'en': 'Expand and collect <var>x</var> on the left.'},
   'sol': {'ru': '5<var>x</var> &minus; 10 = 3<var>x</var> + 8, значит 2<var>x</var> = 18, <var>x</var> = <b>9</b>.', 'en': '5<var>x</var> &minus; 10 = 3<var>x</var> + 8, so 2<var>x</var> = 18, <var>x</var> = <b>9</b>.'}},
  {'q': {'ru': 'Сумма двух чисел 40, одно на 6 больше другого. Найдите их произведение.', 'en': 'The sum of two numbers is 40, and one is 6 more than the other. Find their product.'},
   'hint': {'ru': 'Числа: <var>x</var> и <var>x</var> + 6.', 'en': 'The numbers: <var>x</var> and <var>x</var> + 6.'},
   'sol': {'ru': '2<var>x</var> + 6 = 40, <var>x</var> = 17: числа 17 и 23, произведение <b>391</b>.', 'en': '2<var>x</var> + 6 = 40, <var>x</var> = 17: the numbers are 17 and 23, product <b>391</b>.'}},
  {'q': {'ru': 'Мастер красит забор за 4 часа, ученик &mdash; за 12. За сколько часов они покрасят его вместе?', 'en': 'A painter paints a fence in 4 hours, an apprentice in 12. How long will they take together?'},
   'hint': {'ru': 'Сложите производительности: 1/4 + 1/12.', 'en': 'Add the rates: 1/4 + 1/12.'},
   'sol': {'ru': '1/4 + 1/12 = 1/3 забора в час, значит <b>3 часа</b>.', 'en': '1/4 + 1/12 = 1/3 of the fence per hour, so <b>3 hours</b>.'}},
  {'q': {'ru': 'Смешали 2 литра 30-процентного раствора и 4 литра 15-процентного. Какова концентрация смеси?', 'en': 'Two liters of a 30% solution are mixed with four liters of a 15% solution. What is the concentration of the mixture?'},
   'hint': {'ru': 'Чистое вещество: 0,6 + 0,6 литра.', 'en': 'Pure substance: 0.6 + 0.6 liters.'},
   'sol': {'ru': '1,2 л вещества на 6 л: <b>20&nbsp;%</b>.', 'en': '1.2 L of substance out of 6 L: <b>20%</b>.'}},
  {'q': {'ru': 'В арифметической прогрессии <var>a</var><sub>1</sub> = 7 и <var>d</var> = 4. Найдите <var>a</var><sub>25</sub>.', 'en': 'In an arithmetic sequence, <var>a</var><sub>1</sub> = 7 and <var>d</var> = 4. Find <var>a</var><sub>25</sub>.'},
   'hint': {'ru': 'От первого члена до 25-го &mdash; 24 шага.', 'en': 'From the first term to the 25th there are 24 steps.'},
   'sol': {'ru': '7 + 24&nbsp;&middot;&nbsp;4 = <b>103</b>.', 'en': '7 + 24&nbsp;&middot;&nbsp;4 = <b>103</b>.'}},
  {'q': {'ru': 'Найдите сумму первых 30 нечётных чисел: 1 + 3 + 5 + &hellip; + 59.', 'en': 'Find the sum of the first 30 odd positive integers: 1 + 3 + 5 + &hellip; + 59.'},
   'hint': {'ru': 'Среднее первого и последнего, умноженное на количество.', 'en': 'The mean of the first and last, times the count.'},
   'sol': {'ru': '(1 + 59)/2&nbsp;&middot;&nbsp;30 = <b>900</b>. Красивый факт: сумма первых <var>n</var> нечётных всегда равна <var>n</var><sup>2</sup>.', 'en': '(1 + 59)/2&nbsp;&middot;&nbsp;30 = <b>900</b>. A nice fact: the sum of the first <var>n</var> odd positive integers is always <var>n</var><sup>2</sup>.'}},
  {'q': {'ru': 'В геометрической прогрессии <var>b</var><sub>3</sub> = 18 и <var>b</var><sub>5</sub> = 162. Найдите <var>b</var><sub>1</sub>.', 'en': 'In a geometric sequence, <var>a</var><sub>3</sub> = 18 and <var>a</var><sub>5</sub> = 162. Find <var>a</var><sub>1</sub>.'},
   'hint': {'ru': 'От 3-го до 5-го члена &mdash; два умножения на <var>r</var>.', 'en': 'From the 3rd to the 5th term there are two multiplications by <var>r</var>.'},
   'sol': {'ru': '<var>r</var><sup>2</sup> = 162/18 = 9. Тогда <var>b</var><sub>1</sub> = 18/<var>r</var><sup>2</sup> = <b>2</b> (знак <var>r</var> не важен: делим на <var>r</var><sup>2</sup>).', 'en': '<var>r</var><sup>2</sup> = 162/18 = 9. Then <var>a</var><sub>1</sub> = 18/<var>r</var><sup>2</sup> = <b>2</b> (the sign of <var>r</var> does not matter: we divide by <var>r</var><sup>2</sup>).'}},
  {'q': {'ru': 'Вася решает 2 задачи в минуту, Петя &mdash; 3. Петя начал на 5 минут позже Васи. Через сколько минут после старта Васи у них будет поровну решённых задач?', 'en': 'Maya solves 2 problems per minute; Ben solves 3. Ben starts 5 minutes after Maya. How many minutes after Maya starts will they have solved the same number of problems?'},
   'hint': {'ru': 'Если после старта Васи прошло <var>t</var> минут, сколько минут работал каждый?', 'en': 'If <var>t</var> minutes have passed since Maya started, how long has each of them been working?'},
   'sol': {'ru': 'Вася работал <var>t</var> минут, Петя <var>t</var> &minus; 5: уравнение 2<var>t</var> = 3(<var>t</var> &minus; 5), откуда <var>t</var> = <b>15 минут</b>. Проверка: у обоих по 30 задач.', 'en': 'Maya has worked <var>t</var> minutes, Ben <var>t</var> &minus; 5: the equation 2<var>t</var> = 3(<var>t</var> &minus; 5) gives <var>t</var> = <b>15 minutes</b>. Check: both have solved 30 problems.'}},
 ],
 'answers': {'ru': '9 · 391 · 3 ч · 20 % · 103 · 900 · 2 · 15 мин', 'en': '9, 391, 3 h, 20%, 103, 900, 2, 15 min'},
 'routing': {'ru': 'Норма &mdash; 6 из 8. Ошибки в 1&ndash;2 и 8 &mdash; &laquo;линейные уравнения&raquo;; в 3 &mdash; &laquo;работа&raquo;; в 4 &mdash; &laquo;смеси&raquo;; в 5&ndash;7 &mdash; &laquo;прогрессии&raquo;.',
             'en': 'Mastery bar: 6 of 8. For mistakes in 1&ndash;2 and 8, reread &ldquo;linear equations&rdquo;; for 3, &ldquo;work&rdquo;; for 4, &ldquo;mixtures&rdquo;; for 5&ndash;7, &ldquo;sequences&rdquo;.'},
}
