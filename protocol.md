---
layout: page
title: Protocol
subtitle: Execute sequence. Maintain order.
---

<style>
  .protocol-container {
    max-width: 700px;
    margin: 0 auto;
    font-family: 'Open Sans', sans-serif;
    color: #e0e0e0; /* Light text for dark mode */
  }
  
  /* Section Headers */
  h2.section-title {
    font-size: 1.5rem;
    margin-top: 40px;
    margin-bottom: 20px;
    border-bottom: 1px solid #444;
    padding-bottom: 10px;
    color: #fff;
  }

  /* Dynamic Links Section */
  .add-link-form {
    display: flex;
    gap: 10px;
    margin-bottom: 20px;
    background: #1a1a1a;
    padding: 15px;
    border-radius: 8px;
    border: 1px solid #333;
  }
  .link-input {
    background: #2d2d2d;
    border: 1px solid #444;
    color: #fff;
    padding: 8px 12px;
    border-radius: 4px;
    flex-grow: 1;
  }
  .add-btn {
    background: #008AFF;
    color: white;
    border: none;
    padding: 8px 20px;
    border-radius: 4px;
    cursor: pointer;
  }
  .add-btn:hover {
    background: #0077db;
  }

  .ref-list {
    list-style: none;
    padding: 0;
  }
  .ref-item {
    background: #1a1a1a;
    border: 1px solid #333;
    padding: 15px;
    margin-bottom: 10px;
    border-radius: 8px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    transition: all 0.2s ease;
  }
  .ref-item:hover {
    border-color: #555;
    background: #252525;
  }
  .ref-link-wrapper {
    display: flex;
    flex-direction: column;
  }
  .ref-title {
    font-weight: 600;
    color: #fff;
  }
  .ref-url {
    font-size: 0.8rem;
    color: #888;
  }
  .delete-btn {
    background: transparent;
    border: 1px solid #555;
    color: #888;
    padding: 5px 10px;
    border-radius: 4px;
    cursor: pointer;
    font-size: 0.8rem;
  }
  .delete-btn:hover {
    border-color: #ff4444;
    color: #ff4444;
  }

  /* Daily Notes Section */
  .notes-controls {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 15px;
  }
  input[type="date"] {
    background: #2d2d2d;
    padding: 8px 12px;
    border: 1px solid #444;
    border-radius: 5px;
    font-family: inherit;
    font-size: 1rem;
    color: #fff;
    color-scheme: dark; /* Standard property for date picker in dark mode */
  }
  .save-indicator {
    font-size: 0.85rem;
    color: #888;
    font-style: italic;
    opacity: 0;
    transition: opacity 0.3s;
  }
  .save-indicator.visible {
    opacity: 1;
    color: #48bb78;
  }
  
  textarea.daily-note {
    width: 100%;
    height: 300px;
    padding: 15px;
    border: 1px solid #333;
    border-radius: 8px;
    font-family: 'Courier New', Courier, monospace;
    font-size: 1rem;
    line-height: 1.6;
    resize: vertical;
    background: #1a1a1a;
    color: #e0e0e0;
    box-shadow: inset 0 2px 4px rgba(0,0,0,0.2);
  }
  textarea.daily-note:focus {
    outline: none;
    border-color: #008AFF;
  }

  /* Auth UI (Dark Mode) */
  #auth-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: #121212;
    z-index: 1000;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    color: #fff;
  }
  .auth-box {
    text-align: center;
    padding: 2rem;
    background: #1e1e1e;
    border-radius: 10px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.5);
    border: 1px solid #333;
  }
  .auth-input {
    padding: 10px;
    background: #2d2d2d;
    border: 1px solid #444;
    border-radius: 5px;
    margin-bottom: 10px;
    width: 200px;
    color: #fff;
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
  .relock-btn:hover {
    border-color: #888;
    color: #888;
  }
</style>

<!-- Auth Overlay -->
<div id="auth-overlay">
  <div class="auth-box">
    <h3>Restricted Access</h3>
    <p>Enter authorization code to access protocol.</p>
    <input type="password" id="password-input" class="auth-input" placeholder="Auth Code">
    <br>
    <button onclick="checkPassword()" class="auth-btn">Authorize</button>
    <p id="error-msg" class="error-msg">Access Denied</p>
  </div>
</div>

<!-- Main Container - HIDDEN BY DEFAULT -->
<div class="protocol-container" style="display: none;">

  <!-- REFERENCES SECTION -->
  <h2 class="section-title">📚 Study Material & References</h2>
  
  <div class="add-link-form">
    <input type="text" id="new-link-title" class="link-input" placeholder="Title (e.g. Docs)">
    <input type="text" id="new-link-url" class="link-input" placeholder="URL (e.g. https://...)">
    <button onclick="addNewLink()" class="add-btn">Add</button>
  </div>

  <ul class="ref-list" id="ref-list">
    <!-- Links will be injected here JS -->
  </ul>

  <!-- DAILY NOTES SECTION -->
  <h2 class="section-title">📝 Daily Log</h2>
  
  <div class="notes-controls">
    <input type="date" id="note-date">
    <span id="save-indicator" class="save-indicator">Saved locally</span>
  </div>
  
  <textarea id="daily-note" class="daily-note" placeholder="Log your activities, thoughts, and progress for today..."></textarea>

  <button onclick="relockProtocol()" class="relock-btn">🔒 Relock Protocol</button>

</div>

<script>
  // --- PASSWORD PROTECTION ---
  const CORRECT_PASSWORD = "password123"; 
  const authOverlay = document.getElementById('auth-overlay');
  const passwordInput = document.getElementById('password-input');
  const errorMsg = document.getElementById('error-msg');
  const mainContainer = document.querySelector('.protocol-container');

  function checkPassword() {
    const input = passwordInput.value;
    if (input === CORRECT_PASSWORD) {
      unlockPage();
    } else {
      errorMsg.style.display = 'block';
    }
  }

  function unlockPage() {
    authOverlay.style.display = 'none';
    mainContainer.style.display = 'block';
    localStorage.setItem('routineAuth', 'true');
    initPage(); // Initialize everything after unlock
  }

  function relockProtocol() {
    localStorage.removeItem('routineAuth');
    location.reload();
  }

  if (localStorage.getItem('routineAuth') === 'true') {
    unlockPage();
  }

  // --- INITIALIZATION ---
  function initPage() {
    initNotes();
    loadLinks();
  }

  // --- DYNAMIC LINKS LOGIC ---
  const refListEl = document.getElementById('ref-list');
  const titleInput = document.getElementById('new-link-title');
  const urlInput = document.getElementById('new-link-url');

  function getLinks() {
    return JSON.parse(localStorage.getItem('protocol_links')) || [];
  }

  function saveLinks(links) {
    localStorage.setItem('protocol_links', JSON.stringify(links));
  }

  function loadLinks() {
    const links = getLinks();
    refListEl.innerHTML = '';
    
    links.forEach((link, index) => {
      const li = document.createElement('li');
      li.className = 'ref-item';
      li.innerHTML = `
        <div class="ref-link-wrapper">
          <span class="ref-title">${link.title}</span>
          <a href="${link.url}" target="_blank" class="ref-url">${link.url}</a>
        </div>
        <button onclick="deleteLink(${index})" class="delete-btn">Remove</button>
      `;
      refListEl.appendChild(li);
    });
  }

  function addNewLink() {
    const title = titleInput.value.trim();
    const url = urlInput.value.trim();
    
    if (!title || !url) return;
    
    // Simple URL validation prefix
    let finalUrl = url;
    if (!url.startsWith('http')) {
      finalUrl = 'https://' + url;
    }

    const links = getLinks();
    links.push({ title, url: finalUrl });
    saveLinks(links);
    
    titleInput.value = '';
    urlInput.value = '';
    loadLinks();
  }

  function deleteLink(index) {
    const links = getLinks();
    links.splice(index, 1);
    saveLinks(links);
    loadLinks();
  }

  // --- DAILY NOTES LOGIC ---
  const dateInput = document.getElementById('note-date');
  const noteArea = document.getElementById('daily-note');
  const saveIndicator = document.getElementById('save-indicator');
  let saveTimeout;

  function initNotes() {
    const today = new Date();
    const yyyy = today.getFullYear();
    const mm = String(today.getMonth() + 1).padStart(2, '0');
    const dd = String(today.getDate()).padStart(2, '0');
    dateInput.value = `${yyyy}-${mm}-${dd}`;
    
    loadNoteForDate(dateInput.value);
  }

  function getNoteKey(date) {
    return `protocol_note_${date}`;
  }

  function loadNoteForDate(date) {
    const savedContent = localStorage.getItem(getNoteKey(date));
    noteArea.value = savedContent || '';
  }

  function saveCurrentNote() {
    const date = dateInput.value;
    const content = noteArea.value;
    
    if (!date) return;

    localStorage.setItem(getNoteKey(date), content);
    
    saveIndicator.classList.add('visible');
    clearTimeout(saveTimeout);
    saveTimeout = setTimeout(() => {
      saveIndicator.classList.remove('visible');
    }, 2000);
  }

  // Event Listeners
  dateInput.addEventListener('change', (e) => {
    loadNoteForDate(e.target.value);
  });

  noteArea.addEventListener('input', () => {
    saveCurrentNote();
  });
</script>
