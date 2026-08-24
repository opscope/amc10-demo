#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EN-версия справки об AMC 10 (index-en.html). Задачи и варианты берёт из
build_practice_pdf.py (единый источник с печатной EN-версией)."""
import re, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from build_practice_pdf import EN, KEY

SITE = os.path.dirname(HERE)
ru = open(f'{SITE}/index.html', encoding='utf8').read()
FONTS = '\n'.join(re.findall(r'@font-face\{[^}]+\}', ru))
FAV = re.search(r'<link rel="icon"[^>]+>', ru).group(0)
GC = re.search(r'<script data-goatcounter[^<]+</script>', ru, re.S).group(0)
ROOT = re.search(r':root\{.*?\}', ru, re.S).group(0)
_parts = ru.split('<style>')
CSS = _parts[2].split('</style>')[0] if len(_parts) > 2 else _parts[1].split('</style>')[0]
CSS = CSS[CSS.index('* { box-sizing'):]

HINTS_EN = [
 'Numerator: 2(1+&hellip;+10) = 110; denominator: the sum of the first 10 odd numbers = 100. Answer: 11/10.',
 'Multipliers: 1.2&nbsp;&middot;&nbsp;0.75 = 0.9 &mdash; 10% lower.',
 'Total distance 6 km, total time 0.5 + 1.5 = 2 h: average 3 km/h.',
 '<var>x</var> + <var>y</var> = 17, <var>xy</var> = 60: diagonal&sup2; = 17&sup2; &minus; 2&middot;60 = 169, diagonal 13.',
 'Two-digit multiples of 7: 13; of those, multiples of 21: 4. Answer: 9.',
 '5&middot;12 &minus; 4&middot;13 = 60 &minus; 52 = 8.',
 '2<sup>10</sup>&middot;5<sup>7</sup> = 2&sup3;&middot;10<sup>7</sup> = 8&middot;10<sup>7</sup>: 8 digits.',
 'All teams C(8,3) = 56; teams with both quarreling students C(6,1) = 6. Answer: 50.',
 '64 &minus; &pi;&middot;4&sup2; = 64 &minus; 16&pi;.',
 '302 = 5 + 3(<var>n</var> &minus; 1): <var>n</var> = 100.',
 '<var>s</var>&sup3; &minus; 3<var>s</var> = 125 &minus; 15 = 110.',
 'Prime sums 2, 3, 5, 7, 11: 1 + 2 + 4 + 6 + 2 = 15 outcomes of 36, that is 5/12.',
 'For a right triangle, <var>r</var> = (6 + 8 &minus; 10)/2 = 2.',
 '2025 = 3<sup>4</sup>&middot;5&sup2;. Two fives require <var>n</var> &ge; 10; the threes in 10! number &lfloor;10/3&rfloor; + &lfloor;10/9&rfloor; = 4, which is enough. Answer: 10.',
 '<var>n</var>(<var>n</var>+1) is always even; divisibility by 3 holds for <var>n</var> &equiv; 0 or 2 (mod 3), two cases out of three: 66.',
 'Six equilateral triangles: 6&middot;(&radic;3/4)&middot;16 = 24&radic;3.',
 'Last digit 2 or 4; the other three from the remaining four digits: 2&middot;4&middot;3&middot;2 = 48.',
 '360 = 2&sup3;&middot;3&sup2;&middot;5: the sum of divisors is 15&middot;13&middot;6 = 1170.',
 '|<var>x</var> &minus; 2| &minus; 3 = &plusmn;1, so |<var>x</var> &minus; 2| = 4 or 2: solutions 6, &minus;2, 4, 0; sum 8.',
 'Mass points: from <var>BD</var>&nbsp;:&nbsp;<var>DC</var> = 1&nbsp;:&nbsp;2 assign masses <var>B</var> = 2, <var>C</var> = 1, so <var>D</var> carries 3. <var>E</var> is the midpoint of <var>AD</var>, so <var>A</var> = 3. For <var>F</var> on <var>AC</var>: <var>AF</var>&nbsp;:&nbsp;<var>FC</var> = 1&nbsp;:&nbsp;3.',
 '<var>a</var><sub><var>n</var></sub> = 2<sup><var>n</var></sup> &minus; 1 (check the first terms): <var>a</var><sub>10</sub> = 1023.',
 'Between &minus;2 and 3 the sum equals 5 &lt; 9; outside: on the right <var>x</var> &lt; 5, on the left <var>x</var> &gt; &minus;4. Integers from &minus;3 to 4: 8 of them.',
 'The order of 3 modulo 100 is 20, and 2025 = 20&middot;101 + 5, so 3<sup>2025</sup> &equiv; 3<sup>5</sup> = 243 &equiv; 43 (mod 100).',
 'These are the Catalan numbers: C<sub>5</sub> = 42. Option 14 is the trap for the strict reading &ldquo;below the diagonal&rdquo;.',
 'Base 1 (<var>x</var> = 1, 4); base &minus;1 with an even exponent (<var>x</var> = 2, 3); exponent 0 with a nonzero base (<var>x</var> = 5; the root 4 is already counted). Sum: 1 + 4 + 2 + 3 + 5 = 15.',
]

def problems_html():
    out = ['<ol class="problems">']
    for q, opts in EN:
        o = ''.join(f'<div class="opt"><b>{L}</b>{v}</div>' for L, v in zip('ABCDE', opts))
        out.append(f'<li><div class="q">{q}</div>\n<div class="opts">{o}</div></li>')
    out.append('</ol>')
    return '\n\n'.join(out)

def key_html():
    cells = []
    for row in range(5):
        cells.append(''.join(f'<div><span>{row*5+i+1}</span> <b>{KEY[row*5+i]}</b></div>' for i in range(5)))
    return '\n        '.join(cells)

hints_html = '\n        '.join(f'<p><b>{i+1}.</b> {h}</p>' for i, h in enumerate(HINTS_EN))

BODY = f"""
<div class="wrap">

<header style="margin-bottom:3.2rem">
  <div class="eyebrow">AMC 10 &middot; American Mathematics Competition &nbsp;&middot;&nbsp; <a class="langlink" href="index.html" style="font-family:var(--mono);font-size:.72rem;letter-spacing:.1em;text-transform:uppercase">Русская версия</a></div>
  <h1>The competition format and&nbsp;a&nbsp;practice test</h1>
  <p class="standfirst">A guide for parents and teachers: how the exam works, what it tests, and 25 original problems at the same level for a practice run.</p>
</header>

<div class="notice">
  <strong>About copyright.</strong> Official AMC competition problems are copyrighted by the MAA and are not reproduced here. All 25 problems below were written specifically for this page: they follow the format, topics, and rising difficulty of the real AMC&nbsp;10, but they are not problems from any actual year. Official past tests are freely available on the MAA website and in the Art of Problem Solving wiki.
</div>

<section>
  <h2>What this competition is</h2>
  <p>The AMC&nbsp;10 (American Mathematics Competition) is a nationwide math competition for US school students, run by the Mathematical Association of America. It is the first step of the chain leading to AIME, USA(J)MO, and eventually the national team selection.</p>

  <div class="spec">
    <div class="spec-row"><div class="spec-key">Format</div><div class="spec-val">25 problems in 75 minutes, each multiple choice with five options (A&ndash;E)</div></div>
    <div class="spec-row"><div class="spec-key">Difficulty</div><div class="spec-val">Problems are ordered by difficulty: #&nbsp;1&ndash;10 are accessible to most participants, #&nbsp;11&ndash;20 require solid technique, #&nbsp;21&ndash;25 are olympiad-level and fully solved by few</div></div>
    <div class="spec-row"><div class="spec-key">Who can take it</div><div class="spec-val">Students in grade 10 or below who are under 17.5 years old on competition day</div></div>
    <div class="spec-row"><div class="spec-key">Calculator</div><div class="spec-val">Not allowed &mdash; nor are phones, smartwatches, or any computing devices. The MAA&rsquo;s official line: no problem requires a calculator. Scratch paper, rulers, and compasses are allowed</div></div>
    <div class="spec-row"><div class="spec-key">When</div><div class="spec-val">Two independent versions about a week apart. In 2026: <strong>AMC&nbsp;10A &mdash; Thursday, November&nbsp;5</strong>; <strong>AMC&nbsp;10B &mdash; Friday, November&nbsp;13</strong>. A school may offer either or both. <em>Registration goes through a school or an official test center and closes in advance; at-home online testing is no longer offered.</em></div></div>
    <div class="spec-row"><div class="spec-key">What comes next</div><div class="spec-val">Roughly the top 2.5&nbsp;% of participants are invited to AIME. The cutoff is not fixed: it differs between versions A and B and depends on the year&rsquo;s difficulty. In the 2025&ndash;26 cycle it was 105 points (10A) and 99 points (10B); the historical range is about 90&ndash;120</div></div>
  </div>
</section>

<section>
  <h2>Scoring</h2>
  <div class="scoring">
    <div class="score-card"><div class="score-num">6</div><div class="score-lbl">for a correct answer</div></div>
    <div class="score-card"><div class="score-num">1.5</div><div class="score-lbl">for a skipped problem</div></div>
    <div class="score-card"><div class="score-num">0</div><div class="score-lbl">for a wrong answer</div></div>
  </div>
  <p>The maximum is 150 points. This implies a strategy worth discussing with your student in advance: blind guessing does not pay, because its expected value is 6&nbsp;&middot;&nbsp;&#8533;&nbsp;=&nbsp;1.2 points against 1.5 for an honest skip. But once you can eliminate even one option out of five, guessing becomes worthwhile.</p>
</section>

<section>
  <h2>What the exam tests</h2>
  <div class="topics">
    <div class="yes">
      <h3>Covered</h3>
      <ul class="topic-list">
        <li>Elementary algebra: equations and inequalities, quadratics, functions, sequences</li>
        <li>Geometry: similarity, polygons, circles, areas and volumes, coordinate geometry</li>
        <li>Elementary number theory: divisibility, modular arithmetic, primes</li>
        <li>Counting and probability</li>
      </ul>
    </div>
    <div class="no">
      <h3>Not covered</h3>
      <ul class="topic-list">
        <li>Trigonometry</li>
        <li>Logarithms</li>
        <li>Advanced algebra</li>
        <li>Calculus</li>
      </ul>
    </div>
  </div>
  <p>The last point matters especially for students on the Precalculus track: trigonometry and logarithms appear only on the AMC&nbsp;12, so much of the current school year does not directly prepare for the November competition. What does need preparation is counting, number theory, and competition geometry, which are barely present in the regular school curriculum. One more feature: almost every problem is solvable without heavy computation &mdash; the prize goes to the idea and the technique, not to arithmetic stamina.</p>
</section>

<section>
  <h2>AMC&nbsp;10A vs AMC&nbsp;10B</h2>

  <div class="scoring" style="grid-template-columns:1fr 1fr">
    <div class="score-card"><div class="score-num">10A</div><div class="score-lbl">Thursday, November 5, 2026</div></div>
    <div class="score-card"><div class="score-num">10B</div><div class="score-lbl">Friday, November 13, 2026</div></div>
  </div>

  <p>Nothing fundamental &mdash; they are two independent dates for the same competition, not two difficulty levels.</p>

  <p>The only differences: the versions run on different days about a week apart, and the problems are entirely different &mdash; otherwise later takers would know the questions in advance. They exist for scheduling: a school picks a convenient date, and a student does not miss the competition over an illness or a conflict.</p>

  <p>The format, syllabus, scoring, and status are identical. Both versions count equally toward AIME qualification, and neither is considered more prestigious.</p>

  <p>The writers aim for equal difficulty, but hitting it exactly is impossible in practice, so the AIME cutoff is computed separately for A and B. In the 2025&ndash;26 cycle it was 105 points for 10A and 99 for 10B &mdash; version B turned out slightly harder that year, so the bar was lowered. Predicting which version will be easier is impossible, so picking a date tactically is pointless.</p>

  <p>A practically useful detail: you may take both versions, and that is a fairly common strategy. Registration is separate (and usually paid separately), but two sittings give two chances to qualify &mdash; the better result counts, and clearing the cutoff once is enough. For a first year of participation this is sensible: the first sitting goes into getting used to the format and learning to manage the 75 minutes, and the second shows the real level.</p>

  <p>One more rule that occasionally matters: you cannot take both the AMC&nbsp;10 and the AMC&nbsp;12 on the same day, but you can take different levels on different dates &mdash; say, AMC&nbsp;10A on the first date and AMC&nbsp;12B on the second. For students who have outgrown the 10, this option becomes relevant.</p>

  <p>If you decide to take both, check with your school in advance whether it even offers version B &mdash; many schools run only one of the dates, and then the second has to be found at another test center.</p>
</section>

<section>
  <h2>An AMC 10 style practice test</h2>
  <div class="test-head">
    <span>25 problems</span><span>75 minutes</span><span>no calculator</span><span>answers at the end</span>
  </div>

  {problems_html()}

  <details class="answers">
    <summary>Show answers and solutions</summary>
    <div class="answers-body">
      <div class="key">
        {key_html()}
      </div>

      <div class="hints">
        {hints_html}
      </div>
    </div>
  </details>
</section>

<div class="notice" style="margin:0 0 3rem">
  <strong>Preparation materials.</strong> This test comes with a free <a href="course/index-en.html">ten-week crash course</a>: self-contained, run by a parent with no teacher needed &mdash; theory, worked examples, independent sets with solutions, tests, and printable PDFs.
</div>

<footer>
  All problems on this page are original and do not reproduce official AMC competition problems. Official past tests and rules &mdash; at <a href="https://maa.org/student-programs/amc/">maa.org</a>. Next: <a href="course/index-en.html">the ten-week crash course</a>.
</footer>

</div>
"""

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>AMC 10 · Format and Practice Test</title>
<meta name="description" content="How the AMC 10 works and a 25-problem practice test at the same level. A guide for parents and teachers.">
{FAV}
<style>
{FONTS}
{ROOT}
{CSS}
</style>
{GC}
</head>
<body>
{BODY}
</body>
</html>
"""
open(f'{SITE}/index-en.html', 'w', encoding='utf8').write(html)
print('index-en.html', os.path.getsize(f'{SITE}/index-en.html') // 1024, 'KB')
