/* AdSense auto ads — 페이지 로드마다 한 번씩 push */
(function () {
  if (typeof adsbygoogle === "undefined") return;
  document.querySelectorAll("ins.adsbygoogle").forEach(function (el) {
    if (el.getAttribute("data-adsbygoogle-status")) return;
    try {
      (adsbygoogle = window.adsbygoogle || []).push({});
    } catch (e) {
      console.warn("AdSense push failed:", e);
    }
  });
})();
