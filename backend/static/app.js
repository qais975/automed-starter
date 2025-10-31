async function fetchIntro() {
  const res = await fetch('/api/persona/intro');
  return await res.json();
}

function pickFemaleVoice() {
  const vs = speechSynthesis.getVoices();
  const choices = vs.filter(v =>
    /en/i.test(v.lang) && /(female|woman|samantha|victoria|serena|karen|moira|zira|linda)/i.test(v.name)
  );
  return (choices[0] || vs.find(v => /en/i.test(v.lang)) || vs[0]);
}

function speakLines(linesEN, linesAR, onSubtitle, onEnd) {
  speechSynthesis.cancel();
  const voice = pickFemaleVoice();
  let i = 0;
  const speakNext = () => {
    if (i >= linesEN.length) { onSubtitle("✓ Finished. Automed — Launching soon."); onEnd?.(); return; }
    const en = linesEN[i], ar = linesAR[i] || "";
    onSubtitle(ar);
    const u = new SpeechSynthesisUtterance(en);
    u.voice = voice; u.rate = 0.98; u.pitch = 1.05; u.volume = 1.0;
    u.onend = () => { i++; setTimeout(speakNext, 350); };
    speechSynthesis.speak(u);
  };
  speakNext();
}

window.addEventListener('load', async () => {
  speechSynthesis.onvoiceschanged = () => {};
  const sub = document.getElementById('subtitle');
  const data = await fetchIntro();
  document.getElementById('playBtn').onclick = () => {
    speakLines(data.en, data.ar, (t)=> sub.textContent = t);
  };
  document.getElementById('stopBtn').onclick = () => {
    speechSynthesis.cancel();
    sub.textContent = "Stopped.";
  };
});
