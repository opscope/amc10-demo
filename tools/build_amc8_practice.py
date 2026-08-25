#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Пробный тест AMC 8: страницы RU/EN + печатные PDF RU/EN."""
import os, sys, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from amc8_practice_data import P, KEY, HINTS
import build_algebra as BA

SITE = os.path.dirname(HERE)
CH = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

S = {
 'ru': dict(
  title='Пробный тест AMC 8 · Крэш-курс',
  desc='Пробный тест в стиле AMC 8: 25 оригинальных задач за 40 минут, ключ и разборы.',
  eyebrow='Крэш-курс AMC 8 &middot; Пробный тест', h1='Пробный тест в&nbsp;стиле AMC&nbsp;8',
  stand='25 оригинальных задач того же уровня и формата, что настоящая олимпиада: 40 минут, без калькулятора. Ключ и разборы &mdash; в конце страницы.',
  otherlang='English version', otherhref='practice-test.html',
  head=['25 задач', '40 минут', 'без калькулятора', 'ответы в конце'],
  strategy='<strong>Стратегия AMC 8.</strong> Штрафов за ошибку нет: пустая клетка и неверный ответ стоят одинаково &mdash; ноль. Поэтому отвечайте на все 25 задач, даже наугад. И следите за темпом: 40 минут на 25 задач &mdash; это чуть больше полутора минут на задачу.',
  copyright='<strong>Об авторских правах.</strong> Задачи официальных олимпиад AMC защищены авторским правом MAA и здесь не воспроизводятся. Все 25 задач составлены специально для этой страницы: они повторяют формат, темы и нарастающую сложность настоящего AMC&nbsp;8, но не являются заданиями какого-либо реального года.',
  showkey='Показать ответы и разборы', pdfline='<strong>Для печати:</strong> <a href="practice-test-ru.pdf">пробный тест PDF</a>. Ключ ответов вынесен на отдельную последнюю страницу: её удобно не печатать или отрезать.',
  foot='Задачи составлены оригинально и не воспроизводят задания официальных олимпиад AMC. <a href="index.html">Курс AMC 8</a> &middot; <a href="diagnostics-ru.html">диагностика</a> &middot; <a href="index.html#svyaz">оставить комментарий</a>.',
  pt='Пробный тест в стиле AMC 8', psub='25 задач &middot; 40 минут &middot; без калькулятора &middot; выберите один ответ (A&ndash;E) в каждой задаче',
  nd_l='Имя:', nd_r='Дата:', kh='Ключ ответов и разборы', kwarn='Страница для родителя: отрезать или не распечатывать для ученика. Разборы &mdash; на странице теста онлайн.',
  pfoot='Задачи составлены оригинально и не воспроизводят задания официальных олимпиад AMC &middot; opscope.github.io/amc10-demo/course/amc8/'),
 'en': dict(
  title='AMC 8 Practice Test · Crash Course',
  desc='An AMC 8 style practice test: 25 original problems in 40 minutes, with key and solutions.',
  eyebrow='AMC 8 Crash Course &middot; Practice Test', h1='An AMC&nbsp;8 style practice&nbsp;test',
  stand='25 original problems at the level and format of the real competition: 40 minutes, no calculator. The key and solutions are at the end of the page.',
  otherlang='Русская версия', otherhref='practice-test-ru.html',
  head=['25 problems', '40 minutes', 'no calculator', 'answers at the end'],
  strategy='<strong>AMC 8 strategy.</strong> There is no penalty for a wrong answer: a blank and a mistake both score zero. So answer all 25 problems, even by guessing. And watch the pace: 40 minutes for 25 problems is just over a minute and a half per problem.',
  copyright='<strong>About copyright.</strong> Official AMC competition problems are copyrighted by the MAA and are not reproduced here. All 25 problems were written specifically for this page: they follow the format, topics, and rising difficulty of the real AMC&nbsp;8, but they are not problems from any actual year.',
  showkey='Show answers and solutions', pdfline='<strong>Printable:</strong> <a href="practice-test.pdf">the practice test as a PDF</a>. The answer key is on a separate final page: leave it unprinted or cut it off.',
  foot='All problems are original and do not reproduce official AMC competition problems. <a href="index-en.html">AMC 8 course</a> &middot; <a href="diagnostics.html">diagnostics</a> &middot; <a href="index-en.html#contact">leave a comment</a>.',
  pt='AMC 8 Style Practice Test', psub='25 problems &middot; 40 minutes &middot; no calculator &middot; choose one answer (A&ndash;E) for each problem',
  nd_l='Name:', nd_r='Date:', kh='Answer Key and Solutions', kwarn='Parent page: cut off or do not print for the student. Solutions are on the test page online.',
  pfoot='All problems are original and do not reproduce official AMC competition problems &middot; opscope.github.io/amc10-demo/course/amc8/'),
}

def nav(g):
    if g == 'ru':
        return '''<nav class="side">
<div class="nav-t">Курсы</div>
<details name="course" open><summary>AMC 8</summary>
<a href="index.html#zachem">О курсе</a>
<a href="index.html#programma">Программа</a>
<a class="here" href="practice-test-ru.html">Пробный тест</a>
<a href="diagnostics-ru.html">0 · Диагностика</a>
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
    return '''<nav class="side">
<div class="nav-t">Courses</div>
<details name="course" open><summary>AMC 8</summary>
<a href="index-en.html#why">About the course</a>
<a href="index-en.html#program">Program</a>
<a class="here" href="practice-test.html">Practice test</a>
<a href="diagnostics.html">0 · Diagnostics</a>
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

def problems_html(g):
    out = []
    for q_ru, q_en, oru, oen in P:
        q = q_ru if g == 'ru' else q_en
        opts = oru if (g == 'ru' or oen is None) else oen
        o = ''.join(f'<div class="opt"><b>{L}</b>{v}</div>' for L, v in zip('ABCDE', opts))
        out.append(f'<li><div class="q">{q}</div><div class="opts">{o}</div></li>')
    return '<ol class="tprob">' + '\n'.join(out) + '</ol>'

def page(g):
    s = S[g]
    keyc = ''.join(f'<div><span>{i+1}</span> <b>{a}</b></div>' for i, a in enumerate(KEY))
    hints = ''.join(f'<p><b>{i+1}.</b> {h}</p>' for i, h in enumerate(HINTS[g]))
    heads = ''.join(f'<span>{x}</span>' for x in s['head'])
    body = f'''<div class="layout">
{nav(g)}
<main>
<header style="margin-bottom:2.2rem">
<div class="eyebrow">{s['eyebrow']} &nbsp;&middot;&nbsp; <a class="langlink" href="{s['otherhref']}">{s['otherlang']}</a></div>
<h1>{s['h1']}</h1>
<p class="standfirst">{s['stand']}</p>
</header>
<div class="notice">{s['strategy']}</div>
<div class="notice" style="border-left-color:var(--whisper)">{s['copyright']}</div>
<section class="lesson" style="border-top:none;margin-top:1rem">
<div class="lesson-meta">{heads.replace('<span>','<span>')}</div>
{problems_html(g)}
<details class="answers"><summary>{s['showkey']}</summary><div class="answers-body">
<div class="key">{keyc}</div>
<div class="hints">{hints}</div></div></details>
<div class="pdfline">{s['pdfline']}</div>
</section>
<footer>{s['foot']}</footer>
</main>
</div>'''
    lm = '<div class="lesson-meta">' + ''.join(f'<span>{x}</span>' for x in s['head']) + '</div>'
    body = body.replace(f"<div class=\"lesson-meta\">{heads}</div>", lm)
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

def pdf(g):
    s = S[g]
    out = []
    for q_ru, q_en, oru, oen in P:
        q = q_ru if g == 'ru' else q_en
        opts = oru if (g == 'ru' or oen is None) else oen
        o = ''.join('<span class="opt"><b>%s</b>%s</span>' % (L, v) for L, v in zip('ABCDE', opts))
        out.append(f'<li>{q}<div class="opts">{o}</div></li>')
    probs = '<ol class="plist">' + ''.join(out) + '</ol>'
    rows = []
    for r in range(5):
        ns = ''.join(f'<td>{r*5+i+1}</td>' for i in range(5))
        As = ''.join(f'<td><b>{KEY[r*5+i]}</b></td>' for i in range(5))
        rows.append(f'<tr>{ns}</tr><tr>{As}</tr>')
    hints = ''.join(f'<p><b>{i+1}.</b> {h}</p>' for i, h in enumerate(HINTS[g]))
    return f'''<!DOCTYPE html><html lang="{g}"><head><meta charset="utf-8"><style>{BA.PCSS}</style></head><body>
<header><div class="t1h">{s['pt']}</div><div class="t2h">{s['psub']}</div>
<div style="display:flex;gap:28px;font-size:9.5pt;margin-top:6px"><span style="flex:1;border-bottom:1px solid #000">{s['nd_l']}</span><span style="flex:1;border-bottom:1px solid #000">{s['nd_r']}</span></div></header>
{probs}
<div class="keypage"><h2>{s['kh']}</h2><p class="warn">{s['kwarn']}</p>
<table class="key">{''.join(rows)}</table>
<div class="sollist">{hints}</div>
<div class="colophon">{s['pfoot']}</div></div>
</body></html>'''

def render_pdf(html, out):
    src = f'/tmp/pdf_src_{os.path.basename(out)}.html'
    open(src, 'w', encoding='utf8').write(html)
    subprocess.run([CH, '--headless', '--disable-gpu', f'--print-to-pdf={out}',
                    '--no-pdf-header-footer', 'file://' + src], capture_output=True)
    print(os.path.basename(out), os.path.getsize(out) // 1024, 'KB')

if __name__ == '__main__':
    open(f'{SITE}/course/amc8/practice-test-ru.html', 'w', encoding='utf8').write(page('ru'))
    open(f'{SITE}/course/amc8/practice-test.html', 'w', encoding='utf8').write(page('en'))
    print('pages written')
    render_pdf(pdf('ru'), f'{SITE}/course/amc8/practice-test-ru.pdf')
    render_pdf(pdf('en'), f'{SITE}/course/amc8/practice-test.pdf')
