/* ============================================================
   NEXA ATELIER — main.js
   Render catalogo, link WhatsApp, dati di contatto, nav, animazioni.
   Dati: data/torte.js (NEXA_CONFIG, NEXA_TORTE).
   ============================================================ */
(function () {
  "use strict";

  var config = window.NEXA_CONFIG || {};
  var torte = window.NEXA_TORTE || [];
  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // ---------- WhatsApp ----------
  var MESSAGGI = {
    generale: "Ciao Nexa, vorrei informazioni per un evento. Tipo: … Data indicativa: … Ospiti: …",
    laurea: "Ciao Nexa, vorrei organizzare una festa di laurea. Data indicativa: … Ospiti: …",
    privati: "Ciao Nexa, vorrei organizzare un evento privato (tipo: …). Data indicativa: … Ospiti: …",
    aziende: "Buongiorno Nexa, scrivo per conto di [azienda]. Vorremmo organizzare un evento aziendale. Periodo: … Partecipanti: …"
  };

  function waLink(msg) {
    return "https://wa.me/" + String(config.whatsapp || "").replace(/\D/g, "") +
      "?text=" + encodeURIComponent(msg);
  }

  function setWhatsApp(el, msg) {
    el.href = waLink(msg);
    el.target = "_blank";
    el.rel = "noopener";
  }

  document.querySelectorAll("[data-wa]").forEach(function (el) {
    var msg = MESSAGGI[el.getAttribute("data-wa")];
    if (msg) setWhatsApp(el, msg);
  });

  // ---------- Dati di contatto ----------
  document.querySelectorAll("[data-config]").forEach(function (el) {
    var value = config[el.getAttribute("data-config")];
    if (value !== undefined && value !== null) el.textContent = value;
  });

  if (config.email) {
    document.querySelectorAll("[data-email]").forEach(function (el) {
      el.href = "mailto:" + config.email;
    });
  }

  if (config.instagram) {
    document.querySelectorAll("[data-instagram]").forEach(function (el) {
      el.href = config.instagram;
      el.target = "_blank";
    });
  }

  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });

  // ---------- Monogramma N (placeholder) ----------
  var SVG_NS = "http://www.w3.org/2000/svg";

  function monogram() {
    var svg = document.createElementNS(SVG_NS, "svg");
    svg.setAttribute("viewBox", "0 0 80 100");
    svg.setAttribute("aria-hidden", "true");
    svg.setAttribute("focusable", "false");
    var rect = document.createElementNS(SVG_NS, "rect");
    [["x", "0.5"], ["y", "0.5"], ["width", "79"], ["height", "99"], ["fill", "none"],
      ["stroke", "currentColor"], ["stroke-width", "1"]].forEach(function (a) { rect.setAttribute(a[0], a[1]); });
    var text = document.createElementNS(SVG_NS, "text");
    [["x", "40"], ["y", "69"], ["text-anchor", "middle"], ["font-family", "'Bodoni Moda', 'Bodoni 72', Didot, serif"],
      ["font-size", "58"], ["fill", "none"], ["stroke", "currentColor"], ["stroke-width", "1"]].forEach(function (a) { text.setAttribute(a[0], a[1]); });
    text.textContent = "N";
    svg.appendChild(rect);
    svg.appendChild(text);
    return svg;
  }

  function placeholder(nome) {
    var box = document.createElement("div");
    box.className = "cake__placeholder";
    box.appendChild(monogram());
    var label = document.createElement("span");
    label.textContent = nome;
    box.appendChild(label);
    return box;
  }

  // ---------- Catalogo torte ----------
  var prezzo = new Intl.NumberFormat("it-IT", { maximumFractionDigits: 0 });

  function el(tag, className, text) {
    var node = document.createElement(tag);
    if (className) node.className = className;
    if (text) node.textContent = text;
    return node;
  }

  function cakeCard(torta) {
    var card = el("li", "card cake");
    card.setAttribute("data-reveal", "");

    var media = el("div", "cake__media");
    if (torta.immagine) {
      var img = document.createElement("img");
      img.src = torta.immagine;
      img.alt = "Torta " + torta.nome + ": " + torta.descrizione;
      img.width = 1600;
      img.height = 2000;
      img.loading = "lazy";
      img.decoding = "async";
      img.addEventListener("error", function () {
        img.remove();
        media.appendChild(placeholder(torta.nome));
      });
      media.appendChild(img);
    } else {
      media.appendChild(placeholder(torta.nome));
    }
    card.appendChild(media);

    var body = el("div", "cake__body");
    body.appendChild(el("h3", "cake__name", torta.nome));
    body.appendChild(el("p", "cake__meta", [torta.porzioni, torta.occasione].filter(Boolean).join(" · ")));
    if (torta.descrizione) body.appendChild(el("p", "cake__desc", torta.descrizione));

    var foot = el("div", "cake__foot");
    foot.appendChild(el("p", "cake__price",
      torta.prezzoDa == null ? "Su richiesta" : "da € " + prezzo.format(torta.prezzoDa)));
    var cta = el("a", "text-link", "Richiedi");
    cta.setAttribute("aria-label", "Richiedi la torta " + torta.nome + " su WhatsApp");
    setWhatsApp(cta, "Ciao Nexa, sono interessato alla torta \"" + torta.nome + "\". Data: … Persone: …");
    foot.appendChild(cta);
    body.appendChild(foot);

    card.appendChild(body);
    return card;
  }

  var list = document.getElementById("cakes");
  if (list) {
    var frag = document.createDocumentFragment();
    torte.forEach(function (torta) { frag.appendChild(cakeCard(torta)); });
    list.appendChild(frag);
  }

  // ---------- Hero: immagine o monogramma ----------
  var heroImg = document.querySelector(".hero__img");
  if (heroImg) {
    var heroMedia = heroImg.parentNode;
    var onHeroLoad = function () { heroMedia.classList.add("has-img"); };
    var onHeroError = function () { heroImg.remove(); };
    if (heroImg.complete) {
      if (heroImg.naturalWidth) onHeroLoad(); else onHeroError();
    } else {
      heroImg.addEventListener("load", onHeroLoad);
      heroImg.addEventListener("error", onHeroError);
    }
  }

  // ---------- Nav mobile ----------
  var toggle = document.querySelector(".nav__toggle");
  var menu = document.getElementById("nav-menu");
  if (toggle && menu) {
    var toggleLabel = toggle.querySelector(".visually-hidden");

    var setOpen = function (open) {
      toggle.setAttribute("aria-expanded", String(open));
      menu.classList.toggle("is-open", open);
      toggleLabel.textContent = open ? "Chiudi il menu" : "Apri il menu";
    };

    toggle.addEventListener("click", function () {
      setOpen(toggle.getAttribute("aria-expanded") !== "true");
    });

    menu.addEventListener("click", function (e) {
      if (e.target.closest("a")) setOpen(false);
    });

    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && toggle.getAttribute("aria-expanded") === "true") {
        setOpen(false);
        toggle.focus();
      }
    });

    window.matchMedia("(min-width: 900px)").addEventListener("change", function (mq) {
      if (mq.matches) setOpen(false);
    });
  }

  // ---------- Animazioni d'entrata ----------
  var reveals = document.querySelectorAll("[data-reveal]");

  // stagger 80ms tra elementi fratelli dello stesso gruppo
  reveals.forEach(function (node) {
    var i = 0;
    var prev = node.previousElementSibling;
    while (prev) {
      if (prev.hasAttribute("data-reveal")) i++;
      prev = prev.previousElementSibling;
    }
    node.style.setProperty("--reveal-i", Math.min(i, 6));
  });

  if (reduceMotion || !("IntersectionObserver" in window)) {
    reveals.forEach(function (node) { node.classList.add("is-visible"); });
  } else {
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.1 });
    reveals.forEach(function (node) { observer.observe(node); });
  }

  // ---------- JSON-LD ----------
  var ld = {
    "@context": "https://schema.org",
    "@type": "EventPlanner",
    "name": "Nexa Atelier",
    "description": "Feste di laurea, eventi privati e aziendali progettati su misura, con torte d'atelier da pasticceria artigianale.",
    "areaServed": [
      { "@type": "City", "name": "Milano" },
      { "@type": "AdministrativeArea", "name": "Sicilia" }
    ],
    "founder": { "@type": "Person", "name": "Mattia Di Donato" }
  };
  if (config.email) ld.email = config.email;
  // i valori ancora da completare ("39XXXXXXXXXX", "[P.IVA]") restano fuori
  if (/^\d+$/.test(config.whatsapp)) ld.telephone = "+" + config.whatsapp;
  if (config.instagram) ld.sameAs = [config.instagram];
  if (/^\d+$/.test(config.piva)) ld.vatID = "IT" + config.piva;

  var ldScript = document.createElement("script");
  ldScript.type = "application/ld+json";
  ldScript.textContent = JSON.stringify(ld);
  document.head.appendChild(ldScript);
})();
