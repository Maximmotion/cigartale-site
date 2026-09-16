import os
# The generated pages always belong at the repository root, whatever directory this is run from.
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import os
MARK = '''<svg viewBox="0 0 100 100" width="{s}" height="{s}" aria-hidden="true"><g fill="none" stroke="{c}" stroke-width="{sw}" stroke-linecap="round"><rect x="10" y="{y}" width="80" height="{h}" rx="{r}"/><circle cx="50" cy="50" r="11"/>{inner}<line x1="{l1}" y1="50" x2="30" y2="50"/><line x1="70" y1="50" x2="{l2}" y2="50"/></g></svg>'''
def mark(s, c):
    if s >= 120: g=dict(sw=2.6,y=34,h=32,inner='<circle cx="50" cy="50" r="4.5"/>',l1=22,l2=78)
    elif s >= 56: g=dict(sw=3.6,y=33,h=34,inner='<circle cx="50" cy="50" r="4.5"/>',l1=22,l2=78)
    else: g=dict(sw=5,y=30,h=40,inner='',l1=21,l2=79)
    return MARK.format(s=s,c=c,r=g['h']/2,**g)
CSS = '''
:root{--ink:#1B1712;--cedar:#2A211A;--border:#4A3D31;--cream:#F1E8D6;--cream2:#BDB09B;--muted:#8C8072;--ember:#E5521C;--gold:#C9A86A;--tobacco:#9C5A2E}
*{box-sizing:border-box}html{color-scheme:dark}
body{margin:0;background:var(--ink);color:var(--cream);font-family:Karla,"Helvetica Neue",Arial,sans-serif;font-size:17px;line-height:1.55;-webkit-font-smoothing:antialiased}
a{color:var(--gold)}a:hover{color:var(--cream)}
.wrap{max-width:760px;margin:0 auto;padding:0 20px}
header.top{display:flex;align-items:center;justify-content:space-between;padding:22px 0}
.lockup{display:flex;align-items:center;gap:12px;text-decoration:none;color:var(--cream)}
.word{font-family:"Josefin Sans","Gill Sans",sans-serif;font-weight:300;font-size:15px;letter-spacing:.32em;margin-right:-.32em;text-transform:uppercase;line-height:1}
nav{display:flex;flex-wrap:wrap;justify-content:flex-end;gap:8px 18px}nav a{font-weight:700;font-size:14px;white-space:nowrap;text-decoration:none;color:var(--cream2)}nav a:hover{color:var(--cream)}
h1,h2,h3{font-family:"Big Shoulders Display","Arial Narrow",sans-serif;font-weight:800;text-transform:uppercase;line-height:.95;margin:0}
h1{font-size:clamp(40px,8vw,64px)}h2{font-size:28px;margin-top:44px}h3{font-size:20px;margin-top:28px;color:var(--gold)}
p,li{color:var(--cream2)}p{margin:14px 0}li{margin:6px 0}
.lead{font-weight:700;color:var(--cream);font-size:19px}
.eyebrow{font-weight:700;font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--gold)}
.hero{padding:56px 0 40px}.hero .eyebrow{display:block;margin-bottom:18px}
.band{display:flex;align-items:center;gap:10px;margin:36px 0}.band i{flex:1;height:1.5px;background:var(--gold);display:block}.band b{width:6px;height:6px;border-radius:50%;background:var(--ember);display:block}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:14px;margin:8px 0 24px}
.card{background:var(--cedar);border-radius:4px;padding:18px;box-shadow:0 2px 0 #3A2E24}.card h3{margin:0 0 6px;color:var(--cream)}.card p{margin:0;font-size:15px}
.note{border:1.5px dashed var(--cream2);border-radius:2px;padding:6px 10px;display:inline-block;font-weight:700;font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--cream2);transform:rotate(-1.5deg)}
.meta{font-size:14px;color:var(--muted)}
table{border-collapse:collapse;width:100%;font-size:15px;margin:14px 0}th,td{text-align:left;vertical-align:top;padding:8px 10px 8px 0;border-top:1px solid var(--border);color:var(--cream2)}th{color:var(--cream);font-weight:700}
footer{margin-top:64px;padding:28px 0 40px;border-top:1px solid var(--border);display:flex;flex-wrap:wrap;gap:8px 24px;font-size:14px;color:var(--muted)}footer a{color:var(--cream2);text-decoration:none}footer a:hover{color:var(--cream)}
@media (max-width:480px){header.top{flex-wrap:wrap;gap:10px}nav{justify-content:flex-start}}
'''
def page(title, body, desc):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Josefin+Sans:wght@300&family=Big+Shoulders+Display:wght@800&family=Karla:wght@400;700&display=swap">
<style>{CSS}</style>
</head>
<body>
<div class="wrap">
<header class="top">
  <a class="lockup" href="./">{mark(26,'#F1E8D6')}<span class="word">cigartale</span></a>
  <nav><a href="privacy.html">Privacy</a><a href="terms.html">Terms</a><a href="support.html">Support</a></nav>
</header>
{body}
<footer>
  <span>&copy; 2026 CigarTale</span><a href="privacy.html">Privacy Policy</a><a href="terms.html">Terms of Use</a><a href="support.html">Support</a><a href="mailto:hello@cigartale.app">hello@cigartale.app</a><span>For adults 18 and over. CigarTale does not sell tobacco.</span>
</footer>
</div>
</body>
</html>
'''
index = f'''
<section class="hero">
  <div style="margin-bottom:28px">{mark(140,'#C9A86A')}</div>
  <span class="eyebrow">An audio companion for cigar lovers</span>
  <h1>Every cigar has a story.</h1>
  <p class="lead">Point the camera at the band, or type the name, and a cigar master tells you where the leaf was grown, who rolled it and how the line came to be.</p>
  <p class="meta">Coming to iPhone and Android. Pilot in Dubai, in English and Russian. For adults 18 and over.</p>
</section>
<div class="band"><i></i><b></b><i></i></div>
<div class="grid">
  <div class="card"><h3>Scan a band</h3><p>The camera reads the printed band and finds the cigar line in our catalogue. No photo is kept.</p></div>
  <div class="card"><h3>Hear the story</h3><p>A short teaser for free, then a full story of about nine minutes: the place, the people, the making, the tradition.</p></div>
  <div class="card"><h3>Keep your Humidor</h3><p>Save the cigars you loved with their size, rate them, and pick a story up where you left it.</p></div>
</div>
<p>CigarTale is about history and craft. It does not sell tobacco, does not link to shops and does not tell anyone to smoke. Stories are written from published sources and reviewed by a cigar master; nothing in the app claims that a cigar is genuine or counterfeit.</p>
<p class="meta"><span class="note">Stories &middot; Cigar master &middot; 18+</span></p>
'''
privacy = '''
<section class="hero" style="padding-bottom:8px">
  <span class="eyebrow">Effective 15 September 2026</span>
  <h1>Privacy Policy</h1>
  <p class="lead">CigarTale is an audio app about the history and craft of cigars. This policy explains what we collect, why, where it is processed and how to delete it.</p>
  <p class="meta">"CigarTale", "we" and "us" mean the operator of the CigarTale app and of cigartale.app. Contact: <a href="mailto:hello@cigartale.app">hello@cigartale.app</a>.</p>
</section>
<h2>1. Who the app is for</h2>
<p>CigarTale is for adults aged 18 and over. The app asks you to confirm your age before anything else and stores that confirmation on your device only. We do not knowingly collect data from anyone under 18; if you believe a minor has created an account, write to us and we will delete it.</p>
<h2>2. What we collect</h2>
<h3>Without an account</h3>
<ul>
<li><b>Age confirmation</b> and your language choice, stored on the device.</li>
<li><b>Band scans.</b> When you scan a cigar band, the photo is sent to our servers and to our recognition provider to read the printed text. We keep the extracted text (brand, line, size, factory marks), the result and timing of the scan and a random per-install identifier. <b>We do not store the photo.</b></li>
<li><b>Playback.</b> Which story you started, how far you listened, and playback errors, tied to the per-install identifier, so that the app works and we can see which stories people finish.</li>
<li><b>Device and app diagnostics</b> when something breaks: app version, OS version, device model and the error. Crash reporting is provided by Sentry (EU region) when enabled.</li>
</ul>
<h3>With an account</h3>
<p>You can use the whole app as a guest. An account is offered only when you save a cigar to your Humidor or make a purchase. Then we also keep:</p>
<ul>
<li><b>Sign-in identity:</b> your email address, or the identifier and email that Apple or Google provide when you sign in with them. Email sign-in uses a one-time code sent to your address.</li>
<li><b>Your Humidor:</b> the cigars you saved, their size, your 1&ndash;10 rating and dates.</li>
<li><b>Listening progress</b> for full stories, so you can resume on another device.</li>
<li><b>Requests</b> you send for cigars we do not have yet, as text.</li>
<li><b>Push notification token</b> if you allow notifications; you can turn them off in the app or in system settings at any time.</li>
<li><b>Entitlement</b> to full stories: whether you have the paid tier, its source and expiry. Purchases, when available, are made through Apple or Google and handled by RevenueCat; we never see your payment details.</li>
</ul>
<h2>3. Analytics</h2>
<p>We measure how the app is used in aggregate (for example, how many people finish a story) with PostHog, hosted in the EU, when enabled. We do not use session replay, advertising identifiers or third-party advertising SDKs, and we do not sell or share personal data for advertising.</p>
<h2>4. Where your data is processed</h2>
<table>
<tr><th>Purpose</th><th>Provider</th><th>Location</th></tr>
<tr><td>Database, sign-in, audio storage, server functions</td><td>Supabase</td><td>Frankfurt, Germany (EU)</td></tr>
<tr><td>Reading the text on a scanned band</td><td>OpenAI (API)</td><td>United States; the request is not used for model training and the image is not retained by us</td></tr>
<tr><td>Sign-in codes and account email</td><td>Resend</td><td>Tokyo, Japan</td></tr>
<tr><td>Sign in with Apple / Google</td><td>Apple, Google</td><td>Per their policies</td></tr>
<tr><td>Push notifications</td><td>Expo Push Service, Apple, Google</td><td>United States and per platform</td></tr>
<tr><td>Crash reports and usage analytics (when enabled)</td><td>Sentry, PostHog</td><td>EU</td></tr>
<tr><td>Purchases (when available)</td><td>Apple, Google, RevenueCat</td><td>Per their policies</td></tr>
</table>
<p>Providers act on our instructions under their data processing terms. Where data leaves the country you are in, it is protected by those terms and by the safeguards those providers publish.</p>
<h2>5. Why we process it</h2>
<p>To run the app you asked for (recognising a cigar, playing stories, keeping your Humidor), to keep it secure and working, to understand what people listen to so we can make better stories, and to comply with law. Where consent is required, for example for notifications, we ask for it in the app and you can withdraw it at any time.</p>
<h2>6. How long we keep it</h2>
<ul>
<li>Account data: while your account exists.</li>
<li>Scan records: extracted text and outcome are kept for up to 12 months to improve recognition; they never include the photo.</li>
<li>Diagnostics and analytics: up to 12 months.</li>
<li>Backups: up to 30 days after deletion.</li>
</ul>
<h2>7. Your choices and rights</h2>
<ul>
<li><b>Delete your account</b> in the app: Profile &rarr; Delete account. This removes your account, Humidor, progress, requests and push tokens, and anonymises scan and listening records. It cannot be undone.</li>
<li><b>Notifications</b> can be turned off in Profile or in your device settings.</li>
<li><b>Access, correction, portability, objection:</b> write to <a href="mailto:hello@cigartale.app">hello@cigartale.app</a>. We answer within 30 days. If you are in the EU, the UK or another jurisdiction with a data protection authority, you may also complain to that authority.</li>
</ul>
<h2>8. Security</h2>
<p>Data is encrypted in transit and at rest with our providers. Access to personal data inside CigarTale is limited to people who need it to run the service. Audio and personal records are served only through short-lived, signed links.</p>
<h2>9. Changes</h2>
<p>We will post changes here with a new effective date and, for material changes, tell you in the app.</p>
<h2>10. Contact</h2>
<p><a href="mailto:hello@cigartale.app">hello@cigartale.app</a></p>
'''
terms = '''
<section class="hero" style="padding-bottom:8px">
  <span class="eyebrow">Effective 15 September 2026</span>
  <h1>Terms of Use</h1>
  <p class="lead">These terms apply to the CigarTale app and to cigartale.app. By using them you agree to these terms and to our <a href="privacy.html">Privacy Policy</a>.</p>
</section>
<h2>1. Eligibility</h2>
<p>You must be at least 18 years old, or the legal age for tobacco-related content where you live if that is higher, to use CigarTale. By using the app you confirm that you are.</p>
<h2>2. What CigarTale is</h2>
<p>CigarTale is an educational audio service. It identifies a cigar brand and line from a band photo or a search, and plays narrated stories about the history, the region, the people and the craft behind that line. CigarTale <b>does not sell tobacco</b> or any physical goods, does not link to retailers and does not encourage anyone to smoke. Nothing in the app is medical or health advice.</p>
<h2>3. Recognition is not authentication</h2>
<p>Band recognition tells you which brand and line a band most likely belongs to, so that we can play the matching story. It is not a verification of authenticity, provenance or quality, and it can be wrong. Do not rely on it for any purchase, valuation or legal purpose.</p>
<h2>4. Accounts</h2>
<p>You can use most of the app as a guest. An account, created with Apple, Google or an email code, is needed to save cigars to your Humidor or to buy the full stories. Keep your sign-in credentials to yourself; you are responsible for activity on your account. You can delete your account at any time in Profile &rarr; Delete account.</p>
<h2>5. Free and paid content</h2>
<p>Every published story has a free teaser. Full-length stories may require a paid tier, offered as an in-app purchase through Apple or Google under their terms, including their refund rules. Prices, if any, are shown in the store before you buy. During the pilot the paid tier may be switched off and full stories provided free of charge; that is not a promise that they will stay free.</p>
<h2>6. Content and intellectual property</h2>
<p>Stories, audio, text, the CigarTale name and mark, and the app itself belong to CigarTale or its licensors and are protected by copyright and trademark law. You get a personal, non-transferable licence to use them within the app. Do not copy, record, redistribute or make derivative works from the stories, and do not reverse-engineer the app. Brand names of cigars are the property of their owners; their mention in a story means only that the story is about that cigar, not that the owner endorses CigarTale, unless the story says it was reviewed by the brand.</p>
<h2>7. What you send us</h2>
<p>Ratings, cigar requests and messages you send us may be used to improve the catalogue and the app. Do not send anything unlawful, offensive or that you do not have the right to share. We may remove such content and close accounts that misuse the service.</p>
<h2>8. Acceptable use</h2>
<p>Do not use CigarTale to sell or advertise tobacco, to scrape or overload the service, to interfere with other users, or in any way that breaks the law where you are.</p>
<h2>9. Accuracy</h2>
<p>Stories are written from published sources and reviewed by a cigar master, but history is contested and sources disagree. We do our best and correct mistakes when we learn of them; tell us at <a href="mailto:hello@cigartale.app">hello@cigartale.app</a>. The service is provided "as is", without warranties, to the extent the law allows.</p>
<h2>10. Liability</h2>
<p>To the extent permitted by law, CigarTale is not liable for indirect or consequential losses arising from your use of the app, and our total liability to you for any claim is limited to the amount you paid us in the 12 months before the claim. Nothing in these terms limits liability that cannot be limited by law.</p>
<h2>11. Changes and termination</h2>
<p>We may change the app, the catalogue and these terms; material changes will be announced in the app or here with a new effective date. We may suspend or close accounts that breach these terms. You can stop using the app and delete your account at any time.</p>
<h2>12. Governing law</h2>
<p>These terms are governed by the laws of the United Arab Emirates, where the pilot takes place, without prejudice to mandatory consumer protection rules of the country you live in. Disputes will be settled by the competent courts of Dubai, unless your local law gives you the right to go to your own courts.</p>
<h2>13. Contact</h2>
<p><a href="mailto:hello@cigartale.app">hello@cigartale.app</a></p>
'''
support = '''
<section class="hero" style="padding-bottom:8px">
  <span class="eyebrow">We answer within two working days</span>
  <h1>Support</h1>
  <p class="lead">Write to <a href="mailto:hello@cigartale.app">hello@cigartale.app</a>. Tell us your phone model and what you were doing; a screenshot helps.</p>
</section>
<h2>Common questions</h2>
<h3>The band was not recognised</h3>
<p>Fill the frame with the band in good light and hold still for a moment. If the cigar is not in our catalogue yet, use Search by name or Request this cigar; we add lines as the catalogue grows.</p>
<h3>The story stopped when I locked the screen</h3>
<p>Stories keep playing with the screen off. If yours stopped, check that Low Power Mode is off and that the app is allowed to use mobile data, then press Play again. Tell us the phone model if it repeats.</p>
<h3>Sign-in code did not arrive</h3>
<p>Codes come from hello@cigartale.app within a minute; check the spam folder. Each code works for 15 minutes.</p>
<h3>Delete my account</h3>
<p>In the app: Profile &rarr; Delete account. It removes your account and Humidor immediately; see the <a href="privacy.html">Privacy Policy</a> for what is anonymised.</p>
<h3>Where to download</h3>
<p>CigarTale is in beta on iPhone. Install TestFlight from the App Store, then open <a href="https://testflight.apple.com/join/Asy9JG5T">our TestFlight link</a>. Android comes later; write to us and we will tell you when it opens.</p>
'''
pages = {
 'index.html': ('CigarTale', index, 'Every cigar has a story. CigarTale is an audio companion that recognises a cigar band and tells the history and craft behind the cigar. For adults 18 and over.'),
 'privacy.html': ('Privacy Policy · CigarTale', privacy, 'What CigarTale collects, why, where it is processed and how to delete it.'),
 'terms.html': ('Terms of Use · CigarTale', terms, 'Terms of use for the CigarTale app and website.'),
 'support.html': ('Support · CigarTale', support, 'How to reach CigarTale support and answers to common questions.'),
}
for name,(t,b,d) in pages.items(): open(name,'w').write(page(t,b,d))
open('favicon.svg','w').write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><rect width="100" height="100" rx="22" fill="#2A211A"/><svg x="9" y="9" width="82" height="82" viewBox="0 0 100 100">'+mark(40,'#C9A86A').split('>',1)[1].rsplit('</svg>',1)[0]+'</svg></svg>')
open('CNAME','w').write('cigartale.app\n')
open('404.html','w').write(page('Not found · CigarTale','<section class="hero"><h1>Nothing here.</h1><p class="lead">The page moved or never existed. <a href="./">Back to the start.</a></p></section>','Page not found.'))
open('.nojekyll','w').write('')
print('ok', sorted(os.listdir('.')))
