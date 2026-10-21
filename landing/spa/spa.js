/* Thera+Vida — interacción de las landings: música relajante, videos, respiración, conversiones */
(function () {
  "use strict";
  var d = document, w = window;
  var reduce = w.matchMedia && w.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var desktop = w.matchMedia("(min-width: 960px)");

  function guarda(k, v) { try { localStorage.setItem(k, v); } catch (e) {} }
  function lee(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }

  /* ---------- Conversión de Google Ads: TeraVida_WhatsApp ----------
     Se envía en todos los botones que abren WhatsApp para escribir o reservar
     (no en los de llamada ni en "Cómo llegar"). */
  d.querySelectorAll('a[href*="wa.me/"]').forEach(function (a) {
    a.addEventListener("click", function () {
      if (typeof w.gtag === "function") {
        w.gtag("event", "conversion", { send_to: "AW-18496514239/Eog5CN6Y-6QdEL_R6fNE" });
      }
    });
  });

  /* ---------- Cabecera y barra móvil ---------- */
  var top = d.querySelector(".top"), barra = d.querySelector(".barra"), hero = d.querySelector(".hero");
  function alScroll() {
    var y = w.scrollY || 0;
    if (top) top.classList.toggle("solida", y > 40);
    if (barra && hero) barra.classList.toggle("ver", y > hero.offsetHeight * 0.55);
    if (y > w.innerHeight * 1.3) { var iv = d.querySelector(".invita-musica.ver"); if (iv) iv.classList.remove("ver"); }
  }
  w.addEventListener("scroll", alScroll, { passive: true });
  alScroll();

  /* ---------- Videos: cargan solo cuando se ven, se pausan fuera de pantalla ---------- */
  function cargar(v) {
    if (v.dataset.src && !v.getAttribute("src")) { v.src = v.dataset.src; v.load(); }
  }
  function reproducir(v) {
    if (reduce) return;
    cargar(v);
    var p = v.play(); if (p && p.catch) p.catch(function () {});
  }
  var heroVid = d.querySelector(".hero-media video");
  if (heroVid) {
    if (reduce) { heroVid.removeAttribute("autoplay"); heroVid.pause(); }
    else reproducir(heroVid);
  }
  var vistos = "IntersectionObserver" in w ? new IntersectionObserver(function (es) {
    es.forEach(function (e) {
      var v = e.target;
      if (e.isIntersecting) reproducir(v); else if (!v.paused) v.pause();
    });
  }, { rootMargin: "120px 0px", threshold: 0.15 }) : null;
  d.querySelectorAll("video.perezoso").forEach(function (v) {
    if (vistos) vistos.observe(v); else reproducir(v);
  });

  /* ---------- Carta: vista previa del masaje activo (escritorio) ---------- */
  var vista = d.querySelector(".carta-vista");
  if (vista) {
    var vids = vista.querySelectorAll("video"), cap = vista.querySelector("figcaption");
    var items = d.querySelectorAll(".lista .item");
    var actual = -1;
    function activar(i) {
      if (i === actual || !vids[i]) return;
      actual = i;
      items.forEach(function (it, k) { it.classList.toggle("activo", k === i); });
      vids.forEach(function (v, k) {
        if (k === i) { v.classList.add("on"); reproducir(v); }
        else { v.classList.remove("on"); if (!v.paused) setTimeout(function () { v.pause(); }, 1100); }
      });
      if (cap) cap.textContent = items[i].querySelector("h3").textContent;
    }
    items.forEach(function (it, k) {
      it.addEventListener("mouseenter", function () { if (desktop.matches) activar(k); });
      it.addEventListener("focusin", function () { if (desktop.matches) activar(k); });
    });
    if ("IntersectionObserver" in w) {
      var centro = new IntersectionObserver(function (es) {
        es.forEach(function (e) {
          if (e.isIntersecting && desktop.matches) activar([].indexOf.call(items, e.target));
        });
      }, { rootMargin: "-45% 0px -45% 0px" });
      items.forEach(function (it) { centro.observe(it); });
    }
    if (desktop.matches) activar(0);
    desktop.addEventListener && desktop.addEventListener("change", function (m) { if (m.matches && actual < 0) activar(0); });
  }

  /* ---------- Respiración guiada ---------- */
  var circ = d.querySelector(".circulo span");
  if (circ && !reduce) {
    var fases = [["Inhala", 0], ["Sostén", 4000], ["Exhala", 5000]], timers = [];
    function ciclo() {
      fases.forEach(function (f) {
        timers.push(setTimeout(function () {
          circ.style.opacity = 0;
          setTimeout(function () { circ.textContent = f[0]; circ.style.opacity = 1; }, 300);
        }, f[1]));
      });
    }
    ciclo();
    setInterval(ciclo, 10000);
  }

  /* ---------- Música relajante ----------
     Los navegadores no dejan sonar audio sin un gesto de la persona, así que:
     1) se intenta reproducir al entrar;
     2) si el navegador lo bloquea, empieza con el primer toque o tecla en la página
        (sin contar enlaces, para no sonar mientras la persona abre WhatsApp);
     3) el botón de la cabecera la activa o la silencia, y la elección se recuerda. */
  var PISTAS = [
    { web: "https://upload.wikimedia.org/wikipedia/commons/0/09/Meditation_Impromptu_02_%28ISRC_USUAN1100162%29.mp3", local: "spa/audio/meditacion-1.mp3" },
    { web: "https://upload.wikimedia.org/wikipedia/commons/4/41/Himalayan_Atmosphere_%28ISRC_USUAN1100204%29.mp3", local: "spa/audio/meditacion-2.mp3" }
  ];
  var VOL = 0.55;
  var audio = new Audio();
  audio.preload = "none";
  var pista = 0, usandoLocal = false, sonando = false, quiereSonar = false, fade = null;
  var botones = d.querySelectorAll("[data-musica]");
  var invita = d.querySelector(".invita-musica");
  var preferencia = lee("tv-musica"); // "off" si la persona la apagó antes

  function fuente() { return usandoLocal ? PISTAS[pista].local : PISTAS[pista].web; }
  audio.src = fuente();
  audio.addEventListener("error", function () {
    if (!usandoLocal) { usandoLocal = true; audio.src = fuente(); if (quiereSonar) intentar(); }
  });
  audio.addEventListener("ended", function () {
    pista = (pista + 1) % PISTAS.length; audio.src = fuente(); if (quiereSonar) intentar();
  });

  function pintar() {
    botones.forEach(function (b) {
      b.setAttribute("aria-pressed", sonando ? "true" : "false");
      if (b.classList.contains("sonido")) {
        b.setAttribute("aria-label", sonando ? "Silenciar música relajante" : "Activar música relajante");
        b.classList.toggle("invita", !sonando && preferencia !== "off");
      }
      var t = b.querySelector("[data-musica-txt]");
      if (t) t.textContent = sonando ? b.dataset.on : b.dataset.off;
    });
    if (invita && sonando) invita.classList.remove("ver");
  }
  function subir() {
    clearInterval(fade); audio.volume = 0;
    fade = setInterval(function () {
      var v = Math.min(VOL, audio.volume + 0.02); audio.volume = v; if (v >= VOL) clearInterval(fade);
    }, 90);
  }
  function intentar() {
    quiereSonar = true;
    var p = audio.play();
    if (p && p.then) {
      p.then(function () { sonando = true; subir(); pintar(); quitarGestos(); })
       .catch(function (err) { if (err && err.name === "NotAllowedError") { sonando = false; pintar(); } });
    } else { sonando = true; pintar(); }
  }
  function silenciar() {
    quiereSonar = false; clearInterval(fade);
    var paso = setInterval(function () {
      var v = Math.max(0, audio.volume - 0.04); audio.volume = v;
      if (v <= 0) { clearInterval(paso); audio.pause(); }
    }, 40);
    sonando = false; pintar();
  }
  botones.forEach(function (b) {
    b.addEventListener("click", function (e) {
      e.stopPropagation();
      if (sonando) { preferencia = "off"; guarda("tv-musica", "off"); silenciar(); }
      else { preferencia = "on"; guarda("tv-musica", "on"); intentar(); }
    });
  });

  function gesto(e) {
    if (e.target.closest && e.target.closest("a,[data-musica],.invita-musica,summary,iframe")) return;
    if (!sonando) intentar();
  }
  function quitarGestos() {
    ["pointerdown", "keydown"].forEach(function (t) { d.removeEventListener(t, gesto, true); });
  }
  if (preferencia !== "off") {
    intentar(); // casi siempre queda bloqueado hasta el primer toque
    ["pointerdown", "keydown"].forEach(function (t) { d.addEventListener(t, gesto, true); });
    if (invita) setTimeout(function () {
      if (!sonando && !lee("tv-invita") && (w.scrollY || 0) < w.innerHeight) {
        invita.classList.add("ver");
        setTimeout(function () { invita.classList.remove("ver"); }, 14000);
      }
    }, 2600);
  }
  if (invita) {
    var x = invita.querySelector(".cerrar");
    if (x) x.addEventListener("click", function (e) { e.stopPropagation(); invita.classList.remove("ver"); guarda("tv-invita", "1"); });
  }
  // Pausa si la persona sale de la pestaña (por ejemplo, al abrir WhatsApp) y retoma al volver
  var pausadaPorSalir = false;
  d.addEventListener("visibilitychange", function () {
    if (d.hidden && sonando) { audio.pause(); pausadaPorSalir = true; sonando = false; pintar(); }
    else if (!d.hidden && pausadaPorSalir) { pausadaPorSalir = false; intentar(); }
  });
  pintar();
})();
