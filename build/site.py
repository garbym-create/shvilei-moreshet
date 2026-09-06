# -*- coding: utf-8 -*-
"""בונה את אתר הליווי הסטטי (GitHub Pages)."""
import os, subprocess, html as H

ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); U=os.path.join(ROOT,"units/eretz-israel")
CREDIT="ממעבדת הניסויים של מרי גרבי"   # מופיע במקום אחד בלבד בכל דף — בפוטר
TAGLINE="יחידות לימוד מונגשות"
UNIT="ארץ ישראל: זיכרון, זהות ושייכות"
# המקור הרשמי של המערכים — "שבילי מורשת", המזכירות הפדגוגית, משרד החינוך
MEYDA="https://meyda.education.gov.il/files/Mazkirut_Pedagogit/shviley_moreshet/hativatbeynayim/1"
MEYDA_FILE="shiur{n}-eretzisraelzikaronzehutveshayakhut.pdf"

LESSONS=[
 (1,"מהו בית ומהו זיכרון?","\"נחיתה\" לתוך הדילמה מתוך החוויה האישית",
  "לנחות לתוך הדילמה מתוך החוויה האישית של התלמידים, ולחבר אותה לשאלה המניעה של היחידה.",
  [("פתיחה · 10 דק'","תרגיל \"עוגן\": מהו הדבר שהופך מקום ל'בית' עבורי?"),
   ("גוף השיעור · 25 דק'","ניתוח השיר \"כאן\" / עוזי חיטמן — ציד מילים של עבר מול הווה."),
   ("סיכום · 10 דק'","לוח קיר כיתתי וכתיבה רפלקטיבית: \"זיכרון ישראלי שלי\".")],
  ["\"כאן\" / עוזי חיטמן"]),
 (2,"שורשים וזיקה היסטורית","ביסוס נקודת מבט א' — הקשר ההיסטורי והאמוני",
  "להבין את עמדה א': זהות יהודית-ישראלית משמעותית מתקיימת בארץ בזכות הקשר ההיסטורי והדתי.",
  [("פתיחה · 10 דק'","תזכורת: האם הזיקה שלנו למקום היא רק רגשית, או נטועה בעבר?"),
   ("גוף השיעור · 25 דק'","קריאה קולית ועבודה בזוגות: דברים י\"א ו\"לבי במזרח\" לריה\"ל."),
   ("סיכום · 10 דק'","משימת קישור: כיצד הרעיונות משתקפים במגילת העצמאות?")],
  ["דברים י\"א, י\"א–י\"ב","\"לבי במזרח\" / רבי יהודה הלוי","מגילת העצמאות"]),
 (3,"הבית הוא כאן ועכשיו","ביסוס נקודת מבט ב' — החיים כאן ועכשיו",
  "להבין את עמדה ב': הזהות נובעת מעצם המגורים בארץ, מהמשפחה, מהחברים ומהאחריות המשותפת.",
  [("פתיחה · 10 דק'","סבב מליאה: \"3 דברים שמרגישים לי בית בארץ\"."),
   ("גוף השיעור · 25 דק'","קריאה מודרכת ועבודה בקבוצות: שייכות שנמדדת במעשה."),
   ("סיכום · 10 דק'","כתיבה עצמאית: \"המשמעות שלי כאן\" — מכתב או פתק לעצמי.")],
  ["\"שלום לך ארץ נהדרת\" (מילים: אילן גולדהירש)","עמוס עוז — שמירת הטבע",
   "תמיר היימן — 'טנק בנייה', מלחמת לבנון השנייה"]),
 (4,"הדילמה הגדולה · פרשת אוגנדה","שיא הדיון הדיאלקטי ביחידה",
  "להבין את המתח בין \"מקלט לילה\" לבין הזיקה הערכית-היסטורית לארץ, ולנסח עמדה אישית מנומקת.",
  [("פתיחה · 10 דק'","הרצאה קצרה והצגת הדילמה — פרשת אוגנדה, 1903."),
   ("גוף השיעור · 10 דק'","דיבייט כיתתי או ג'יקסו בין שתי העמדות."),
   ("סיכום · 25 דק'","מה הכריע בסוף, והשלכות להיום: \"מקלט\" או \"מהות\"?")],
  ["תוכנית אוגנדה (1903)","מדברי יחיאל צ'לנוב בקונגרס הציוני השישי",
   "מדברי בנימין זאב הרצל בקונגרס הציוני השישי","אוגנדה על המפה"]),
 (5,"סיור: בנתיבי זהות","סיכום היחידה במרחב האמיתי",
  "לחוש פיזית את המקומות המייצגים את שתי העמדות, ולבחון את השילוב ביניהן במרחב האמיתי.",
  [("פתיחה · 10 דק'","הצגת \"מפת הדילמה\" בנקודת תצפית או כיכר מרכזית."),
   ("גוף הסיור · 25 דק'","\"מסע צילום וגילוי\" — חוקרי עבר וחוקרי הווה."),
   ("סיכום · 25 דק'","\"מעגל השייכות\" ומשפט סיכום אישי.")],
  ["הנחיות לקבוצות בסיור","דגשים למורה בסיור"]),
]

TRAILS=[("rimon","שביל הרימון"),("zayit","שביל הזית"),("teena","שביל התאנה")]

def shell(title, body, depth=0, nav="", desc=""):
    b="../"*depth
    navs=[("בית",b+"index.html","home"),("היחידה",b+"units/eretz-israel/index.html","unit"),
          ("אזור המורה",b+"units/eretz-israel/teacher.html","teacher"),
          ("מקורות",b+"units/eretz-israel/sources.html","sources")]
    CUR=' aria-current="page"'
    items="".join(f'<a href="{u}"{CUR if k==nav else ""}>{t}</a>' for t,u,k in navs)
    return f"""<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{H.escape(title)}</title>
<meta name="description" content="{H.escape(desc or UNIT)}">
<link href="https://fonts.googleapis.com/css2?family=Assistant:wght@400;600;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{b}assets/style.css">
</head>
<body>
<a class="skip" href="#main">דלג לתוכן</a>
<header class="site"><div class="wrap">
<a class="logo" href="{b}index.html">שבילי מורשת<small>{TAGLINE}</small></a>
<nav aria-label="ניווט ראשי">{items}</nav>
</div></header>
<main id="main">{body}</main>
<footer class="site-foot"><div class="wrap">
<span>🧪 <b>{CREDIT}</b></span>
<span>{UNIT} · כיתות ז'–ח'</span>
</div></footer>
</body></html>"""

POS="""<div class="grid two">
<div class="card a"><span class="tag">עמדה א' · העבר</span>
<p><b>הארץ היא הבית שלנו בגלל ההיסטוריה.</b></p>
<p>אלפי שנים של זיכרון, תפילה, סיפורים ומורשת מחברים אותנו למקום הזה.</p></div>
<div class="card b"><span class="tag">עמדה ב' · ההווה</span>
<p><b>הארץ היא הבית שלנו בגלל החיים כאן.</b></p>
<p>המשפחה, החברים, השכונה, השפה והאחריות שלנו זה לזה — הם שהופכים אותה לבית.</p></div></div>"""

DRIVING="""<div class="q">האם הזיקה שלנו למקום נובעת מהקשר היסטורי, אמוני ומסורתי —
או מעצם מגורינו כאן בצד משפחה, חברים והקהילות המרכיבות את עם ישראל, ואחריות לרווחתו ולשגשוגו?</div>"""

def lesson_cards(depth):
    b="../"*depth
    out=[]
    for n,t,sub,_,_,_ in LESSONS:
        out.append(f'<a class="lesson" href="{b}units/eretz-israel/lesson-{n}.html">'
                   f'<span class="n">{n}</span><span><b>{t}</b><span>{sub}</span></span></a>')
    return '<div class="lessons">'+"".join(out)+'</div>'

# ── דף הבית ──────────────────────────────────────────────
home=f"""<section class="hero"><div class="wrap">
<span class="eyebrow">שבילי מורשת · כיתות ז'–ח'</span>
<h1>{UNIT}</h1>
<p class="sub">רצף למידה בן חמישה שיעורים, מונגש לתלמידים עם לקויות למידה — מצגות להקרנה, דפי עבודה בשלוש גרסאות, וחומרי מורה.</p>
</div></section>
<div class="wrap">
{DRIVING}
<h2>שתי העמדות שמלוות את היחידה</h2>
{POS}
<h2>השיעורים</h2>
{lesson_cards(0)}
<div class="note"><b>למורה:</b> ב<a href="units/eretz-israel/teacher.html">אזור המורה</a> תמצאו את מדריך ההתאמות,
נספח מערכי השיעור המלאים, ומפתח שלושת השבילים.</div>
</div>"""
open(os.path.join(ROOT,"index.html"),"w",encoding="utf-8").write(
    shell(f"{UNIT} · שבילי מורשת",home,0,"home",
          "רצף למידה מונגש לכיתות ז'–ח' בנושא הזיקה לארץ ישראל"))

# ── דף היחידה ────────────────────────────────────────────
unit=f"""<section class="hero"><div class="wrap">
<span class="eyebrow">היחידה במבט-על</span>
<h1>{UNIT}</h1>
<p class="sub">היחידה עוסקת במשמעות הקשר של היחיד והעם לארץ ישראל מתוך החיים כאן והדילמות שהם יוצרים.</p>
</div></section>
<div class="wrap">
{DRIVING}
<h2>מפת היחידה</h2>
<p>הזיקה לארץ ישראל נארגת משלושה חוטים שלובים: קשר היסטורי-אמוני לאורך הדורות; חיים יומיומיים כאן, לצד משפחה, חברים וקהילה; ושאיפה להיות חלק מתרבות עולמית בלי לאבד את הייחוד.</p>
{POS}
<h2>השיעורים</h2>
{lesson_cards(2)}
<h2>דפי העבודה — שלושת השבילים</h2>
<p>אותם מקורות ואותן שאלות מנחות בשלוש גרסאות. שני עמודים לכל שיעור, להדפסה דו-צדדית.
<b>על הדף לא מופיעה רמת קושי</b> — רק שם השביל.</p>
<div class="btns">
<a class="btn rimon" href="worksheets/rimon.html">שביל הרימון</a>
<a class="btn zayit" href="worksheets/zayit.html">שביל הזית</a>
<a class="btn teena" href="worksheets/teena.html">שביל התאנה</a>
</div>
<div class="note"><b>המפתח מי מקבל מה</b> נמצא באזור המורה בלבד — לא על הדף ולא בכיתה.</div>
</div>"""
open(os.path.join(U,"index.html"),"w",encoding="utf-8").write(
    shell(f"היחידה · {UNIT}",unit,2,"unit"))

# ── דפי שיעור ────────────────────────────────────────────
for n,t,sub,goal,stages,srcs in LESSONS:
    st="".join(f'<li><span><b>{a}</b><small>{b}</small></span></li>' for a,b in
               [(x.split(" · ")[0]+" <small>· "+x.split(" · ")[1]+"</small>",y) for x,y in stages])
    sl="".join(f"<li>{s}</li>" for s in srcs)
    prev=f'<a class="btn" href="lesson-{n-1}.html">→ שיעור {n-1}</a>' if n>1 else ""
    nxt=f'<a class="btn" href="lesson-{n+1}.html">שיעור {n+1} ←</a>' if n<5 else ""
    body=f"""<section class="hero"><div class="wrap">
<span class="eyebrow">שיעור {n} מתוך 5</span>
<h1>{t}</h1><p class="sub">{sub}</p>
</div></section>
<div class="wrap">
<div class="btns">
<a class="btn pri" href="decks/lesson-{n}.html">▶ פתיחת המצגת</a>
<a class="btn" href="{MEYDA}/{MEYDA_FILE.format(n=n)}" target="_blank" rel="noopener">📄 מערך השיעור המקורי באתר משרד החינוך ↗</a>
</div>
<h2>מטרת השיעור</h2><p>{goal}</p>
<h2>מבנה השיעור</h2><ol class="stages">{st}</ol>
<h2>מקורות ומשאבי הלימוד</h2><ul>{sl}</ul>
<h2>דפי עבודה לשיעור</h2>
<p>דף העבודה נפתח בשיעור {n}. אפשר להדפיס עמוד בודד או את כל השביל.</p>
<div class="btns">
<a class="btn rimon" href="worksheets/rimon.html#l{n}">שביל הרימון</a>
<a class="btn zayit" href="worksheets/zayit.html#l{n}">שביל הזית</a>
<a class="btn teena" href="worksheets/teena.html#l{n}">שביל התאנה</a>
</div>
<div class="btns" style="margin-top:30px">{prev}{nxt}</div>
</div>"""
    open(os.path.join(U,f"lesson-{n}.html"),"w",encoding="utf-8").write(
        shell(f"שיעור {n} · {t}",body,2,"unit",sub))

# ── המרת מסמכי מורה ──────────────────────────────────────
def md2html(path):
    return subprocess.run(["npx","--yes","marked","-i",path],capture_output=True,
                          text=True,cwd=ROOT).stdout

teacher_md=os.path.join(U,"teacher-guide.md")
appendix_md=os.path.join(U,"appendix.md")
t_html=md2html(teacher_md); a_html=md2html(appendix_md)

teacher=f"""<section class="hero"><div class="wrap">
<span class="eyebrow">אזור המורה</span><h1>מדריך ההתאמות וההנגשה</h1>
<p class="sub">איך מנהלים את היחידה בכיתה שבה יש דיסלקציה, קשיי קשב, קשיי כתיבה וקשיים בתפקודים ניהוליים.</p>
</div></section>
<div class="wrap">
<div class="btns"><a class="btn pri" href="appendix.html">📘 נספח מערכי השיעור המלאים</a>
<a class="btn" href="sources.html">📄 המערכים המקוריים</a></div>
{t_html}</div>"""
open(os.path.join(U,"teacher.html"),"w",encoding="utf-8").write(
    shell("אזור המורה · מדריך התאמות",teacher,2,"teacher"))

appendix=f"""<div class="wrap" style="padding-top:30px">
<div class="btns"><a class="btn" href="teacher.html">→ חזרה למדריך ההתאמות</a></div>
{a_html}</div>"""
open(os.path.join(U,"appendix.html"),"w",encoding="utf-8").write(
    shell("נספח מערכי השיעור המלאים",appendix,2,"teacher"))

# ── דף מקורות ────────────────────────────────────────────
plans="".join(f'<li><a href="{MEYDA}/{MEYDA_FILE.format(n=n)}" target="_blank" rel="noopener">'
              f'מערך שיעור {n} — {t} ↗</a></li>'
              for n,t,_,_,_,_ in LESSONS)
sources=f"""<section class="hero"><div class="wrap">
<span class="eyebrow">מקורות</span><h1>החומרים שהערכה מבוססת עליהם</h1>
<p class="sub">מערכי השיעור המקוריים של היחידה — לצד הערת זכויות על חומרים שלא נכללו.</p>
</div></section>
<div class="wrap">
<h2>מערכי השיעור המקוריים</h2>
<p>המערכים הם חלק מ<b>"שבילי מורשת"</b> של המזכירות הפדגוגית במשרד החינוך. הקישורים מובילים ישירות לקבצים באתר משרד החינוך, כך שתמיד תגיעו לגרסה העדכנית — ואין באתר הזה עותקים שמתיישנים.</p>
<ul class="files">{plans}</ul>
<h2>מה לא נכלל בערכה, ולמה</h2>
<table><tr><th>פריט</th><th>סיבה</th><th>מה לעשות</th></tr>
<tr><td>מילות השירים "כאן" ו"שלום לך ארץ נהדרת" במלואן</td><td>זכויות יוצרים</td><td>להביא מהמקור המורשה</td></tr>
<tr><td>מפת אוגנדה</td><td>זכויות תמונה</td><td>אטלס בית ספר או מקור מורשה</td></tr>
<tr><td>הטקסטים המלאים של עמוס עוז ותמיר היימן</td><td>זכויות יוצרים</td><td>מוצגים בתקציר; להביא את המקור לקריאה</td></tr></table>
<div class="note"><b>יש לך קישורים למקורות?</b> אפשר להחליף את הפריטים שבטבלה בקישורים חיצוניים —
המבנה של האתר מוכן לכך.</div>
</div>"""
open(os.path.join(U,"sources.html"),"w",encoding="utf-8").write(
    shell("מקורות · מערכי השיעור המקוריים",sources,2,"sources"))

open(os.path.join(ROOT,".nojekyll"),"w").write("")
print("site built")
