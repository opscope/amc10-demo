#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Печатные PDF пробного теста AMC 10: RU + EN. Рендер: headless Chrome."""
import subprocess, os

RU_PROBLEMS = open('/tmp/ru_problems.html', encoding='utf8').read().replace('\u23a2\xa0', '|\u2009').replace('\xa0\u23a4', '\u2009|')

def frac(a, b):
    return f'<span class="frac"><span>{a}</span><span>{b}</span></span>'

EN = [
 (f'What is the value of {frac("2 + 4 + 6 + &hellip; + 20","1 + 3 + 5 + &hellip; + 19")}?',
  [frac(9,10), '1', frac(11,10), frac(6,5), frac(11,9)]),
 ('A price first increased by 20%, and then the new price decreased by 25%. How does the final price compare to the original?',
  ['10% lower','5% lower','unchanged','5% higher','10% higher']),
 ('Anna walked the first 3 km at 6 km/h and the next 3 km at 2 km/h. What was her average speed for the whole walk?',
  ['2.5 km/h','3 km/h','3.5 km/h','4 km/h','4.5 km/h']),
 ('A rectangle has perimeter 34 and area 60. What is the length of its diagonal?',
  ['10','11','12','13','14']),
 ('How many two-digit numbers are divisible by 7 but not divisible by 3?',
  ['7','8','9','10','13']),
 ('The average of five numbers is 12. One number is removed, and the average of the remaining four becomes 13. What number was removed?',
  ['5','6','7','8','10']),
 ('How many digits does the number 2<sup>10</sup>&nbsp;&middot;&nbsp;5<sup>7</sup> have?',
  ['8','9','10','11','17']),
 ('A class has 8 students. A team of 3 must be chosen, but two of the students have quarreled and cannot both be on the team. In how many ways can the team be chosen?',
  ['40','44','48','50','56']),
 ('A circle is inscribed in a square with side 8. What is the area of the part of the square lying outside the circle?',
  ['64 &minus; 8&pi;','64 &minus; 16&pi;','64 &minus; 32&pi;','32 &minus; 16&pi;','16 &minus; 4&pi;']),
 ('In an arithmetic sequence the first term is 5 and the common difference is 3. Which term of the sequence is the number 302?',
  ['99th','100th','101st','102nd','103rd']),
 (f'A real number <var>x</var> satisfies <var>x</var> + {frac("1","<var>x</var>")} = 5. What is <var>x</var><sup>3</sup> + {frac("1","<var>x</var><sup>3</sup>")}?',
  ['110','115','120','125','130']),
 ('Two standard dice are rolled. What is the probability that the sum of the numbers shown is a prime number?',
  [frac(1,3), frac(2,5), frac(5,12), frac(1,2), frac(7,12)]),
 ('A right triangle has legs 6 and 8. What is the radius of its inscribed circle?',
  ['1.5','2','2.4','2.5','3']),
 ('What is the least positive integer <var>n</var> such that <var>n</var>! is divisible by 2025?',
  ['10','11','12','15','25']),
 ('How many integers <var>n</var> with 1 &le; <var>n</var> &le; 100 are such that <var>n</var><sup>2</sup> + <var>n</var> is divisible by 6?',
  ['33','50','66','67','83']),
 ('What is the area of a regular hexagon with side 4?',
  ['16&radic;3','24&radic;3','32&radic;3','48&radic;3','96']),
 ('How many four-digit even numbers have all digits distinct and taken from the set {1, 2, 3, 4, 5}?',
  ['24','36','48','60','72']),
 ('What is the sum of all positive divisors of 360, including 1 and 360 itself?',
  ['1024','1080','1120','1170','1260']),
 ('What is the sum of all real roots of the equation |&thinsp;|<var>x</var> &minus; 2| &minus; 3&thinsp;| = 1?',
  ['0','4','6','8','10']),
 ('In triangle <var>ABC</var>, point <var>D</var> lies on side <var>BC</var> so that <var>BD</var>&nbsp;:&nbsp;<var>DC</var> = 1&nbsp;:&nbsp;2. Point <var>E</var> is the midpoint of <var>AD</var>. Line <var>BE</var> meets side <var>AC</var> at point <var>F</var>. What is the ratio <var>AF</var>&nbsp;:&nbsp;<var>FC</var>?',
  ['1 : 2','2 : 5','2 : 3','1 : 4','1 : 3']),
 ('A sequence is defined by <var>a</var><sub>1</sub> = 1 and <var>a</var><sub><var>n</var>+1</sub> = 2<var>a</var><sub><var>n</var></sub> + 1 for all <var>n</var> &ge; 1. What is <var>a</var><sub>10</sub>?',
  ['511','512','1022','1023','2047']),
 ('How many integers <var>x</var> satisfy the inequality |<var>x</var> &minus; 3| + |<var>x</var> + 2| &lt; 9?',
  ['7','8','9','10','11']),
 ('What are the last two digits of 3<sup>2025</sup>?',
  ['01','07','27','43','83']),
 ('Lattice paths from (0, 0) to (5, 5) consist of unit steps right and up. How many such paths never go above the line <var>y</var> = <var>x</var>?',
  ['14','32','42','120','252']),
 ('What is the sum of all real numbers <var>x</var> for which (<var>x</var><sup>2</sup> &minus; 5<var>x</var> + 5)<sup>&thinsp;<var>x</var><sup>2</sup> &minus; 9<var>x</var> + 20</sup> = 1?',
  ['9','10','13','14','15']),
]

KEY = ['C','A','B','D','C','D','A','D','B','B','A','C','B','A','C','B','C','D','D','E','D','B','D','C','E']

CSS = """
@page { size: letter; margin: 16mm 16mm 18mm; }
* { box-sizing: border-box; }
body { font-family: Georgia, 'Times New Roman', serif; font-size: 10.6pt; line-height: 1.42; color: #000; margin: 0; }
header { border-bottom: 2px solid #000; padding-bottom: 8px; margin-bottom: 14px; }
.t1 { font-size: 17pt; font-weight: bold; margin: 0 0 2px; }
.t2 { font-size: 9.5pt; margin: 0 0 8px; }
.nd { display: flex; gap: 28px; font-size: 9.5pt; margin-top: 6px; }
.nd span { flex: 1; border-bottom: 1px solid #000; padding-bottom: 1px; }
ol.problems { list-style: none; margin: 0; padding: 0; counter-reset: p; }
ol.problems > li { counter-increment: p; margin: 0 0 11px; page-break-inside: avoid; display: block; }
ol.problems > li::before { content: counter(p) ". "; font-weight: bold; }
ol.problems .q { display: inline; }
.opts { display: flex; flex-wrap: wrap; gap: 2px 20px; margin: 4px 0 0 16px; }
.opt { display: inline-flex; align-items: baseline; gap: 5px; background: none; padding: 0; }
.opt b { font-weight: bold; }
.opt b::before { content: "("; } .opt b::after { content: ")"; }
.frac { display: inline-flex; flex-direction: column; vertical-align: middle; text-align: center; font-size: 0.72em; line-height: 1.2; position: relative; top: -0.08em; }
.frac > span:first-child { border-bottom: 0.8px solid #000; padding: 0 3px; }
.frac > span:last-child { padding: 0 3px; }
var { font-style: italic; }
.keypage { page-break-before: always; }
.keypage h2 { font-size: 13pt; border-bottom: 1.5px solid #000; padding-bottom: 4px; }
.warn { font-size: 9.5pt; font-style: italic; margin-bottom: 12px; }
table.key { border-collapse: collapse; }
table.key td { border: 1px solid #000; padding: 4px 9px; text-align: center; font-size: 10pt; vertical-align: middle; line-height: 1; }
table.key td.n { font-weight: normal; color: #444; }
table.key td.a { font-weight: bold; }
.colophon { margin-top: 24px; padding-top: 6px; border-top: 0.8px solid #999; font-size: 8pt; color: #555; }
"""

def en_problems_html():
    out = ['<ol class="problems">']
    for q, opts in EN:
        o = ''.join(f'<span class="opt"><b>{L}</b>{v}</span>' for L, v in zip('ABCDE', opts))
        out.append(f'<li><span class="q">{q}</span><div class="opts">{o}</div></li>')
    out.append('</ol>')
    return '\n'.join(out)

def key_table():
    rows = []
    for r in range(5):
        ns = ''.join(f'<td class="n">{r*5+i+1}</td>' for i in range(5))
        As = ''.join(f'<td class="a">{KEY[r*5+i]}</td>' for i in range(5))
        rows.append(f'<tr>{ns}</tr><tr>{As}</tr>')
    return '<table class="key">' + ''.join(rows) + '</table>'

def page(lang):
    if lang == 'ru':
        title = 'Пробный тест в стиле AMC 10'
        sub = '25 задач &middot; 75 минут &middot; без калькулятора &middot; выберите один ответ (A&ndash;E) в каждой задаче'
        nd = '<div class="nd"><span>Имя:</span><span>Дата:</span></div>'
        body = RU_PROBLEMS
        kh, warn = 'Ключ ответов', 'Страница для родителя: отрезать или не распечатывать для ученика. Полные решения — на странице теста онлайн.'
        foot = 'Задачи составлены оригинально и не воспроизводят задания официальных олимпиад AMC &middot; opscope.github.io/amc10-demo'
    else:
        title = 'AMC 10 Style Practice Test'
        sub = '25 problems &middot; 75 minutes &middot; no calculator &middot; choose one answer (A&ndash;E) for each problem'
        nd = '<div class="nd"><span>Name:</span><span>Date:</span></div>'
        body = en_problems_html()
        kh, warn = 'Answer Key', 'Parent page: cut off or do not print for the student. Full solutions are available on the test page online.'
        foot = 'All problems are original and do not reproduce official AMC competition problems &middot; opscope.github.io/amc10-demo'
    return f"""<!DOCTYPE html><html lang="{lang}"><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<header><div class="t1">{title}</div><div class="t2">{sub}</div>{nd}</header>
{body}
<div class="keypage"><h2>{kh}</h2><div class="warn">{warn}</div>{key_table()}<div class="colophon">{foot}</div></div>
</body></html>"""

CH = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
for lang, out in [('ru', 'amc10-probnik-ru.pdf'), ('en', 'amc10-practice-en.pdf')]:
    src = f'/tmp/print_{lang}.html'
    open(src, 'w', encoding='utf8').write(page(lang))
    dst = f'/Users/andreikovrijnykh/amc10demo/kurs/{out}'
    subprocess.run([CH, '--headless', '--disable-gpu', f'--print-to-pdf={dst}',
                    '--no-pdf-header-footer', 'file://' + src], capture_output=True)
    print(out, os.path.getsize(dst) // 1024, 'KB')
