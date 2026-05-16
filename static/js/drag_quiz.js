/* drag_quiz.js — One-at-a-time quiz engine */

const state = {
  answers:      {},
  currentSlide: 0,
  totalSlides:  0,
};

document.addEventListener("DOMContentLoaded", () => {
  state.totalSlides = window.TOTAL_QUESTIONS || 0;
  initAllSlides();
  updateDots();
  updateCounter();
});

function initAllSlides() {
  document.querySelectorAll(".question-slide").forEach(slide => {
    initChipsOnSlide(slide);
    initDropTarget(slide);
  });
}

function initChipsOnSlide(slide) {
  slide.querySelectorAll(".option-chip").forEach(chip => {
    chip.addEventListener("dragstart", e => {
      chip.classList.add("dragging");
      e.dataTransfer.effectAllowed = "move";
      e.dataTransfer.setData("text/plain", chip.dataset.label);
    });
    chip.addEventListener("dragend", () => chip.classList.remove("dragging"));
    chip.addEventListener("touchstart", handleTouchStart, { passive: true });
    chip.addEventListener("touchmove",  handleTouchMove,  { passive: false });
    chip.addEventListener("touchend",   handleTouchEnd,   { passive: true });
  });
}

function initDropTarget(slide) {
  const zone = slide.querySelector(".drop-target");
  if (!zone) return;
  zone.addEventListener("dragover",  e => { e.preventDefault(); zone.classList.add("drag-over"); });
  zone.addEventListener("dragleave", () => zone.classList.remove("drag-over"));
  zone.addEventListener("drop", e => {
    e.preventDefault();
    zone.classList.remove("drag-over");
    const label    = e.dataTransfer.getData("text/plain");
    const qid      = zone.dataset.qid;
    const slideIdx = parseInt(slide.dataset.index);
    placeAnswer(zone, qid, slideIdx, label);
  });
}

function placeAnswer(zone, qid, slideIdx, label) {
  const old = zone.dataset.answer;
  if (old && old !== label) {
    const oldChip = document.querySelector(`#slide-${slideIdx} .option-chip[data-label="${CSS.escape(old)}"]`);
    if (oldChip) oldChip.classList.remove("used");
  }

  zone.querySelector(".drop-ghost").classList.add("hidden");
  const placed = zone.querySelector(".placed-answer");
  placed.textContent = label;
  placed.classList.remove("hidden");
  zone.querySelector(".remove-btn").classList.remove("hidden");
  zone.classList.add("has-answer");
  zone.dataset.answer = label;

  const chip = document.querySelector(`#slide-${slideIdx} .option-chip[data-label="${CSS.escape(label)}"]`);
  if (chip) chip.classList.add("used");

  state.answers[qid] = label;
  unlockNext(slideIdx);
  updateProgress();
  updateDots();
  updateCounter();
}

function clearAnswer(qid, slideIdx) {
  const zone = document.getElementById("drop-" + qid);
  const old  = zone.dataset.answer;
  if (old) {
    const chip = document.querySelector(`#slide-${slideIdx} .option-chip[data-label="${CSS.escape(old)}"]`);
    if (chip) chip.classList.remove("used");
  }
  zone.querySelector(".drop-ghost").classList.remove("hidden");
  zone.querySelector(".placed-answer").classList.add("hidden");
  zone.querySelector(".remove-btn").classList.add("hidden");
  zone.classList.remove("has-answer");
  delete zone.dataset.answer;
  delete state.answers[qid];
  lockNext(slideIdx);
  updateProgress();
  updateDots();
  updateCounter();
}

function unlockNext(slideIdx) {
  const btn = document.getElementById("next-" + slideIdx)
           || (slideIdx === state.totalSlides - 1 ? document.getElementById("submit-btn") : null);
  if (btn) btn.disabled = false;
}
function lockNext(slideIdx) {
  const btn = document.getElementById("next-" + slideIdx)
           || (slideIdx === state.totalSlides - 1 ? document.getElementById("submit-btn") : null);
  if (btn) btn.disabled = true;
}

function goToSlide(idx) {
  const slides = document.querySelectorAll(".question-slide");
  const dir    = idx > state.currentSlide ? "forward" : "back";

  slides[state.currentSlide].classList.add("slide-out-" + dir);
  setTimeout(() => {
    slides[state.currentSlide].classList.remove("active", "slide-out-" + dir);
    slides[idx].classList.add("slide-in-" + dir, "active");
    setTimeout(() => slides[idx].classList.remove("slide-in-" + dir), 350);
    state.currentSlide = idx;
    updateCounter();
    updateDots();
    document.getElementById("stage").scrollTop = 0;
  }, 200);
}

function updateProgress() {
  const answered = Object.keys(state.answers).length;
  document.getElementById("progress-bar").style.width = (answered / state.totalSlides * 100) + "%";
  document.getElementById("live-score").textContent   = answered;
}

function updateDots() {
  document.querySelectorAll(".dot").forEach((dot, i) => {
    const slide = document.getElementById("slide-" + i);
    const qid   = slide ? slide.dataset.qid : null;
    dot.className = "dot";
    if (qid && state.answers[qid]) dot.classList.add("answered");
    if (i === state.currentSlide)  dot.classList.add("current");
  });
}

function updateCounter() {
  const el = document.getElementById("q-counter");
  if (el) el.innerHTML = `Question <strong>${state.currentSlide + 1}</strong> of ${state.totalSlides}`;
}

/* ── Touch drag ── */
let _touchChip = null, _touchClone = null;

function handleTouchStart(e) {
  _touchChip  = e.currentTarget;
  _touchClone = _touchChip.cloneNode(true);
  Object.assign(_touchClone.style, {
    position: "fixed", pointerEvents: "none", zIndex: 9999,
    opacity: "0.85", transform: "scale(1.1)", transition: "none",
    boxShadow: "0 8px 24px rgba(0,0,0,0.3)",
  });
  document.body.appendChild(_touchClone);
  _moveTouchClone(e.touches[0]);
}
function handleTouchMove(e) {
  e.preventDefault();
  _moveTouchClone(e.touches[0]);
  document.querySelectorAll(".drop-target").forEach(z => z.classList.remove("drag-over"));
  const el   = document.elementFromPoint(e.touches[0].clientX, e.touches[0].clientY);
  const zone = el ? el.closest(".drop-target") : null;
  if (zone) zone.classList.add("drag-over");
}
function handleTouchEnd(e) {
  if (_touchClone) { _touchClone.remove(); _touchClone = null; }
  document.querySelectorAll(".drop-target").forEach(z => z.classList.remove("drag-over"));
  const touch = e.changedTouches[0];
  const el    = document.elementFromPoint(touch.clientX, touch.clientY);
  const zone  = el ? el.closest(".drop-target") : null;
  if (zone && _touchChip) {
    const slide    = _touchChip.closest(".question-slide");
    placeAnswer(zone, zone.dataset.qid, parseInt(slide.dataset.index), _touchChip.dataset.label);
  }
  _touchChip = null;
}
function _moveTouchClone(touch) {
  if (!_touchClone) return;
  _touchClone.style.left = (touch.clientX - 55) + "px";
  _touchClone.style.top  = (touch.clientY - 24) + "px";
}

/* ── Submit & Results ── */
async function submitQuiz() {
  const btn = document.getElementById("submit-btn");
  btn.disabled = true; btn.textContent = "Submitting…";
  const answersArray = Object.entries(state.answers).map(([qid, answer]) => ({
    question_id: parseInt(qid), answer,
  }));
  try {
    const resp = await fetch("/submit", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ answers: answersArray }),
    });
    if (!resp.ok) throw new Error("Server " + resp.status);
    showResults(await resp.json());
  } catch (err) {
    alert("Submission failed. Please try again.\n" + err.message);
    btn.disabled = false; btn.textContent = "Submit ✓";
  }
}

function showResults(data) {
  const passClass = data.passed ? "pass" : "fail";
  const qMap = {};
  (window.QUIZ_QUESTIONS || []).forEach(q => { qMap[q.id] = q; });

  const rows = data.results.map(r => {
    const q = qMap[r.question_id] || {};
    const imgHtml = q.image_path
      ? `<img src="/static/${q.image_path}" class="res-img" alt="" onerror="this.style.display='none'">`
      : `<div class="res-img-placeholder">📋</div>`;
    return `
      <div class="res-row ${r.correct ? "ok" : "no"}">
        ${imgHtml}
        <div class="res-info">
          <p class="res-prompt">${q.prompt || ""}</p>
          <p>Your answer: <strong>${r.given_answer || "—"}</strong></p>
          <p>Correct: <strong>${r.correct_answer}</strong></p>
          <span class="res-badge ${r.correct ? "badge-ok" : "badge-no"}">
            ${r.correct ? "✓ Correct" : "✗ Wrong"}
          </span>
        </div>
      </div>`;
  }).join("");

  document.querySelector("main").innerHTML = `
    <div class="results-page">
      <div class="score-hero ${passClass}">
        <div class="score-big">${data.score}<span class="score-denom">/${data.total}</span></div>
        <div class="score-pct">${data.percentage}%</div>
        <div class="pass-pill ${passClass}">${data.passed ? "PASS" : "FAIL"}</div>
        <p class="pass-sub">${data.passed ? "Excellent! You passed." : "Keep practising — you can do it!"}</p>
      </div>
      <h3 class="breakdown-hd">Question Breakdown</h3>
      <div class="res-list">${rows}</div>
      <div class="res-actions">
        <a href="/quiz" class="btn-redo">🔁 Try Again</a>
        <a href="/" class="btn-home2">🏠 Home</a>
      </div>
    </div>`;
}
