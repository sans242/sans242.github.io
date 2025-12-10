---
layout: page
title: Protocol
subtitle: Execute sequence. Maintain order.
---

<style>
  /* FULL WIDTH RESET */
  .container-md, .container {
    max-width: 100% !important;
    padding: 0 !important;
    margin: 0 !important;
    width: 100% !important;
  }
  
  /* Remove default margins if any from page-content */
  .page-content { overflow-x: hidden; }

  /* MAIN LAYOUT WRAPPER */
  .protocol-layout {
    font-family: 'Open Sans', sans-serif;
    color: #e0e0e0;
    margin-top: 20px;
    width: 100%;
    position: relative;
    /* Create space for the fixed sidebar */
    padding-left: 320px; 
    padding-right: 40px;
    box-sizing: border-box;
  }

  /* REFS: FIXED SIDEBAR LEFT */
  .refs-container {
    position: fixed;
    top: 100px; /* Adjust based on navbar height, typically ~80px */
    left: 20px;
    width: 280px;
    background: #1a1a1a;
    border: 1px solid #333;
    border-radius: 8px;
    padding: 15px;
    z-index: 100;
    max-height: calc(100vh - 120px);
    overflow-y: auto;
    box-shadow: 0 4px 10px rgba(0,0,0,0.3);
  }

  /* HEADER & DATE */
  .header-section {
    display: flex;
    justify-content: flex-end;
    margin-bottom: 30px;
    padding-top: 20px;
  }

  h2.section-title {
    font-size: 1rem;
    margin-bottom: 10px;
    border-bottom: 1px solid #444;
    padding-bottom: 5px;
    color: #fff;
    font-weight: 700;
    margin-top: 0;
    text-transform: uppercase;
  }

  /* LINKS FORM */
  .add-link-form { display: flex; gap: 5px; margin-bottom: 15px; }
  .link-input { 
    background: #2d2d2d; border: 1px solid #444; color: #fff; 
    padding: 8px; border-radius: 4px; font-size: 0.85rem; width: 100%;
  }
  .add-btn { 
    background: #008AFF; color: white; border: none; padding: 0 12px; 
    border-radius: 4px; cursor: pointer; font-size: 1rem;
  }
  .add-btn:hover { background: #0077db; }

  .ref-list { list-style: none; padding: 0; margin: 0; }
  .ref-item { 
    background: #252525; border: 1px solid #333; padding: 10px; 
    margin-bottom: 8px; border-radius: 4px; display: flex; 
    justify-content: space-between; align-items: center; 
  }
  .ref-item:hover { background: #333; border-color: #555; }
  
  .ref-link-wrapper { overflow: hidden; display: flex; flex-direction: column; }
  .ref-title { font-weight: 600; color: #fff; font-size: 0.9rem; }
  .ref-url { font-size: 0.75rem; color: #008AFF; text-decoration: none; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; max-width: 190px; }
  
  .delete-btn { color: #666; background: none; border: none; cursor: pointer; font-size: 1.1rem; }
  .delete-btn:hover { color: #ff4444; }


  /* DATE PICKER */
  .date-wrapper {
    position: relative;
    display: flex;
    align-items: center;
    background: #1a1a1a;
    border: 1px solid #444;
    min-width: 250px;
    border-radius: 8px;
    padding: 0; /* Important for full coverage */
    z-index: 10;
    cursor: pointer;
  }
  .date-display-btn {
    color: #fff;
    padding: 10px 20px;
    font-size: 1.2rem;
    font-family: 'Montserrat', sans-serif;
    pointer-events: none; /* Text shouldn't block */
    display: flex;
    align-items: center;
    gap: 15px;
    width: 100%;
  }
  input[type="date"] {
    position: absolute;
    top: 0; left: 0;
    width: 100%; height: 100%;
    opacity: 0;
    z-index: 20; /* TOP LAYER */
    cursor: pointer;
    font-size: 1.2rem; /* Make the target area nice */
  }
  /* Fix for some browsers ignoring opacity on inputs */
  input[type="date"]::-webkit-calendar-picker-indicator {
    position: absolute;
    top: 0; left: 0;
    width: 100%; height: 100%;
    opacity: 0;
    cursor: pointer;
    background: transparent;
  }

  
  /* GRID LOGS */
  .log-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 30px;
    width: 100%;
  }
  /* Mobile stack */
  @media (max-width: 1100px) {
    .protocol-layout { padding-left: 20px; } /* Reset padding */
    .refs-container { position: relative; top: 0; left: 0; width: 100%; margin-bottom: 20px; max-height: none; }
    .log-grid { grid-template-columns: 1fr; }
  }

  .log-card {
    background: #1a1a1a;
    border: 1px solid #333;
    border-radius: 8px;
    padding: 25px;
    display: flex;
    flex-direction: column;
    min-height: 400px;
  }
  .card-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
  }
  .card-title {
    font-weight: 700;
    color: #fff;
    text-transform: uppercase;
    font-size: 1.2rem;
    letter-spacing: 0.05em;
  }
  
  /* STATUS */
  .status-toggle {
    cursor: pointer;
    font-size: 0.8rem;
    padding: 8px 16px;
    border-radius: 4px;
    background: #2d2d2d;
    color: #aeaeae;
    border: 1px solid #444;
    font-weight: 700;
    transition: all 0.2s;
    user-select: none;
    text-transform: uppercase;
    z-index: 30; /* Ensure clickability */
    position: relative;
  }
  .status-toggle:hover { background: #383838; color: #fff; border-color: #666; }
  .status-toggle.success { background: #1c4526; border-color: #2f855a; color: #48bb78; }
  .status-toggle.fail { background: #4a1c1c; border-color: #9b2c2c; color: #f56565; }

  textarea.category-note {
    width: 100%;
    flex-grow: 1; /* Fill remaining card space */
    background: #121212;
    border: 1px solid #333;
    border-radius: 6px;
    padding: 15px;
    color: #ddd;
    font-family: 'Courier New', monospace;
    font-size: 1rem;
    line-height: 1.6;
    resize: none; /* Clean look */
    z-index: 2;
  }
  textarea.category-note:focus { outline: none; border-color: #008AFF; }

  .relock-btn {
    display: block;
    margin: 40px auto;
    background: transparent;
    border: 1px solid #555;
    color: #666;
    padding: 8px 20px;
    border-radius: 4px;
    cursor: pointer;
    font-size: 0.9rem;
    z-index: 30;
    position: relative;
  }
  .relock-btn:hover { border-color: #888; color: #888; }
  
  /* Auth styles */
  #auth-overlay {
    position: fixed; top: 0; left: 0; width: 100%; height: 100%;
    background: #121212; z-index: 9999;
    display: flex; flex-direction: column;
    justify-content: center; align-items: center; color: #fff;
  }
  .auth-box {
    text-align: center; padding: 2rem; background: #1e1e1e;
    border-radius: 10px; border: 1px solid #333;
    box-shadow: 0 4px 12px rgba(0,0,0,0.5);
  }
  .auth-input {
    padding: 10px; background: #2d2d2d; border: 1px solid #444; color: #fff;
    border-radius: 5px; margin-bottom: 10px; width: 200px;
  }
  .auth-btn {
    padding: 10px 20px; background: #008AFF; color: white; border: none;
    border-radius: 5px; cursor: pointer;
  }
</style>

<div id="auth-overlay">
  <div class="auth-box">
    <h3>Restricted Access</h3>
    <p>Enter authorization code.</p>
    <input type="password" id="password-input" class="auth-input" placeholder="Auth Code">
    <br>
    <button onclick="checkPassword()" class="auth-btn">Authorize</button>
    <p id="error-msg" style="color:red; display:none; margin-top:10px;">Access Denied</p>
  </div>
</div>

<div class="protocol-layout" style="display: none;">

  <!-- REFS: FIXED LEFT SIDEBAR -->
  <div class="refs-container">
    <h2 class="section-title">📚 Study & Refs</h2>
    <div class="add-link-form">
      <input type="text" id="new-link-title" class="link-input" placeholder="Title">
      <input type="text" id="new-link-url" class="link-input" placeholder="URL">
      <button onclick="addNewLink()" class="add-btn">+</button>
    </div>
    <ul class="ref-list" id="ref-list"></ul>
  </div>

  <!-- MAIN CONTENT -->
  <div class="header-section">
    <div class="date-wrapper">
      <div class="date-display-btn">
        <span style="opacity: 0.7;">📅</span>
        <span id="formatted-date">Loading date...</span>
      </div>
      <input type="date" id="note-date">
    </div>
  </div>

  <div class="log-grid">
    <!-- PROBABILITY -->
    <div class="log-card">
      <div class="card-header">
        <span class="card-title">Probability</span>
        <button class="status-toggle" id="toggle-prob" onclick="toggleStatus('probability')">SET STATUS</button>
      </div>
      <textarea id="note-probability" class="category-note" placeholder="Log probability progress..."></textarea>
    </div>

    <!-- DSA -->
    <div class="log-card">
      <div class="card-header">
        <span class="card-title">DSA</span>
        <button class="status-toggle" id="toggle-dsa" onclick="toggleStatus('dsa')">SET STATUS</button>
      </div>
      <textarea id="note-dsa" class="category-note" placeholder="Log DSA progress..."></textarea>
    </div>

    <!-- PROJECT -->
    <div class="log-card">
      <div class="card-header">
        <span class="card-title">Project</span>
        <button class="status-toggle" id="toggle-project" onclick="toggleStatus('project')">SET STATUS</button>
      </div>
      <textarea id="note-project" class="category-note" placeholder="Log project updates..."></textarea>
    </div>
  </div>

  <button onclick="relockProtocol()" class="relock-btn">🔒 Relock</button>
</div>

<script>
  // --- AUTH ---
  const CORRECT_PASSWORD = "password123";
  const authOverlay = document.getElementById('auth-overlay');
  const passwordInput = document.getElementById('password-input');
  const mainContainer = document.querySelector('.protocol-layout');

  function checkPassword() {
    if (passwordInput.value === CORRECT_PASSWORD) {
      unlockPage();
    } else {
      document.getElementById('error-msg').style.display = 'block';
    }
  }
  function unlockPage() {
    authOverlay.style.display = 'none';
    mainContainer.style.display = 'block';
    localStorage.setItem('routineAuth', 'true');
    initPage();
  }
  function relockProtocol() {
    localStorage.removeItem('routineAuth');
    location.reload();
  }
  if (localStorage.getItem('routineAuth') === 'true') unlockPage();

  // --- INIT ---
  function initPage() {
    loadLinks();
    initDate();
  }

  // --- DATE LOGIC ---
  const dateInput = document.getElementById('note-date');
  const dateDisplay = document.getElementById('formatted-date');
  
  const els = {
    probability: { note: document.getElementById('note-probability'), status: document.getElementById('toggle-prob') },
    dsa: { note: document.getElementById('note-dsa'), status: document.getElementById('toggle-dsa') },
    project: { note: document.getElementById('note-project'), status: document.getElementById('toggle-project') },
  };

  function initDate() {
    const today = new Date();
    // Ensure we set the input value correctly to today YYYY-MM-DD
    const yyyy = today.getFullYear();
    const mm = String(today.getMonth() + 1).padStart(2, '0');
    const dd = String(today.getDate()).padStart(2, '0');
    const isoDate = `${yyyy}-${mm}-${dd}`;
    
    dateInput.value = isoDate;
    updateDateDisplay(isoDate);
    loadDataForDate(isoDate);
  }

  function updateDateDisplay(dateString) {
    if(!dateString) return;
    // Create date from YYYY-MM-DD (append time to avoid UTC shift)
    const dateObj = new Date(dateString + 'T12:00:00'); 
    
    const options = { day: 'numeric', month: 'long', year: 'numeric' };
    dateDisplay.textContent = dateObj.toLocaleDateString('en-GB', options);
  }

  // Handle Input Changes
  function onDateChange(e) {
    const val = e.target.value;
    if(val) {
        updateDateDisplay(val);
        loadDataForDate(val);
    }
  }
  
  // Listen for both input (immediate) and change (commit)
  dateInput.addEventListener('input', onDateChange);
  dateInput.addEventListener('change', onDateChange);

  // --- DATA ---
  function getNoteKey(date) { return `protocol_data_${date}`; }

  function loadDataForDate(date) {
    const json = localStorage.getItem(getNoteKey(date));
    const data = json ? JSON.parse(json) : {};
    ['probability', 'dsa', 'project'].forEach(cat => {
      const entry = data[cat] || { text: '', status: 'neutral' };
      els[cat].note.value = entry.text || '';
      renderStatus(cat, entry.status);
    });
  }

  function saveData() {
    const date = dateInput.value;
    if(!date) return;
    
    const data = {};
    ['probability', 'dsa', 'project'].forEach(cat => {
      data[cat] = {
        text: els[cat].note.value,
        status: els[cat].status.getAttribute('data-status') || 'neutral'
      };
    });
    localStorage.setItem(getNoteKey(date), JSON.stringify(data));
  }

  ['probability', 'dsa', 'project'].forEach(cat => {
    els[cat].note.addEventListener('input', saveData);
  });

  // --- TOGGLES ---
  function toggleStatus(cat) {
    const btn = els[cat].status;
    let current = btn.getAttribute('data-status') || 'neutral';
    let next = current === 'neutral' ? 'success' : (current === 'success' ? 'fail' : 'neutral');
    renderStatus(cat, next);
    saveData();
  }

  function renderStatus(cat, status) {
    const btn = els[cat].status;
    btn.setAttribute('data-status', status);
    btn.classList.remove('success', 'fail');
    
    if (status === 'neutral') {
      btn.textContent = 'SET STATUS';
      btn.style.color = '#aeaeae';
    } else if (status === 'success') {
      btn.textContent = 'RIGHT';
      btn.classList.add('success');
      btn.style.color = '';
    } else if (status === 'fail') {
      btn.textContent = 'WRONG';
      btn.classList.add('fail');
      btn.style.color = '';
    }
  }

  // --- LINKS ---
  function loadLinks() {
    const list = document.getElementById('ref-list');
    const links = JSON.parse(localStorage.getItem('protocol_links')) || [];
    list.innerHTML = '';
    links.forEach((link, idx) => {
      let displayUrl = link.url.length > 30 ? link.url.substring(0, 27) + '...' : link.url;
      list.innerHTML += `
      <li class="ref-item">
        <div class="ref-link-wrapper">
          <span class="ref-title">${link.title}</span>
          <a href="${link.url}" target="_blank" class="ref-url" title="${link.url}">${displayUrl}</a>
        </div>
        <button onclick="deleteLink(${idx})" class="delete-btn">×</button>
      </li>`;
    });
  }
  function addNewLink() {
    const t = document.getElementById('new-link-title').value.trim();
    let u = document.getElementById('new-link-url').value.trim();
    if(!t || !u) return;
    if(!u.startsWith('http')) u = 'https://' + u;
    const links = JSON.parse(localStorage.getItem('protocol_links')) || [];
    links.push({ title: t, url: u });
    localStorage.setItem('protocol_links', JSON.stringify(links));
    document.getElementById('new-link-title').value = '';
    document.getElementById('new-link-url').value = '';
    loadLinks();
  }
  function deleteLink(idx) {
    const links = JSON.parse(localStorage.getItem('protocol_links')) || [];
    links.splice(idx, 1);
    localStorage.setItem('protocol_links', JSON.stringify(links));
    loadLinks();
  }
</script>
