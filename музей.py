HTML = r"""<!DOCTYPE html>
<html lang="uk">
<head>
	<meta charset="UTF-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0" />
	<meta name="theme-color" content="#101918" />
	<title>Галерея «Лінія» — музей сучасного мистецтва</title>
	<style>
		@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap');

		:root {
			--ink: #101918;
			--muted: #78817e;
			--paper: #f3f4f0;
			--blue: #477df4;
			--green: #a7da73;
			--line: rgba(16, 25, 24, .12);
		}

		* { box-sizing: border-box; }
		html { scroll-behavior: smooth; }
		body {
			margin: 0;
			color: var(--ink);
			background: var(--paper);
			font-family: 'DM Sans', sans-serif;
			-webkit-font-smoothing: antialiased;
		}
		a { color: inherit; text-decoration: none; }
		.wrap { width: min(1180px, calc(100% - 64px)); margin: 0 auto; }

		header {
			position: absolute;
			z-index: 3;
			top: 0;
			left: 0;
			width: 100%;
			padding: 27px 0;
			color: white;
		}
		.topbar { display: flex; align-items: center; justify-content: space-between; gap: 24px; }
		.brand { display: inline-flex; align-items: center; gap: 11px; font-size: 15px; font-weight: 700; letter-spacing: .08em; }
		.brand-mark { width: 32px; height: 32px; display: grid; place-items: center; border: 1px solid rgba(255,255,255,.72); border-radius: 50%; font-family: Georgia, serif; font-size: 19px; font-weight: 400; }
		nav { display: flex; gap: 5px; padding: 5px; border: 1px solid rgba(255,255,255,.22); border-radius: 999px; background: rgba(10,18,17,.32); backdrop-filter: blur(12px); }
		nav a { padding: 10px 17px; border-radius: 999px; color: rgba(255,255,255,.66); font-size: 12px; transition: .25s ease; }
		nav a:hover, nav a:focus-visible { color: #fff; background: linear-gradient(110deg, var(--blue), #36ad8a); outline: none; }
		.ticket-link { padding: 11px 18px; border: 1px solid rgba(255,255,255,.65); border-radius: 999px; font-size: 12px; transition: .2s; }
		.ticket-link:hover { color: var(--ink); background: white; }

		.hero {
			position: relative;
			min-height: 690px;
			height: min(820px, 91vh);
			display: flex;
			align-items: center;
			overflow: hidden;
			color: #fff;
			background: #18211f url('https://images.unsplash.com/photo-1579783902614-a3fb3927b6a5?auto=format&fit=crop&w=2200&q=85') center 43% / cover no-repeat;
		}
		.hero::before { content: ''; position: absolute; inset: 0; background: linear-gradient(90deg, rgba(10,17,16,.82) 0%, rgba(10,17,16,.54) 43%, rgba(10,17,16,.08) 100%), linear-gradient(0deg, rgba(10,17,16,.55), transparent 38%); }
		.hero-content { position: relative; z-index: 1; padding-top: 85px; max-width: 700px; }
		.eyebrow { display: flex; align-items: center; gap: 10px; text-transform: uppercase; letter-spacing: .17em; font-size: 10px; font-weight: 700; }
		.eyebrow::before { content: ''; width: 27px; height: 1px; background: var(--green); }
		h1 { margin: 23px 0 19px; font-family: 'Playfair Display', Georgia, serif; font-size: clamp(56px, 8vw, 104px); line-height: .98; font-weight: 500; letter-spacing: -.055em; }
		h1 em { color: var(--green); font-weight: 500; }
		.hero-copy { max-width: 390px; margin: 0; color: rgba(255,255,255,.76); font-size: 15px; line-height: 1.8; }
		.hero-actions { display: flex; align-items: center; gap: 25px; margin-top: 34px; }
		.button { display: inline-flex; align-items: center; gap: 17px; padding: 15px 19px; border-radius: 3px; background: var(--green); color: #10201c; font-size: 12px; font-weight: 700; transition: .2s; }
		.button:hover { background: #c4ee96; transform: translateY(-2px); }
		.text-link { font-size: 12px; color: white; border-bottom: 1px solid rgba(255,255,255,.5); padding-bottom: 5px; }
		.hero-bottom { position: absolute; z-index: 1; bottom: 30px; left: 0; width: 100%; display: flex; justify-content: space-between; align-items: end; color: rgba(255,255,255,.75); font-size: 10px; letter-spacing: .08em; text-transform: uppercase; }
		.hero-bottom span:last-child { display: flex; align-items: center; gap: 9px; }
		.live-dot { width: 7px; height: 7px; border-radius: 50%; background: var(--green); box-shadow: 0 0 12px var(--green); }

		.intro { padding: 106px 0 100px; display: grid; grid-template-columns: 1fr 1fr; gap: 70px; align-items: start; }
		.section-label { color: #78817e; text-transform: uppercase; letter-spacing: .16em; font-size: 10px; font-weight: 700; }
		.intro h2, .section-heading h2, .visit h2 { margin: 17px 0 0; font-family: 'Playfair Display', Georgia, serif; font-size: clamp(37px, 5vw, 58px); font-weight: 500; letter-spacing: -.04em; line-height: 1.08; }
		.intro-copy { max-width: 440px; margin: 36px 0 0; color: #626c68; font-size: 14px; line-height: 1.9; }
		.stats { display: flex; gap: 44px; margin-top: 33px; }
		.stat strong { display: block; font-family: 'Playfair Display', Georgia, serif; font-size: 27px; font-weight: 500; }
		.stat span { display: block; margin-top: 4px; color: var(--muted); font-size: 10px; }

		.news { padding: 84px 0 100px; background: #e9ece8; }
		.section-heading { display: flex; align-items: end; justify-content: space-between; gap: 20px; margin-bottom: 39px; }
		.section-heading h2 { margin-top: 12px; }
		.all-news { margin-bottom: 8px; padding: 0 0 6px; border: 0; border-bottom: 1px solid #929b96; background: none; color: inherit; font: inherit; font-size: 12px; cursor: pointer; }
		.cards { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; }
		.extra-card { display: none; }
		.cards.show-all .extra-card { display: block; }
		.card { min-width: 0; background: var(--paper); transition: transform .25s ease, box-shadow .25s ease; }
		.card:hover { transform: translateY(-5px); box-shadow: 0 18px 38px rgba(20,35,30,.1); }
		.card-image { position: relative; height: 235px; overflow: hidden; background: #cbd2ca; }
		.card-image img { width: 100%; height: 100%; display: block; object-fit: cover; transition: transform .5s ease; }
		.card:hover img { transform: scale(1.04); }
		.tag { position: absolute; top: 15px; left: 15px; padding: 7px 10px; background: rgba(243,244,240,.93); font-size: 9px; text-transform: uppercase; letter-spacing: .1em; }
		.card-body { padding: 22px 23px 25px; }
		.date { color: #89918e; font-size: 10px; }
		.card h3 { margin: 12px 0 11px; font-family: 'Playfair Display', Georgia, serif; font-size: 22px; font-weight: 500; line-height: 1.2; }
		.card p { margin: 0; color: #6e7773; font-size: 12px; line-height: 1.75; }
		.read-more { display: inline-flex; gap: 8px; margin-top: 20px; font-size: 11px; font-weight: 700; }

		.visit { padding: 100px 0; background: #14201e; color: white; }
		.visit-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 70px; align-items: center; }
		.visit .section-label { color: #a4b4ac; }
		.visit h2 { margin-bottom: 27px; }
		.visit-copy { max-width: 420px; color: #aeb9b4; font-size: 13px; line-height: 1.85; }
		.details { display: grid; grid-template-columns: 1fr 1fr; gap: 25px 35px; margin-top: 34px; }
		.detail-label { color: #8d9d96; text-transform: uppercase; letter-spacing: .12em; font-size: 9px; }
		.detail-value { margin-top: 9px; font-size: 13px; line-height: 1.65; }
		.detail-value a { color: var(--green); }
		.map { min-height: 390px; position: relative; overflow: hidden; background: #243531; }
		.map::before { content: ''; position: absolute; inset: 0; opacity: .46; background-image: linear-gradient(32deg, transparent 47%, #668177 48%, #668177 49%, transparent 50%), linear-gradient(112deg, transparent 47%, #668177 48%, #668177 49%, transparent 50%), linear-gradient(0deg, transparent 95%, rgba(185,205,192,.35) 96%); background-size: 150px 140px, 190px 160px, 100% 65px; transform: scale(1.4) rotate(-8deg); }
		.map::after { content: ''; position: absolute; width: 72px; height: 72px; top: 45%; left: 52%; border: 1px solid rgba(167,218,115,.45); border-radius: 50%; background: rgba(167,218,115,.09); transform: translate(-50%,-50%); }
		.pin { position: absolute; z-index: 1; top: 45%; left: 52%; width: 15px; height: 15px; border: 4px solid white; border-radius: 50% 50% 50% 0; background: var(--blue); box-shadow: 0 0 0 7px rgba(71,125,244,.25); transform: translate(-50%,-80%) rotate(-45deg); }
		.map-caption { position: absolute; z-index: 1; bottom: 20px; left: 20px; padding: 12px 15px; background: #f3f4f0; color: var(--ink); font-size: 11px; }

		footer { padding: 25px 0; background: #0e1716; color: #91a09a; font-size: 10px; }
		.footer-row { display: flex; justify-content: space-between; gap: 20px; align-items: center; }
		.footer-brand { color: white; font-weight: 700; letter-spacing: .08em; }
		.social { display: flex; gap: 18px; }
		.social a:hover { color: var(--green); }

		@media (max-width: 760px) {
			.wrap { width: min(100% - 36px, 560px); }
			header { padding: 19px 0; }
			.topbar { flex-wrap: wrap; }
			nav { order: 3; width: 100%; justify-content: center; overflow-x: auto; }
			nav a { padding: 9px 13px; white-space: nowrap; }
			.ticket-link { margin-left: auto; }
			.hero { min-height: 650px; height: 90vh; background-position: 58% center; }
			.hero-content { padding-top: 95px; }
			.hero-bottom { bottom: 20px; }
			.intro, .visit-grid { grid-template-columns: 1fr; gap: 35px; }
			.intro { padding: 74px 0; }
			.intro-copy { margin-top: 0; }
			.news, .visit { padding: 72px 0; }
			.cards { grid-template-columns: 1fr; gap: 16px; }
			.card-image { height: 250px; }
			.visit-grid { gap: 38px; }
			.map { min-height: 320px; }
		}
		@media (max-width: 420px) {
			.brand { font-size: 12px; }
			.brand-mark { width: 28px; height: 28px; }
			.ticket-link { padding: 9px 12px; font-size: 10px; }
			nav { justify-content: flex-start; }
			.hero-actions { gap: 17px; }
			.button { padding: 13px; }
			.details { gap: 22px 15px; }
			.footer-row { flex-wrap: wrap; }
		}
	</style>
</head>
<body>
	<header>
		<div class="wrap topbar">
			<a class="brand" href="#home" aria-label="Галерея Лінія — на головну"><span class="brand-mark">Л</span><span>ГАЛЕРЕЯ «ЛІНІЯ»</span></a>
			<nav aria-label="Головна навігація">
				<a href="#news">Новини</a>
				<a href="#about">Про музей</a>
				<a href="#visit">Як дістатися</a>
				<a href="#hours">Години роботи</a>
			</nav>
			<a class="ticket-link" href="TICKETS_PAGE" target="_blank" rel="noopener">Квитки ↗</a>
		</div>
	</header>

	<main>
		<section class="hero" id="home">
			<div class="wrap hero-content">
				<div class="eyebrow">Музей сучасного мистецтва · Київ</div>
				<h1>Мистецтво<br />бути <em>тут.</em></h1>
				<p class="hero-copy">Місце зустрічі з мистецтвом, яке допомагає побачити знайомий світ по-новому.</p>
				<div class="hero-actions">
					<a class="button" href="PLAN_PAGE" target="_blank" rel="noopener">Спланувати візит <span>↗</span></a>
					<a class="text-link" href="#news">Що відбувається</a>
				</div>
			</div>
			<div class="wrap hero-bottom"><span>Київ · Поділ · з 2014 року</span><span><i class="live-dot"></i> Відкрито сьогодні до 20:00</span></div>
		</section>

		<section class="wrap intro" id="about">
			<div>
				<div class="section-label">Простір для відкриттів</div>
				<h2>Дивитися.<br />Відчувати. Думати.</h2>
			</div>
			<div>
				<p class="intro-copy">«Лінія» — незалежний музей живого мистецтва. Ми збираємо роботи українських митців, створюємо виставки та події, що відкривають нові погляди й об’єднують людей.</p>
				<div class="stats">
					<div class="stat"><strong>12</strong><span>років поруч із мистецтвом</span></div>
					<div class="stat"><strong>4 800+</strong><span>робіт у колекції</span></div>
					<div class="stat"><strong>35</strong><span>виставок щороку</span></div>
				</div>
			</div>
		</section>

		<section class="news" id="news">
			<div class="wrap">
				<div class="section-heading">
					<div><div class="section-label">З життя музею</div><h2>Новини та події</h2></div>
					<button class="all-news" type="button" aria-expanded="false" aria-controls="news-cards">Усі новини ↗</button>
				</div>
				<div class="cards" id="news-cards">
					<article class="card">
						<div class="card-image"><img src="https://images.unsplash.com/photo-1577083552431-6e5fd01aa342?auto=format&fit=crop&w=900&q=80" alt="Яскрава картина на виставці" /><span class="tag">Виставка</span></div>
						<div class="card-body"><div class="date">15 червня — 28 серпня 2025</div><h3>Колір, що пам’ятає</h3><p>Нова виставка про міста, дитинство та кольори, які залишаються з нами.</p><a class="read-more" href="EXHIBITION_PAGE" target="_blank" rel="noopener">Дізнатися більше <span>→</span></a></div>
					</article>
					<article class="card">
						<div class="card-image"><img src="https://images.unsplash.com/photo-1579783901586-d88db74b4fe4?auto=format&fit=crop&w=900&q=80" alt="Відвідувач розглядає картину в музеї" /><span class="tag">Зустріч</span></div>
						<div class="card-body"><div class="date">22 червня 2025 · 16:00</div><h3>Мистецтво без поспіху</h3><p>Екскурсія-розмова з кураторкою виставки. Для тих, хто любить ставити запитання.</p><a class="read-more" href="mailto:hello@liniya.art">Зареєструватися <span>→</span></a></div>
					</article>
					<article class="card">
						<div class="card-image"><img src="https://images.unsplash.com/photo-1578301978693-85fa9c0320b9?auto=format&fit=crop&w=900&q=80" alt="Абстрактний живопис у музейній залі" /><span class="tag">Майстерня</span></div>
						<div class="card-body"><div class="date">Щосуботи · 12:00</div><h3>Власна лінія</h3><p>Творча майстерня для дітей і дорослих. Матеріали та натхнення вже чекають.</p><a class="read-more" href="mailto:hello@liniya.art">Обрати дату <span>→</span></a></div>
					</article>
					<article class="card extra-card">
						<div class="card-image"><img src="https://images.unsplash.com/photo-1579783901586-d88db74b4fe4?auto=format&fit=crop&w=900&q=80" alt="Живописний портрет із музейної колекції" /><span class="tag">Колекція</span></div>
						<div class="card-body"><div class="date">З 5 липня 2025</div><h3>Нове з музейної колекції</h3><p>Добірка робіт українських митців відкриває несподівані історії про наш час.</p><a class="read-more" href="mailto:hello@liniya.art">Дізнатися більше <span>→</span></a></div>
					</article>
					<article class="card extra-card">
						<div class="card-image"><img src="https://images.unsplash.com/photo-1511818966892-d7d671e672a2?auto=format&fit=crop&w=900&q=80" alt="Архітектурні фасади міста для розмови про міські деталі" /><span class="tag">Лекція</span></div>
						<div class="card-body"><div class="date">6 липня 2025 · 17:00</div><h3>Місто в деталях</h3><p>Розмова про те, як архітектура та щоденні маршрути надихають художників.</p><a class="read-more" href="mailto:hello@liniya.art">Зареєструватися <span>→</span></a></div>
					</article>
					<article class="card extra-card">
						<div class="card-image"><img src="https://images.unsplash.com/photo-1513364776144-60967b0f800f?auto=format&fit=crop&w=900&q=80" alt="Людина малює фарбами під час творчої майстерні" /><span class="tag">Для родини</span></div>
						<div class="card-body"><div class="date">Щонеділі · 12:00</div><h3>Недільний арт-день</h3><p>Творча зустріч для всієї родини: досліджуємо кольори, форми та власні ідеї.</p><a class="read-more" href="mailto:hello@liniya.art">Деталі та запис <span>→</span></a></div>
					</article>
				</div>
			</div>
		</section>

		<section class="visit" id="visit">
			<div class="wrap visit-grid">
				<div>
					<div class="section-label">Будемо раді бачити</div>
					<h2>Знайдіть<br />свою дорогу.</h2>
					<p class="visit-copy">Ми в самому серці Подолу — за кілька хвилин пішки від метро «Контрактова площа». Завітайте на виставку або просто на каву в музейному дворику.</p>
					<div class="details">
						<div><div class="detail-label">Адреса</div><div class="detail-value">вул. Нижній Вал, 21<br />Київ, 04071</div></div>
						<div id="hours"><div class="detail-label">Години роботи</div><div class="detail-value">Вт — Нд: 11:00–20:00<br />Понеділок: вихідний</div></div>
						<div><div class="detail-label">Телефон</div><div class="detail-value"><a href="tel:+380442345678">+38 (044) 234 56 78</a></div></div>
						<div><div class="detail-label">Електронна пошта</div><div class="detail-value"><a href="mailto:hello@liniya.art">hello@liniya.art</a></div></div>
					</div>
				</div>
				<div class="map" role="img" aria-label="Схематична карта розташування музею на Подолі"><span class="pin"></span><div class="map-caption">Галерея «Лінія» · Нижній Вал, 21</div></div>
			</div>
		</section>
	</main>

	<footer>
		<div class="wrap footer-row"><a class="footer-brand" href="#home">ГАЛЕРЕЯ «ЛІНІЯ»</a><span>© 2025 · Мистецтво для кожного</span><div class="social"><a href="#visit">Instagram</a><a href="#visit">Facebook</a></div></div>
	</footer>
	<script>
		const allNewsButton = document.querySelector('.all-news');
		const newsCards = document.querySelector('#news-cards');
		allNewsButton.addEventListener('click', () => {
			const isExpanded = allNewsButton.getAttribute('aria-expanded') === 'true';
			allNewsButton.setAttribute('aria-expanded', String(!isExpanded));
			newsCards.classList.toggle('show-all', !isExpanded);
			allNewsButton.textContent = isExpanded ? 'Усі новини ↗' : 'Менше новин ↑';
		});
	</script>
</body>
</html>"""


PLAN_HTML = r"""<!DOCTYPE html>
<html lang="uk">
<head>
	<meta charset="UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0" />
	<meta name="theme-color" content="#101918" /><title>Спланувати візит — Галерея «Лінія»</title>
	<style>
		@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap');
		:root{--ink:#101918;--paper:#f3f4f0;--green:#a7da73;--blue:#477df4;--muted:#78817e}*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font-family:'DM Sans',sans-serif;-webkit-font-smoothing:antialiased}a{color:inherit;text-decoration:none}.wrap{width:min(1180px,calc(100% - 64px));margin:auto}
		header{position:absolute;z-index:2;top:0;width:100%;padding:27px 0;color:white}.topbar{display:flex;justify-content:space-between;align-items:center;gap:20px}.brand{font-size:14px;font-weight:700;letter-spacing:.08em}.back{font-size:12px;color:#eee;border-bottom:1px solid #aaa;padding-bottom:5px}
		.hero{position:relative;min-height:400px;display:flex;align-items:flex-end;padding:145px 0 52px;color:white;background:#18211f url('https://images.unsplash.com/photo-1579783902614-a3fb3927b6a5?auto=format&fit=crop&w=2200&q=85') center 43%/cover no-repeat}.hero:before{content:'';position:absolute;inset:0;background:linear-gradient(90deg,rgba(10,17,16,.82),rgba(10,17,16,.3)),linear-gradient(0deg,rgba(10,17,16,.45),transparent)}.hero-content{position:relative;animation:rise .75s both}.eyebrow,.label{text-transform:uppercase;letter-spacing:.16em;font-size:10px;font-weight:700}.eyebrow{color:var(--green)}h1,h2{font-family:'Playfair Display',Georgia,serif;font-weight:500;letter-spacing:-.04em}h1{margin:14px 0 10px;font-size:clamp(46px,7vw,76px);line-height:1}.hero p{margin:0;color:#ddd;font-size:14px;line-height:1.8}
		main{padding:68px 0 90px}.booking{display:grid;grid-template-columns:minmax(0,1.3fr) minmax(260px,.7fr);gap:60px;align-items:start}.form-panel{animation:rise .8s .08s both}.form-panel h2{margin:0 0 10px;font-size:34px}.intro{margin:0 0 30px;color:#626c68;font-size:13px;line-height:1.8}form{display:grid;grid-template-columns:1fr 1fr;gap:19px}.field{display:grid;gap:8px}.full{grid-column:1/-1}label{font-size:11px;font-weight:600}input,select,textarea{width:100%;min-height:48px;padding:12px 13px;border:1px solid rgba(16,25,24,.18);border-radius:2px;background:white;color:var(--ink);font:13px 'DM Sans',sans-serif}textarea{min-height:90px;resize:vertical}input:focus,select:focus,textarea:focus{outline:2px solid var(--blue);outline-offset:2px}.submit{justify-self:start;display:flex;gap:16px;margin-top:3px;padding:15px 19px;border:0;border-radius:2px;background:var(--green);color:#10201c;font:700 12px 'DM Sans',sans-serif;cursor:pointer;transition:.2s}.submit:hover{background:#c4ee96;transform:translateY(-2px)}.note{grid-column:1/-1;margin:-8px 0 0;color:#78817e;font-size:10px;line-height:1.6}.confirmation{display:none;grid-column:1/-1;padding:15px;background:#e4f2d5;color:#20371c;font-size:13px;line-height:1.6}.confirmation.visible{display:block;animation:rise .35s both}
		.info{padding:27px;background:#e9ece8;animation:rise .8s .2s both}.info h2{margin:0 0 16px;font-size:26px}.info-row{padding:15px 0;border-bottom:1px solid rgba(16,25,24,.12)}.info-row:last-child{border:0}.label{color:var(--muted);font-size:9px}.value{margin-top:8px;font-size:12px;line-height:1.7}.value a{color:#315fc2}footer{padding:23px 0;background:#0e1716;color:#91a09a;font-size:10px}.footer-row{display:flex;justify-content:space-between;gap:16px}
		@keyframes rise{from{opacity:0;transform:translateY(18px)}to{opacity:1;transform:translateY(0)}}@media(max-width:760px){.wrap{width:min(100% - 36px,560px)}.booking{grid-template-columns:1fr;gap:35px}main{padding:48px 0 65px}.hero{min-height:360px}}@media(max-width:480px){form{grid-template-columns:1fr}.full,.note,.confirmation{grid-column:1}.topbar,.footer-row{align-items:flex-start;flex-direction:column}}@media(prefers-reduced-motion:reduce){*,*::before,*::after{animation-duration:.01ms!important;transition-duration:.01ms!important}}
	</style>
</head>
<body>
	<header><div class="wrap topbar"><a class="brand" href="HOME_PAGE">ГАЛЕРЕЯ «ЛІНІЯ»</a><a class="back" href="HOME_PAGE">← Повернутися на головну</a></div></header>
	<section class="hero"><div class="wrap hero-content"><div class="eyebrow">Ваш час для мистецтва</div><h1>Сплануйте візит.</h1><p>Оберіть зручний день — ми подбаємо, щоб зустріч із мистецтвом була особливою.</p></div></section>
	<main class="wrap booking"><section class="form-panel"><h2>Запланувати відвідування</h2><p class="intro">Заповніть форму, щоб підготувати запит на візит. Ми чекаємо на вас за адресою: вул. Нижній Вал, 21, Київ.</p>
		<form id="booking-form"><div class="field"><label for="name">Ваше ім’я</label><input id="name" name="name" autocomplete="name" required placeholder="Як до вас звертатися?" /></div><div class="field"><label for="email">Електронна пошта</label><input id="email" name="email" type="email" autocomplete="email" required placeholder="name@example.com" /></div>
		<div class="field"><label for="date">Бажана дата</label><input id="date" name="date" type="date" required /></div><div class="field"><label for="time">Час початку</label><select id="time" name="time" required><option value="" disabled selected>Оберіть час</option><option>11:00</option><option>12:00</option><option>13:00</option><option>14:00</option><option>15:00</option><option>16:00</option><option>17:00</option><option>18:00</option><option>19:00</option></select></div>
		<div class="field"><label for="guests">Кількість відвідувачів</label><select id="guests" name="guests"><option>1</option><option selected>2</option><option>3</option><option>4</option><option>5</option><option>6</option></select></div><div class="field"><label for="format">Формат візиту</label><select id="format" name="format"><option>Самостійний огляд</option><option>Екскурсія з куратором</option><option>Сімейний візит</option></select></div>
		<div class="field full"><label for="message">Побажання або запитання (необов’язково)</label><textarea id="message" name="message" placeholder="Розкажіть про особливі побажання"></textarea></div><p class="note">Галерея відкрита Вт — Нд: 11:00–20:00. Дані запиту зберігаються на цьому комп’ютері. Надсилання відкриє вашу поштову програму для підтвердження.</p><button class="submit full" type="submit">Надіслати запит <span>↗</span></button><div class="confirmation" id="confirmation" role="status" aria-live="polite">Запит підготовлено. Завершіть надсилання у поштовій програмі — команда галереї підтвердить візит електронною поштою.</div></form>
	</section><aside class="info"><h2>Корисна інформація</h2><div class="info-row"><div class="label">АДРЕСА</div><div class="value">вул. Нижній Вал, 21<br />Київ, 04071 · Поділ</div></div><div class="info-row"><div class="label">ГОДИНИ РОБОТИ</div><div class="value">Вт — Нд: 11:00–20:00<br />Понеділок: вихідний</div></div><div class="info-row"><div class="label">ЗВ’ЯЗОК</div><div class="value"><a href="tel:+380442345678">+38 (044) 234 56 78</a><br /><a href="mailto:hello@liniya.art">hello@liniya.art</a></div></div><div class="info-row"><div class="label">ЯК ДІСТАТИСЯ</div><div class="value">Кілька хвилин пішки від метро «Контрактова площа».</div></div></aside></main>
	<footer><div class="wrap footer-row"><span>ГАЛЕРЕЯ «ЛІНІЯ»</span><span>© 2025 · Мистецтво для кожного</span></div></footer>
	<script>
		const dateInput=document.querySelector('#date');const today=new Date();dateInput.min=new Date(today.getTime()-today.getTimezoneOffset()*60000).toISOString().slice(0,10);
		document.querySelector('#booking-form').addEventListener('submit',async event=>{event.preventDefault();const data=new FormData(event.currentTarget);const request={kind:'visit',name:data.get('name'),email:data.get('email'),date:data.get('date'),time:data.get('time'),quantity:data.get('guests'),format:data.get('format'),note:data.get('message')};const confirmation=document.querySelector('#confirmation');try{const response=await fetch('/api/requests',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(request)});if(!response.ok)throw new Error('Не вдалося зберегти запит');const subject=encodeURIComponent('Запит на відвідування галереї «Лінія»');const body=encodeURIComponent(`Ім’я: ${request.name}\nEmail: ${request.email}\nДата: ${request.date}\nЧас: ${request.time}\nВідвідувачів: ${request.quantity}\nФормат: ${request.format}\nПобажання: ${request.note||'немає'}`);confirmation.textContent='Запит збережено. Завершіть надсилання у поштовій програмі — команда галереї підтвердить візит електронною поштою.';confirmation.classList.add('visible');window.location.href=`mailto:hello@liniya.art?subject=${subject}&body=${body}`;}catch(error){confirmation.textContent='Не вдалося зберегти запит. Перевірте, що сайт запущено з файлу музей.py, і спробуйте ще раз.';confirmation.classList.add('visible');}});
	</script>
</body>
</html>"""


TICKETS_HTML = r"""<!DOCTYPE html>
<html lang="uk">
<head>
	<meta charset="UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0" />
	<meta name="theme-color" content="#101918" /><title>Квитки — Галерея «Лінія»</title>
	<style>
		@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap');
		:root{--ink:#101918;--paper:#f3f4f0;--green:#a7da73;--muted:#78817e;--blue:#477df4;--line:rgba(16,25,24,.12)}*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--paper);color:var(--ink);font-family:'DM Sans',sans-serif;-webkit-font-smoothing:antialiased}a{color:inherit;text-decoration:none}.wrap{width:min(1180px,calc(100% - 64px));margin:auto}
		header{position:absolute;z-index:2;top:0;width:100%;padding:27px 0;color:white}.topbar{display:flex;justify-content:space-between;align-items:center;gap:20px}.brand{display:flex;align-items:center;gap:11px;font-size:14px;font-weight:700;letter-spacing:.08em}.mark{width:32px;height:32px;display:grid;place-items:center;border:1px solid rgba(255,255,255,.72);border-radius:50%;font:19px Georgia,serif}.back{font-size:12px;color:#eee;border-bottom:1px solid #aaa;padding-bottom:5px}
		.hero{position:relative;min-height:430px;display:flex;align-items:flex-end;padding:145px 0 55px;color:white;background:#18211f url('https://images.unsplash.com/photo-1579783902614-a3fb3927b6a5?auto=format&fit=crop&w=2200&q=85') center 43%/cover no-repeat}.hero:before{content:'';position:absolute;inset:0;background:linear-gradient(90deg,rgba(10,17,16,.82),rgba(10,17,16,.3)),linear-gradient(0deg,rgba(10,17,16,.45),transparent)}.hero-content{position:relative;animation:rise .75s both}.eyebrow,.label{text-transform:uppercase;letter-spacing:.16em;font-size:10px;font-weight:700}.eyebrow{color:var(--green)}h1,h2{font-family:'Playfair Display',Georgia,serif;font-weight:500;letter-spacing:-.04em}h1{margin:14px 0 10px;font-size:clamp(46px,7vw,76px);line-height:1}.hero p{margin:0;color:#ddd;font-size:14px;line-height:1.8}
		main{padding:68px 0 90px}.ticket-layout{display:grid;grid-template-columns:minmax(0,1.3fr) minmax(270px,.7fr);gap:55px;align-items:start}.heading{margin:0 0 10px;font-size:34px}.intro{margin:0 0 30px;color:#626c68;font-size:13px;line-height:1.8}.ticket-list{display:grid;gap:13px}.ticket{display:grid;grid-template-columns:1fr auto;gap:15px;align-items:center;padding:20px 21px;background:white;border:1px solid transparent;transition:transform .25s,box-shadow .25s,border-color .25s}.ticket:hover{transform:translateY(-3px);box-shadow:0 14px 32px rgba(20,35,30,.09)}.ticket:has(input:checked){border-color:#8dbd60;box-shadow:0 0 0 2px rgba(167,218,115,.25)}.ticket-title{font-family:'Playfair Display',Georgia,serif;font-size:20px}.ticket-desc{margin-top:5px;color:#737d78;font-size:11px;line-height:1.6}.price{font-size:14px;font-weight:700;white-space:nowrap}.price small{display:block;margin-top:3px;color:var(--muted);font-size:9px;font-weight:400;text-align:right}.ticket input{accent-color:#477df4;width:17px;height:17px;margin:0 8px 0 0;vertical-align:middle}.side{padding:27px;background:#e9ece8;animation:rise .8s .18s both}.side h2{margin:0 0 14px;font-size:26px}.side p{color:#626c68;font-size:12px;line-height:1.8}.field{display:grid;gap:8px;margin-top:16px}label{font-size:11px;font-weight:600}input[type=date],input[type=number]{width:100%;min-height:45px;padding:11px;border:1px solid rgba(16,25,24,.18);border-radius:2px;background:white;color:var(--ink);font:13px 'DM Sans',sans-serif}input:focus{outline:2px solid var(--blue);outline-offset:2px}.submit{display:flex;justify-content:space-between;align-items:center;width:100%;margin-top:20px;padding:15px 17px;border:0;border-radius:2px;background:var(--green);color:#10201c;font:700 12px 'DM Sans',sans-serif;cursor:pointer;transition:.2s}.submit:hover{background:#c4ee96;transform:translateY(-2px)}.note{margin:14px 0 0;color:var(--muted);font-size:10px;line-height:1.6}.confirmation{display:none;margin-top:14px;padding:12px;background:#e4f2d5;color:#20371c;font-size:11px;line-height:1.6}.confirmation.visible{display:block;animation:rise .35s both}.visit-note{margin-top:25px;padding-top:20px;border-top:1px solid var(--line);font-size:11px;line-height:1.8}.visit-note a{color:#315fc2}footer{padding:23px 0;background:#0e1716;color:#91a09a;font-size:10px}.footer-row{display:flex;justify-content:space-between;gap:16px}
		@keyframes rise{from{opacity:0;transform:translateY(18px)}to{opacity:1;transform:translateY(0)}}@media(max-width:760px){.wrap{width:min(100% - 36px,560px)}.ticket-layout{grid-template-columns:1fr;gap:30px}main{padding:48px 0 65px}.hero{min-height:360px}}@media(max-width:480px){.topbar,.footer-row{align-items:flex-start;flex-direction:column}.ticket{padding:16px}.heading{font-size:29px}}@media(prefers-reduced-motion:reduce){*,*::before,*::after{animation-duration:.01ms!important;transition-duration:.01ms!important;scroll-behavior:auto!important}}
	</style>
</head>
<body>
	<header><div class="wrap topbar"><a class="brand" href="HOME_PAGE"><span class="mark">Л</span>ГАЛЕРЕЯ «ЛІНІЯ»</a><a class="back" href="HOME_PAGE">← Повернутися на головну</a></div></header>
	<section class="hero"><div class="wrap hero-content"><div class="eyebrow">Ваша зустріч із мистецтвом</div><h1>Квитки до галереї.</h1><p>Оберіть формат візиту та підготуйте запит — ми допоможемо з усім іншим.</p></div></section>
	<main class="wrap ticket-layout"><section><h2 class="heading">Оберіть квиток</h2><p class="intro">Квиток дає змогу відвідати поточні виставки у зручному для вас темпі. Діти до 7 років — безкоштовно.</p>
		<form id="ticket-form"><div class="ticket-list">
			<label class="ticket"><span><span class="ticket-title"><input type="radio" name="type" value="Дорослий квиток — 250 грн" checked />Дорослий</span><span class="ticket-desc">Самостійний огляд усіх поточних виставок</span></span><span class="price">250 ₴<small>за відвідувача</small></span></label>
			<label class="ticket"><span><span class="ticket-title"><input type="radio" name="type" value="Пільговий квиток — 150 грн" />Пільговий</span><span class="ticket-desc">Для студентів, пенсіонерів та військовослужбовців · за наявності посвідчення</span></span><span class="price">150 ₴<small>за відвідувача</small></span></label>
			<label class="ticket"><span><span class="ticket-title"><input type="radio" name="type" value="Сімейний квиток — 550 грн" />Сімейний</span><span class="ticket-desc">Для двох дорослих і дітей до 16 років</span></span><span class="price">550 ₴<small>за сім’ю</small></span></label>
			<label class="ticket"><span><span class="ticket-title"><input type="radio" name="type" value="Екскурсія з куратором — 400 грн з особи" />Екскурсія з куратором</span><span class="ticket-desc">Відвідування виставки та розмова про мистецтво · за попереднім записом</span></span><span class="price">400 ₴<small>з особи</small></span></label>
		</div>
		<aside class="side"><h2>Підготуйте запит</h2><p>Залиште контакти, дату й кількість квитків. Відкриється ваша поштова програма з готовим листом для підтвердження.</p><div class="field"><label for="customer-name">Ваше ім’я</label><input id="customer-name" name="name" autocomplete="name" required /></div><div class="field"><label for="customer-email">Електронна пошта</label><input id="customer-email" name="email" type="email" autocomplete="email" required /></div><div class="field"><label for="date">Бажана дата</label><input id="date" name="date" type="date" required /></div><div class="field"><label for="count">Кількість квитків</label><input id="count" name="count" type="number" min="1" max="10" value="1" required /></div><button class="submit" type="submit">Запитати квитки <span>↗</span></button><p class="note">Дані запиту зберігаються на цьому комп’ютері для обробки адміністратором. Оплата та підтвердження узгоджуються з командою галереї електронною поштою.</p><div class="confirmation" id="confirmation" role="status" aria-live="polite">Запит підготовлено. Завершіть надсилання у поштовій програмі.</div><div class="visit-note">Вт — Нд: 11:00–20:00<br />вул. Нижній Вал, 21, Київ<br /><a href="mailto:hello@liniya.art">hello@liniya.art</a> · <a href="tel:+380442345678">+38 (044) 234 56 78</a></div></aside></form>
	</section></main>
	<footer><div class="wrap footer-row"><span>ГАЛЕРЕЯ «ЛІНІЯ»</span><span>© 2025 · Мистецтво для кожного</span></div></footer>
	<script>
		const dateInput=document.querySelector('#date');const today=new Date();dateInput.min=new Date(today.getTime()-today.getTimezoneOffset()*60000).toISOString().slice(0,10);
		document.querySelector('#ticket-form').addEventListener('submit',async event=>{event.preventDefault();const data=new FormData(event.currentTarget);const request={kind:'ticket',name:data.get('name'),email:data.get('email'),date:data.get('date'),quantity:data.get('count'),ticket_type:data.get('type')};const confirmation=document.querySelector('#confirmation');try{const response=await fetch('/api/requests',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(request)});if(!response.ok)throw new Error('Не вдалося зберегти запит');const subject=encodeURIComponent('Запит на квитки до галереї «Лінія»');const body=encodeURIComponent(`Ім’я: ${request.name}\nEmail: ${request.email}\nТип квитка: ${request.ticket_type}\nДата: ${request.date}\nКількість: ${request.quantity}`);confirmation.textContent='Запит збережено. Завершіть надсилання у поштовій програмі.';confirmation.classList.add('visible');window.location.href=`mailto:hello@liniya.art?subject=${subject}&body=${body}`;}catch(error){confirmation.textContent='Не вдалося зберегти запит. Перевірте, що сайт запущено з файлу музей.py, і спробуйте ще раз.';confirmation.classList.add('visible');}});
	</script>
</body>
</html>"""


EXHIBITION_HTML = r"""<!DOCTYPE html>
<html lang="uk">
<head>
	<meta charset="UTF-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0" />
	<meta name="theme-color" content="#101918" />
	<title>Колір, що пам’ятає — Галерея «Лінія»</title>
	<style>
		@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap');
		:root { --ink:#101918; --muted:#78817e; --paper:#f3f4f0; --green:#a7da73; --line:rgba(16,25,24,.12); }
		* { box-sizing:border-box; }
		body { margin:0; color:var(--ink); background:var(--paper); font-family:'DM Sans',sans-serif; -webkit-font-smoothing:antialiased; }
		a { color:inherit; text-decoration:none; }
		.wrap { width:min(1080px,calc(100% - 48px)); margin:0 auto; }
		header { padding:24px 0; background:#14201e; color:white; }
		.topbar { display:flex; justify-content:space-between; align-items:center; gap:20px; }
		.brand { font-size:13px; font-weight:700; letter-spacing:.08em; }
		.back-link { color:#d5dfd9; font-size:12px; }
		.back-link:hover { color:var(--green); }
		.cover { position:relative; height:clamp(280px,48vw,530px); overflow:hidden; background:#26332d; }
		.cover img { display:block; width:100%; height:100%; object-fit:cover; }
		.cover::after { content:''; position:absolute; inset:45% 0 0; background:linear-gradient(transparent,rgba(10,17,16,.55)); }
		.cover-label { position:absolute; z-index:1; top:22px; left:22px; padding:9px 12px; background:var(--paper); font-size:10px; text-transform:uppercase; letter-spacing:.12em; }
		main { padding:68px 0 90px; }
		.content { display:grid; grid-template-columns:minmax(0,1.5fr) minmax(230px,.7fr); gap:70px; align-items:start; }
		.eyebrow,.label { color:var(--muted); text-transform:uppercase; letter-spacing:.15em; font-size:10px; font-weight:700; }
		h1,h2 { font-family:'Playfair Display',Georgia,serif; font-weight:500; letter-spacing:-.04em; }
		h1 { margin:15px 0 20px; font-size:clamp(42px,6vw,72px); line-height:1.04; }
		.lead { max-width:650px; color:#626c68; font-size:16px; line-height:1.85; }
		.story { margin-top:35px; color:#626c68; font-size:14px; line-height:1.95; }
		h2 { margin:34px 0 12px; font-size:31px; }
		.info { padding:25px; background:#e9ece8; }
		.info-row { padding:16px 0; border-bottom:1px solid var(--line); }
		.info-row:last-child { border-bottom:0; }
		.info-value { margin-top:8px; font-size:13px; line-height:1.7; }
		.visit-link { display:inline-flex; gap:10px; margin-top:25px; padding:14px 17px; background:#14201e; color:white; font-size:12px; font-weight:600; }
		.visit-link:hover { background:#263b34; }
		footer { padding:22px 0; background:#0e1716; color:#91a09a; font-size:10px; }
		.footer-row { display:flex; justify-content:space-between; gap:16px; }
		@media(max-width:700px) { .wrap { width:calc(100% - 36px); } .content { grid-template-columns:1fr; gap:35px; } main { padding:48px 0 65px; } .info { order:-1; } }
		@media(max-width:420px) { .topbar,.footer-row { align-items:flex-start; flex-direction:column; } }
	</style>
</head>
<body>
	<header><div class="wrap topbar"><a class="brand" href="HOME_PAGE">ГАЛЕРЕЯ «ЛІНІЯ»</a><a class="back-link" href="HOME_PAGE">← Повернутися на головну</a></div></header>
	<div class="cover"><img src="https://images.unsplash.com/photo-1577083552431-6e5fd01aa342?auto=format&fit=crop&w=1800&q=85" alt="Живопис на виставці «Колір, що пам’ятає»" /><span class="cover-label">Виставка · 15 червня — 28 серпня 2025</span></div>
	<main class="wrap content">
		<article>
			<div class="eyebrow">Мистецтво, пам’ять і місто</div>
			<h1>Колір, що пам’ятає</h1>
			<p class="lead">Нова виставка про міста, дитинство та кольори, які залишаються з нами. Запрошуємо побачити, як особисті спогади перетворюються на спільну історію.</p>
			<div class="story">
				<p>Колір часто зберігає те, чого не втримують слова: тепле світло літнього подвір’я, відтінок стін у домі дитинства, знайомий краєвид дорогою до школи. У виставці «Колір, що пам’ятає» українські художники досліджують, як місця нашого життя залишаються всередині нас.</p>
				<h2>Особисте стає спільним</h2>
				<p>Живопис, графіка та змішані техніки об’єднані темою пам’яті й міського досвіду. Роботи ведуть від конкретних родинних історій до образу міста, яке змінюється, але продовжує жити у спогадах. Тут можна рухатися у власному темпі, зупинятися біля деталей і знаходити кольори, знайомі саме вам.</p>
				<p>Виставка відкрита з 15 червня до 28 серпня 2025 року в Галереї «Лінія» на Подолі. Для відвідувачів доступні самостійний огляд та екскурсії-розмови з кураторкою.</p>
			</div>
		</article>
		<aside class="info">
			<div class="info-row"><div class="label">Дати</div><div class="info-value">15 червня — 28 серпня 2025</div></div>
			<div class="info-row"><div class="label">Місце</div><div class="info-value">Галерея «Лінія»<br />вул. Нижній Вал, 21, Київ</div></div>
			<div class="info-row"><div class="label">Години роботи</div><div class="info-value">Вт — Нд: 11:00–20:00<br />Понеділок: вихідний</div></div>
			<div class="info-row"><div class="label">Вартість</div><div class="info-value">Квитки та запитання:<br /><a href="mailto:hello@liniya.art">hello@liniya.art</a></div></div>
			<a class="visit-link" href="HOME_PAGE#visit">Спланувати візит <span>↗</span></a>
		</aside>
	</main>
	<footer><div class="wrap footer-row"><span>ГАЛЕРЕЯ «ЛІНІЯ»</span><span>© 2025 · Мистецтво для кожного</span></div></footer>
</body>
</html>"""



ADMIN_PANEL = r"""
	<style>
		#admin-panel{position:fixed;inset:0;z-index:30;overflow:auto;padding:30px 18px;background:rgba(10,17,16,.72);backdrop-filter:blur(8px);color:#101918;animation:admin-fade .2s both}
		#admin-panel[hidden]{display:none}
		.admin-window{width:min(1120px,100%);margin:2vh auto;padding:clamp(22px,4vw,42px);background:#f3f4f0;box-shadow:0 28px 90px #0006;animation:rise .35s both}
		.admin-heading{display:flex;justify-content:space-between;align-items:flex-start;gap:20px}
		.admin-eyebrow{color:#78817e;text-transform:uppercase;letter-spacing:.16em;font-size:10px;font-weight:700}
		.admin-window h2{margin:10px 0 7px;font:500 clamp(31px,5vw,46px)/1.08 'Playfair Display',Georgia,serif;letter-spacing:-.04em}
		.admin-subtitle{margin:0;color:#626c68;font-size:12px;line-height:1.7}
		.admin-actions{display:flex;flex-wrap:wrap;gap:9px}
		.admin-button{min-height:40px;padding:10px 14px;border:1px solid rgba(16,25,24,.18);background:transparent;color:#101918;font:600 11px 'DM Sans',sans-serif;cursor:pointer;transition:.2s}
		.admin-button:hover{transform:translateY(-2px);border-color:#477df4;color:#315fc2}
		.admin-button.primary{border-color:#a7da73;background:#a7da73;color:#10201c}
		.admin-stats{display:grid;grid-template-columns:repeat(3,1fr);gap:13px;margin:27px 0}
		.admin-stat{padding:18px 20px;background:#e9ece8}
		.admin-stat strong{display:block;font:500 30px 'Playfair Display',Georgia,serif}
		.admin-stat span{display:block;margin-top:3px;color:#78817e;font-size:10px}
		.admin-toolbar{display:flex;gap:10px;margin-bottom:14px}
		.admin-toolbar input,.admin-toolbar select{min-height:42px;padding:10px 12px;border:1px solid rgba(16,25,24,.18);background:white;color:#101918;font:12px 'DM Sans',sans-serif}
		.admin-toolbar input{flex:1;min-width:180px}
		.admin-table-wrap{overflow:auto;background:white}
		.admin-table{width:100%;border-collapse:collapse;text-align:left;font-size:11px}
		.admin-table th{padding:12px 10px;background:#14201e;color:white;font-size:9px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;white-space:nowrap}
		.admin-table td{padding:13px 10px;border-bottom:1px solid rgba(16,25,24,.1);vertical-align:top}
		.admin-table tr{animation:rise .3s both}
		.admin-table select{max-width:130px;padding:8px;border:1px solid rgba(16,25,24,.18);background:#f3f4f0;font:11px 'DM Sans',sans-serif}
		.admin-customer{font-weight:700}.admin-email{display:block;margin-top:4px;color:#477df4}
		.admin-muted{display:block;margin-top:4px;color:#78817e;line-height:1.55}
		.admin-delete{border:0;background:none;color:#a33b32;font:600 10px 'DM Sans',sans-serif;cursor:pointer}
		.admin-empty{padding:34px!important;text-align:center;color:#78817e}
		#admin-message{min-height:20px;margin:8px 0;color:#a33b32;font-size:11px}
		@keyframes admin-fade{from{opacity:0}to{opacity:1}}
		@media(max-width:680px){#admin-panel{padding:10px}.admin-window{margin:0 auto;padding:21px 16px}.admin-heading{flex-direction:column}.admin-stats{gap:7px}.admin-stat{padding:13px 10px}.admin-stat strong{font-size:24px}.admin-toolbar{flex-direction:column}.admin-toolbar input{min-width:0}}
		@media(prefers-reduced-motion:reduce){#admin-panel,.admin-table tr{animation:none}}
	</style>
	<section id="admin-panel" hidden aria-label="Адміністративна панель">
		<div class="admin-window" role="dialog" aria-modal="true" aria-labelledby="admin-title">
			<div class="admin-heading">
				<div><div class="admin-eyebrow">Галерея «Лінія» · робочий простір</div><h2 id="admin-title">Замовлення та записи</h2><p class="admin-subtitle">Запити з форм квитків і планування візиту. Дані зберігаються в локальній базі на цьому комп’ютері.</p></div>
				<div class="admin-actions"><button class="admin-button" type="button" id="admin-refresh">Оновити</button><button class="admin-button primary" type="button" id="admin-export">Експорт CSV</button><button class="admin-button" type="button" id="admin-close">Закрити</button></div>
			</div>
			<div class="admin-stats" aria-live="polite">
				<div class="admin-stat"><strong id="admin-total">0</strong><span>Усього запитів</span></div>
				<div class="admin-stat"><strong id="admin-new">0</strong><span>Очікують підтвердження</span></div>
				<div class="admin-stat"><strong id="admin-visitors">0</strong><span>Відвідувачів / квитків</span></div>
			</div>
			<div class="admin-toolbar"><input id="admin-search" type="search" placeholder="Пошук за ім’ям або email" aria-label="Пошук замовлень" /><select id="admin-filter" aria-label="Фільтр запитів"><option value="all">Усі запити</option><option value="ticket">Квитки</option><option value="visit">Планування візиту</option></select></div>
			<div id="admin-message" role="status" aria-live="polite"></div>
			<div class="admin-table-wrap"><table class="admin-table"><thead><tr><th>Відвідувач</th><th>Запит</th><th>Дата</th><th>Статус</th><th>Дія</th></tr></thead><tbody id="admin-rows"></tbody></table></div>
		</div>
	</section>
	"""

ANALYTICS_SCRIPT = r"""<script>
(() => {
	const key = 'liniya_analytics_v1';
	const consentKey = 'liniya_analytics_consent';
	const load = () => { try { return JSON.parse(localStorage.getItem(key) || '[]'); } catch (_) { return []; } };
	const save = rows => { try { localStorage.setItem(key, JSON.stringify(rows.slice(-1000))); } catch (_) {} };
	const record = (action) => {
		if (localStorage.getItem(consentKey) !== 'yes') return;
		const rows = load();
		rows.push({time: new Date().toISOString(), action, page: location.pathname || '/', session: sessionStorage.getItem('liniya_session') || ''});
		save(rows);
	};
	let banner;
	try {
		if (localStorage.getItem(consentKey) === 'yes') {
			if (!sessionStorage.getItem('liniya_session')) sessionStorage.setItem('liniya_session', (crypto.randomUUID ? crypto.randomUUID() : String(Date.now()) + Math.random().toString(36).slice(2)));
			record('Перегляд сторінки');
		} else if (!localStorage.getItem(consentKey)) {
			banner = document.createElement('aside');
			banner.setAttribute('role', 'dialog');
			banner.setAttribute('aria-label', 'Налаштування аналітики');
			banner.style.cssText = 'position:fixed;z-index:20;bottom:16px;left:16px;max-width:440px;padding:18px;background:#14201e;color:white;box-shadow:0 8px 32px #0004;font:13px/1.6 sans-serif';
			banner.innerHTML = 'Дозволити анонімну статистику переглядів і натискань? Значення форм та персональні дані не збираються; журнал зберігається лише в цьому браузері.<br><button type="button" data-choice="yes">Дозволити</button> <button type="button" data-choice="no">Відмовитися</button>';
			banner.addEventListener('click', event => {
				const choice = event.target.dataset.choice;
				if (!choice) return;
				try { localStorage.setItem(consentKey, choice); } catch (_) {}
				banner.remove();
				if (choice === 'yes') {
					try { sessionStorage.setItem('liniya_session', (crypto.randomUUID ? crypto.randomUUID() : String(Date.now()) + Math.random().toString(36).slice(2))); } catch (_) {}
					record('Перегляд сторінки');
				}
			});
			document.body.appendChild(banner);
		}
	} catch (_) {}

	document.addEventListener('click', event => {
		const target = event.target.closest('a,button,input[type="submit"]');
		if (!target || target.closest('#admin-panel') || target.closest('[aria-label="Налаштування аналітики"]')) return;
		const label = (target.innerText || target.getAttribute('aria-label') || target.tagName).replace(/\s+/g, ' ').trim().slice(0, 60);
		record('Натискання: ' + label);
	});
	document.addEventListener('submit', event => record('Надсилання форми: ' + (event.target.id || 'форма')));
	let maxScroll = 0;
	document.addEventListener('scroll', () => {
		const depth = Math.round((scrollY + innerHeight) / document.documentElement.scrollHeight * 100);
		if (depth >= maxScroll + 25) { maxScroll = Math.floor(depth / 25) * 25; if (maxScroll > 0) record('Глибина перегляду: ' + Math.min(maxScroll, 100) + '%'); }
	}, {passive: true});

	const panel = document.querySelector('#admin-panel');
	if (!panel) return;
	const adminMessage = document.querySelector('#admin-message');
	let requests = [];
	const filteredRequests = () => {
		const type = document.querySelector('#admin-filter').value;
		const search = document.querySelector('#admin-search').value.trim().toLocaleLowerCase();
		return requests.filter(item => (type === 'all' || item.kind === type) && (!search || `${item.name} ${item.email}`.toLocaleLowerCase().includes(search)));
	};
	const refresh = async () => {
		adminMessage.textContent = '';
		try {
			const response = await fetch('/api/requests');
			if (!response.ok) throw new Error('Не вдалося завантажити заявки.');
			requests = await response.json();
			render();
		} catch (error) {
			adminMessage.textContent = 'Не вдалося завантажити заявки. Переконайтеся, що музей.py запущено.';
		}
	};
	const render = () => {
		const visible = filteredRequests();
		document.querySelector('#admin-total').textContent = String(requests.length);
		document.querySelector('#admin-new').textContent = String(requests.filter(item => item.status === 'new').length);
		document.querySelector('#admin-visitors').textContent = String(requests.reduce((sum, item) => sum + Number(item.quantity || 0), 0));
		const tbody = document.querySelector('#admin-rows');
		tbody.replaceChildren();
		if (!visible.length) {
			const tr = document.createElement('tr');
			const td = document.createElement('td');
			td.className = 'admin-empty';
			td.colSpan = 5;
			td.textContent = requests.length ? 'За цим фільтром нічого не знайдено.' : 'Заявок поки немає. Нові запити з’являться тут.';
			tr.appendChild(td);
			tbody.appendChild(tr);
			return;
		}
		visible.forEach(item => {
			const tr = document.createElement('tr');
			const customer = document.createElement('td');
			const customerName = document.createElement('span');
			customerName.className = 'admin-customer';
			customerName.textContent = item.name;
			const email = document.createElement('a');
			email.className = 'admin-email';
			email.href = `mailto:${item.email}`;
			email.textContent = item.email;
			customer.append(customerName, email);
			const detail = document.createElement('td');
			detail.textContent = item.kind === 'ticket' ? 'Квитки' : 'Візит';
			const detailText = item.kind === 'ticket' ? item.ticket_type : item.format;
			if (detailText) {
				const description = document.createElement('span');
				description.className = 'admin-muted';
				description.textContent = detailText;
				detail.appendChild(description);
			}
			const quantity = document.createElement('span');
			quantity.className = 'admin-muted';
			quantity.textContent = `Кількість: ${item.quantity}`;
			detail.appendChild(quantity);
			if (item.note) {
				const note = document.createElement('span');
				note.className = 'admin-muted';
				note.textContent = `Побажання: ${item.note}`;
				detail.appendChild(note);
			}
			const date = document.createElement('td');
			date.textContent = item.date || '';
			const dateExtra = document.createElement('span');
			dateExtra.className = 'admin-muted';
			dateExtra.textContent = item.time ? `Час: ${item.time}` : `Створено: ${new Date(item.created_at).toLocaleString()}`;
			date.appendChild(dateExtra);
			const statusCell = document.createElement('td');
			const status = document.createElement('select');
			status.setAttribute('aria-label', `Статус заявки ${item.id}`);
			[['new','Нова'],['confirmed','Підтверджена'],['completed','Виконана'],['cancelled','Скасована']].forEach(([value,label]) => {
				const option = document.createElement('option');
				option.value = value;
				option.textContent = label;
				status.appendChild(option);
			});
			status.value = item.status;
			status.addEventListener('change', async () => {
				try {
					const response = await fetch(`/api/requests/${item.id}/status`, {method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({status:status.value})});
					if (!response.ok) throw new Error('Не вдалося оновити статус.');
					item.status = status.value;
					render();
				} catch (error) {
					adminMessage.textContent = 'Не вдалося змінити статус заявки.';
					status.value = item.status;
				}
			});
			statusCell.appendChild(status);
			const actions = document.createElement('td');
			const remove = document.createElement('button');
			remove.className = 'admin-delete';
			remove.type = 'button';
			remove.textContent = 'Видалити';
			remove.addEventListener('click', async () => {
				if (!confirm(`Видалити заявку від ${item.name}?`)) return;
				try {
					const response = await fetch(`/api/requests/${item.id}`, {method:'DELETE'});
					if (!response.ok) throw new Error('Не вдалося видалити заявку.');
					requests = requests.filter(row => row.id !== item.id);
					render();
				} catch (error) {
					adminMessage.textContent = 'Не вдалося видалити заявку.';
				}
			});
			actions.appendChild(remove);
			tr.append(customer, detail, date, statusCell, actions);
			tbody.appendChild(tr);
		});
	};
	const toggle = open => {
		panel.hidden = !open;
		if (open) {
			history.replaceState(null, '', '#admin');
			document.body.style.overflow = 'hidden';
			document.querySelector('#admin-close').focus();
			refresh();
		} else {
			document.body.style.overflow = '';
			if (location.hash === '#admin') history.replaceState(null, '', location.pathname + location.search);
		}
	};
	document.querySelector('#admin-close').addEventListener('click', () => toggle(false));
	document.querySelector('#admin-refresh').addEventListener('click', refresh);
	document.querySelector('#admin-filter').addEventListener('change', render);
	document.querySelector('#admin-search').addEventListener('input', render);
	document.addEventListener('keydown', event => { if (event.key === 'Escape' && !panel.hidden) toggle(false); });
	panel.addEventListener('click', event => { if (event.target === panel) toggle(false); });
	document.querySelector('#admin-export').addEventListener('click', () => {
		const columns = ['Дата заявки','Тип','Ім’я','Email','Дата візиту','Час','Кількість','Тип квитка / формат','Статус','Побажання'];
		const rows = filteredRequests().map(item => [item.created_at,item.kind === 'ticket' ? 'Квитки' : 'Візит',item.name,item.email,item.date,item.time,item.quantity,item.ticket_type || item.format,item.status,item.note]);
		const csv = [columns, ...rows].map(row => row.map(value => '"' + String(value || '').replace(/"/g, '""') + '"').join(',')).join('\n');
		const link = document.createElement('a');
		link.href = URL.createObjectURL(new Blob(['\ufeff' + csv], {type:'text/csv;charset=utf-8'}));
		link.download = 'liniya-requests.csv';
		link.click();
		URL.revokeObjectURL(link.href);
	});
	if (location.hash === '#admin') toggle(true);
})();
</script>"""

HTML = HTML.replace('</body>', ADMIN_PANEL + '</body>', 1)


if __name__ == "__main__":
	import json
	import sqlite3
	from datetime import date
	from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
	from pathlib import Path
	import webbrowser
	from urllib.parse import urlparse

	database_path = Path(__file__).with_name("museum_requests.sqlite3")
	with sqlite3.connect(database_path) as connection:
		connection.execute("""
			CREATE TABLE IF NOT EXISTS requests (
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				created_at TEXT NOT NULL,
				kind TEXT NOT NULL CHECK (kind IN ('ticket', 'visit')),
				name TEXT NOT NULL,
				email TEXT NOT NULL,
				date TEXT NOT NULL,
				time TEXT NOT NULL DEFAULT '',
				quantity INTEGER NOT NULL,
				ticket_type TEXT NOT NULL DEFAULT '',
				format TEXT NOT NULL DEFAULT '',
				note TEXT NOT NULL DEFAULT '',
				status TEXT NOT NULL DEFAULT 'new'
			)
		""")

	class MuseumHandler(BaseHTTPRequestHandler):
		def send_json(self, payload, status=200):
			body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
			self.send_response(status)
			self.send_header("Content-Type", "application/json; charset=utf-8")
			self.send_header("Content-Length", str(len(body)))
			self.send_header("Cache-Control", "no-store")
			self.end_headers()
			self.wfile.write(body)

		def read_json(self):
			try:
				length = int(self.headers.get("Content-Length", "0"))
			except ValueError:
				return None
			if length < 1 or length > 65536:
				return None
			try:
				payload = json.loads(self.rfile.read(length))
			except (json.JSONDecodeError, UnicodeDecodeError):
				return None
			return payload if isinstance(payload, dict) else None

		def do_GET(self):
			path = urlparse(self.path).path
			if path == "/api/requests":
				with sqlite3.connect(database_path) as connection:
					connection.row_factory = sqlite3.Row
					rows = connection.execute(
						"SELECT * FROM requests ORDER BY id DESC"
					).fetchall()
				return self.send_json([dict(row) for row in rows])

			pages = {
				"/": HTML.replace("EXHIBITION_PAGE", "/exhibition.html").replace(
					"PLAN_PAGE", "/plan.html"
				).replace("TICKETS_PAGE", "/tickets.html"),
				"/plan.html": PLAN_HTML.replace("HOME_PAGE", "/"),
				"/tickets.html": TICKETS_HTML.replace("HOME_PAGE", "/"),
				"/exhibition.html": EXHIBITION_HTML.replace("HOME_PAGE", "/"),
			}
			page = pages.get(path)
			if page is None:
				return self.send_error(404)
			if path == "/":
				page = page.replace("</body>", ADMIN_PANEL + "</body>", 1)
			page = page.replace("</body>", ANALYTICS_SCRIPT + "</body>", 1)
			body = page.encode("utf-8")
			self.send_response(200)
			self.send_header("Content-Type", "text/html; charset=utf-8")
			self.send_header("Content-Length", str(len(body)))
			self.send_header("Cache-Control", "no-store")
			self.end_headers()
			self.wfile.write(body)

		def do_POST(self):
			path = urlparse(self.path).path
			if path.startswith("/api/requests/") and path.endswith("/status"):
				parts = path.strip("/").split("/")
				if len(parts) != 4 or parts[0:2] != ["api", "requests"]:
					return self.send_json({"error": "Invalid request path"}, 404)
				try:
					request_id = int(parts[2])
				except ValueError:
					return self.send_json({"error": "Invalid request id"}, 400)
				payload = self.read_json()
				allowed_statuses = {"new", "confirmed", "completed", "cancelled"}
				if not payload or not isinstance(payload.get("status"), str) or payload["status"] not in allowed_statuses:
					return self.send_json({"error": "Invalid status"}, 400)
				with sqlite3.connect(database_path) as connection:
					cursor = connection.execute(
						"UPDATE requests SET status = ? WHERE id = ?",
						(payload["status"], request_id),
					)
				if not cursor.rowcount:
					return self.send_json({"error": "Request not found"}, 404)
				return self.send_json({"ok": True})

			if path != "/api/requests":
				return self.send_json({"error": "Not found"}, 404)
			payload = self.read_json()
			if not payload:
				return self.send_json({"error": "Invalid JSON body"}, 400)

			def text_field(name, limit, required=True):
				value = payload.get(name, "")
				if not isinstance(value, str):
					return None
				value = value.strip()
				if (required and not value) or len(value) > limit:
					return None
				return value

			kind = payload.get("kind")
			name = text_field("name", 120)
			email = text_field("email", 254)
			request_date = text_field("date", 10)
			if not isinstance(kind, str) or kind not in {"ticket", "visit"} or not name or not email or "@" not in email or not request_date:
				return self.send_json({"error": "Please check the required fields"}, 400)
			try:
				date.fromisoformat(request_date)
				quantity = int(payload.get("quantity"))
			except (TypeError, ValueError):
				return self.send_json({"error": "Invalid date or quantity"}, 400)
			if not 1 <= quantity <= (10 if kind == "ticket" else 6):
				return self.send_json({"error": "Invalid quantity"}, 400)
			ticket_type = text_field("ticket_type", 120, required=False)
			visit_format = text_field("format", 120, required=False)
			note = text_field("note", 1000, required=False)
			time = text_field("time", 5, required=False)
			if ticket_type is None or visit_format is None or note is None or time is None:
				return self.send_json({"error": "A field is too long or invalid"}, 400)
			if kind == "ticket" and ticket_type not in {
				"Дорослий квиток — 250 грн",
				"Пільговий квиток — 150 грн",
				"Сімейний квиток — 550 грн",
				"Екскурсія з куратором — 400 грн з особи",
			}:
				return self.send_json({"error": "Invalid ticket type"}, 400)
			if kind == "visit" and (time not in {
				"11:00", "12:00", "13:00", "14:00", "15:00",
				"16:00", "17:00", "18:00", "19:00",
			} or visit_format not in {
				"Самостійний огляд", "Екскурсія з куратором", "Сімейний візит",
			}):
				return self.send_json({"error": "Invalid visit details"}, 400)

			with sqlite3.connect(database_path) as connection:
				cursor = connection.execute(
					"""INSERT INTO requests
					(created_at, kind, name, email, date, time, quantity, ticket_type, format, note)
					VALUES (strftime('%Y-%m-%dT%H:%M:%SZ', 'now'), ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
					(kind, name, email, request_date, time, quantity, ticket_type, visit_format, note),
				)
				request_id = cursor.lastrowid
			return self.send_json({"ok": True, "id": request_id}, 201)

		def do_DELETE(self):
			parts = urlparse(self.path).path.strip("/").split("/")
			if len(parts) != 3 or parts[:2] != ["api", "requests"]:
				return self.send_json({"error": "Not found"}, 404)
			try:
				request_id = int(parts[2])
			except ValueError:
				return self.send_json({"error": "Invalid request id"}, 400)
			with sqlite3.connect(database_path) as connection:
				cursor = connection.execute("DELETE FROM requests WHERE id = ?", (request_id,))
			if not cursor.rowcount:
				return self.send_json({"error": "Request not found"}, 404)
			return self.send_json({"ok": True})

	server = ThreadingHTTPServer(("127.0.0.1", 8000), MuseumHandler)
	admin_url = "http://127.0.0.1:8000/#admin"
	print(f"Музей відкрито: http://127.0.0.1:8000/")
	print(f"Адмін-панель: {admin_url}")
	print(f"Заявки зберігаються у: {database_path}")
	webbrowser.open_new_tab("http://127.0.0.1:8000/")
	try:
		server.serve_forever()
	except KeyboardInterrupt:
		print("\nСервер зупинено.")
	finally:
		server.server_close()
