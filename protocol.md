---
layout: page
title: Protocol
subtitle: Execute sequence. Maintain order.
---

<style>
  /* FULL WIDTH LAYOUT */
  .container-md, .container {
    max-width: 100% !important;
    padding-left: 40px !important; 
    padding-right: 40px !important;
    margin: 0 !important;
  }
  
  /* Reset page wrapper if it exists in theme */
  .page-content {
    width: 100%;
  }

  .protocol-layout {
    display: flex;
    gap: 40px;
    font-family: 'Open Sans', sans-serif;
    color: #e0e0e0;
    margin-top: 20px;
    width: 100%;
  }
  
  /* LEFT SIDEBAR: REFERENCES */
  .sidebar-section {
    flex: 0 0 280px;
    padding-right: 20px;
    border-right: 1px solid #333;
  }

  /* RIGHT MAIN: DAILY LOG */
  .main-section {
    flex: 1;
    min-width: 0;
  }

  /* Section Headers */
  h2.section-title {
    font-size: 1.25rem;
    margin-bottom: 20px;
    border-bottom: 1px solid #444;
    padding-bottom: 5px;
    color: #fff;
    font-weight: 600;
    margin-top: 0;
  }

  /* DYNAMIC LINKS */
  .add-link-form {
    display: flex;
    flex-direction: column;
    gap: 10px;
    margin-bottom: 20px;
  }
  .link-input {
    background: #2d2d2d;
    border: 1px solid #444;
    color: #fff;
    padding: 8px 12px;
    border-radius: 4px;
    font-size: 0.9rem;
  }
  .add-btn {
    background: #008AFF;
    color: white;
    border: none;
    padding: 8px;
    border-radius: 4px;
    cursor: pointer;
    font-size: 0.9rem;
    transition: background 0.2s;
  }
  .add-btn:hover { background: #0077db; }

  .ref-list {
    list-style: none;
    padding: 0;
  }
  .ref-item {
    background: #1a1a1a;
    border: 1px solid #333;
    padding: 10px;
    margin-bottom: 8px;
    border-radius: 6px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    transition: all 0.2s;
  }
  .ref-item:hover { background: #252525; }
  
  .ref-link-wrapper {
    overflow: hidden;
  }
  .ref-title {
    display: block;
    font-weight: 600;
    color: #fff;
    font-size: 0.95rem;
  }
  .ref-url {
    display: block;
    font-size: 0.75rem;
    color: #008AFF;
    text-decoration: none;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    max-width: 180px;
  }
  .ref-url:hover { text-decoration: underline; }
  
  .delete-btn {
    background: transparent;
    border: none;
    color: #666;
    cursor: pointer;
    font-size: 1.2rem;
    padding: 0 5px;
    line-height: 1;
  }
  .delete-btn:hover { color: #ff4444; }


  /* LOG CONTROLS & DATE */
  .log-header {
    display: flex; /* Align items horizontally */
    align-items: center; /* Center items vertically */
    justify-content: flex-end; /* Push to the right */
    margin-bottom: 20px;
    background: transparent;
  }
  
  /* Custom Date Picker */
  .date-wrapper {
    position: relative;
    display: inline-block;
  }
  .date-display-btn {
    background: #1a1a1a;
    border: 1px solid #444;
    color: #fff;
    padding: 10px 20px;
    border-radius: 8px;
    font-size: 1.2rem;
    font-family: 'Montserrat', sans-serif;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 10px;
  }
  .date-display-btn:hover {
    border-color: #008AFF;
  }
  /* Hide real input but cover the button */
  input[type="date"] {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    opacity: 0;
    cursor: pointer;
    z-index: 2;
  }
  
  /* GRID FOR 3 CATEGORIES */
  .log-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
  }
  @media (max-width: 992px) {
    .log-grid { grid-template-columns: 1fr; }
    .sidebar-section { flex: none; width: 100%; border-right: none; border-bottom: 1px solid #333; padding-bottom: 20px; }
    .protocol-layout { flex-direction: column; }
  }

  .log-card {
    background: #1a1a1a;
    border: 1px solid #333;
    border-radius: 8px;
    padding: 20px;
    display: flex;
    flex-direction: column;
  }
  .card-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 15px;
  }
  .card-title {
    font-weight: 700;
    color: #fff;
    text-transform: uppercase;
    font-size: 1.1rem;
    letter-spacing: 0.05em;
  }
  
  /* STATUS TOGGLE */
  .status-toggle {
    cursor: pointer;
    font-size: 0.75rem;
    padding: 6px 12px;
    border-radius: 4px;
    background: #2d2d2d;
    color: #888;
    border: 1px solid #444;
    font-weight: 600;
    transition: all 0.3s;
    user-select: none;
    text-transform: uppercase;
  }
  .status-toggle:hover {
    border-color: #666;
  }
  .status-toggle.success {
    background: #1c4526;
    border-color: #2f855a;
    color: #48bb78;
  }
  .status-toggle.fail {
    background: #4a1c1c;
    border-color: #9b2c2c;
    color: #f56565;
  }

  textarea.category-note {
    width: 100%;
    height: 200px; /* Taller notes */
    background: #121212;
    border: 1px solid #333;
    border-radius: 4px;
    padding: 12px;
    color: #ddd;
    font-family: 'Courier New', monospace;
    font-size: 0.95rem;
    line-height: 1.5;
    resize: vertical;
  }
  textarea.category-note:focus {
    outline: none;
    border-color: #008AFF;
  }

  .relock-btn {
    display: block;
    margin: 40px auto 10px;
    background: transparent;
    border: 1px solid #555;
    color: #666;
    padding: 5px 15px;
    border-radius: 4px;
    cursor: pointer;
    font-size: 0.8rem;
  }
  .relock-btn:hover { border-color: #888; color: #888; }
  
  /* Auth styles */
  #auth-overlay {
    position: fixed; top: 0; left: 0; width: 100%; height: 100%;
    background: #121212; z-index: 1000;
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

  <!-- LEFT SIDEBAR: STUDY MATERIAL -->
  <aside class="sidebar-section">
    <h2 class="section-title">📚 Study & Refs</h2>
    
    <div class="add-link-form">
      <input type="text" id="new-link-title" class="link-input" placeholder="Title (e.g. Blitzstein)">
      <input type="text" id="new-link-url" class="link-input" placeholder="URL">
      <button onclick="addNewLink()" class="add-btn">Add Link</button>
    </div>

    <ul class="ref-list" id="ref-list">
      <!-- Dynamic Links JS -->
    </ul>
  </aside>

  <!-- RIGHT MAIN: DAILY LOG -->
  <main class="main-section">
    <div class="log-header">
      
      <!-- Custom Date Picker -->
      <div class="date-wrapper">
        <div class="date-display-btn">
          <span style="opacity: 0.7;">📅</span>
          <span id="formatted-date">Select Date</span>
        </div>
        <input type="date" id="note-date">
      </div>

    </div>

    <div class="log-grid">
      
      <!-- CARD 1: PROBABILITY -->
      <div class="log-card">
        <div class="card-header">
          <span class="card-title">Probability</span>
          <button class="status-toggle" id="toggle-prob" onclick="toggleStatus('probability')" title="Click to change status">SET STATUS</button>
        </div>
        <textarea id="note-probability" class="category-note" placeholder="Log probability progress..."></textarea>
      </div>

      <!-- CARD 2: DSA -->
      <div class="log-card">
        <div class="card-header">
          <span class="card-title">DSA</span>
          <button class="status-toggle" id="toggle-dsa" onclick="toggleStatus('dsa')" title="Click to change status">SET STATUS</button>
        </div>
        <textarea id="note-dsa" class="category-note" placeholder="Log DSA progress..."></textarea>
      </div>

      <!-- CARD 3: PROJECT -->
      <div class="log-card">
        <div class="card-header">
          <span class="card-title">Project</span>
          <button class="status-toggle" id="toggle-project" onclick="toggleStatus('project')" title="Click to change status">SET STATUS</button>
        </div>
        <textarea id="note-project" class="category-note" placeholder="Log project updates..."></textarea>
      </div>

    </div>

    <button onclick="relockProtocol()" class="relock-btn">🔒 Relock</button>
  </main>
  
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
    mainContainer.style.display = 'flex';
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

  // --- DATE & NOTES LOGIC ---
  const dateInput = document.getElementById('note-date');
  const dateDisplay = document.getElementById('formatted-date');
  
  // Elements
  const els = {
    probability: { note: document.getElementById('note-probability'), status: document.getElementById('toggle-prob') },
    dsa: { note: document.getElementById('note-dsa'), status: document.getElementById('toggle-dsa') },
    project: { note: document.getElementById('note-project'), status: document.getElementById('toggle-project') },
  };

  function initDate() {
    const today = new Date();
    // Default to today
    setDate(today);
  }

  function setDate(dateObj) {
    const yyyy = dateObj.getFullYear();
    const mm = String(dateObj.getMonth() + 1).padStart(2, '0');
    const dd = String(dateObj.getDate()).padStart(2, '0');
    const dateStr = `${yyyy}-${mm}-${dd}`;
    
    dateInput.value = dateStr;
    updateDateDisplay(dateObj);
    loadDataForDate(dateStr);
  }

  function updateDateDisplay(dateObj) {
    // Format: 11 December 2025
    const options = { day: 'numeric', month: 'long', year: 'numeric' };
    dateDisplay.textContent = dateObj.toLocaleDateString('en-GB', options);
  }

  dateInput.addEventListener('change', (e) => {
    // Handle manual date picker change
    if(e.target.value) {
        const parts = e.target.value.split('-');
        const newDate = new Date(parts[0], parts[1]-1, parts[2]);
        updateDateDisplay(newDate);
        loadDataForDate(e.target.value);
    }
  });

  // --- DATA SAVING/LOADING ---
  function getNoteKey(date) { return `protocol_data_${date}`; }

  function loadDataForDate(date) {
    const json = localStorage.getItem(getNoteKey(date));
    const data = json ? JSON.parse(json) : {};
    
    // Categories: probability, dsa, project
    ['probability', 'dsa', 'project'].forEach(cat => {
      const entry = data[cat] || { text: '', status: 'neutral' };
      els[cat].note.value = entry.text || '';
      renderStatus(cat, entry.status);
    });
  }

  function saveData(date) {
    const data = {};
    ['probability', 'dsa', 'project'].forEach(cat => {
      const currentStatus = els[cat].status.getAttribute('data-status') || 'neutral';
      data[cat] = {
        text: els[cat].note.value,
        status: currentStatus
      };
    });
    localStorage.setItem(getNoteKey(date), JSON.stringify(data));
  }

  // Saving triggers
  ['probability', 'dsa', 'project'].forEach(cat => {
    els[cat].note.addEventListener('input', () => saveData(dateInput.value));
  });

  // --- STATUS TOGGLES ---
  function toggleStatus(cat) {
    const btn = els[cat].status;
    let current = btn.getAttribute('data-status') || 'neutral';
    
    // Cycle: neutral -> success -> fail -> neutral
    let next = 'neutral';
    if (current === 'neutral') next = 'success';
    else if (current === 'success') next = 'fail';
    else if (current === 'fail') next = 'neutral';
    
    renderStatus(cat, next);
    saveData(dateInput.value);
  }

  function renderStatus(cat, status) {
    const btn = els[cat].status;
    btn.setAttribute('data-status', status);
    btn.classList.remove('success', 'fail');
    
    if (status === 'neutral') {
      btn.textContent = 'SET STATUS';
      btn.style.color = '#888';
    } else if (status === 'success') {
      btn.textContent = 'RIGHT';
      btn.classList.add('success');
      btn.style.color = ''; // use class color
    } else if (status === 'fail') {
      btn.textContent = 'WRONG';
      btn.classList.add('fail');
      btn.style.color = ''; // use class color
    }
  }

  // --- LINKS ---
  function loadLinks() {
    const list = document.getElementById('ref-list');
    const links = JSON.parse(localStorage.getItem('protocol_links')) || [];
    list.innerHTML = '';
    
    links.forEach((link, idx) => {
      list.innerHTML += `
      <li class="ref-item">
        <div class="ref-link-wrapper">
          <span class="ref-title">${link.title}</span>
          <a href="${link.url}" target="_blank" class="ref-url" title="${link.url}">${link.url}</a>
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
