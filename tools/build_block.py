#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Обобщённая сборка блоков 2–4 крэш-курса AMC 10: страницы RU/EN + 4 PDF на блок.

Использование: python3 build_block.py geometry|number-theory|counting|all
Схема данных и вёрстка — как в build_algebra.py (блок 1)."""
import re, os, sys, subprocess
SCR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCR)

SITE = '/Users/andreikovrijnykh/amc10demo'
CH = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

idx = open(f'{SITE}/index.html', encoding='utf8').read()
FONTS = '\n'.join(re.findall(r'@font-face\{[^}]+\}', idx))
FAV = re.search(r'<link rel="icon"[^>]+>', idx).group(0)
GC = re.search(r'<script data-goatcounter[^<]+</script>', idx, re.S).group(0)
ROOT = re.search(r':root\{.*?\}', idx, re.S).group(0)
import build_algebra as BA  # переиспользуем собранный CSS
CSS_FULL = BA.CSS

# ---------- конфигурация блоков ----------

def load_geometry():
    from geometry_data_a import L21, L22
    from geometry_data_b import L23, L24
    from geometry_data_c import L25, L26
    from geometry_data_d import T2, STARS
    return [L21, L22, L23, L24, L25, L26], T2, STARS

def load_ntheory():
    from number_theory_data_a import L31, L32
    from number_theory_data_b import L33, L34, T3, STARS
    return [L31, L32, L33, L34], T3, STARS

def load_counting():
    from counting_data_a import L41, L42
    from counting_data_b import L43, L44
    from counting_data_c import L45, T4, STARS
    return [L41, L42, L43, L44, L45], T4, STARS

BLOCKS = {
 'geometry': dict(
   num=2, tname_ru='Т2', tname_en='T2', slug='geometry', load=load_geometry,
   name_ru='Геометрия', name_en='Geometry',
   stand_ru='Шесть уроков и тест: углы, подобие и Пифагор, площади, окружность, координаты, стереометрия-минимум. Каждый урок &mdash; 45 + 45 минут.',
   stand_en='Six lessons and a test: angles, similarity and the Pythagorean theorem, areas, circles, coordinates, minimal solid geometry. Each lesson is 45 + 45 minutes.',
   tintro_ru='Тест закрывает блок: углы, подобие и особые треугольники, площади, окружность, координатная геометрия, объёмы. Ниже порога &mdash; один добор-урок по проваленным подтемам (маршрутизация в разборе), не &laquo;всё заново&raquo;.',
   tintro_en='The test wraps up the block: angles, similarity and special triangles, areas, circles, coordinate geometry, volumes. Below the bar, assign one catch-up lesson on the missed subtopics (the review maps each problem to a lesson) &mdash; not a full redo.',
   desc_ru='Геометрия для AMC 10: шесть уроков с теорией, разобранными задачами, самостоятельными порциями и тест блока.',
   desc_en='Geometry for the AMC 10: six lessons with theory, worked examples, independent sets, and the block test.'),
 'number-theory': dict(
   num=3, tname_ru='Т3', tname_en='T3', slug='number-theory', load=load_ntheory,
   name_ru='Теория чисел', name_en='Number Theory',
   stand_ru='Четыре урока и тест: делимость и простые, НОД и НОК, остатки и цикличность степеней, факториалы и цифры. Каждый урок &mdash; 45 + 45 минут.',
   stand_en='Four lessons and a test: divisibility and primes, GCD and LCM, remainders and power cycles, factorials and digits. Each lesson is 45 + 45 minutes.',
   tintro_ru='Тест закрывает блок: делимость и разложение на простые, НОД/НОК, арифметика остатков, факториалы и цифровые задачи. Ниже порога &mdash; один добор-урок по проваленным подтемам, не &laquo;всё заново&raquo;.',
   tintro_en='The test wraps up the block: divisibility and prime factorization, GCD/LCM, modular arithmetic, factorials and digit problems. Below the bar, assign one catch-up lesson on the missed subtopics &mdash; not a full redo.',
   desc_ru='Теория чисел для AMC 10: четыре урока с теорией, разобранными задачами, самостоятельными порциями и тест блока.',
   desc_en='Number theory for the AMC 10: four lessons with theory, worked examples, independent sets, and the block test.'),
 'counting': dict(
   num=4, tname_ru='Т4', tname_en='T4', slug='counting', load=load_counting,
   name_ru='Комбинаторика и вероятность', name_en='Counting and Probability',
   stand_ru='Пять уроков и тест: правила подсчёта и перестановки, сочетания, кейсворк и включения-исключения, вероятность, пути и рекуррентные подсчёты. Каждый урок &mdash; 45 + 45 минут.',
   stand_en='Five lessons and a test: counting rules and permutations, combinations, casework and inclusion-exclusion, probability, lattice paths and recursive counting. Each lesson is 45 + 45 minutes.',
   tintro_ru='Тест закрывает блок: перестановки и размещения, сочетания, кейсворк и дополнение, вероятность, пути и рекурсии. Ниже порога &mdash; один добор-урок по проваленным подтемам, не &laquo;всё заново&raquo;.',
   tintro_en='The test wraps up the block: permutations and arrangements, combinations, casework and complements, probability, paths and recursions. Below the bar, assign one catch-up lesson on the missed subtopics &mdash; not a full redo.',
   desc_ru='Комбинаторика и вероятность для AMC 10: пять уроков с теорией, разобранными задачами, самостоятельными порциями и тест блока.',
   desc_en='Counting and probability for the AMC 10: five lessons with theory, worked examples, independent sets, and the block test.'),
}

# соответствие задач теста урокам — по фактическому составу тестов
TMAP = {
 'geometry': {
  'ru': 'Провалы соотнесите с уроками: 1&ndash;2 &rarr; 2.1, 3&ndash;4 &rarr; 2.2, 5&ndash;6 &rarr; 2.3, 7&ndash;8 &rarr; 2.4, 9 &rarr; 2.5, 10 &rarr; 2.6.',
  'en': 'Map misses to lessons: 1&ndash;2 &rarr; 2.1, 3&ndash;4 &rarr; 2.2, 5&ndash;6 &rarr; 2.3, 7&ndash;8 &rarr; 2.4, 9 &rarr; 2.5, 10 &rarr; 2.6.'},
 'number-theory': {
  'ru': 'Провалы соотнесите с уроками: 1&ndash;2 &rarr; 3.1, 3&ndash;5 &rarr; 3.2, 6&ndash;8 &rarr; 3.3, 9&ndash;10 &rarr; 3.4.',
  'en': 'Map misses to lessons: 1&ndash;2 &rarr; 3.1, 3&ndash;5 &rarr; 3.2, 6&ndash;8 &rarr; 3.3, 9&ndash;10 &rarr; 3.4.'},
 'counting': {
  'ru': 'Провалы соотнесите с уроками: 1&ndash;2 &rarr; 4.1, 3&ndash;4 &rarr; 4.2, 5&ndash;6 &rarr; 4.3, 7&ndash;8 &rarr; 4.4, 9&ndash;10 &rarr; 4.5.',
  'en': 'Map misses to lessons: 1&ndash;2 &rarr; 4.1, 3&ndash;4 &rarr; 4.2, 5&ndash;6 &rarr; 4.3, 7&ndash;8 &rarr; 4.4, 9&ndash;10 &rarr; 4.5.'},
}

NAV_ITEMS = [
    ('0', 'diagnostics-ru.html', 'diagnostics.html', 'Диагностика', 'Diagnostics'),
    ('1', 'algebra-ru.html', 'algebra.html', 'Алгебра', 'Algebra'),
    ('2', 'geometry-ru.html', 'geometry.html', 'Геометрия', 'Geometry'),
    ('3', 'number-theory-ru.html', 'number-theory.html', 'Теория чисел', 'Number theory'),
    ('4', 'counting-ru.html', 'counting.html', 'Комбинаторика', 'Counting'),
    ('5', 'strategy-ru.html', 'strategy.html', 'Стратегия и моки', 'Strategy and mocks'),
]

def nav_html(g, here_num):
    rows = []
    for num, hru, hen, tru, ten in NAV_ITEMS:
        href = hru if g == 'ru' else hen
        label = f'{num} · {tru if g == "ru" else ten}'
        cls = ' class="here"' if num == str(here_num) else ''
        rows.append(f'<a{cls} href="{href}">{label}</a>')
    items = '\n'.join(rows)
    if g == 'ru':
        return f'''<nav class="side">
<div class="nav-t">Курсы</div>
<details name="course"><summary>AMC 8</summary>
<a href="../amc8/index.html">О курсе и программа</a>
<div class="nav-note">блоки готовятся</div>
</details>
<details name="course" open><summary>AMC 10</summary>
<a href="index.html#zachem">Зачем он сделан</a>
<a href="index.html#ustroystvo">Как устроен</a>
<a href="index.html#polzovanie">Как пользоваться</a>
{items}
<a href="index.html#svyaz">Комментарии</a>
</details>
<details name="course"><summary>AMC 12</summary>
<div class="nav-note">готовится к сезону 2027</div>
</details>
<div class="nav-t">Ещё</div>
<a href="../../index.html">Справка об AMC 10 и пробный тест</a>
<a href="../index.html">Все курсы</a>
</nav>'''
    return f'''<nav class="side">
<div class="nav-t">Courses</div>
<details name="course"><summary>AMC 8</summary>
<a href="../amc8/index-en.html">About the course and program</a>
<div class="nav-note">blocks in production</div>
</details>
<details name="course" open><summary>AMC 10</summary>
<a href="index-en.html#why">Why it exists</a>
<a href="index-en.html#how">How it works</a>
<a href="index-en.html#use">How to use it</a>
{items}
<a href="index-en.html#contact">Comments</a>
</details>
<details name="course"><summary>AMC 12</summary>
<div class="nav-note">coming for the 2027 season</div>
</details>
<div class="nav-t">More</div>
<a href="../../index-en.html">AMC 10 overview and practice test</a>
<a href="../index-en.html">All courses</a>
</nav>'''

def make_S(cfg, tmap):
    n = cfg['num']
    lessons_word = {'geometry': ('Шесть уроков', 'Six lessons'),
                    'number-theory': ('Четыре урока', 'Four lessons'),
                    'counting': ('Пять уроков', 'Five lessons')}
    slug = cfg['slug']
    return {
 'ru': dict(theory='Теория (15 минут)', worked='Разобранные задачи (30 минут)',
   selfp='Самостоятельная порция (30 минут, потом разбор 15)',
   selfnote='Подсказку открываем после честной попытки; решение &mdash; после ответа или второй попытки.',
   star='Задача со звёздочкой (уровень AMC №11&ndash;15)',
   hint='Подсказка', sol='Решение', parent='Разбор для родителя (15 минут)',
   check='Сверьте ответы:', metaA='A: теория + разобранные, 45 мин', metaB='B: самостоятельная + разбор, 45 мин',
   t1title=f'Тест {cfg["tname_ru"]} по блоку', t1meta='10 задач &middot; 30 минут &middot; порог усвоения 7 из 10 &middot; без калькулятора',
   t1intro=cfg['tintro_ru'],
   showkey='Показать ключ и разбор',
   keywarn='Для родителя: ключ и однострочные разборы. ' + tmap['ru'],
   pdfs='Для печати:', pdf_lessons=f'уроки блока {n} (PDF)', pdf_test=f'тест {cfg["tname_ru"]} (PDF)',
   header_eyebrow=f'Крэш-курс AMC 10 &middot; Блок {n}', header_h1=f'Блок {n} &mdash; {cfg["name_ru"]}',
   header_stand=cfg['stand_ru'],
   lesson_word='урок', otherlang='English version', otherhref=f'{slug}.html',
   foot='Задачи курса составлены оригинально и не воспроизводят задания официальных олимпиад AMC. <a href="index.html">Оглавление курса</a> &middot; <a href="../../index.html">справка об AMC 10 и пробный тест</a> &middot; <a href="index.html#svyaz">оставить комментарий</a>.',
   title=f'Блок {n} · {cfg["name_ru"]} · Крэш-курс AMC 10',
   desc=cfg['desc_ru'],
   pdf_lessons_file=f'{slug}-lessons-ru.pdf', pdf_test_file=f'{slug}-test-ru.pdf'),
 'en': dict(theory='Concepts (15 minutes)', worked='Worked examples (30 minutes)',
   selfp='On-your-own set (30 minutes, then 15 for review)',
   selfnote='Open the hint only after a genuine attempt; open the solution after you have an answer, or after a second attempt.',
   star='Challenge problem (AMC #11&ndash;15 level)',
   hint='Hint', sol='Solution', parent='Parent review (15 minutes)',
   check='Check the answers:', metaA='A: theory + worked examples, 45 min', metaB='B: independent set + review, 45 min',
   t1title=f'Block Test {cfg["tname_en"]}', t1meta='10 problems &middot; 30 minutes &middot; mastery bar 7 of 10 &middot; no calculator',
   t1intro=cfg['tintro_en'],
   showkey='Show answer key',
   keywarn='For the parent: the answer key with one-line explanations. ' + tmap['en'],
   pdfs='Printable:', pdf_lessons=f'Block {n} lessons (PDF)', pdf_test=f'Test {cfg["tname_en"]} (PDF)',
   header_eyebrow=f'AMC 10 Crash Course &middot; Block {n}', header_h1=f'Block {n} &mdash; {cfg["name_en"]}',
   header_stand=cfg['stand_en'],
   lesson_word='lesson', otherlang='Русская версия', otherhref=f'{slug}-ru.html',
   foot='All problems are original and do not reproduce official AMC competition problems. <a href="index-en.html">Course contents</a> &middot; <a href="../../index-en.html">AMC 10 overview and practice test</a> &middot; <a href="index-en.html#contact">leave a comment</a>.',
   title=f'Block {n} · {cfg["name_en"]} · AMC 10 Crash Course',
   desc=cfg['desc_en'],
   pdf_lessons_file=f'{slug}-lessons.pdf', pdf_test_file=f'{slug}-test.pdf'),
}

# ---------- HTML ----------

def lesson_html(L, g, S, STARS):
    s = S[g]
    w = ''.join(f'''<div class="wp"><div class="wp-num">{x['tag'][g]}</div><div>{x['q'][g]}</div>
<div class="sol"><b>{s['sol']}.</b> {x['sol'][g]}</div></div>''' for x in L['worked'])
    sp = ''.join(f'''<li><div class="q">{x['q'][g]}</div>
<details class="hint"><summary>{s['hint']}</summary><div>{x['hint'][g]}</div></details>
<details class="full"><summary>{s['sol']}</summary><div>{x['sol'][g]}</div></details></li>''' for x in L['selfp'])
    x = STARS[L['id']]
    star = f"""<h3>&#9733; {s['star']}</h3>
<ol class="selfp" style="counter-reset: sp 8"><li><div class="q">{x['q'][g]}</div>
<details class="hint"><summary>{s['hint']}</summary><div>{x['hint'][g]}</div></details>
<details class="full"><summary>{s['sol']}</summary><div>{x['sol'][g]}</div></details></li></ol>"""
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
{star}
<div class="parent"><h3>{s['parent']}</h3>
<p>{s['check']} <b>{L['answers'][g]}</b>. {L['routing'][g]}</p></div>
</section>'''

def test_html(g, S, TEST, anchor):
    s = S[g]
    probs = ''.join(f'''<li><div class="q">{p['q'][g]}</div><div class="opts">{''.join(f'<div class="opt"><b>{L}</b>{v}</div>' for L, v in zip('ABCDE', p['opts'][g]))}</div></li>''' for p in TEST['problems'])
    keyc = ''.join(f'<div><span>{i+1}</span> <b>{a}</b></div>' for i, a in enumerate(TEST['key']))
    hints = ''.join(f'<p>{h}</p>' for h in TEST['hints'][g])
    return f'''<section class="lesson" id="{anchor}">
<div class="lesson-id">{s['header_eyebrow']} &middot; {s['t1title']}</div>
<h2>{s['t1title']}</h2>
<div class="lesson-meta"><span>{s['t1meta']}</span></div>
<p>{s['t1intro']}</p>
<ol class="tprob">{probs}</ol>
<details class="answers"><summary>{s['showkey']}</summary><div class="answers-body">
<div class="key">{keyc}</div>
<p style="font-size:.85rem;color:var(--mist);margin-bottom:1rem">{s['keywarn']}</p>
<div class="hints">{hints}</div></div></details>
<div class="pdfline"><strong>{s['pdfs']}</strong> <a href="{s['pdf_lessons_file']}">{s['pdf_lessons']}</a> &middot; <a href="{s['pdf_test_file']}">{s['pdf_test']}</a></div>
</section>'''

def page(g, cfg, S, LESSONS, TEST, STARS):
    s = S[g]
    tlabel = cfg['tname_ru'] if g == 'ru' else cfg['tname_en']
    anchor = 't' + str(cfg['num'])
    chips = ''.join(f'<a href="#{L["anchor"]}">{L["id"]}</a>' for L in LESSONS) + f'<a href="#{anchor}">{tlabel}</a>'
    lessons = '\n'.join(lesson_html(L, g, S, STARS) for L in LESSONS)
    body = f'''<div class="layout">
{nav_html(g, cfg['num'])}
<main>
<header style="margin-bottom:2.2rem">
<div class="eyebrow">{s['header_eyebrow']} &nbsp;&middot;&nbsp; <a class="langlink" href="{s['otherhref']}">{s['otherlang']}</a></div>
<h1>{s['header_h1']}</h1>
<p class="standfirst">{s['header_stand']}</p>
<div class="chips">{chips}</div>
</header>
{lessons}
{test_html(g, S, TEST, anchor)}
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
{CSS_FULL}
</style>
{GC}
</head>
<body>
{body}
</body>
</html>
'''

# ---------- PDF ----------
PCSS = BA.PCSS

def make_PS(cfg, tmap):
    n, slug = cfg['num'], cfg['slug']
    ids = 'уроки' if True else ''
    return {
 'ru': dict(lt=f'Крэш-курс AMC 10 · Блок {n} · {cfg["name_ru"]}',
   lsub='Теория, разобранные задачи и самостоятельные порции. Решения самостоятельных &mdash; в конце файла.',
   theory='Теория', worked='Разобранные задачи', selfp='Самостоятельная порция',
   solsec='Решения самостоятельных порций', urok='Урок',
   tt=f'Крэш-курс AMC 10 · Тест {cfg["tname_ru"]} · {cfg["name_ru"]}', tsub='10 задач &middot; 30 минут &middot; без калькулятора &middot; порог 7 из 10',
   nd='<div class="nd" style="display:flex;gap:28px;font-size:9.5pt;margin-top:6px"><span style="flex:1;border-bottom:1px solid #000">Имя:</span><span style="flex:1;border-bottom:1px solid #000">Дата:</span></div>',
   kh='Ключ и разбор', kwarn='Страница для родителя: отрезать или не распечатывать для ученика. ' + tmap['ru'],
   foot='Задачи составлены оригинально и не воспроизводят задания официальных олимпиад AMC &middot; opscope.github.io/amc10-demo/course/amc10/'),
 'en': dict(lt=f'AMC 10 Crash Course · Block {n} · {cfg["name_en"]}',
   lsub='Theory, worked examples, and independent sets. Solutions to the independent sets are at the end of the file.',
   theory='Theory', worked='Worked examples', selfp='Independent set',
   solsec='Solutions to the independent sets', urok='Lesson',
   tt=f'AMC 10 Crash Course · Test {cfg["tname_en"]} · {cfg["name_en"]}', tsub='10 problems &middot; 30 minutes &middot; no calculator &middot; mastery bar 7 of 10',
   nd='<div class="nd" style="display:flex;gap:28px;font-size:9.5pt;margin-top:6px"><span style="flex:1;border-bottom:1px solid #000">Name:</span><span style="flex:1;border-bottom:1px solid #000">Date:</span></div>',
   kh='Answer Key and Review', kwarn='Parent page: cut off or do not print for the student. ' + tmap['en'],
   foot='All problems are original and do not reproduce official AMC competition problems &middot; opscope.github.io/amc10-demo/course/amc10/'),
}

def pdf_lessons(g, PSd, LESSONS, STARS):
    s = PSd[g]
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

def pdf_test(g, PSd, TEST):
    s = PSd[g]
    def optrow(p):
        return ''.join('<span class="opt"><b>%s</b>%s</span>' % (L, v) for L, v in zip('ABCDE', p['opts'][g]))
    probs = ''.join('<li>%s<div class="opts">%s</div></li>' % (p['q'][g], optrow(p)) for p in TEST['problems'])
    ns = ''.join(f'<td>{i+1}</td>' for i in range(10))
    As = ''.join(f'<td><b>{a}</b></td>' for a in TEST['key'])
    hints = ''.join(f'<p>{h}</p>' for h in TEST['hints'][g])
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

def build(key):
    cfg = BLOCKS[key]
    LESSONS, TEST, STARS = cfg['load']()
    S = make_S(cfg, TMAP[key])
    PSd = make_PS(cfg, TMAP[key])
    slug = cfg['slug']
    open(f'{SITE}/course/amc10/{slug}-ru.html', 'w', encoding='utf8').write(page('ru', cfg, S, LESSONS, TEST, STARS))
    open(f'{SITE}/course/amc10/{slug}.html', 'w', encoding='utf8').write(page('en', cfg, S, LESSONS, TEST, STARS))
    print(f'{slug}: pages written')
    render_pdf(pdf_lessons('ru', PSd, LESSONS, STARS), f'{SITE}/course/amc10/{slug}-lessons-ru.pdf')
    render_pdf(pdf_lessons('en', PSd, LESSONS, STARS), f'{SITE}/course/amc10/{slug}-lessons.pdf')
    render_pdf(pdf_test('ru', PSd, TEST), f'{SITE}/course/amc10/{slug}-test-ru.pdf')
    render_pdf(pdf_test('en', PSd, TEST), f'{SITE}/course/amc10/{slug}-test.pdf')

if __name__ == '__main__':
    arg = sys.argv[1] if len(sys.argv) > 1 else 'all'
    for key in (BLOCKS if arg == 'all' else [arg]):
        build(key)
