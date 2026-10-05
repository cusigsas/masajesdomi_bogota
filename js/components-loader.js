/* =========================================================
   Thera+Vida — components-loader.js
   Carga navbar, footer y botón flotante de WhatsApp.
   Requiere servidor local (Live Server); con file:// falla por CORS.
   ========================================================= */
(function () {
  const root = document.body.dataset.root || "";
  const slots = Array.from(document.querySelectorAll("[data-component]"));

  const load = async (slot) => {
    const name = slot.dataset.component;
    try {
      const res = await fetch(`${root}components/${name}.html`);
      if (!res.ok) throw new Error(res.status);
      const html = (await res.text()).replaceAll("{{ROOT}}", root);
      slot.outerHTML = html;
    } catch (err) {
      console.error(`No se pudo cargar el componente "${name}". ¿Estás usando Live Server?`, err);
    }
  };

  Promise.all(slots.map(load)).then(() => {
    window.__componentsLoaded = true;
    document.dispatchEvent(new CustomEvent("components:loaded"));
  });
})();
