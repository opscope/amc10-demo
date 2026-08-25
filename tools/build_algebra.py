#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Сборка блока 1 «Алгебра»: страницы RU/EN + 4 PDF (уроки и тест Т1 на двух языках)."""
import re, os, sys, subprocess
SCR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCR)
from algebra_data_a import L11, L12
from algebra_data_b import L13, L14
from algebra_data_c import L15, T1, STARS

LESSONS = [L11, L12, L13, L14, L15]
SITE = '/Users/andreikovrijnykh/amc10demo'
CH = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

idx = open(f'{SITE}/index.html', encoding='utf8').read()
FONTS = '\n'.join(re.findall(r'@font-face\{[^}]+\}', idx))
FAV = re.search(r'<link rel="icon"[^>]+>', idx).group(0)
GC = re.search(r'<script data-goatcounter[^<]+</script>', idx, re.S).group(0)
ROOT = re.search(r':root\{.*?\}', idx, re.S).group(0)
CSS = open(f'{SCR}/course-style.css', encoding='utf8').read() + """
.chips { display: flex; flex-wrap: wrap; gap: .4rem; margin: 1.2rem 0 0; }
.chips a { font-family: var(--mono); font-size: .72rem; letter-spacing: .08em; text-transform: uppercase; color: var(--tang-deep); text-decoration: none; border: 1px solid var(--rule-strong); padding: .3rem .7rem; }
.chips a:hover { background: var(--paper); }
nav.side details { margin: 0; }
nav.side summary { cursor: pointer; list-style: none; font-family: var(--mono); font-size: .72rem; font-weight: 500; letter-spacing: .13em; text-transform: uppercase; color: var(--tang-deep); padding: .45rem 0; }
nav.side summary::-webkit-details-marker { display: none; }
nav.side summary::before { content: "+ "; }
nav.side details[open] > summary::before { content: "\\2212 "; }
nav.side details[open] > summary { color: var(--ink); }
nav.side .nav-note { color: var(--mist); font-size: .85rem; padding: .2rem 0 .2rem .7rem; border-left: 2px solid var(--whisper); }
.langlink { font-family: var(--mono); font-size: .72rem; letter-spacing: .1em; text-transform: uppercase; }
ol.tprob { list-style: none; margin: 0; padding: 0; counter-reset: tp; }
ol.tprob > li { counter-increment: tp; display: grid; grid-template-columns: 2.5rem 1fr; align-items: baseline; padding: 1.05rem 0; border-top: 1px solid var(--rule); }
ol.tprob > li::before { content: counter(tp); font-family: var(--serif); font-size: 1.15rem; color: var(--tang); font-variant-numeric: tabular-nums; }
ol.tprob .q { grid-column: 2; }
.opts { grid-column: 2; margin-top: .6rem; display: grid; grid-template-columns: repeat(5, 1fr); gap: .4rem; }
@media (max-width: 40rem) { .opts { grid-template-columns: repeat(2, 1fr); } }
.opt { background: var(--paper); padding: .42rem .6rem; font-size: .93rem; display: flex; align-items: baseline; gap: .4rem; min-width: 0; }
.opt b { font-family: var(--mono); font-size: .72rem; color: var(--tang-deep); font-weight: 500; flex: none; }
details.answers { background: var(--ink); color: var(--porcelain); margin-top: 2rem; }
details.answers summary { cursor: pointer; padding: 1.05rem 1.4rem; font-family: var(--mono); font-size: .76rem; font-weight: 500; letter-spacing: .13em; text-transform: uppercase; color: var(--tang); list-style: none; display: flex; align-items: center; gap: .55rem; }
details.answers summary::-webkit-details-marker { display: none; }
details.answers summary::before { content: "+"; }
details.answers[open] summary::before { content: "\\2212"; }
.answers-body { padding: .3rem 1.4rem 1.5rem; }
.key { display: grid; grid-template-columns: repeat(auto-fill, minmax(3.2rem, 1fr)); gap: .35rem; margin-bottom: 1.4rem; }
.key div { border: 1px solid var(--rule-dark); padding: .38rem; text-align: center; font-family: var(--mono); font-size: .82rem; }
.key div span { color: var(--mist); opacity: .7; }
.key div b { color: var(--tang); font-weight: 500; }
.hints { font-size: .93rem; color: var(--mist); }
.hints p { margin-bottom: .7rem; }
.hints b { color: var(--porcelain); font-family: var(--mono); font-size: .82rem; font-weight: 500; }
.hints var { color: var(--porcelain); }
.pdfline { background: var(--paper); border-left: 3px solid var(--tang); padding: .9rem 1.2rem; font-size: .93rem; margin-top: 1.6rem; }
"""

S = {
 'ru': dict(theory='Теория (15 минут)', worked='Разобранные задачи (30 минут)',
   selfp='Самостоятельная порция (30 минут, потом разбор 15)',
   selfnote='Подсказку открываем после честной попытки; решение &mdash; после ответа или второй попытки.',
   star='Задача со звёздочкой (уровень AMC №11&ndash;15)',
   hint='Подсказка', sol='Решение', parent='Разбор для родителя (15 минут)',
   check='Сверьте ответы:', metaA='A: теория + разобранные, 45 мин', metaB='B: самостоятельная + разбор, 45 мин',
   t1title='Тест Т1 по блоку', t1meta='10 задач &middot; 30 минут &middot; порог усвоения 7 из 10 &middot; без калькулятора',
   t1intro='Тест закрывает блок: проценты и отношения, уравнения, работа и смеси, прогрессии, Виета и вершина, тождества, модуль. Ниже порога &mdash; один добор-урок по проваленным подтемам (маршрутизация в разборе), не &laquo;всё заново&raquo;.',
   showkey='Показать ключ и разбор', keywarn='Для родителя: ключ и однострочные разборы. Провалы соотнесите с уроками: 1&ndash;3 &rarr; 1.1&ndash;1.2, 4 и 6&ndash;8 &rarr; 1.3&ndash;1.4, 5 &rarr; 1.2, 9 &rarr; 1.4, 10 &rarr; 1.5.',
   pdfs='Для печати:', pdf_lessons='уроки блока 1 (PDF)', pdf_test='тест Т1 (PDF)',
   header_eyebrow='Крэш-курс AMC 10 &middot; Блок 1', header_h1='Блок 1 &mdash; Алгебра',
   header_stand='Пять уроков и тест: проценты и отношения, уравнения и прогрессии, квадратный трёхчлен, тождества и трюки, модуль. Каждый урок &mdash; 45 + 45 минут.',
   lesson_word='урок', otherlang='English version', otherhref='algebra.html',
   foot='Задачи курса составлены оригинально и не воспроизводят задания официальных олимпиад AMC. <a href="index.html">Оглавление курса</a> &middot; <a href="../../index.html">справка об AMC 10 и пробный тест</a> &middot; <a href="index.html#svyaz">оставить комментарий</a>.',
   title='Блок 1 · Алгебра · Крэш-курс AMC 10',
   desc='Алгебра для AMC 10: пять уроков с теорией, разобранными задачами, самостоятельными порциями и тест блока.'),
 'en': dict(theory='Concepts (15 minutes)', worked='Worked examples (30 minutes)',
   selfp='On-your-own set (30 minutes, then 15 for review)',
   selfnote='Open the hint only after a genuine attempt; open the solution after you have an answer, or after a second attempt.',
   star='Challenge problem (AMC #11&ndash;15 level)',
   hint='Hint', sol='Solution', parent='Parent review (15 minutes)',
   check='Check the answers:', metaA='A: theory + worked examples, 45 min', metaB='B: independent set + review, 45 min',
   t1title='Block Test T1', t1meta='10 problems &middot; 30 minutes &middot; mastery bar 7 of 10 &middot; no calculator',
   t1intro='The test wraps up the block: percents and ratios, equations, work and mixtures, sequences, Vieta&rsquo;s formulas and the vertex, identities, absolute value. Below the bar, assign one catch-up lesson on the missed subtopics (the review maps each problem to a lesson) &mdash; not a full redo.',
   showkey='Show answer key', keywarn='For the parent: the answer key with one-line explanations. Map misses to lessons: 1&ndash;3 &rarr; 1.1&ndash;1.2, 4 and 6&ndash;8 &rarr; 1.3&ndash;1.4, 5 &rarr; 1.2, 9 &rarr; 1.4, 10 &rarr; 1.5.',
   pdfs='Printable:', pdf_lessons='Block 1 lessons (PDF)', pdf_test='Test T1 (PDF)',
   header_eyebrow='AMC 10 Crash Course &middot; Block 1', header_h1='Block 1 &mdash; Algebra',
   header_stand='Five lessons and a test: percents and ratios, equations and sequences, quadratics, identities and tricks, absolute value. Each lesson is 45 + 45 minutes.',
   lesson_word='lesson', otherlang='Русская версия', otherhref='algebra-ru.html',
   foot='All problems are original and do not reproduce official AMC competition problems. <a href="index-en.html">Course contents</a> &middot; <a href="../../index-en.html">AMC 10 overview and practice test</a> &middot; <a href="index-en.html#contact">leave a comment</a>.',
   title='Block 1 · Algebra · AMC 10 Crash Course',
   desc='Algebra for the AMC 10: five lessons with theory, worked examples, independent sets, and the block test.'),
}

def lesson_html(L, g):
    s = S[g]
    w = ''.join(f'''<div class="wp"><div class="wp-num">{x['tag'][g]}</div><div>{x['q'][g]}</div>
<div class="sol"><b>{s['sol']}.</b> {x['sol'][g]}</div></div>''' for x in L['worked'])
    sp = ''.join(f'''<li><div class="q">{x['q'][g]}</div>
<details class="hint"><summary>{s['hint']}</summary><div>{x['hint'][g]}</div></details>
<details class="full"><summary>{s['sol']}</summary><div>{x['sol'][g]}</div></details></li>''' for x in L['selfp'])
    return f'''<section class="lesson" id="{L['anchor']}">
<div class="lesson-id">{s['header_eyebrow']} &middot; {'урок' if g=='ru' else 'lesson'} {L['id']}</div>
<h2>{L['title'][g]}</h2>
<div class="lesson-meta"><span>{s['metaA']}</span><span>{s['metaB']}</span></div>
<h3>{s['theory']}</h3>
<div class="theory">{L['theory'][g]}</div>
<h3>{s['worked']}</h3>
{w}
<h3>{s['selfp']}</h3>
<p>{s['selfnote']}</p>
<ol class="selfp">{sp}</ol>
{star_html(L, g)}
<div class="parent"><h3>{s['parent']}</h3>
<p>{s['check']} <b>{L['answers'][g]}</b>. {L['routing'][g]}</p></div>
</section>'''

def star_html(L, g):
    s = S[g]
    x = STARS[L['id']]
    return f"""<h3>&#9733; {s['star']}</h3>
<ol class="selfp" style="counter-reset: sp 8"><li><div class="q">{x['q'][g]}</div>
<details class="hint"><summary>{s['hint']}</summary><div>{x['hint'][g]}</div></details>
<details class="full"><summary>{s['sol']}</summary><div>{x['sol'][g]}</div></details></li></ol>"""

def t1_html(g):
    s = S[g]
    probs = ''.join(f'''<li><div class="q">{p['q'][g]}</div><div class="opts">{''.join(f'<div class="opt"><b>{L}</b>{v}</div>' for L, v in zip('ABCDE', p['opts'][g]))}</div></li>''' for p in T1['problems'])
    keyc = ''.join(f'<div><span>{i+1}</span> <b>{a}</b></div>' for i, a in enumerate(T1['key']))
    hints = ''.join(f'<p>{h}</p>' for h in T1['hints'][g])
    return f'''<section class="lesson" id="t1">
<div class="lesson-id">{s['header_eyebrow']} &middot; {s['t1title']}</div>
<h2>{s['t1title']}</h2>
<div class="lesson-meta"><span>{s['t1meta']}</span></div>
<p>{s['t1intro']}</p>
<ol class="tprob">{probs}</ol>
<details class="answers"><summary>{s['showkey']}</summary><div class="answers-body">
<div class="key">{keyc}</div>
<p style="font-size:.85rem;color:var(--mist);margin-bottom:1rem">{s['keywarn']}</p>
<div class="hints">{hints}</div></div></details>
<div class="pdfline"><strong>{s['pdfs']}</strong> <a href="{'algebra-lessons-ru.pdf' if g=='ru' else 'algebra-lessons.pdf'}">{s['pdf_lessons']}</a> &middot; <a href="{'algebra-test-ru.pdf' if g=='ru' else 'algebra-test.pdf'}">{s['pdf_test']}</a></div>
</section>'''

def page(g):
    s = S[g]
    chips = ''.join(f'<a href="#{L["anchor"]}">{L["id"]}</a>' for L in LESSONS) + '<a href="#t1">Т1</a>' if g == 'ru' else ''.join(f'<a href="#{L["anchor"]}">{L["id"]}</a>' for L in LESSONS) + '<a href="#t1">T1</a>'
    lessons = '\n'.join(lesson_html(L, g) for L in LESSONS)
    d1 = 'class="here"'
    if g == 'ru':
        nav = '''<nav class="side">
<div class="nav-t">Курсы</div>
<details name="course"><summary>AMC 8</summary>
<a href="../amc8/index.html">О курсе и программа</a>
<div class="nav-note">блоки готовятся</div>
</details>
<details name="course" open><summary>AMC 10</summary>
<a href="index.html#zachem">Зачем он сделан</a>
<a href="index.html#ustroystvo">Как устроен</a>
<a href="index.html#polzovanie">Как пользоваться</a>
<a href="diagnostics-ru.html">0 · Диагностика</a>
<a class="here" href="algebra-ru.html">1 · Алгебра</a>
<a class="dim" href="index.html#programma">2 · Геометрия</a>
<a class="dim" href="index.html#programma">3 · Теория чисел</a>
<a class="dim" href="index.html#programma">4 · Комбинаторика</a>
<a class="dim" href="index.html#programma">5 · Стратегия и моки</a>
<a href="index.html#svyaz">Комментарии</a>
</details>
<details name="course"><summary>AMC 12</summary>
<div class="nav-note">готовится к сезону 2027</div>
</details>
<div class="nav-t">Ещё</div>
<a href="../../index.html">Справка об AMC 10 и пробный тест</a>
<a href="../index.html">Все курсы</a>
</nav>'''
    else:
        nav = '''<nav class="side">
<div class="nav-t">Courses</div>
<details name="course"><summary>AMC 8</summary>
<a href="../amc8/index-en.html">About the course and program</a>
<div class="nav-note">blocks in production</div>
</details>
<details name="course" open><summary>AMC 10</summary>
<a href="index-en.html#why">Why it exists</a>
<a href="index-en.html#how">How it works</a>
<a href="index-en.html#use">How to use it</a>
<a href="diagnostics.html">0 · Diagnostics</a>
<a class="here" href="algebra.html">1 · Algebra</a>
<a class="dim" href="index-en.html#program">2 · Geometry</a>
<a class="dim" href="index-en.html#program">3 · Number theory</a>
<a class="dim" href="index-en.html#program">4 · Counting</a>
<a class="dim" href="index-en.html#program">5 · Strategy and mocks</a>
<a href="index-en.html#contact">Comments</a>
</details>
<details name="course"><summary>AMC 12</summary>
<div class="nav-note">coming for the 2027 season</div>
</details>
<div class="nav-t">More</div>
<a href="../../index-en.html">AMC 10 overview and practice test</a>
<a href="../index-en.html">All courses</a>
</nav>'''
    body = f'''<div class="layout">
{nav}
<main>
<header style="margin-bottom:2.2rem">
<div class="eyebrow">{s['header_eyebrow']} &nbsp;&middot;&nbsp; <a class="langlink" href="{s['otherhref']}">{s['otherlang']}</a></div>
<h1>{s['header_h1']}</h1>
<p class="standfirst">{s['header_stand']}</p>
<div class="chips">{chips}</div>
</header>
{lessons}
{t1_html(g)}
<footer>{s['foot']}</footer>
</main>
</div>'''
    return f'''<!DOCTYPE html>
<html lang="{g}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{s['title']}</title>
<meta name="description" content="{s['desc']}">
{FAV}
<style>
{FONTS}
{ROOT}
{CSS}
</style>
{GC}
</head>
<body>
{body}
</body>
</html>
'''

# ---------- PDF ----------
PCSS = """
@page { size: letter; margin: 16mm 16mm 18mm; }
* { box-sizing: border-box; }
body { font-family: Georgia, 'Times New Roman', serif; font-size: 10.4pt; line-height: 1.42; color: #000; margin: 0; }
header { border-bottom: 2px solid #000; padding-bottom: 8px; margin-bottom: 14px; }
.t1h { font-size: 16pt; font-weight: bold; margin: 0 0 2px; }
.t2h { font-size: 9.5pt; margin: 0; }
h2 { font-size: 13pt; border-bottom: 1.2px solid #000; padding-bottom: 3px; margin: 18px 0 8px; page-break-after: avoid; }
h3 { font-size: 10pt; text-transform: uppercase; letter-spacing: .06em; margin: 12px 0 6px; page-break-after: avoid; }
p { margin: 0 0 7px; }
.frm { border: 1px solid #000; padding: 5px 9px; margin: 7px 0; }
.wp { margin: 0 0 9px; padding-left: 12px; border-left: 2px solid #999; page-break-inside: avoid; }
.wp-num { font-weight: bold; font-size: 9pt; text-transform: uppercase; letter-spacing: .04em; }
.sol { font-size: 9.7pt; color: #222; margin-top: 3px; }
ol.plist { margin: 0; padding: 0; list-style: none; counter-reset: p; }
ol.plist > li { counter-increment: p; margin: 0 0 8px; page-break-inside: avoid; }
ol.plist > li::before { content: counter(p) ". "; font-weight: bold; }
.opts { display: flex; flex-wrap: wrap; gap: 2px 18px; margin: 3px 0 0 15px; }
.opt { display: inline-flex; align-items: baseline; gap: 5px; }
.opt b::before { content: "("; } .opt b::after { content: ")"; }
.frac { display: inline-flex; flex-direction: column; vertical-align: middle; text-align: center; font-size: 0.72em; line-height: 1.2; position: relative; top: -0.08em; }
.frac > span:first-child { border-bottom: 0.8px solid #000; padding: 0 3px; }
.frac > span:last-child { padding: 0 3px; }
var { font-style: italic; }
.keypage { page-break-before: always; }
table.key { border-collapse: collapse; margin: 8px 0; }
table.key td { border: 1px solid #000; padding: 4px 9px; text-align: center; font-size: 10pt; vertical-align: middle; line-height: 1; }
.warn { font-style: italic; font-size: 9.5pt; }
.colophon { margin-top: 22px; padding-top: 6px; border-top: 0.8px solid #999; font-size: 8pt; color: #555; }
.sollist p { margin: 0 0 5px; font-size: 9.7pt; }
"""

PS = {
 'ru': dict(lt='Крэш-курс AMC 10 · Блок 1 · Алгебра · уроки 1.1–1.5',
   lsub='Теория, разобранные задачи и самостоятельные порции. Решения самостоятельных &mdash; в конце файла.',
   theory='Теория', worked='Разобранные задачи', selfp='Самостоятельная порция',
   solsec='Решения самостоятельных порций', urok='Урок',
   tt='Крэш-курс AMC 10 · Тест Т1 · Алгебра', tsub='10 задач &middot; 30 минут &middot; без калькулятора &middot; порог 7 из 10',
   nd='<div class="nd" style="display:flex;gap:28px;font-size:9.5pt;margin-top:6px"><span style="flex:1;border-bottom:1px solid #000">Имя:</span><span style="flex:1;border-bottom:1px solid #000">Дата:</span></div>',
   kh='Ключ и разбор', kwarn='Страница для родителя: отрезать или не распечатывать для ученика.',
   foot='Задачи составлены оригинально и не воспроизводят задания официальных олимпиад AMC &middot; opscope.github.io/amc10-demo/course/amc10/'),
 'en': dict(lt='AMC 10 Crash Course · Block 1 · Algebra · Lessons 1.1–1.5',
   lsub='Theory, worked examples, and independent sets. Solutions to the independent sets are at the end of the file.',
   theory='Theory', worked='Worked examples', selfp='Independent set',
   solsec='Solutions to the independent sets', urok='Lesson',
   tt='AMC 10 Crash Course · Test T1 · Algebra', tsub='10 problems &middot; 30 minutes &middot; no calculator &middot; mastery bar 7 of 10',
   nd='<div class="nd" style="display:flex;gap:28px;font-size:9.5pt;margin-top:6px"><span style="flex:1;border-bottom:1px solid #000">Name:</span><span style="flex:1;border-bottom:1px solid #000">Date:</span></div>',
   kh='Answer Key and Review', kwarn='Parent page: cut off or do not print for the student.',
   foot='All problems are original and do not reproduce official AMC competition problems &middot; opscope.github.io/amc10-demo/course/amc10/'),
}

def strip_details(html):
    return html

def pdf_lessons(g):
    s = PS[g]
    parts = []
    for L in LESSONS:
        w = ''.join(f'<div class="wp"><div class="wp-num">{x["tag"][g]}</div><div>{x["q"][g]}</div><div class="sol"><b>&rarr;</b> {x["sol"][g]}</div></div>' for x in L['worked'])
        sp = ''.join(f'<li>{x["q"][g]}</li>' for x in L['selfp'])
        sp += f'<li><b>&#9733;</b> {STARS[L["id"]]["q"][g]}</li>'
        parts.append(f'''<h2>{s['urok']} {L['id']}. {L['title'][g]}</h2>
<h3>{s['theory']}</h3>{L['theory'][g]}
<h3>{s['worked']}</h3>{w}
<h3>{s['selfp']}</h3><ol class="plist">{sp}</ol>''')
    sols = []
    for L in LESSONS:
        rows = ''.join(f'<p><b>{i+1}.</b> {x["sol"][g]}</p>' for i, x in enumerate(L['selfp']))
        rows += f'<p><b>&#9733;</b> {STARS[L["id"]]["sol"][g]}</p>'
        sols.append(f'<h3>{s["urok"]} {L["id"]}</h3><div class="sollist">{rows}</div>')
    return f'''<!DOCTYPE html><html lang="{g}"><head><meta charset="utf-8"><style>{PCSS}</style></head><body>
<header><div class="t1h">{s['lt']}</div><div class="t2h">{s['lsub']}</div></header>
{''.join(parts)}
<div class="keypage"><h2>{s['solsec']}</h2>{''.join(sols)}
<div class="colophon">{s['foot']}</div></div>
</body></html>'''

def pdf_test(g):
    s = PS[g]
    def optrow(p):
        return ''.join('<span class="opt"><b>%s</b>%s</span>' % (L, v) for L, v in zip('ABCDE', p['opts'][g]))
    probs = ''.join('<li>%s<div class="opts">%s</div></li>' % (p['q'][g], optrow(p)) for p in T1['problems'])
    ns = ''.join(f'<td>{i+1}</td>' for i in range(10))
    As = ''.join(f'<td><b>{a}</b></td>' for a in T1['key'])
    hints = ''.join(f'<p>{h}</p>' for h in T1['hints'][g])
    return f'''<!DOCTYPE html><html lang="{g}"><head><meta charset="utf-8"><style>{PCSS}</style></head><body>
<header><div class="t1h">{s['tt']}</div><div class="t2h">{s['tsub']}</div>{s['nd']}</header>
<ol class="plist">{probs}</ol>
<div class="keypage"><h2>{s['kh']}</h2><p class="warn">{s['kwarn']}</p>
<table class="key"><tr>{ns}</tr><tr>{As}</tr></table>
<div class="sollist">{hints}</div>
<div class="colophon">{s['foot']}</div></div>
</body></html>'''

def render_pdf(html, out):
    src = f'/tmp/pdf_src_{os.path.basename(out)}.html'
    open(src, 'w', encoding='utf8').write(html)
    subprocess.run([CH, '--headless', '--disable-gpu', f'--print-to-pdf={out}',
                    '--no-pdf-header-footer', 'file://' + src], capture_output=True)
    print(os.path.basename(out), os.path.getsize(out) // 1024, 'KB')

if __name__ == '__main__':
    open(f'{SITE}/course/amc10/algebra-ru.html', 'w', encoding='utf8').write(page('ru'))
    open(f'{SITE}/course/amc10/algebra.html', 'w', encoding='utf8').write(page('en'))
    print('pages written')
    render_pdf(pdf_lessons('ru'), f'{SITE}/course/amc10/algebra-lessons-ru.pdf')
    render_pdf(pdf_lessons('en'), f'{SITE}/course/amc10/algebra-lessons.pdf')
    render_pdf(pdf_test('ru'), f'{SITE}/course/amc10/algebra-test-ru.pdf')
    render_pdf(pdf_test('en'), f'{SITE}/course/amc10/algebra-test.pdf')
