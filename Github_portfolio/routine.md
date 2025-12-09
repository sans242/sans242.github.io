---
layout: page
title: Daily Routine
subtitle: Stay consistent, stay awesome.
---

<style>
  .routine-container {
    max-width: 600px;
    margin: 0 auto;
    font-family: 'Open Sans', sans-serif;
  }
  .task-item {
    display: flex;
    align-items: center;
    background: #fdfdfd;
    border: 1px solid #eee;
    padding: 15px;
    margin-bottom: 10px;
    border-radius: 8px;
    transition: all 0.2s ease;
    cursor: pointer;
  }
  .task-item:hover {
    box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    background: #fff;
  }
  .task-item.completed {
    background: #f0fff4;
    border-color: #c6f6d5;
  }
  .task-item.completed .task-text {
    text-decoration: line-through;
    color: #888;
  }
  .checkbox-wrapper {
    margin-right: 15px;
    display: flex;
    align-items: center;
  }
  .custom-checkbox {
    width: 24px;
    height: 24px;
    border: 2px solid #ddd;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    transition: all 0.2s;
  }
  .task-item.completed .custom-checkbox {
    background: #48bb78;
    border-color: #48bb78;
  }
  .task-text {
    font-size: 1.1rem;
    flex-grow: 1;
  }
  .progress-bar-container {
    background: #eee;
    border-radius: 10px;
    height: 10px;
    width: 100%;
    margin-bottom: 30px;
    overflow: hidden;
  }
  .progress-bar {
    background: linear-gradient(90deg, #63b3ed, #4299e1);
    height: 100%;
    width: 0%;
    transition: width 0.3s ease;
  }
  .stats {
    text-align: center;
    margin-bottom: 20px;
    font-size: 0.9rem;
    color: #666;
  }
  
  /* Password Protection Styles */
  #auth-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: white;
    z-index: 1000;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
  .auth-box {
    text-align: center;
    padding: 2rem;
    background: #f9f9f9;
    border-radius: 10px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  }
  .auth-input {
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
    margin-bottom: 10px;
    width: 200px;
  }
  .auth-btn {
    padding: 10px 20px;
    background: #4299e1;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  .auth-btn:hover {
    background: #3182ce;
  }
  .error-msg {
    color: red;
    margin-top: 10px;
    display: none;
  }
</style>

<!-- Auth Overlay -->
<div id="auth-overlay">
  <div class="auth-box">
    <h3>Restricted Access</h3>
    <p>Please enter the password to view your routine.</p>
    <input type="password" id="password-input" class="auth-input" placeholder="Enter password">
    <br>
    <button onclick="checkPassword()" class="auth-btn">Unlock</button>
    <p id="error-msg" class="error-msg">Incorrect password</p>
  </div>
</div>

<div class="routine-container">
  
  <div class="stats">
    <span id="completed-count">0</span> / <span id="total-count">0</span> completed
  </div>
  
  <div class="progress-bar-container">
    <div class="progress-bar" id="progress-bar"></div>
  </div>

  <div id="task-list">
    <!-- Tasks will be injected here -->
  </div>

</div>

<script>
  // --- PASSWORD PROTECTION ---
  const CORRECT_PASSWORD = "password123"; // CHANGE THIS IF YOU WANT
  const authOverlay = document.getElementById('auth-overlay');
  const passwordInput = document.getElementById('password-input');
  const errorMsg = document.getElementById('error-msg');

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
    localStorage.setItem('routineAuth', 'true');
  }

  // Check if they already logged in on this browser
  if (localStorage.getItem('routineAuth') === 'true') {
    authOverlay.style.display = 'none';
  }

  // --- ROUTINE LOGIC ---
  
  // Default routine tasks
  const defaultTasks = [
    { id: 'task_1', text: 'Wake up at 7:00 AM' },
    { id: 'task_2', text: 'Drink 500ml Water' },
    { id: 'task_3', text: 'Morning Workout (30 mins)' },
    { id: 'task_4', text: 'Read 10 pages' },
    { id: 'task_5', text: 'Code for 2 hours' },
    { id: 'task_6', text: 'Review Goals' }
  ];

  // Load from LocalStorage or use default
  let userStatus = JSON.parse(localStorage.getItem('routineStatus')) || {};

  const taskListEl = document.getElementById('task-list');
  const progressBarEl = document.getElementById('progress-bar');
  const completedCountEl = document.getElementById('completed-count');
  const totalCountEl = document.getElementById('total-count');

  function saveStatus() {
    localStorage.setItem('routineStatus', JSON.stringify(userStatus));
    updateStats();
  }

  function updateStats() {
    const total = defaultTasks.length;
    let completed = 0;
    
    defaultTasks.forEach(task => {
      if (userStatus[task.id]) completed++;
    });

    completedCountEl.textContent = completed;
    totalCountEl.textContent = total;
    
    const percentage = (completed / total) * 100;
    progressBarEl.style.width = percentage + '%';
  }

  function renderTasks() {
    taskListEl.innerHTML = '';
    
    defaultTasks.forEach(task => {
      const isCompleted = userStatus[task.id] === true;
      
      const item = document.createElement('div');
      item.className = `task-item ${isCompleted ? 'completed' : ''}`;
      item.onclick = () => toggleTask(task.id);
      
      item.innerHTML = `
        <div class="checkbox-wrapper">
          <div class="custom-checkbox">
            ${isCompleted ? '✓' : ''}
          </div>
        </div>
        <div class="task-text">${task.text}</div>
      `;
      
      taskListEl.appendChild(item);
    });
    
    updateStats();
  }

  function toggleTask(taskId) {
    userStatus[taskId] = !userStatus[taskId];
    saveStatus();
    renderTasks();
  }

  // Initial render
  renderTasks();
</script>
