#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AMC 8: лендинг (RU/EN) и диагностика (RU/EN). Самодостаточно, без отсылок к AMC 10."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_algebra as BA

SITE = os.path.dirname(HERE)
FORM_ACTION = 'https://amc10-forma.opscope.workers.dev/'

SPEC_CSS = '''
.spec { border-top: 1px solid var(--rule-strong); margin: 1.4rem 0; }
.spec-row { display: grid; grid-template-columns: 10.5rem 1fr; gap: 1rem; padding: .85rem 0; border-bottom: 1px solid var(--rule); align-items: baseline; }
.spec-key { font-family: var(--mono); font-size: .72rem; font-weight: 500; letter-spacing: .1em; text-transform: uppercase; color: var(--ash); }
.spec-val { font-size: .97rem; }
.spec-val em { color: var(--ash); }
@media (max-width: 34rem) { .spec-row { grid-template-columns: 1fr; gap: .15rem; } }
'''

def shell(lang, title, desc, body):
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
{BA.FAV}
<style>
{BA.FONTS}
{BA.ROOT}
{BA.CSS}
{SPEC_CSS}
</style>
{BA.GC}
</head>
<body>
<div class="layout">
{body}
</div>
</body>
</html>
'''

def nav(g, here):
    def h(k):
        return 'class="here" ' if here == k else ''
    if g == 'ru':
        return f'''<nav class="side">
<div class="nav-t">Курсы</div>
<details name="course" open><summary>AMC 8</summary>
<a {h('about')}href="index.html#zachem">О курсе</a>
<a href="index.html#programma">Программа</a>
<a {h('practice')}href="practice-test-ru.html">Пробный тест</a>
<a {h('diag')}href="diagnostics-ru.html">0 · Диагностика</a>
<a href="numbers-ru.html">1 · Числа и арифметика</a>
<a href="index.html#svyaz">Комментарии</a>
</details>
<details name="course"><summary>AMC 10</summary>
<a href="../amc10/index.html">Открыть курс AMC 10</a>
</details>
<details name="course"><summary>AMC 12</summary>
<div class="nav-note">готовится к сезону 2027</div>
</details>
<div class="nav-t">Ещё</div>
<a href="../index.html">Все курсы</a>
</nav>'''
    return f'''<nav class="side">
<div class="nav-t">Courses</div>
<details name="course" open><summary>AMC 8</summary>
<a {h('about')}href="index-en.html#why">About the course</a>
<a href="index-en.html#program">Program</a>
<a {h('practice')}href="practice-test.html">Practice test</a>
<a {h('diag')}href="diagnostics.html">0 · Diagnostics</a>
<a href="numbers.html">1 · Numbers and arithmetic</a>
<a href="index-en.html#contact">Comments</a>
</details>
<details name="course"><summary>AMC 10</summary>
<a href="../amc10/index-en.html">Open the AMC 10 course</a>
</details>
<details name="course"><summary>AMC 12</summary>
<div class="nav-note">coming for the 2027 season</div>
</details>
<div class="nav-t">More</div>
<a href="../index-en.html">All courses</a>
</nav>'''

def form(g):
    if g == 'ru':
        return f'''<form class="fb" action="{FORM_ACTION}" method="POST">
    <input type="hidden" name="lang" value="ru">
    <input type="hidden" name="course" value="amc8">
    <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">
    <div class="row2">
      <div><label for="fb-name">Имя (необязательно)</label><input id="fb-name" type="text" name="name" autocomplete="name"></div>
      <div><label for="fb-contact">Контакт для ответа (почта или телеграм)</label><input id="fb-contact" type="text" name="contact" autocomplete="email"></div>
    </div>
    <div><label for="fb-msg">Комментарий</label><textarea id="fb-msg" name="message" required></textarea></div>
    <button type="submit">Отправить</button>
    <p class="fine">Сообщение уходит прямо нам. Ничего, кроме того, что вы написали, не отправляется.</p>
  </form>'''
    return f'''<form class="fb" action="{FORM_ACTION}" method="POST">
    <input type="hidden" name="lang" value="en">
    <input type="hidden" name="course" value="amc8">
    <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">
    <div class="row2">
      <div><label for="fb-name">Name (optional)</label><input id="fb-name" type="text" name="name" autocomplete="name"></div>
      <div><label for="fb-contact">Contact for a reply (email or Telegram)</label><input id="fb-contact" type="text" name="contact" autocomplete="email"></div>
    </div>
    <div><label for="fb-msg">Comment</label><textarea id="fb-msg" name="message" required></textarea></div>
    <button type="submit">Send</button>
    <p class="fine">The message goes straight to us. Nothing beyond what you wrote is sent.</p>
  </form>'''

# ---------- ЛЕНДИНГ ----------
LAND_RU = lambda: nav('ru', 'about') + f'''
<main>
<header style="margin-bottom:3rem">
  <div class="eyebrow">AMC 8 &middot; Крэш-курс &middot; сезон 2026&ndash;27 &nbsp;&middot;&nbsp; <a class="langlink" href="index-en.html">English version</a></div>
  <h1>Подготовка к AMC&nbsp;8</h1>
  <p class="standfirst">Самодостаточный курс для семьи: родитель ведёт занятия без преподавателя, всё преподавание зашито в материалы. Бесплатно, весь контент открыт.</p>
</header>

<section id="zachem">
  <h2>Что такое AMC 8</h2>
  <p>AMC&nbsp;8 &mdash; общенациональная олимпиада по математике для учеников 8 класса и младше, которую проводит Математическая ассоциация Америки. Это первая большая математическая олимпиада в жизни школьника &mdash; и лучший способ понять, интересна ли ему олимпиадная математика вообще.</p>
  <div class="spec">
    <div class="spec-row"><div class="spec-key">Кто участвует</div><div class="spec-val">Ученики 8 класса и младше, которым на день олимпиады меньше 15,5 лет</div></div>
    <div class="spec-row"><div class="spec-key">Формат</div><div class="spec-val">25 задач за 40 минут, каждая с выбором одного ответа из пяти (A&ndash;E)</div></div>
    <div class="spec-row"><div class="spec-key">Баллы</div><div class="spec-val">1 балл за верный ответ, 0 за неверный и за пропуск. Штрафов нет &mdash; поэтому <strong>отвечать выгодно на все задачи</strong>, даже наугад</div></div>
    <div class="spec-row"><div class="spec-key">Когда</div><div class="spec-val">Окно <strong>21&ndash;27 января 2027</strong>: школа или центр проведения выбирает день внутри окна. <em>Регистрация идёт через школу или официальный центр и закрывается заранее (обычный дедлайн &mdash; начало января).</em></div></div>
    <div class="spec-row"><div class="spec-key">Что дальше</div><div class="spec-val">Следующего раунда нет: лучшие попадают в списки почёта (Honor Roll &mdash; примерно топ-5&nbsp;%, Distinguished Honor Roll &mdash; топ-1&nbsp;%). Дальше естественная ступень &mdash; AMC&nbsp;10 в ноябре</div></div>
    <div class="spec-row"><div class="spec-key">Калькулятор</div><div class="spec-val">Запрещён; черновики и линейка разрешены</div></div>
  </div>
  <p>Темп &mdash; главная особенность: полторы минуты на задачу. Олимпиада проверяет не глубину, а уверенное владение школьной арифметикой, здравый смысл и внимательность на скорости.</p>
</section>

<section id="ustroystvo">
  <h2>Как устроен курс</h2>
  <p>Родитель здесь администратор, не учитель: выдаёт материалы по расписанию, засекает время, сверяет ответы с ключом. Теорию ученик читает сам; у каждой разобранной задачи есть полное решение, у каждой самостоятельной &mdash; подсказка-направление и решение в раскрывающихся блоках; у тестов &mdash; ключ и разбор для родителя.</p>
  <div class="ritm">
    <b>РИТМ</b><br>
    Урок длится 90 минут и разбит на две половинки по 45.
    <b>Половинка A</b>: теория 15 минут, разобранные задачи 30.
    <b>Половинка B</b>: самостоятельная порция 30 минут, разбор 15.
    Можно заниматься три раза в неделю по 90 или шесть раз по 45. После каждого блока &mdash; тест: 10 задач за 20 минут, порог усвоения 7 из 10. Ниже порога &mdash; один добор-урок по проваленным подтемам, не &laquo;всё заново&raquo;.
  </div>
  <div class="notice">
    <strong>Правило задач.</strong> Каждая задача либо решена, либо разобрана письменно. &laquo;Посмотрел ответ и кивнул&raquo; не считается: подсмотренная задача возвращается в очередь через несколько дней.
  </div>
</section>

<section id="programma">
  <h2>Программа</h2>
  <p>Сезон: старт в начале ноября, финиш к олимпиаде в конце января. Начните с пробного теста &mdash; он даст честную карту пробелов.</p>
  <div class="toc-item"><div class="n">&#9998;</div><div><a href="practice-test-ru.html">Пробный тест</a><div class="d">25 оригинальных задач в формате AMC&nbsp;8 &middot; ключ и разборы &middot; печатный PDF</div></div><div class="tag go">открыт</div></div>
  <div class="toc-item"><div class="n">0</div><div><a href="diagnostics-ru.html">Диагностика</a><div class="d">Пробный тест 25&times;40 в боевом режиме + протокол для родителя</div></div><div class="tag go">открыта</div></div>
  <div class="toc-item"><div class="n">1</div><div><a href="numbers-ru.html">Числа и арифметика</a><div class="d">Дроби · проценты · отношения и пропорции · средние · прикидка и последняя цифра · тест Т1 · <a class="langlink" href="numbers.html">English version</a> · PDF</div></div><div class="tag go">открыт целиком</div></div>
  <div class="toc-item"><div class="n">2</div><div>Геометрия<div class="d">Углы · периметры и площади · сетки и разрезания · объёмы</div></div><div class="tag">готовится</div></div>
  <div class="toc-item"><div class="n">3</div><div>Счёт и вероятность<div class="d">Подсчёты · таблицы и деревья · простая вероятность · паттерны</div></div><div class="tag">готовится</div></div>
  <div class="toc-item"><div class="n">4</div><div>Логика и текстовые задачи<div class="d">Движение и работа · уравнения без иксов · перебор и организация случаев</div></div><div class="tag">готовится</div></div>
  <div class="toc-item"><div class="n">5</div><div>Стратегия и прогоны<div class="d">Темп 40 минут, &laquo;отвечать на всё&raquo;, прогоны по настоящим тестам прошлых лет</div></div><div class="tag">готовится</div></div>
  <p style="margin-top:1.2rem; color:var(--ash); font-size:.93rem">Блоки публикуются с опережением графика. Пробные прогоны в конце курса &mdash; по настоящим тестам прошлых лет: они свободно опубликованы в вики <a href="https://artofproblemsolving.com/wiki/index.php/AMC_8_Problems_and_Solutions">Art of Problem Solving</a>.</p>
</section>

<section id="svyaz">
  <h2>Комментарии и пожелания</h2>
  <p>Нашли ошибку, чего-то не хватает, хотите присоединиться к подготовке &mdash; напишите. Имя и контакт нужны только если хотите, чтобы мы ответили.</p>
  {form('ru')}
</section>
<footer>
  Задачи курса составлены оригинально и не воспроизводят задания официальных олимпиад AMC. <a href="../index.html">Все курсы</a>.
</footer>
</main>
'''

LAND_EN = lambda: nav('en', 'about') + f'''
<main>
<header style="margin-bottom:3rem">
  <div class="eyebrow">AMC 8 &middot; Crash Course &middot; 2026&ndash;27 season &nbsp;&middot;&nbsp; <a class="langlink" href="index.html">Русская версия</a></div>
  <h1>AMC&nbsp;8 preparation</h1>
  <p class="standfirst">A self-contained course for a family: a parent runs the lessons without a teacher &mdash; all the teaching is built into the materials. Free, with everything open.</p>
</header>

<section id="why">
  <h2>What the AMC 8 is</h2>
  <p>The AMC&nbsp;8 is a nationwide math competition for students in grade 8 and below, run by the Mathematical Association of America. For most students it is the first big math competition of their lives &mdash; and the best way to find out whether competition math is their thing at all.</p>
  <div class="spec">
    <div class="spec-row"><div class="spec-key">Who can take it</div><div class="spec-val">Students in grade 8 or below who are under 15.5 years old on competition day</div></div>
    <div class="spec-row"><div class="spec-key">Format</div><div class="spec-val">25 problems in 40 minutes, each multiple choice with five options (A&ndash;E)</div></div>
    <div class="spec-row"><div class="spec-key">Scoring</div><div class="spec-val">1 point for a correct answer, 0 for a wrong answer or a blank. No penalties &mdash; so <strong>it always pays to answer every problem</strong>, even by guessing</div></div>
    <div class="spec-row"><div class="spec-key">When</div><div class="spec-val">The window is <strong>January 21&ndash;27, 2027</strong>: each school or test center picks a day inside it. <em>Registration goes through a school or an official center and closes in advance (the regular deadline is early January).</em></div></div>
    <div class="spec-row"><div class="spec-key">What comes next</div><div class="spec-val">There is no next round: top scorers make the Honor Roll (roughly top 5%) and Distinguished Honor Roll (top 1%). The natural next step is the AMC&nbsp;10 in November</div></div>
    <div class="spec-row"><div class="spec-key">Calculator</div><div class="spec-val">Not allowed; scratch paper and a ruler are fine</div></div>
  </div>
  <p>Pace is the defining feature: about a minute and a half per problem. The competition tests not depth but confident command of school arithmetic, common sense, and attention at speed.</p>
</section>

<section id="how">
  <h2>How the course works</h2>
  <p>The parent here is an administrator, not a teacher: hand out the materials on schedule, run the timer, check answers against the key. The student reads the theory alone; every worked example has a full solution, every independent problem has a direction-only hint and a full solution in expandable blocks, and every test comes with a key and a parent review.</p>
  <div class="ritm">
    <b>RHYTHM</b><br>
    A lesson runs 90 minutes and splits into two 45-minute halves.
    <b>Half A</b>: 15 minutes of theory, 30 minutes of worked examples.
    <b>Half B</b>: a 30-minute independent set, 15 minutes of review.
    Work three times a week for 90 minutes or six times for 45. After each block there is a test: 10 problems in 20 minutes, mastery bar 7 of 10. Below the bar, assign one catch-up lesson on the missed subtopics &mdash; not a full redo.
  </div>
  <div class="notice">
    <strong>The problem rule.</strong> Every problem is either solved or worked through in writing. &ldquo;Glanced at the answer and nodded&rdquo; does not count: a peeked problem returns to the queue a few days later.
  </div>
</section>

<section id="program">
  <h2>Program</h2>
  <p>The season starts in early November and finishes at the late-January competition. Start with the practice test &mdash; it gives an honest map of the gaps.</p>
  <div class="toc-item"><div class="n">&#9998;</div><div><a href="practice-test.html">Practice test</a><div class="d">25 original problems in AMC&nbsp;8 format &middot; key and solutions &middot; printable PDF</div></div><div class="tag go">open</div></div>
  <div class="toc-item"><div class="n">0</div><div><a href="diagnostics.html">Diagnostics</a><div class="d">The 25&times;40 practice test under real conditions + a parent protocol</div></div><div class="tag go">open</div></div>
  <div class="toc-item"><div class="n">1</div><div><a href="numbers.html">Numbers and arithmetic</a><div class="d">Fractions · percents · ratios and proportions · averages · estimation and the last digit · test T1 · <a class="langlink" href="numbers-ru.html">Русская версия</a> · PDF</div></div><div class="tag go">fully open</div></div>
  <div class="toc-item"><div class="n">2</div><div>Geometry<div class="d">Angles · perimeters and areas · grids and dissections · volumes</div></div><div class="tag">in production</div></div>
  <div class="toc-item"><div class="n">3</div><div>Counting and probability<div class="d">Counting · tables and trees · simple probability · patterns</div></div><div class="tag">in production</div></div>
  <div class="toc-item"><div class="n">4</div><div>Logic and word problems<div class="d">Motion and work · equations without x&rsquo;s · organized casework</div></div><div class="tag">in production</div></div>
  <div class="toc-item"><div class="n">5</div><div>Strategy and mock runs<div class="d">The 40-minute pace, &ldquo;answer everything&rdquo;, real past-year runs</div></div><div class="tag">in production</div></div>
  <p style="margin-top:1.2rem; color:var(--ash); font-size:.93rem">Blocks ship ahead of the course schedule. The mock runs at the end of the course use real past exams, freely published in the <a href="https://artofproblemsolving.com/wiki/index.php/AMC_8_Problems_and_Solutions">Art of Problem Solving wiki</a>.</p>
</section>

<section id="contact">
  <h2>Comments and requests</h2>
  <p>Found a mistake, missing something, want to join the preparation &mdash; write to us. The name and contact are needed only if you want a reply.</p>
  {form('en')}
</section>
<footer>
  All course problems are original and do not reproduce official AMC competition problems. <a href="../index-en.html">All courses</a>.
</footer>
</main>
'''

# ---------- ДИАГНОСТИКА ----------
DIAG_RU = lambda: nav('ru', 'diag') + '''
<main>
<header style="margin-bottom:2.5rem">
  <div class="eyebrow">Крэш-курс AMC 8 &middot; Блок 0 &nbsp;&middot;&nbsp; <a class="langlink" href="diagnostics.html">English version</a></div>
  <h1>Диагностика</h1>
  <p class="standfirst">Пробный тест в боевом режиме: честная карта пробелов до старта занятий.</p>
</header>
<section class="lesson" id="diagnostics">
<div class="lesson-id">Блок 0 &middot; неделя 1</div>
<h2>Диагностика</h2>
<div class="lesson-meta"><span>40 минут тест</span><span>45 минут разбор на следующий день</span></div>

<p>Первый шаг &mdash; <a href="practice-test-ru.html">пробный тест из 25 задач</a> в боевом режиме: ровно 40 минут, без калькулятора. Не готовимся, не разминаемся: цель &mdash; честная карта пробелов, а не красивый результат.</p>

<p>Для печати: <a href="practice-test-ru.pdf">пробный тест PDF</a>. Ключ ответов на отдельной последней странице: её удобно не печатать или отрезать.</p>

<div class="parent">
<h3>Протокол для родителя</h3>
<p><b>До:</b> распечатайте или откройте тест, выдайте черновик, уберите телефон, поставьте таймер на 40 минут. Скажите одну фразу: &laquo;на AMC&nbsp;8 штрафов нет &mdash; отвечай на все задачи, даже наугад&raquo;.</p>
<p><b>После:</b> посчитайте балл: 1 за верную, 0 за остальное. Любой первый результат нормален: типичный школьник без подготовки решает 10&ndash;15 из 25. Запишите три списка: решено уверенно / решено с трудом или наугад / не успел.</p>
<p><b>Назавтра:</b> разбор по решениям на странице теста, начиная с задач &laquo;с трудом&raquo; и &laquo;не успел&raquo;. Отдельно посмотрите на ВРЕМЯ: если ученик не дошёл до задачи 20, главный враг пока темп, а не темы.</p>
</div>
</section>
<footer>
  Задачи курса составлены оригинально и не воспроизводят задания официальных олимпиад AMC. <a href="index.html">Курс AMC 8</a> &middot; <a href="index.html#svyaz">оставить комментарий</a>.
</footer>
</main>
'''

DIAG_EN = lambda: nav('en', 'diag') + '''
<main>
<header style="margin-bottom:2.5rem">
  <div class="eyebrow">AMC 8 Crash Course &middot; Block 0 &nbsp;&middot;&nbsp; <a class="langlink" href="diagnostics-ru.html">Русская версия</a></div>
  <h1>Diagnostics</h1>
  <p class="standfirst">The practice test under real conditions: an honest map of the gaps before lessons begin.</p>
</header>
<section class="lesson" id="diagnostics">
<div class="lesson-id">Block 0 &middot; week 1</div>
<h2>Diagnostics</h2>
<div class="lesson-meta"><span>40-minute test</span><span>45-minute review the next day</span></div>

<p>The first step is the <a href="practice-test.html">25-problem practice test</a> under real conditions: exactly 40 minutes, no calculator. No preparation, no warm-up: the goal is an honest map of the gaps, not a pretty score.</p>

<p>Printable: <a href="practice-test.pdf">the practice test as a PDF</a>. The answer key is on a separate final page: leave it unprinted or cut it off.</p>

<div class="parent">
<h3>Parent protocol</h3>
<p><b>Before:</b> print or open the test, hand out scratch paper, take the phone away, set a timer for 40 minutes. Say one sentence: &ldquo;there are no penalties on the AMC&nbsp;8 &mdash; answer every problem, even by guessing.&rdquo;</p>
<p><b>After:</b> score it: 1 per correct answer, 0 otherwise. Any first result is normal: a typical student with no preparation solves 10&ndash;15 of 25. Write down three lists: solved confidently / solved with difficulty or by guessing / ran out of time.</p>
<p><b>The next day:</b> go through the solutions on the test page, starting with the &ldquo;with difficulty&rdquo; and &ldquo;ran out of time&rdquo; problems. Look separately at TIME: if the student never reached problem 20, the main enemy for now is pace, not topics.</p>
</div>
</section>
<footer>
  All course problems are original and do not reproduce official AMC competition problems. <a href="index-en.html">AMC 8 course</a> &middot; <a href="index-en.html#contact">leave a comment</a>.
</footer>
</main>
'''

if __name__ == '__main__':
    open(f'{SITE}/course/amc8/index.html', 'w', encoding='utf8').write(shell('ru',
        'Крэш-курс AMC 8 · Подготовка', 'Самодостаточный бесплатный курс подготовки к AMC 8: формат олимпиады, программа блоков, пробный тест.', LAND_RU()))
    open(f'{SITE}/course/amc8/index-en.html', 'w', encoding='utf8').write(shell('en',
        'AMC 8 Crash Course · Preparation', 'A free self-contained AMC 8 prep course: the competition format, block program, and practice test.', LAND_EN()))
    open(f'{SITE}/course/amc8/diagnostics-ru.html', 'w', encoding='utf8').write(shell('ru',
        'Блок 0 · Диагностика · Крэш-курс AMC 8', 'Диагностический прогон пробного теста AMC 8 с протоколом для родителя.', DIAG_RU()))
    open(f'{SITE}/course/amc8/diagnostics.html', 'w', encoding='utf8').write(shell('en',
        'Block 0 · Diagnostics · AMC 8 Crash Course', 'A diagnostic run of the AMC 8 practice test with a parent protocol.', DIAG_EN()))
    print('amc8 landing + diagnostics written')
