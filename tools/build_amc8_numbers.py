#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AMC 8, блок 1 «Числа и арифметика»: страницы RU/EN + 4 PDF."""
import re, os, sys, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from amc8_numbers_data_a import L11, L12
from amc8_numbers_data_b import L13, L14
from amc8_numbers_data_c import L15, T1, STARS
import build_algebra as BA   # переиспользуем CSS, lesson_html-подход и PDF-движок

LESSONS = [L11, L12, L13, L14, L15]
SITE = os.path.dirname(HERE)
CH = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

S = {
 'ru': dict(BA.S['ru']), 'en': dict(BA.S['en']),
}
S['ru'].update(
 star='Задача со звёздочкой (уровень AMC 8 №18&ndash;25)',
 t1meta='10 задач &middot; 20 минут &middot; порог усвоения 7 из 10 &middot; без калькулятора',
 t1intro='Тест закрывает блок: дроби, проценты, отношения, средние, прикидка и последняя цифра. Ниже порога &mdash; один добор-урок по проваленным подтемам (маршрутизация в разборе), не &laquo;всё заново&raquo;.',
 keywarn='Для родителя: ключ и однострочные разборы. Провалы соотнесите с уроками: 1&ndash;2 &rarr; 1.1, 3&ndash;4 &rarr; 1.2, 5&ndash;6 &rarr; 1.3, 7&ndash;8 &rarr; 1.4, 9&ndash;10 &rarr; 1.5.',
 pdf_lessons='уроки блока 1 (PDF)', pdf_test='тест Т1 (PDF)',
 header_eyebrow='Крэш-курс AMC 8 &middot; Блок 1', header_h1='Блок 1 &mdash; Числа и арифметика',
 header_stand='Пять уроков и тест: дроби, проценты, отношения и пропорции, средние, прикидка и последняя цифра. Каждый урок &mdash; 45 + 45 минут.',
 otherlang='English version', otherhref='numbers.html',
 foot='Задачи курса составлены оригинально и не воспроизводят задания официальных олимпиад AMC. <a href="index.html">Курс AMC 8</a> &middot; <a href="practice-test-ru.html">пробный тест</a> &middot; <a href="index.html#svyaz">оставить комментарий</a>.',
 title='Блок 1 · Числа и арифметика · Крэш-курс AMC 8',
 desc='Числа и арифметика для AMC 8: пять уроков с теорией, разобранными задачами, самостоятельными порциями и тест блока.')
S['en'].update(
 star='Challenge problem (AMC 8 #18&ndash;25 level)',
 t1meta='10 problems &middot; 20 minutes &middot; mastery bar 7 of 10 &middot; no calculator',
 t1intro='The test wraps up the block: fractions, percents, ratios, averages, estimation and the last digit. Below the bar, assign one catch-up lesson on the missed subtopics (the review maps each problem to a lesson) &mdash; not a full redo.',
 keywarn='For the parent: the answer key with one-line explanations. Map misses to lessons: 1&ndash;2 &rarr; 1.1, 3&ndash;4 &rarr; 1.2, 5&ndash;6 &rarr; 1.3, 7&ndash;8 &rarr; 1.4, 9&ndash;10 &rarr; 1.5.',
 pdf_lessons='Block 1 lessons (PDF)', pdf_test='Test T1 (PDF)',
 header_eyebrow='AMC 8 Crash Course &middot; Block 1', header_h1='Block 1 &mdash; Numbers and Arithmetic',
 header_stand='Five lessons and a test: fractions, percents, ratios and proportions, averages, estimation and the last digit. Each lesson is 45 + 45 minutes.',
 otherlang='Русская версия', otherhref='numbers-ru.html',
 foot='All problems are original and do not reproduce official AMC competition problems. <a href="index-en.html">AMC 8 course</a> &middot; <a href="practice-test.html">practice test</a> &middot; <a href="index-en.html#contact">leave a comment</a>.',
 title='Block 1 · Numbers and Arithmetic · AMC 8 Crash Course',
 desc='Numbers and arithmetic for the AMC 8: five lessons with theory, worked examples, independent sets, and the block test.')

def star_html(L, g):
    s = S[g]; x = STARS[L['id']]
    return f'''<h3>&#9733; {s['star']}</h3>
<ol class="selfp" style="counter-reset: sp 8"><li><div class="q">{x['q'][g]}</div>
<details class="hint"><summary>{s['hint']}</summary><div>{x['hint'][g]}</div></details>
<details class="full"><summary>{s['sol']}</summary><div>{x['sol'][g]}</div></details></li></ol>'''

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

def t1_html(g):
    s = S[g]
    def optrow(p):
        return ''.join('<div class="opt"><b>%s</b>%s</div>' % (L, v) for L, v in zip('ABCDE', p['opts'][g]))
    probs = ''.join('<li><div class="q">%s</div><div class="opts">%s</div></li>' % (p['q'][g], optrow(p)) for p in T1['problems'])
    keyc = ''.join(f'<div><span>{i+1}</span> <b>{a}</b></div>' for i, a in enumerate(T1['key']))
    hints = ''.join(f'<p>{h}</p>' for h in T1['hints'][g])
    pdfs = ('numbers-lessons-ru.pdf', 'numbers-test-ru.pdf') if g == 'ru' else ('numbers-lessons.pdf', 'numbers-test.pdf')
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
<div class="pdfline"><strong>{s['pdfs']}</strong> <a href="{pdfs[0]}">{s['pdf_lessons']}</a> &middot; <a href="{pdfs[1]}">{s['pdf_test']}</a></div>
</section>'''

def nav(g):
    if g == 'ru':
        return '''<nav class="side">
<div class="nav-t">Курсы</div>
<details name="course" open><summary>AMC 8</summary>
<a href="index.html#zachem">О курсе</a>
<a href="index.html#programma">Программа</a>
<a href="practice-test-ru.html">Пробный тест</a>
<a href="diagnostics-ru.html">0 · Диагностика</a>
<a class="here" href="numbers-ru.html">1 · Числа и арифметика</a>
<a href="geometry-ru.html">2 · Геометрия</a>
<a class="dim" href="index.html#programma">3 · Счёт и вероятность</a>
<a class="dim" href="index.html#programma">4 · Логика и текстовые</a>
<a class="dim" href="index.html#programma">5 · Стратегия и прогоны</a>
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
    return '''<nav class="side">
<div class="nav-t">Courses</div>
<details name="course" open><summary>AMC 8</summary>
<a href="index-en.html#why">About the course</a>
<a href="index-en.html#program">Program</a>
<a href="practice-test.html">Practice test</a>
<a href="diagnostics.html">0 · Diagnostics</a>
<a class="here" href="numbers.html">1 · Numbers and arithmetic</a>
<a href="geometry.html">2 · Geometry</a>
<a class="dim" href="index-en.html#program">3 · Counting and probability</a>
<a class="dim" href="index-en.html#program">4 · Logic and word problems</a>
<a class="dim" href="index-en.html#program">5 · Strategy and mock runs</a>
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

def page(g):
    s = S[g]
    chips = ''.join(f'<a href="#{L["anchor"]}">{L["id"]}</a>' for L in LESSONS) + ('<a href="#t1">Т1</a>' if g == 'ru' else '<a href="#t1">T1</a>')
    lessons = '\n'.join(lesson_html(L, g) for L in LESSONS)
    body = f'''<div class="layout">
{nav(g)}
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
{BA.FAV}
<style>
{BA.FONTS}
{BA.ROOT}
{BA.CSS}
</style>
{BA.GC}
</head>
<body>
{body}
</body>
</html>
'''

# ---------- PDF ----------
PS = {
 'ru': dict(lt='Крэш-курс AMC 8 · Блок 1 · Числа и арифметика · уроки 1.1–1.5',
   lsub='Теория, разобранные задачи и самостоятельные порции. Решения самостоятельных &mdash; в конце файла.',
   theory='Теория', worked='Разобранные задачи', selfp='Самостоятельная порция',
   solsec='Решения самостоятельных порций', urok='Урок',
   tt='Крэш-курс AMC 8 · Тест Т1 · Числа и арифметика', tsub='10 задач &middot; 20 минут &middot; без калькулятора &middot; порог 7 из 10',
   nd='<div style="display:flex;gap:28px;font-size:9.5pt;margin-top:6px"><span style="flex:1;border-bottom:1px solid #000">Имя:</span><span style="flex:1;border-bottom:1px solid #000">Дата:</span></div>',
   kh='Ключ и разбор', kwarn='Страница для родителя: отрезать или не распечатывать для ученика.',
   foot='Задачи составлены оригинально и не воспроизводят задания официальных олимпиад AMC &middot; opscope.github.io/amc10-demo/course/amc8/'),
 'en': dict(lt='AMC 8 Crash Course · Block 1 · Numbers and Arithmetic · Lessons 1.1–1.5',
   lsub='Theory, worked examples, and independent sets. Solutions to the independent sets are at the end of the file.',
   theory='Theory', worked='Worked examples', selfp='Independent set',
   solsec='Solutions to the independent sets', urok='Lesson',
   tt='AMC 8 Crash Course · Test T1 · Numbers and Arithmetic', tsub='10 problems &middot; 20 minutes &middot; no calculator &middot; mastery bar 7 of 10',
   nd='<div style="display:flex;gap:28px;font-size:9.5pt;margin-top:6px"><span style="flex:1;border-bottom:1px solid #000">Name:</span><span style="flex:1;border-bottom:1px solid #000">Date:</span></div>',
   kh='Answer Key and Review', kwarn='Parent page: cut off or do not print for the student.',
   foot='All problems are original and do not reproduce official AMC competition problems &middot; opscope.github.io/amc10-demo/course/amc8/'),
}

def pdf_lessons(g):
    s = PS[g]
    parts, sols = [], []
    for L in LESSONS:
        w = ''.join(f'<div class="wp"><div class="wp-num">{x["tag"][g]}</div><div>{x["q"][g]}</div><div class="sol"><b>&rarr;</b> {x["sol"][g]}</div></div>' for x in L['worked'])
        sp = ''.join(f'<li>{x["q"][g]}</li>' for x in L['selfp'])
        sp += f'<li><b>&#9733;</b> {STARS[L["id"]]["q"][g]}</li>'
        parts.append(f'''<h2>{s['urok']} {L['id']}. {L['title'][g]}</h2>
<h3>{s['theory']}</h3>{L['theory'][g]}
<h3>{s['worked']}</h3>{w}
<h3>{s['selfp']}</h3><ol class="plist">{sp}</ol>''')
        rows = ''.join(f'<p><b>{i+1}.</b> {x["sol"][g]}</p>' for i, x in enumerate(L['selfp']))
        rows += f'<p><b>&#9733;</b> {STARS[L["id"]]["sol"][g]}</p>'
        sols.append(f'<h3>{s["urok"]} {L["id"]}</h3><div class="sollist">{rows}</div>')
    return f'''<!DOCTYPE html><html lang="{g}"><head><meta charset="utf-8"><style>{BA.PCSS}</style></head><body>
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
    return f'''<!DOCTYPE html><html lang="{g}"><head><meta charset="utf-8"><style>{BA.PCSS}</style></head><body>
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
    open(f'{SITE}/course/amc8/numbers-ru.html', 'w', encoding='utf8').write(page('ru'))
    open(f'{SITE}/course/amc8/numbers.html', 'w', encoding='utf8').write(page('en'))
    print('pages written')
    render_pdf(pdf_lessons('ru'), f'{SITE}/course/amc8/numbers-lessons-ru.pdf')
    render_pdf(pdf_lessons('en'), f'{SITE}/course/amc8/numbers-lessons.pdf')
    render_pdf(pdf_test('ru'), f'{SITE}/course/amc8/numbers-test-ru.pdf')
    render_pdf(pdf_test('en'), f'{SITE}/course/amc8/numbers-test.pdf')
