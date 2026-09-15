import os, json, re
exec(open(__import__('os').path.join(__import__('os').path.dirname(__file__),'legal.py')).read().split("pages = {")[0])  # reuse mark(), CSS, page() and legal texts
EXTRA_CSS = '''
.lang{font-size:13px;letter-spacing:.06em;text-transform:uppercase}
.hero2{display:grid;grid-template-columns:1.1fr .9fr;gap:36px;align-items:center;padding:48px 0 24px}
@media (max-width:720px){.hero2{grid-template-columns:1fr}.phone-wrap{justify-content:center}}
.cta{display:inline-block;background:var(--ember);color:var(--ink);font-weight:700;font-size:16px;padding:14px 26px;border-radius:999px;text-decoration:none;box-shadow:0 2px 0 #3A2E24}.cta:hover{background:#C2440F;color:var(--ink)}
.cta2{display:inline-block;border:1.5px solid var(--cream2);color:var(--cream);font-weight:700;font-size:15px;padding:12px 22px;border-radius:999px;text-decoration:none;margin-left:10px}.cta2:hover{border-color:var(--cream);color:var(--cream)}
.phone-wrap{display:flex;justify-content:flex-end}
.phone{width:300px;height:620px;background:var(--ink);border:1px solid var(--border);border-radius:36px;padding:44px 18px 22px;box-sizing:border-box;display:flex;flex-direction:column;gap:12px;box-shadow:0 30px 60px rgba(0,0,0,.5)}
.phone .lockup .word{font-size:11px}
.phone .slogan{font-family:"Big Shoulders Display","Arial Narrow",sans-serif;font-weight:800;font-size:34px;line-height:.95;color:var(--cream);margin-top:8px}
.phone .q{font-weight:700;font-size:14px;color:var(--cream)}
.phone .pill{height:42px;border-radius:999px;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:13px}
.phone .p1{background:var(--ember);color:var(--ink);box-shadow:0 2px 0 #3A2E24}.phone .p2{border:1.5px solid var(--muted);color:var(--cream)}
.phone .eyebrow{font-size:10px;margin-top:6px}
.phone .card{padding:12px;display:flex;gap:10px;align-items:center}.phone .card .win{width:44px;height:44px;border-radius:50%;border:2px solid var(--gold);display:flex;align-items:center;justify-content:center;flex:none}.phone .card .win i{width:34px;height:34px;border-radius:50%;background:var(--tobacco);display:block}
.phone .card .t1{font-weight:700;font-size:11px;letter-spacing:.04em;text-transform:uppercase;color:var(--cream)}.phone .card .t2{font-family:"Big Shoulders Display",sans-serif;font-weight:800;font-size:15px;text-transform:uppercase;color:var(--cream);line-height:1}
.phone .prog{display:flex;align-items:center;margin-top:5px}.phone .prog .a{flex:4;height:3px;background:#B9B2A6;border-radius:2px}.phone .prog .e{width:7px;height:7px;border-radius:50%;background:var(--ember);box-shadow:0 0 8px var(--ember)}.phone .prog .b{flex:6;height:5px;background:var(--tobacco);border-radius:3px}
.phone .tabs{margin-top:auto;border-top:1px solid var(--border);padding-top:10px;display:flex;justify-content:space-around;font-size:10px;color:var(--cream2)}.phone .tabs span{display:flex;flex-direction:column;align-items:center;gap:3px}
.steps{counter-reset:s}.steps .card{position:relative;padding-left:56px}.steps .card::before{counter-increment:s;content:counter(s);position:absolute;left:18px;top:16px;font-family:"Big Shoulders Display",sans-serif;font-weight:800;font-size:28px;color:var(--gold);line-height:1}
.stories{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:14px;margin:8px 0 10px}
.story{background:var(--cedar);border-radius:4px;padding:16px;box-shadow:0 2px 0 #3A2E24;display:flex;flex-direction:column;gap:6px}
.story .brand{font-weight:700;font-size:12px;letter-spacing:.04em;text-transform:uppercase;color:var(--cream)}
.story h3{margin:0;color:var(--cream);font-size:19px}.story p{margin:0;font-size:14px}.story .m{font-size:12px;color:var(--muted);margin-top:auto;padding-top:6px}
.not{list-style:none;padding:0;margin:0}.not li{padding-left:22px;position:relative}.not li::before{content:"";position:absolute;left:0;top:11px;width:10px;height:1.5px;background:var(--gold)}
'''
CSS2 = CSS + EXTRA_CSS
def shell(lang, title, desc, body, alt_href, alt_label, nav):
    root = '../' if lang=='ru' else ''
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="{root}favicon.svg" type="image/svg+xml">
<link rel="alternate" hreflang="en" href="https://cigartale.app/"><link rel="alternate" hreflang="ru" href="https://cigartale.app/ru/">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:url" content="https://cigartale.app/{'ru/' if lang=='ru' else ''}"><meta property="og:type" content="website">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Josefin+Sans:wght@300&family=Big+Shoulders+Display:wght@800&family=Karla:wght@400;700&display=swap">
<style>{CSS2}</style>
</head>
<body>
<div class="wrap">
<header class="top">
  <a class="lockup" href="{root}">{mark(26,'#F1E8D6')}<span class="word">cigartale</span></a>
  <nav>{nav}<a class="lang" href="{alt_href}">{alt_label}</a></nav>
</header>
{body}
<footer>
  <span>&copy; 2026 CigarTale</span><a href="{root}privacy.html">Privacy Policy</a><a href="{root}terms.html">Terms of Use</a><a href="{root}support.html">Support</a><a href="mailto:hello@cigartale.app">hello@cigartale.app</a><span>{'Для взрослых от 18 лет. CigarTale не продаёт табак.' if lang=='ru' else 'For adults 18 and over. CigarTale does not sell tobacco.'}</span>
</footer>
</div>
</body>
</html>
'''
CATALOG = '/Users/maximmotin/cigartale-build/scripts/catalog/dubai-pilot.json'  # app repository checkout
cat = json.load(open(CATALOG))
def stories(lang):
    out=[]
    for e in cat:
        s=[x for x in e['stories'] if x['languageCode']==lang][0]
        mins=round(s['durationSeconds']/60)
        region={'Vuelta Abajo':'Vuelta Abajo, Cuba','Dominican Republic':'Dominican Republic','Estelí':'Estelí, Nicaragua','San Andrés':'San Andrés, Mexico'}[e['cigar']['region']]
        if lang=='ru': region={'Vuelta Abajo, Cuba':'Вуэльта-Абахо, Куба','Dominican Republic':'Доминиканская Республика','Estelí, Nicaragua':'Эстели, Никарагуа','San Andrés, Mexico':'Сан-Андрес, Мексика'}[region]
        m=f'{region} · {"около" if lang=="ru" else "about"} {mins} {"мин" if lang=="ru" else "min"}'
        out.append(f'<div class="story"><span class="brand">{e["brand"]["name"]} · {e["cigar"]["name"]}</span><h3>{s["title"]}</h3><p>{s["subtitle"]}</p><span class="m">{m}</span></div>')
    return '\n'.join(out)
def phone(lang):
    if lang=='ru': slogan,q,b1,b2,cont,brand,title,left,tabs='У каждой сигары есть история.','Какая сигара у вас в руке?','Сканировать бант','Найти по названию','Продолжить','Cohiba','Шестнадцать лет только в подарок','осталось 4 мин · Сигарный мастер',('Главная','Хьюмидор','Профиль')
    else: slogan,q,b1,b2,cont,brand,title,left,tabs='Every cigar has a story.','Which cigar is in your hand?','Scan a band','Search by name','Continue listening','Cohiba','Sixteen years as a gift','4 min left · Cigar master',('Home','Humidor','Profile')
    return f'''<div class="phone-wrap"><div class="phone" aria-hidden="true">
  <span class="lockup">{mark(20,'#F1E8D6')}<span class="word">cigartale</span></span>
  <div class="slogan">{slogan}</div><div class="q">{q}</div>
  <div class="pill p1">{b1}</div><div class="pill p2">{b2}</div>
  <span class="eyebrow">{cont}</span>
  <div class="card"><div class="win"><i></i></div><div style="flex:1"><div class="t1">{brand}</div><div class="t2">{title}</div><div class="prog"><span class="a"></span><span class="e"></span><span class="b"></span></div><div style="font-size:10px;color:var(--cream2);margin-top:3px">{left}</div></div></div>
  <div class="tabs"><span>{mark(18,'#C9A86A')}{tabs[0]}</span><span><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#BDB09B" stroke-width="1.75"><rect x="3" y="8" width="18" height="12" rx="1"/><path d="M3 11h18M12 11v9M5 8l1.5-3h11L19 8"/></svg>{tabs[1]}</span><span><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#BDB09B" stroke-width="1.75"><circle cx="12" cy="8" r="3.5"/><path d="M5 20a7 7 0 0 1 14 0"/></svg>{tabs[2]}</span></div>
</div></div>'''
EN = dict(
 nav='<a href="#how">How it works</a><a href="#stories">Stories</a><a href="support.html">Support</a>',
 eyebrow='An audio companion for cigar lovers', h1='Every cigar has a story.',
 lead='Point the camera at the band, or type the name, and a cigar master tells you where the leaf was grown, who rolled it and how the line came to be. About nine minutes a cigar.',
 cta='Request an invite', cta_href='mailto:hello@cigartale.app?subject=CigarTale%20pilot%20invite', cta2='How it works', meta='Private pilot in Dubai, iPhone first. English and Russian. For adults 18 and over.',
 how='How an evening goes',
 steps=[('Scan the band','Frame the band of the cigar in your hand. The app reads the printed text and finds the line in our catalogue. If we do not know it yet, search by name or ask us to record it.'),('Press play','A free teaser, then the full story with chapters: the place, the people, how it is made, the tradition. It keeps playing with the screen locked, so the phone goes back in the pocket.'),('Keep it','Save the cigar with its size to your Humidor, rate it out of ten, and pick the story up where you left it, on any device.')],
 stories_h='Eleven stories to start', stories_p='Seven Cuban lines from Vuelta Abajo, one Dominican, one Nicaraguan, one Mexican, and one Cuban brand that began as a diplomatic gift. Written from published sources, with a fact table behind every claim, reviewed by a cigar master. More lines are added as the pilot goes.',
 not_h='What CigarTale is not',
 nots=['Not a shop. No prices, no retailers, no store locator. Stories are history and craft.','Not a verdict. Recognition finds the brand and line so the right story plays; it never claims a cigar is genuine or counterfeit.','Not for minors. The app asks for an 18+ confirmation before anything else.','Not a screen to stare at. Press play, lock the phone, enjoy the company.'],
 contact_h='Get in touch', contact_p='For an invite to the pilot, a story request or anything else: <a href="mailto:hello@cigartale.app">hello@cigartale.app</a>.',
 title='CigarTale', desc='Every cigar has a story. CigarTale is an audio companion that recognises a cigar band and tells the history and craft behind the cigar. For adults 18 and over.')
RU = dict(
 nav='<a href="#how">Как это работает</a><a href="#stories">Истории</a><a href="../support.html">Поддержка</a>',
 eyebrow='Аудиоспутник для тех, кто любит сигары', h1='У каждой сигары есть история.',
 lead='Наведите камеру на бант или введите название, и сигарный мастер расскажет, где рос лист, кто крутил сигару и как появилась линия. Примерно девять минут на сигару.',
 cta='Попросить приглашение', cta_href='mailto:hello@cigartale.app?subject=CigarTale%20pilot%20invite', cta2='Как это работает', meta='Закрытый пилот в Дубае, сначала iPhone. Английский и русский. Для взрослых от 18 лет.',
 how='Как проходит вечер',
 steps=[('Сканируйте бант','Возьмите сигару в кадр так, чтобы был виден бант. Приложение прочитает надписи и найдёт линию в каталоге. Если её ещё нет, найдите по названию или попросите нас записать историю.'),('Нажмите Play','Бесплатный тизер, затем полная история по главам: место, люди, производство, традиция. Она играет с заблокированным экраном, телефон можно убрать в карман.'),('Сохраните','Положите сигару с её размером в хьюмидор, поставьте оценку по десятибалльной шкале и продолжите историю с того же места на любом устройстве.')],
 stories_h='Одиннадцать историй для начала', stories_p='Семь кубинских линий из Вуэльта-Абахо, одна доминиканская, одна никарагуанская, одна мексиканская и одна кубинская марка, начинавшаяся как дипломатический подарок. Написаны по опубликованным источникам, за каждым утверждением стоит таблица фактов, тексты проверяет сигарный мастер. Новые линии добавляются по ходу пилота.',
 not_h='Чем CigarTale не является',
 nots=['Не магазин. Ни цен, ни продавцов, ни карты магазинов. Истории про историю и ремесло.','Не экспертиза. Распознавание находит марку и линию, чтобы включить нужную историю; оно никогда не утверждает, что сигара подлинная или поддельная.','Не для несовершеннолетних. Первым делом приложение просит подтвердить 18+.','Не экран, в который надо смотреть. Нажмите Play, заблокируйте телефон, наслаждайтесь компанией.'],
 contact_h='Связаться', contact_p='За приглашением в пилот, с просьбой записать историю или по любому другому вопросу: <a href="mailto:hello@cigartale.app">hello@cigartale.app</a>.',
 title='CigarTale', desc='У каждой сигары есть история. CigarTale распознаёт бант сигары и рассказывает историю и ремесло, стоящие за ней. Для взрослых от 18 лет.')
def landing(lang, T):
    steps=''.join(f'<div class="card"><h3>{a}</h3><p>{b}</p></div>' for a,b in T['steps'])
    nots=''.join(f'<li>{x}</li>' for x in T['nots'])
    body=f'''
<section class="hero2">
  <div>
    <span class="eyebrow" style="display:block;margin-bottom:16px">{T['eyebrow']}</span>
    <h1>{T['h1']}</h1>
    <p class="lead">{T['lead']}</p>
    <p style="margin:24px 0 12px"><a class="cta" href="{T['cta_href']}">{T['cta']}</a><a class="cta2" href="#how">{T['cta2']}</a></p>
    <p class="meta">{T['meta']}</p>
  </div>
  {phone(lang)}
</section>
<div class="band"><i></i><b></b><i></i></div>
<h2 id="how">{T['how']}</h2>
<div class="grid steps">{steps}</div>
<h2 id="stories">{T['stories_h']}</h2>
<p>{T['stories_p']}</p>
<div class="stories">{stories(lang)}</div>
<h2>{T['not_h']}</h2>
<ul class="not">{nots}</ul>
<h2>{T['contact_h']}</h2>
<p>{T['contact_p']}</p>
'''
    return shell(lang, T['title'], T['desc'], body, ('./' if lang=='ru' else 'ru/'), ('EN' if lang=='ru' else 'RU'), T['nav'])
open('index.html','w').write(landing('en', EN))
os.makedirs('ru', exist_ok=True); open('ru/index.html','w').write(landing('ru', RU))
print('landing ok', len(open('index.html').read())//1024, 'KB')
