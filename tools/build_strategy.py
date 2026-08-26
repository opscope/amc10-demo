#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Блок 5 «Стратегия и моки»: страницы RU/EN + PDF-памятка на двух языках."""
import os, sys
SCR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCR)
from build_block import SITE, FONTS, FAV, GC, ROOT, CSS_FULL, PCSS, nav_html, render_pdf

TXT = {
 'ru': dict(
  title='Блок 5 · Стратегия и моки · Крэш-курс AMC 10',
  desc='Стратегия AMC 10: тайминг 75 минут, правило пропуска, протокол баллов и план четырёх полных моков.',
  eyebrow='Крэш-курс AMC 10 &middot; Блок 5', h1='Блок 5 &mdash; Стратегия и моки',
  stand='Один урок стратегии и четыре полных мока. Здесь курс перестаёт учить математике и начинает учить набирать баллы.',
  otherlang='English version', otherhref='strategy.html',
  s1h='С.1 · Урок стратегии (90 минут)',
  s1=f"""
<h3>Протокол баллов</h3>
<p>За верный ответ &mdash; <b>6 баллов</b>, за пустую клетку &mdash; <b>1,5</b>, за неверный &mdash; <b>0</b>. Из этого следует всё остальное: пустой ответ &mdash; это не поражение, а актив. 25 задач &times; 6 = 150; цель-минимум курса (&asymp;100+) достигается так: решаем 1&ndash;18, допуская две осечки, задачи 19&ndash;25 оставляем пустыми &mdash; 16&nbsp;верных&nbsp;&middot;&nbsp;6 + 7&nbsp;пустых&nbsp;&middot;&nbsp;1,5 = 106,5.</p>
<h3>Тайминг 75 минут</h3>
<div class="frm"><b>25 минут</b> на задачи 1&ndash;10 &middot; <b>30 минут</b> на 11&ndash;20 &middot; <b>20 минут</b> на выбранные из 21&ndash;25.</div>
<p>Первая десятка должна стоить дёшево: если задача из 1&ndash;10 съела больше трёх минут &mdash; вы решаете её неправильным способом. В 21&ndash;25 не &laquo;идём по порядку&raquo;, а выбираем одну-две своих: прочитать все пять, взять ту, где виден путь.</p>
<h3>Правило пропуска и угадывания</h3>
<p>Слепое угадывание даёт в среднем 6/5 = 1,2 балла &mdash; <b>меньше</b>, чем 1,5 за пустую клетку. Значит: не исключил ни одного варианта &mdash; оставляй пустым. Исключил два&nbsp;варианта &mdash; ожидание угадывания 2 балла, уже выгодно. Граница проста: <b>угадываем только после честного исключения хотя бы двух вариантов</b>.</p>
<h3>Ловушки формулировок</h3>
<p>Перед записью ответа &mdash; перечитать вопрос: спрашивают <var>x</var> или <var>y</var>? сумму или произведение? &laquo;чему равно&raquo; или &laquo;чему НЕ может равняться&raquo;? На AMC неверная величина почти всегда есть среди вариантов. Привычка стоит пять секунд и приносит 6 баллов за тест.</p>
<h3>Чек-лист боевого дня</h3>
<p>Выспаться; калькулятора нет &mdash; и не нужен; черновик размечаем по номерам задач; ответы переносим в бланк блоками по пять; последние 3 минуты &mdash; только перенос и проверка бланка, не решение.</p>""",
  mocksh='Четыре полных мока',
  mocks=f"""
<p>Моки &mdash; настоящие AMC 10 прошлых лет (свободно опубликованы в вики AoPS), не самодельные: калибровка сложности и формулировок должна быть родная. Каждый мок &mdash; это 75 минут по боевому протоколу плюс разбор; <b>мок без разбора не считается сделанным</b> &mdash; разбор и есть половина ценности.</p>
<table class="mocktab">
<tr><th>Мок</th><th>Когда</th><th>Что</th></tr>
<tr><td>Мок 1</td><td>неделя 9, после С.1</td><td>75 мин + разбор 60. Первая калибровка: карта потерь &mdash; где минус от незнания, где от спешки.</td></tr>
<tr><td>Мок 2</td><td>неделя 10</td><td>75 мин + разбор 60. Сверка динамики с моком 1; добор-уроки по темам провалов.</td></tr>
<tr><td>Мок 3</td><td>неделя 10</td><td>75 мин + разбор 60. Отработка тайминга: жёсткие 25/30/20.</td></tr>
<tr><td>Мок 4</td><td>за 4&ndash;5 дней до 10A</td><td>Генеральная: лёгкий день, боевой протокол, разбор 45. После него ничего нового не учим.</td></tr>
</table>
<p>Между моками &mdash; точечные добор-уроки по темам провалов (&asymp;2 часа резерва заложено в разборы). Разбор мока: сначала задачи, где ответ был близко (спешка, арифметика, прочтение), потом одна-две темы, где провал системный.</p>
<h3>Как провести мок: протокол для родителя</h3>
<p><b>Где взять тест.</b> Все AMC 10 прошлых лет с решениями свободно опубликованы в вики AoPS: <a href="https://artofproblemsolving.com/wiki/index.php/AMC_10_Problems_and_Solutions">artofproblemsolving.com &rarr; AMC 10 Problems and Solutions</a>. Для четырёх моков берите свежие годы по порядку: 2024&nbsp;10A, 2024&nbsp;10B, 2025&nbsp;10A, 2025&nbsp;10B (страницу с решениями до конца разбора не открывать).</p>
<p><b>Проведение.</b> Распечатайте задачи (или откройте на отдельном экране), выдайте черновик и лист для ответов с номерами 1&ndash;25. Таймер на 75 минут на виду; телефона и калькулятора на столе нет. В процессе не подсказывать и не комментировать &mdash; даже взглядом. По сигналу таймера &mdash; ручки на стол, лист сдаётся.</p>
<p><b>Подсчёт.</b> Сверьте с ключом на той же вики-странице: верный &times; 6, пустой &times; 1,5, неверный &times; 0. Запишите три числа (верных / пустых / неверных) и итоговый балл &mdash; по ним будет видна динамика от мока к моку. Разбор &mdash; на следующий день, по правилу из раздела выше.</p>""",
  twoh='Стратегия двух версий: 10A и 10B',
  two="""
<p>Регистрируемся на обе версии: <b>10A &mdash; четверг 5 ноября</b>, <b>10B &mdash; пятница 13 ноября</b>. 10A играем как первый боевой заход: привыкание к залу, протоколу и нервам. 10B &mdash; основная попытка: формат уже знаком, между версиями &mdash; неделя точечного добора по итогам A. В зачёт идёт лучший результат, так что первая версия ничем не рискует.</p>""",
  pdfs='Для печати:', pdfl='памятка стратегии (PDF)',
  foot='Задачи курса составлены оригинально и не воспроизводят задания официальных олимпиад AMC. <a href="index.html">Оглавление курса</a> &middot; <a href="../../index.html">справка об AMC 10 и пробный тест</a> &middot; <a href="index.html#svyaz">оставить комментарий</a>.',
  pdf_file='strategy-ru.pdf',
  pdft='Крэш-курс AMC 10 · Блок 5 · Стратегия', pdfsub='Памятка: протокол баллов, тайминг, правило пропуска, план моков.'),
 'en': dict(
  title='Block 5 · Strategy and Mocks · AMC 10 Crash Course',
  desc='AMC 10 strategy: the 75-minute timing plan, the skip rule, the scoring protocol, and a four-mock schedule.',
  eyebrow='AMC 10 Crash Course &middot; Block 5', h1='Block 5 &mdash; Strategy and Mocks',
  stand='One strategy lesson and four full mocks. This is where the course stops teaching math and starts teaching scoring.',
  otherlang='Русская версия', otherhref='strategy-ru.html',
  s1h='S.1 · The strategy lesson (90 minutes)',
  s1=f"""
<h3>The scoring protocol</h3>
<p>A correct answer is worth <b>6 points</b>, a blank <b>1.5</b>, a wrong answer <b>0</b>. Everything else follows from this: a blank is not a defeat, it is an asset. 25 problems &times; 6 = 150; the course&rsquo;s minimum goal (&asymp;100+) is reached like this: work 1&ndash;18 allowing two slips, and leave 19&ndash;25 blank &mdash; 16&nbsp;correct&nbsp;&middot;&nbsp;6 + 7&nbsp;blanks&nbsp;&middot;&nbsp;1.5 = 106.5.</p>
<h3>The 75-minute timing plan</h3>
<div class="frm"><b>25 minutes</b> for problems 1&ndash;10 &middot; <b>30 minutes</b> for 11&ndash;20 &middot; <b>20 minutes</b> for your picks from 21&ndash;25.</div>
<p>The first ten must come cheap: if a problem from 1&ndash;10 has taken more than three minutes, you are solving it the wrong way. In 21&ndash;25 you do not &ldquo;go in order&rdquo;: read all five, pick the one or two where you can see a path.</p>
<h3>The skip-or-guess rule</h3>
<p>A blind guess is worth 6/5 = 1.2 points on average &mdash; <b>less</b> than the 1.5 for a blank. So: eliminated nothing &mdash; leave it blank. Eliminated two choices &mdash; the expected value of a guess is 2 points, now it pays. The line is simple: <b>guess only after honestly eliminating at least two choices</b>.</p>
<h3>Wording traps</h3>
<p>Before marking an answer, reread the question: do they ask for <var>x</var> or <var>y</var>? the sum or the product? &ldquo;what is&rdquo; or &ldquo;what CANNOT be&rdquo;? On the AMC the wrong quantity is almost always among the choices. The habit costs five seconds and earns six points per test.</p>
<h3>Test-day checklist</h3>
<p>Sleep; there is no calculator &mdash; and none is needed; label scratch work by problem number; transfer answers to the sheet in blocks of five; the last 3 minutes are for transfer and bubble checking only, not solving.</p>""",
  mocksh='Four full mocks',
  mocks=f"""
<p>The mocks are real past AMC 10 tests (freely published on the AoPS wiki), not homemade ones: the difficulty and phrasing calibration must be authentic. Each mock is 75 minutes under the real protocol plus a review; <b>a mock without a review does not count</b> &mdash; the review is half the value.</p>
<table class="mocktab">
<tr><th>Mock</th><th>When</th><th>What</th></tr>
<tr><td>Mock 1</td><td>week 9, after S.1</td><td>75 min + 60 review. First calibration: a loss map &mdash; where points die of not knowing vs. of rushing.</td></tr>
<tr><td>Mock 2</td><td>week 10</td><td>75 min + 60 review. Compare against Mock 1; catch-up lessons on the failed topics.</td></tr>
<tr><td>Mock 3</td><td>week 10</td><td>75 min + 60 review. Timing drill: strict 25/30/20.</td></tr>
<tr><td>Mock 4</td><td>4&ndash;5 days before 10A</td><td>Dress rehearsal: a light day, real protocol, 45-minute review. Nothing new is learned after it.</td></tr>
</table>
<p>Between mocks: targeted catch-up lessons on failed topics (&asymp;2 hours of reserve is built into the reviews). Review order: first the problems where the answer was close (rushing, arithmetic, misreading), then the one or two topics where the failure is systematic.</p>
<h3>Running a mock: the parent protocol</h3>
<p><b>Where to get the test.</b> Every past AMC 10 with solutions is freely published on the AoPS wiki: <a href="https://artofproblemsolving.com/wiki/index.php/AMC_10_Problems_and_Solutions">artofproblemsolving.com &rarr; AMC 10 Problems and Solutions</a>. For the four mocks take recent years in order: 2024&nbsp;10A, 2024&nbsp;10B, 2025&nbsp;10A, 2025&nbsp;10B (do not open the solutions page until the review is done).</p>
<p><b>Running it.</b> Print the problems (or open them on a separate screen), hand over scratch paper and an answer sheet numbered 1&ndash;25. A visible 75-minute timer; no phone or calculator on the desk. No hints and no commentary during the test &mdash; not even a look. When the timer sounds: pens down, sheet handed in.</p>
<p><b>Scoring.</b> Check against the key on the same wiki page: correct &times; 6, blank &times; 1.5, wrong &times; 0. Write down three numbers (correct / blank / wrong) and the total &mdash; they show the trend from mock to mock. The review happens the next day, by the rule above.</p>""",
  twoh='The two-version strategy: 10A and 10B',
  two="""
<p>Register for both versions: <b>10A &mdash; Thursday, November 5</b>, <b>10B &mdash; Friday, November 13</b>. Play 10A as the first live run: getting used to the room, the protocol, and the nerves. 10B is the main attempt: the format is familiar, and the week between the versions is spent on targeted catch-up based on A. The better score counts, so the first version risks nothing.</p>""",
  pdfs='Printable:', pdfl='strategy cheat sheet (PDF)',
  foot='All problems are original and do not reproduce official AMC competition problems. <a href="index-en.html">Course contents</a> &middot; <a href="../../index-en.html">AMC 10 overview and practice test</a> &middot; <a href="index-en.html#contact">leave a comment</a>.',
  pdf_file='strategy.pdf',
  pdft='AMC 10 Crash Course · Block 5 · Strategy', pdfsub='Cheat sheet: scoring protocol, timing plan, skip rule, mock schedule.'),
}

EXTRA_CSS = """
table.mocktab { border-collapse: collapse; width: 100%; margin: 1rem 0 1.4rem; font-size: .93rem; }
table.mocktab th { font-family: var(--mono); font-size: .72rem; letter-spacing: .1em; text-transform: uppercase; text-align: left; color: var(--tang-deep); border-bottom: 1px solid var(--rule-strong); padding: .45rem .6rem; }
table.mocktab td { border-bottom: 1px solid var(--rule); padding: .55rem .6rem; vertical-align: top; }
table.mocktab td:first-child { font-family: var(--mono); font-size: .8rem; white-space: nowrap; }
"""

def page(g):
    t = TXT[g]
    body = f'''<div class="layout">
{nav_html(g, 5)}
<main>
<header style="margin-bottom:2.2rem">
<div class="eyebrow">{t['eyebrow']} &nbsp;&middot;&nbsp; <a class="langlink" href="{t['otherhref']}">{t['otherlang']}</a></div>
<h1>{t['h1']}</h1>
<p class="standfirst">{t['stand']}</p>
</header>
<section class="lesson" id="s1">
<div class="lesson-id">{t['eyebrow']}</div>
<h2>{t['s1h']}</h2>
<div class="theory">{t['s1']}</div>
</section>
<section class="lesson" id="mocks">
<h2>{t['mocksh']}</h2>
<div class="theory">{t['mocks']}</div>
</section>
<section class="lesson" id="ab">
<h2>{t['twoh']}</h2>
<div class="theory">{t['two']}</div>
<div class="pdfline"><strong>{t['pdfs']}</strong> <a href="{t['pdf_file']}">{t['pdfl']}</a></div>
</section>
<footer>{t['foot']}</footer>
</main>
</div>'''
    return f'''<!DOCTYPE html>
<html lang="{g}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t['title']}</title>
<meta name="description" content="{t['desc']}">
{FAV}
<style>
{FONTS}
{ROOT}
{CSS_FULL}
{EXTRA_CSS}
</style>
{GC}
</head>
<body>
{body}
</body>
</html>
'''

def pdf(g):
    t = TXT[g]
    return f'''<!DOCTYPE html><html lang="{g}"><head><meta charset="utf-8"><style>{PCSS}
table.mocktab {{ border-collapse: collapse; width: 100%; margin: 8px 0; }}
table.mocktab th, table.mocktab td {{ border: 1px solid #000; padding: 4px 7px; text-align: left; font-size: 9.7pt; vertical-align: top; }}
table.mocktab th {{ font-size: 8.5pt; text-transform: uppercase; letter-spacing: .05em; }}
</style></head><body>
<header><div class="t1h">{t['pdft']}</div><div class="t2h">{t['pdfsub']}</div></header>
<h2>{t['s1h']}</h2>{t['s1']}
<h2>{t['mocksh']}</h2>{t['mocks']}
<h2>{t['twoh']}</h2>{t['two']}
<div class="colophon">{'Задачи составлены оригинально и не воспроизводят задания официальных олимпиад AMC' if g == 'ru' else 'All problems are original and do not reproduce official AMC competition problems'} &middot; opscope.github.io/amc10-demo/course/amc10/</div>
</body></html>'''

if __name__ == '__main__':
    open(f'{SITE}/course/amc10/strategy-ru.html', 'w', encoding='utf8').write(page('ru'))
    open(f'{SITE}/course/amc10/strategy.html', 'w', encoding='utf8').write(page('en'))
    print('strategy pages written')
    render_pdf(pdf('ru'), f'{SITE}/course/amc10/strategy-ru.pdf')
    render_pdf(pdf('en'), f'{SITE}/course/amc10/strategy.pdf')
