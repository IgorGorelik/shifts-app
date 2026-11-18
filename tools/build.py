#!/usr/bin/env python3
"""Builds the app's public pages (about, privacy, terms) in three languages into the repository root.

Run: python3 tools/build.py   (site.css, site.js and the icons are edited by hand)
"""
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
ISSUES = "https://github.com/IgorGorelik/shifts-app/issues"
POLICY = "https://developers.google.com/terms/api-services-user-data-policy"
PERMS = "https://myaccount.google.com/permissions"
DATE = {"en": "18 November 2026", "he": "18 בנובמבר 2026", "ru": "18 ноября 2026 г."}

NAV = [
    ("index.html", "./", {"en": "About", "he": "אודות", "ru": "О приложении"}),
    ("privacy.html", "privacy.html", {"en": "Privacy", "he": "פרטיות", "ru": "Конфиденциальность"}),
    ("terms.html", "terms.html", {"en": "Terms", "he": "תנאי שימוש", "ru": "Условия"}),
]
NAME = {"en": "Shifts", "he": "משמרות", "ru": "Смены"}
FOOT = {
    "en": "An independent project made by a volunteer. Not an official app of the Israel Police or the Civil Guard.",
    "he": "פרויקט עצמאי שפיתח מתנדב. זו לא אפליקציה רשמית של משטרת ישראל או של המשמר האזרחי.",
    "ru": "Независимый проект добровольца. Это не официальное приложение полиции Израиля или Гражданской охраны.",
}
CONTACT = {"en": "Contact: GitHub Issues", "he": "יצירת קשר: GitHub Issues", "ru": "Связь: GitHub Issues"}


def attrs(d):
    return " ".join(f'data-{k}="{v}"' for k, v in d.items())


def page(file, titles, sections, description):
    current = ' aria-current="page"'
    nav = "\n    ".join(
        f'<a href="{href}" data-page="{href}"{current if f == file else ""} {attrs(t)}>{t["en"]}</a>'
        for f, href, t in NAV
    )
    body = "\n".join(
        f'<section lang="{l}" dir="{"rtl" if l == "he" else "ltr"}" data-title="{titles[l]}">\n{sections[l].strip()}\n</section>'
        for l in ("en", "he", "ru")
    )
    return f"""<!doctype html>
<html lang="en" dir="ltr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titles["en"]}</title>
<meta name="description" content="{description}">
<link rel="icon" href="favicon.png" type="image/png">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="stylesheet" href="site.css">
</head>
<body>
<header class="top"><div class="wrap">
  <a class="brand" href="./" data-page="./"><img src="favicon.png" alt="" width="28" height="28"><span {attrs(NAME)}>Shifts</span></a>
  <nav class="pages">
    {nav}
  </nav>
  <div class="langs" role="group" aria-label="Language">
    <button type="button" data-lang="en">EN</button>
    <button type="button" data-lang="he" lang="he">עב</button>
    <button type="button" data-lang="ru" lang="ru">RU</button>
  </div>
</div></header>
<main class="wrap">
{body}
</main>
<footer><div class="wrap">
  <p {attrs(FOOT)}>{FOOT["en"]}</p>
  <p><a href="{ISSUES}" {attrs(CONTACT)}>{CONTACT["en"]}</a></p>
</div></footer>
<script src="site.js"></script>
</body>
</html>
"""


# ---------------------------------------------------------------- about

ABOUT = {
"en": f"""
<p class="label">iPhone · Apple Watch</p>
<div class="hero">
  <img src="icon.png" alt="Shifts app icon" width="84" height="84">
  <div><h1>Shifts</h1><p class="names">Shifts · <span lang="he">משמרות</span> · <span lang="ru">Смены</span></p></div>
</div>
<div class="bars"><i></i><i></i><i></i></div>
<p class="lead">The shift roster in your pocket: an iPhone and Apple Watch app for a volunteer team that keeps its shift schedule in a Google Sheet.</p>

<h2>What it does</h2>
<ul>
  <li>Shows your upcoming shifts and who is on each one with you, read from your team's Google Sheet.</li>
  <li>Shows the shifts that still need people.</li>
  <li>Keeps your Google Calendar up to date: after you confirm, it adds, moves and removes your shift events, with the guests you choose.</li>
  <li>Tells you when your shifts change in the sheet.</li>
  <li>Widgets, a Live Activity during the shift, an Apple Watch app and watch face complications.</li>
  <li>In English, Hebrew and Russian.</li>
</ul>

<h2>How it uses your Google data</h2>
<div class="box">
  <p>You sign in with your Google account, and the app asks for:</p>
  <ul>
    <li><strong>Your email address</strong> — to show which account is signed in.</li>
    <li><strong>Google Sheets, read-only</strong> — to read the roster from the one sheet whose link you give it. The app never changes the sheet.</li>
    <li><strong>Google Calendar events</strong> — to find its shift events in your calendar, and to add, move, rename and remove them after you confirm.</li>
  </ul>
  <p>Everything stays on your iPhone and Apple Watch. The app has no servers, no analytics and no ads, and the developer never receives your data. The details are in the <a href="privacy.html" data-page="privacy.html">Privacy Policy</a>.</p>
</div>

<div class="cta">
  <a href="privacy.html" data-page="privacy.html">Privacy Policy</a>
  <a href="terms.html" data-page="terms.html">Terms of Use</a>
  <a href="{ISSUES}">Contact</a>
</div>
""",
"he": f"""
<p class="label">iPhone · Apple Watch</p>
<div class="hero">
  <img src="icon.png" alt="סמל האפליקציה משמרות" width="84" height="84">
  <div><h1>משמרות</h1><p class="names"><span lang="en">Shifts</span> · משמרות · <span lang="ru">Смены</span></p></div>
</div>
<div class="bars"><i></i><i></i><i></i></div>
<p class="lead">סידור המשמרות בכיס: אפליקציה לאייפון ול־Apple Watch בשביל צוות מתנדבים שמנהל את סידור המשמרות בגיליון Google.</p>

<h2>מה היא עושה</h2>
<ul>
  <li>מציגה את המשמרות הקרובות שלכם ומי איתכם בכל משמרת, מתוך גיליון Google של הצוות.</li>
  <li>מציגה את המשמרות שעדיין חסרים בהן אנשים.</li>
  <li>שומרת על יומן Google שלכם מעודכן: אחרי שאישרתם, היא מוסיפה, מזיזה ומוחקת את אירועי המשמרת שלכם, עם האורחים שבחרתם.</li>
  <li>מודיעה לכם כשהמשמרות שלכם משתנות בגיליון.</li>
  <li>ווידג׳טים, Live Activity בזמן המשמרת, אפליקציה ל־Apple Watch ותצוגות על פני השעון.</li>
  <li>בעברית, באנגלית וברוסית.</li>
</ul>

<h2>איך היא משתמשת בנתוני Google שלכם</h2>
<div class="box">
  <p>מתחברים עם חשבון Google, והאפליקציה מבקשת:</p>
  <ul>
    <li><strong>את כתובת האימייל שלכם</strong> — כדי להציג באיזה חשבון התחברתם.</li>
    <li><strong>Google Sheets, קריאה בלבד</strong> — כדי לקרוא את הסידור מהגיליון היחיד שאת הקישור אליו נתתם לה. האפליקציה אף פעם לא משנה את הגיליון.</li>
    <li><strong>אירועים ביומן Google</strong> — כדי למצוא את אירועי המשמרת שלה ביומן שלכם, ולהוסיף, להזיז, לשנות שם ולמחוק אותם אחרי שאישרתם.</li>
  </ul>
  <p>הכול נשאר באייפון וב־Apple Watch שלכם. לאפליקציה אין שרתים, אין ניתוח נתוני שימוש ואין פרסומות, והמפתח אף פעם לא מקבל את הנתונים שלכם. הפרטים ב<a href="privacy.html" data-page="privacy.html">מדיניות הפרטיות</a>.</p>
</div>

<div class="cta">
  <a href="privacy.html" data-page="privacy.html">מדיניות פרטיות</a>
  <a href="terms.html" data-page="terms.html">תנאי שימוש</a>
  <a href="{ISSUES}">יצירת קשר</a>
</div>
""",
"ru": f"""
<p class="label">iPhone · Apple Watch</p>
<div class="hero">
  <img src="icon.png" alt="Значок приложения «Смены»" width="84" height="84">
  <div><h1>Смены</h1><p class="names"><span lang="en">Shifts</span> · <span lang="he">משמרות</span> · Смены</p></div>
</div>
<div class="bars"><i></i><i></i><i></i></div>
<p class="lead">Расписание смен в кармане: приложение для iPhone и Apple Watch для команды добровольцев, которая ведёт расписание смен в Google Таблице.</p>

<h2>Что оно умеет</h2>
<ul>
  <li>Показывает ваши ближайшие смены и кто с вами в каждой из них — по Google Таблице команды.</li>
  <li>Показывает смены, где ещё нужны люди.</li>
  <li>Поддерживает ваш Google Календарь в актуальном виде: после вашего подтверждения добавляет, переносит и удаляет события ваших смен — с теми гостями, которых вы выбрали.</li>
  <li>Сообщает, когда ваши смены меняются в таблице.</li>
  <li>Виджеты, Live Activity во время смены, приложение для Apple Watch и усложнения циферблата.</li>
  <li>На русском, иврите и английском.</li>
</ul>

<h2>Как приложение использует ваши данные Google</h2>
<div class="box">
  <p>Вы входите через свой аккаунт Google, и приложение просит:</p>
  <ul>
    <li><strong>Адрес вашей почты</strong> — чтобы показать, в какой аккаунт выполнен вход.</li>
    <li><strong>Google Таблицы, только чтение</strong> — чтобы читать расписание из той единственной таблицы, ссылку на которую вы ему дали. Приложение никогда не меняет таблицу.</li>
    <li><strong>События Google Календаря</strong> — чтобы находить свои события смен в вашем календаре и после вашего подтверждения добавлять, переносить, переименовывать и удалять их.</li>
  </ul>
  <p>Всё остаётся на вашем iPhone и Apple Watch. У приложения нет серверов, аналитики и рекламы, и разработчик никогда не получает ваши данные. Подробности — в <a href="privacy.html" data-page="privacy.html">Политике конфиденциальности</a>.</p>
</div>

<div class="cta">
  <a href="privacy.html" data-page="privacy.html">Политика конфиденциальности</a>
  <a href="terms.html" data-page="terms.html">Условия использования</a>
  <a href="{ISSUES}">Связь</a>
</div>
""",
}

# ---------------------------------------------------------------- privacy

PRIVACY = {
"en": f"""
<p class="label">Shifts</p>
<h1>Privacy Policy</h1>
<div class="bars"><i></i><i></i><i></i></div>
<p class="date">Effective {DATE["en"]}</p>

<p>Shifts (<span lang="he">משמרות</span> · <span lang="ru">Смены</span>) is a free iPhone and Apple Watch app. It shows a volunteer team's shift roster from a Google Sheet and can put your own shifts into your Google Calendar. It is an independent app made by a volunteer; it is not an official app of the Israel Police or of the Civil Guard (<span lang="he">משמר אזרחי</span>).</p>
<div class="box"><p><strong>In short:</strong> the app has no servers, no accounts of its own, no analytics and no ads. Your data goes only between your own devices and Google.</p></div>

<h2>What the app accesses, and why</h2>
<p>When you sign in with Google, you allow the app:</p>
<ul>
  <li><strong>Your Google account email address</strong> (<code>openid</code>, <code>email</code>) — only to show which account is signed in.</li>
  <li><strong>Read-only access to Google Sheets</strong> (<code>spreadsheets.readonly</code>). The app reads only the spreadsheet whose link you paste into it, to show the roster: your shifts, who is on each shift, and which shifts still need people. It cannot change any spreadsheet and does not.</li>
  <li><strong>Your Google Calendar events</strong> (<code>calendar.events</code>). The app reads the events in your primary calendar for the coming weeks, to find the shift events it created (by their name) and to suggest a name for them. After you confirm, it creates, moves, renames and deletes your shift events in your primary calendar. It does not change your other events.</li>
</ul>
<p>If you add guests to your shift events, their names and email addresses — typed in by you or picked from your Contacts — are kept in the app and sent to Google Calendar as the events' guests; Google Calendar then sends them the invitations and updates. The app uses the system contact picker: it gets only the contact you pick, not your contact list.</p>

<h2>Where your data is kept</h2>
<ul>
  <li><strong>On your iPhone:</strong> your Google sign-in tokens (in the iOS Keychain), your email address, your settings, your guest list, and the last roster the app read, so that the app and its widgets also work offline.</li>
  <li><strong>On your Apple Watch:</strong> a copy of your upcoming shifts, which your iPhone sends to the watch app and its complications.</li>
  <li><strong>Notifications</strong> about changes in your shifts are made on your iPhone; no server sends them. When iOS allows it, the app reads the sheet in the background to find such changes.</li>
</ul>
<p>The app has no servers. It collects no analytics, does not track you, shows no ads and contains no third-party SDKs. It sends nothing anywhere except to Google's APIs, to do what you asked, and to your own Apple Watch.</p>

<h2>Sharing</h2>
<p>The app does not sell, rent or share your data with anyone. The developer never receives it.</p>

<h2>Google API Services User Data Policy</h2>
<p>Shifts' use and transfer to any other app of information received from Google APIs will adhere to the <a href="{POLICY}">Google API Services User Data Policy</a>, including the Limited Use requirements.</p>
<p>Google user data is used only for the features described above. It is not used for advertising, is not transferred to others, is not used to develop, improve or train AI or machine learning models, and no person reads it.</p>

<h2>Your choices, and deleting your data</h2>
<ul>
  <li><strong>Sign out</strong> in the app's Settings: the app revokes its access at Google and removes the sign-in tokens and your email address from your iPhone.</li>
  <li><strong>Delete the app</strong> to remove all of its data from your iPhone and Apple Watch.</li>
  <li>You can also remove the app's access at any time at <a href="{PERMS}">myaccount.google.com/permissions</a>.</li>
  <li>Shift events the app created stay in your calendar until you delete them, like any other events.</li>
</ul>

<h2>Children</h2>
<p>The app is not directed to children under 13.</p>

<h2>Changes</h2>
<p>If this policy changes, the new version will be published on this page with a new date.</p>

<h2>Contact</h2>
<p>Questions about privacy: open an issue at <a href="{ISSUES}">github.com/IgorGorelik/shifts-app/issues</a>.</p>
""",
"he": f"""
<p class="label">משמרות</p>
<h1>מדיניות פרטיות</h1>
<div class="bars"><i></i><i></i><i></i></div>
<p class="date">בתוקף מ־{DATE["he"]}</p>

<p>משמרות (<span lang="en">Shifts</span> · <span lang="ru">Смены</span>) היא אפליקציה חינמית לאייפון ול־Apple Watch. היא מציגה את סידור המשמרות של צוות מתנדבים מגיליון Google, ויכולה להכניס את המשמרות שלכם ליומן Google שלכם. זו אפליקציה עצמאית שפיתח מתנדב; היא לא אפליקציה רשמית של משטרת ישראל או של המשמר האזרחי.</p>
<div class="box"><p><strong>בקצרה:</strong> לאפליקציה אין שרתים, אין חשבונות משלה, אין ניתוח נתוני שימוש ואין פרסומות. הנתונים שלכם עוברים רק בין המכשירים שלכם לבין Google.</p></div>

<h2>למה האפליקציה ניגשת, ולמה</h2>
<p>כשמתחברים עם Google, מאשרים לאפליקציה:</p>
<ul>
  <li><strong>את כתובת האימייל של חשבון Google שלכם</strong> (<code dir="ltr">openid</code>, <code dir="ltr">email</code>) — רק כדי להציג באיזה חשבון התחברתם.</li>
  <li><strong>גישת קריאה בלבד ל־Google Sheets</strong> (<code dir="ltr">spreadsheets.readonly</code>). האפליקציה קוראת רק את הגיליון שאת הקישור אליו הדבקתם בה, כדי להציג את הסידור: המשמרות שלכם, מי בכל משמרת ובאילו משמרות עדיין חסרים אנשים. היא לא יכולה לשנות גיליונות ולא משנה אותם.</li>
  <li><strong>אירועים ביומן Google שלכם</strong> (<code dir="ltr">calendar.events</code>). האפליקציה קוראת את האירועים ביומן הראשי שלכם לשבועות הקרובים, כדי למצוא את אירועי המשמרת שיצרה (לפי השם שלהם) ולהציע להם שם. אחרי שאישרתם, היא יוצרת, מזיזה, משנה שם ומוחקת את אירועי המשמרת שלכם ביומן הראשי. אירועים אחרים שלכם היא לא משנה.</li>
</ul>
<p>אם מוסיפים אורחים לאירועי המשמרת, השמות וכתובות האימייל שלהם — שהקלדתם או שבחרתם מאנשי הקשר — נשמרים באפליקציה ונשלחים ליומן Google כאורחי האירועים; יומן Google שולח להם את ההזמנות והעדכונים. האפליקציה משתמשת בבוחר אנשי הקשר של המערכת: היא מקבלת רק את איש הקשר שבחרתם, ולא את רשימת אנשי הקשר שלכם.</p>

<h2>איפה הנתונים נשמרים</h2>
<ul>
  <li><strong>באייפון:</strong> אסימוני ההתחברות ל־Google (במחזיק המפתחות של iOS), כתובת האימייל שלכם, ההגדרות שלכם, רשימת האורחים והסידור האחרון שהאפליקציה קראה, כדי שהאפליקציה והווידג׳טים שלה יעבדו גם בלי רשת.</li>
  <li><strong>ב־Apple Watch:</strong> עותק של המשמרות הקרובות שלכם, שהאייפון שולח לאפליקציה בשעון ולתצוגות על פני השעון.</li>
  <li><strong>התראות</strong> על שינויים במשמרות שלכם נוצרות באייפון; אף שרת לא שולח אותן. כש־iOS מאפשרת, האפליקציה קוראת את הגיליון ברקע כדי למצוא שינויים כאלה.</li>
</ul>
<p>לאפליקציה אין שרתים. היא לא אוספת נתוני שימוש, לא עוקבת אחריכם, לא מציגה פרסומות ולא כוללת ערכות פיתוח (SDK) של צד שלישי. היא לא שולחת שום דבר לשום מקום, מלבד לממשקי ה־API של Google — כדי לבצע את מה שביקשתם — ול־Apple Watch שלכם.</p>

<h2>שיתוף</h2>
<p>האפליקציה לא מוכרת, לא משכירה ולא משתפת את הנתונים שלכם עם אף אחד. המפתח אף פעם לא מקבל אותם.</p>

<h2>מדיניות נתוני המשתמשים של Google API</h2>
<p>השימוש של משמרות במידע שהתקבל מממשקי ה־API של Google, וההעברה שלו לכל אפליקציה אחרת, יעמדו ב<a href="{POLICY}">מדיניות נתוני המשתמשים של שירותי Google API</a>, כולל דרישות השימוש המוגבל (Limited Use).</p>
<p>נתוני משתמש מ־Google משמשים רק לתכונות שתוארו למעלה. הם לא משמשים לפרסום, לא מועברים לאחרים, לא משמשים לפיתוח, לשיפור או לאימון של מודלים של בינה מלאכותית או למידת מכונה, ואף אדם לא קורא אותם.</p>

<h2>הבחירות שלכם ומחיקת הנתונים</h2>
<ul>
  <li><strong>התנתקות</strong> בהגדרות האפליקציה: האפליקציה מבטלת את הגישה שלה ב־Google ומוחקת מהאייפון את אסימוני ההתחברות ואת כתובת האימייל שלכם.</li>
  <li><strong>מחיקת האפליקציה</strong> מוחקת את כל הנתונים שלה מהאייפון ומה־Apple Watch.</li>
  <li>אפשר גם לבטל את הגישה של האפליקציה בכל עת בכתובת <a href="{PERMS}" dir="ltr">myaccount.google.com/permissions</a>.</li>
  <li>אירועי משמרת שהאפליקציה יצרה נשארים ביומן עד שמוחקים אותם, כמו כל אירוע אחר.</li>
</ul>

<h2>ילדים</h2>
<p>האפליקציה לא מיועדת לילדים מתחת לגיל 13.</p>

<h2>שינויים</h2>
<p>אם המדיניות תשתנה, הגרסה החדשה תפורסם בדף הזה עם תאריך חדש.</p>

<h2>יצירת קשר</h2>
<p>שאלות על פרטיות: פתחו issue בכתובת <a href="{ISSUES}" dir="ltr">github.com/IgorGorelik/shifts-app/issues</a>.</p>
""",
"ru": f"""
<p class="label">Смены</p>
<h1>Политика конфиденциальности</h1>
<div class="bars"><i></i><i></i><i></i></div>
<p class="date">Действует с {DATE["ru"]}</p>

<p>«Смены» (<span lang="en">Shifts</span> · <span lang="he">משמרות</span>) — бесплатное приложение для iPhone и Apple Watch. Оно показывает расписание смен команды добровольцев из Google Таблицы и может вносить ваши смены в ваш Google Календарь. Это независимое приложение, которое сделал доброволец; это не официальное приложение полиции Израиля или Гражданской охраны (<span lang="he">משמר אזרחי</span>).</p>
<div class="box"><p><strong>Коротко:</strong> у приложения нет серверов, собственных аккаунтов, аналитики и рекламы. Ваши данные передаются только между вашими устройствами и Google.</p></div>

<h2>К чему приложение получает доступ и зачем</h2>
<p>Входя через Google, вы разрешаете приложению:</p>
<ul>
  <li><strong>Адрес почты вашего аккаунта Google</strong> (<code>openid</code>, <code>email</code>) — только чтобы показать, в какой аккаунт выполнен вход.</li>
  <li><strong>Доступ к Google Таблицам только для чтения</strong> (<code>spreadsheets.readonly</code>). Приложение читает только ту таблицу, ссылку на которую вы в него вставили, чтобы показать расписание: ваши смены, кто в каждой смене и где ещё нужны люди. Менять таблицы оно не может и не меняет.</li>
  <li><strong>События вашего Google Календаря</strong> (<code>calendar.events</code>). Приложение читает события основного календаря на ближайшие недели, чтобы найти созданные им события смен (по названию) и предложить для них название. После вашего подтверждения оно создаёт, переносит, переименовывает и удаляет события ваших смен в основном календаре. Другие ваши события оно не меняет.</li>
</ul>
<p>Если вы добавляете гостей в события смен, их имена и адреса почты — введённые вами или выбранные из Контактов — хранятся в приложении и передаются в Google Календарь как гости событий; приглашения и изменения им отправляет Google Календарь. Приложение использует системный выбор контакта: оно получает только выбранный вами контакт, а не вашу адресную книгу.</p>

<h2>Где хранятся данные</h2>
<ul>
  <li><strong>На iPhone:</strong> токены входа в Google (в Связке ключей iOS), адрес вашей почты, ваши настройки, список гостей и последнее прочитанное расписание — чтобы приложение и его виджеты работали и без сети.</li>
  <li><strong>На Apple Watch:</strong> копия ваших ближайших смен, которую iPhone передаёт приложению на часах и усложнениям циферблата.</li>
  <li><strong>Уведомления</strong> об изменениях в ваших сменах создаются на iPhone; никакой сервер их не отправляет. Когда iOS позволяет, приложение в фоне читает таблицу, чтобы найти такие изменения.</li>
</ul>
<p>У приложения нет серверов. Оно не собирает аналитику, не отслеживает вас, не показывает рекламу и не содержит сторонних SDK. Оно ничего никуда не отправляет, кроме API Google — чтобы выполнить то, что вы попросили, — и ваших собственных Apple Watch.</p>

<h2>Передача данных</h2>
<p>Приложение не продаёт, не сдаёт в аренду и никому не передаёт ваши данные. Разработчик никогда их не получает.</p>

<h2>Политика Google в отношении данных пользователей API</h2>
<p>Использование приложением «Смены» информации, полученной от API Google, и её передача любому другому приложению соответствуют <a href="{POLICY}">Политике Google в отношении данных пользователей сервисов API</a> (Google API Services User Data Policy), включая требования ограниченного использования (Limited Use).</p>
<p>Данные пользователя Google используются только для описанных выше функций. Они не используются для рекламы, не передаются другим, не используются для разработки, улучшения или обучения моделей ИИ и машинного обучения, и их не читает ни один человек.</p>

<h2>Ваш выбор и удаление данных</h2>
<ul>
  <li><strong>Выход из аккаунта</strong> в Настройках приложения: приложение отзывает свой доступ в Google и удаляет с iPhone токены входа и адрес вашей почты.</li>
  <li><strong>Удаление приложения</strong> стирает все его данные с iPhone и Apple Watch.</li>
  <li>Отозвать доступ приложения можно и в любой момент на странице <a href="{PERMS}">myaccount.google.com/permissions</a>.</li>
  <li>События смен, созданные приложением, остаются в календаре, пока вы их не удалите, как и любые другие события.</li>
</ul>

<h2>Дети</h2>
<p>Приложение не предназначено для детей младше 13 лет.</p>

<h2>Изменения</h2>
<p>Если политика изменится, новая версия будет опубликована на этой странице с новой датой.</p>

<h2>Связь</h2>
<p>Вопросы о конфиденциальности: создайте issue на <a href="{ISSUES}">github.com/IgorGorelik/shifts-app/issues</a>.</p>
""",
}

# ---------------------------------------------------------------- terms

TERMS = {
"en": f"""
<p class="label">Shifts</p>
<h1>Terms of Use</h1>
<div class="bars"><i></i><i></i><i></i></div>
<p class="date">Effective {DATE["en"]}</p>

<p>By using Shifts you agree to these terms.</p>
<ol>
  <li><strong>The app.</strong> Shifts is a free app that shows a shift roster from a Google Sheet you choose and, if you want, adds your shifts to your Google Calendar. It is an independent volunteer project, not an official app of the Israel Police or the Civil Guard.</li>
  <li><strong>The sheet decides.</strong> The roster in the Google Sheet is the source of truth. The app reads it and can show something wrong — for example, if the sheet's layout changes or its latest changes have not been read yet. Check what matters about your shifts in the sheet or with your coordinator.</li>
  <li><strong>Your part.</strong> Use only a spreadsheet you are allowed to access, and add as guests only people who agree to receive the invitations.</li>
  <li><strong>Google services.</strong> The app works with your Google account through Google's APIs, and your use of Google services is subject to Google's terms. How the app handles your data is described in the <a href="privacy.html" data-page="privacy.html">Privacy Policy</a>.</li>
  <li><strong>No warranty.</strong> The app is provided "as is" and "as available", without warranties of any kind. It may have errors, stop working or change.</li>
  <li><strong>Limitation of liability.</strong> To the extent the law allows, the developer is not liable for any damage or loss from using the app or from being unable to use it, including missed or wrongly shown shifts, calendar events or notifications.</li>
  <li><strong>Changes.</strong> These terms may change; the new version will be published on this page with a new date. Using the app after that means you accept it.</li>
  <li><strong>Contact.</strong> <a href="{ISSUES}">github.com/IgorGorelik/shifts-app/issues</a></li>
</ol>
""",
"he": f"""
<p class="label">משמרות</p>
<h1>תנאי שימוש</h1>
<div class="bars"><i></i><i></i><i></i></div>
<p class="date">בתוקף מ־{DATE["he"]}</p>

<p>השימוש במשמרות מהווה הסכמה לתנאים האלה.</p>
<ol>
  <li><strong>האפליקציה.</strong> משמרות היא אפליקציה חינמית שמציגה סידור משמרות מגיליון Google שבחרתם, ואם תרצו — מוסיפה את המשמרות שלכם ליומן Google שלכם. זה פרויקט התנדבותי עצמאי, ולא אפליקציה רשמית של משטרת ישראל או של המשמר האזרחי.</li>
  <li><strong>הגיליון קובע.</strong> הסידור בגיליון Google הוא המקור הקובע. האפליקציה קוראת אותו ועלולה להציג משהו לא נכון — למשל אם מבנה הגיליון השתנה או שהשינויים האחרונים בו עוד לא נקראו. את מה שחשוב במשמרות שלכם בדקו בגיליון או מול הרכז.</li>
  <li><strong>החלק שלכם.</strong> השתמשו רק בגיליון שמותר לכם לגשת אליו, והוסיפו כאורחים רק אנשים שמסכימים לקבל את ההזמנות.</li>
  <li><strong>שירותי Google.</strong> האפליקציה עובדת עם חשבון Google שלכם דרך ממשקי ה־API של Google, והשימוש שלכם בשירותי Google כפוף לתנאים של Google. איך האפליקציה מטפלת בנתונים שלכם מתואר ב<a href="privacy.html" data-page="privacy.html">מדיניות הפרטיות</a>.</li>
  <li><strong>בלי אחריות.</strong> האפליקציה מסופקת "כמות שהיא" ו"כפי שהיא זמינה", בלי אחריות מכל סוג. ייתכנו בה שגיאות, והיא עלולה להפסיק לעבוד או להשתנות.</li>
  <li><strong>הגבלת אחריות.</strong> במידה המרבית שהחוק מתיר, המפתח לא אחראי לשום נזק או הפסד מהשימוש באפליקציה או מחוסר היכולת להשתמש בה, כולל משמרות שהוחמצו או שהוצגו לא נכון, אירועי יומן או התראות.</li>
  <li><strong>שינויים.</strong> התנאים עשויים להשתנות; הגרסה החדשה תפורסם בדף הזה עם תאריך חדש. שימוש באפליקציה אחרי כן פירושו הסכמה לה.</li>
  <li><strong>יצירת קשר.</strong> <a href="{ISSUES}" dir="ltr">github.com/IgorGorelik/shifts-app/issues</a></li>
</ol>
""",
"ru": f"""
<p class="label">Смены</p>
<h1>Условия использования</h1>
<div class="bars"><i></i><i></i><i></i></div>
<p class="date">Действуют с {DATE["ru"]}</p>

<p>Пользуясь приложением «Смены», вы соглашаетесь с этими условиями.</p>
<ol>
  <li><strong>Приложение.</strong> «Смены» — бесплатное приложение: оно показывает расписание смен из выбранной вами Google Таблицы и, если хотите, вносит ваши смены в ваш Google Календарь. Это независимый проект добровольца, а не официальное приложение полиции Израиля или Гражданской охраны.</li>
  <li><strong>Главное — таблица.</strong> Источник истины — расписание в Google Таблице. Приложение читает его и может показать что-то неверно — например, если изменилось устройство таблицы или последние изменения ещё не прочитаны. Важное о своих сменах проверяйте в таблице или у координатора.</li>
  <li><strong>Ваша часть.</strong> Используйте только таблицу, к которой у вас есть право доступа, и добавляйте в гости только тех, кто согласен получать приглашения.</li>
  <li><strong>Сервисы Google.</strong> Приложение работает с вашим аккаунтом Google через API Google, и пользование сервисами Google регулируется условиями Google. Как приложение обращается с вашими данными, описано в <a href="privacy.html" data-page="privacy.html">Политике конфиденциальности</a>.</li>
  <li><strong>Без гарантий.</strong> Приложение предоставляется «как есть» и «по мере доступности», без каких-либо гарантий. В нём могут быть ошибки, оно может перестать работать или измениться.</li>
  <li><strong>Ограничение ответственности.</strong> В той мере, в какой это допускает закон, разработчик не отвечает за ущерб или убытки от использования приложения или невозможности им воспользоваться, в том числе за пропущенные или неверно показанные смены, события календаря и уведомления.</li>
  <li><strong>Изменения.</strong> Условия могут меняться; новая версия будет опубликована на этой странице с новой датой. Пользуясь приложением после этого, вы её принимаете.</li>
  <li><strong>Связь.</strong> <a href="{ISSUES}">github.com/IgorGorelik/shifts-app/issues</a></li>
</ol>
""",
}

PAGES = [
    ("index.html",
     {"en": "Shifts — shift roster for iPhone and Apple Watch", "he": "משמרות — סידור משמרות לאייפון ול־Apple Watch",
      "ru": "Смены — расписание смен для iPhone и Apple Watch"},
     ABOUT,
     "Shifts: an iPhone and Apple Watch app that shows a volunteer team's shift roster from a Google Sheet and keeps your shifts in Google Calendar."),
    ("privacy.html",
     {"en": "Privacy Policy — Shifts", "he": "מדיניות פרטיות — משמרות", "ru": "Политика конфиденциальности — Смены"},
     PRIVACY,
     "How the Shifts app handles your data: no servers, no analytics; read-only Google Sheets and your shift events in Google Calendar."),
    ("terms.html",
     {"en": "Terms of Use — Shifts", "he": "תנאי שימוש — משמרות", "ru": "Условия использования — Смены"},
     TERMS,
     "Terms of use of the Shifts app."),
]

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for file, titles, sections, desc in PAGES:
        with open(os.path.join(OUT, file), "w", encoding="utf-8") as f:
            f.write(page(file, titles, sections, desc))
        print("wrote", file)
