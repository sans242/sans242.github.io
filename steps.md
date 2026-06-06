---
layout: page
title: Steps
subtitle: Daily Steps Dashboard
---

<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">

<style>
  .container-md, .container { max-width: 100% !important; width: 100% !important; padding: 0 !important; margin: 0 !important; }
  .steps-app { font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif; background: #0a0a0f; color: #e0e0e0; min-height: 100vh; padding: 0 20px 60px; }

  /* HERO */
  .hero { text-align: center; padding: 50px 20px 30px; position: relative; overflow: hidden; }
  .hero::before { content: ''; position: absolute; top: -50%; left: -50%; width: 200%; height: 200%; background: radial-gradient(ellipse at center, rgba(124,77,255,0.06) 0%, transparent 60%); pointer-events: none; }
  .hero-title { font-size: 2.8rem; font-weight: 900; background: linear-gradient(135deg, #7C4DFF, #B388FF, #E040FB); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; margin: 0 0 8px; letter-spacing: -0.02em; }
  .hero-sub { color: #666; font-size: 1rem; font-weight: 400; margin: 0; }
  .hero-sub .last-sync { color: #B388FF; font-family: 'JetBrains Mono', monospace; font-size: 0.85rem; }
  .connection-badge { display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; border-radius: 20px; font-size: 0.7rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; margin-top: 12px; }
  .connection-badge.online { background: rgba(124,77,255,0.1); color: #B388FF; border: 1px solid rgba(124,77,255,0.2); }
  .connection-badge.offline { background: rgba(245,101,101,0.1); color: #f56565; border: 1px solid rgba(245,101,101,0.2); }
  .connection-dot { width: 6px; height: 6px; border-radius: 50%; background: currentColor; animation: pulse-dot 2s infinite; }
  @keyframes pulse-dot { 0%, 100% { opacity: 1; } 50% { opacity: 0.4; } }

  /* SYNC BUTTONS */
  .hero-actions { display: flex; justify-content: center; gap: 10px; margin-top: 16px; flex-wrap: wrap; }
  .btn-sync { display: inline-flex; align-items: center; gap: 8px; padding: 10px 22px; border-radius: 12px; font-size: 0.8rem; font-weight: 700; font-family: 'Inter', sans-serif; cursor: pointer; transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1); border: 1px solid; text-transform: uppercase; letter-spacing: 0.05em; }
  .btn-sync:active { transform: scale(0.97); }
  .btn-sync.primary { background: linear-gradient(135deg, rgba(124,77,255,0.15), rgba(179,136,255,0.08)); border-color: rgba(124,77,255,0.4); color: #B388FF; }
  .btn-sync.primary:hover { background: linear-gradient(135deg, rgba(124,77,255,0.25), rgba(179,136,255,0.15)); box-shadow: 0 4px 20px rgba(124,77,255,0.2); }
  .btn-sync.secondary { background: rgba(255,255,255,0.03); border-color: #2a2a36; color: #888; }
  .btn-sync.secondary:hover { border-color: #444; color: #ccc; background: rgba(255,255,255,0.06); }
  .btn-sync:disabled { opacity: 0.5; cursor: not-allowed; }
  .btn-sync .btn-spinner { width: 14px; height: 14px; border: 2px solid transparent; border-top-color: currentColor; border-radius: 50%; animation: spin 0.6s linear infinite; display: none; }
  .btn-sync.loading .btn-spinner { display: block; }
  .btn-sync.loading .btn-icon { display: none; }

  /* STAT CARDS */
  .stats-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 16px; max-width: 1200px; margin: 30px auto; }
  .stat-card { background: linear-gradient(135deg, #111118, #141420); border: 1px solid #1e1e2e; border-radius: 16px; padding: 24px; text-align: center; transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1); position: relative; overflow: hidden; }
  .stat-card::before { content: ''; position: absolute; inset: 0; background: linear-gradient(135deg, rgba(124,77,255,0.04), transparent); opacity: 0; transition: opacity 0.3s; }
  .stat-card:hover { border-color: rgba(124,77,255,0.3); transform: translateY(-3px); box-shadow: 0 12px 32px rgba(0,0,0,0.3); }
  .stat-card:hover::before { opacity: 1; }
  .stat-icon { font-size: 1.6rem; margin-bottom: 8px; display: block; }
  .stat-value { font-size: 1.8rem; font-weight: 800; color: #B388FF; display: block; line-height: 1.1; font-family: 'JetBrains Mono', monospace; position: relative; z-index: 1; }
  .stat-label { font-size: 0.7rem; color: #666; text-transform: uppercase; letter-spacing: 0.1em; margin-top: 6px; display: block; position: relative; z-index: 1; }

  /* SECTION HEADERS */
  .section-header { max-width: 1200px; margin: 40px auto 20px; display: flex; align-items: center; gap: 12px; }
  .section-header h2 { font-size: 1.3rem; font-weight: 800; color: #fff; margin: 0; }
  .section-line { flex: 1; height: 1px; background: linear-gradient(90deg, #1e1e2e, transparent); }

  /* RECORDS */
  .records-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 16px; max-width: 1200px; margin: 0 auto; }
  .record-card { background: linear-gradient(135deg, #111118, #14141e); border: 1px solid #1e1e2e; border-radius: 16px; padding: 20px 24px; display: flex; align-items: center; gap: 16px; transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1); }
  .record-card:hover { border-color: rgba(124,77,255,0.3); transform: translateY(-2px); box-shadow: 0 8px 24px rgba(0,0,0,0.3); }
  .record-icon { width: 52px; height: 52px; border-radius: 14px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; flex-shrink: 0; }
  .record-icon.purple { background: linear-gradient(135deg, rgba(124,77,255,0.15), rgba(179,136,255,0.1)); }
  .record-icon.gold { background: linear-gradient(135deg, rgba(255,215,0,0.15), rgba(255,165,0,0.1)); }
  .record-icon.green { background: linear-gradient(135deg, rgba(0,230,118,0.15), rgba(0,200,83,0.1)); }
  .record-icon.blue { background: linear-gradient(135deg, rgba(66,165,245,0.15), rgba(33,150,243,0.1)); }
  .record-icon.red { background: linear-gradient(135deg, rgba(239,83,80,0.15), rgba(229,57,53,0.1)); }
  .record-icon.orange { background: linear-gradient(135deg, rgba(255,167,38,0.15), rgba(255,143,0,0.1)); }
  .record-info { flex: 1; min-width: 0; }
  .record-title { font-size: 0.8rem; color: #888; text-transform: uppercase; letter-spacing: 0.05em; margin: 0 0 4px; }
  .record-value { font-size: 1.4rem; font-weight: 800; color: #fff; font-family: 'JetBrains Mono', monospace; margin: 0; }
  .record-detail { font-size: 0.75rem; color: #555; margin: 2px 0 0; }

  /* CHART */
  .chart-container { max-width: 1200px; margin: 0 auto; background: linear-gradient(135deg, #111118, #14141e); border: 1px solid #1e1e2e; border-radius: 16px; padding: 24px; }
  .chart-tabs { display: flex; gap: 8px; margin-bottom: 20px; flex-wrap: wrap; }
  .chart-tab { padding: 6px 16px; background: #0a0a0f; border: 1px solid #1e1e2e; border-radius: 10px; color: #888; font-size: 0.75rem; font-weight: 600; cursor: pointer; transition: all 0.3s; font-family: 'Inter', sans-serif; }
  .chart-tab:hover { border-color: #444; color: #ccc; }
  .chart-tab.active { background: linear-gradient(135deg, rgba(124,77,255,0.12), rgba(179,136,255,0.08)); border-color: #7C4DFF; color: #B388FF; }
  #steps-chart { width: 100%; height: 300px; display: block; }

  /* GOAL PROGRESS BAR */
  .goal-bar-outer { max-width: 1200px; margin: 0 auto; background: linear-gradient(135deg, #111118, #14141e); border: 1px solid #1e1e2e; border-radius: 16px; padding: 24px; }
  .goal-bar-label { display: flex; justify-content: space-between; margin-bottom: 10px; font-size: 0.85rem; color: #888; }
  .goal-bar-label .goal-pct { font-weight: 800; color: #B388FF; font-family: 'JetBrains Mono', monospace; }
  .goal-bar-track { width: 100%; height: 16px; background: #1a1a28; border-radius: 8px; overflow: hidden; position: relative; }
  .goal-bar-fill { height: 100%; border-radius: 8px; background: linear-gradient(90deg, #7C4DFF, #B388FF, #E040FB); transition: width 0.8s cubic-bezier(0.16, 1, 0.3, 1); position: relative; }
  .goal-bar-fill::after { content: ''; position: absolute; inset: 0; background: linear-gradient(90deg, transparent, rgba(255,255,255,0.15), transparent); animation: shimmer 2s infinite; }
  @keyframes shimmer { 0% { transform: translateX(-100%); } 100% { transform: translateX(100%); } }

  /* WEEKLY BREAKDOWN */
  .weekly-grid { display: grid; grid-template-columns: repeat(7, 1fr); gap: 8px; max-width: 1200px; margin: 0 auto; }
  .week-day-card { background: linear-gradient(135deg, #111118, #14141e); border: 1px solid #1e1e2e; border-radius: 12px; padding: 16px 8px; text-align: center; transition: all 0.3s; }
  .week-day-card:hover { border-color: rgba(124,77,255,0.25); transform: translateY(-2px); }
  .week-day-card .day-name { font-size: 0.65rem; color: #666; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 6px; }
  .week-day-card .day-steps { font-size: 1.1rem; font-weight: 800; color: #B388FF; font-family: 'JetBrains Mono', monospace; }
  .week-day-card.today { border-color: rgba(124,77,255,0.4); box-shadow: 0 0 20px rgba(124,77,255,0.1); }

  /* MONTHLY STATS */
  .monthly-container { max-width: 1200px; margin: 0 auto; }
  .month-tabs { display: flex; gap: 8px; margin-bottom: 20px; flex-wrap: wrap; justify-content: center; }
  .month-tab { padding: 8px 18px; background: #111118; border: 1px solid #1e1e2e; border-radius: 12px; color: #888; font-size: 0.75rem; font-weight: 600; cursor: pointer; transition: all 0.3s; font-family: 'Inter', sans-serif; }
  .month-tab:hover { border-color: #444; color: #ccc; }
  .month-tab.active { background: linear-gradient(135deg, rgba(124,77,255,0.12), rgba(179,136,255,0.08)); border-color: #7C4DFF; color: #B388FF; }
  .monthly-stats-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 14px; margin-bottom: 20px; }
  .monthly-stat { background: linear-gradient(135deg, #111118, #14141e); border: 1px solid #1e1e2e; border-radius: 14px; padding: 18px; text-align: center; transition: all 0.3s; }
  .monthly-stat:hover { border-color: rgba(124,77,255,0.25); transform: translateY(-2px); }
  .monthly-stat-icon { font-size: 1.2rem; display: block; margin-bottom: 4px; }
  .monthly-stat-val { font-size: 1.4rem; font-weight: 800; color: #B388FF; font-family: 'JetBrains Mono', monospace; display: block; line-height: 1.2; }
  .monthly-stat-label { font-size: 0.6rem; color: #666; text-transform: uppercase; letter-spacing: 0.1em; margin-top: 4px; display: block; }

  /* DATA TABLE */
  .table-container { max-width: 1200px; margin: 0 auto; background: linear-gradient(135deg, #111118, #14141e); border: 1px solid #1e1e2e; border-radius: 16px; overflow: hidden; }
  .table-toolbar { display: flex; justify-content: space-between; align-items: center; padding: 16px 20px; border-bottom: 1px solid #1e1e2e; flex-wrap: wrap; gap: 12px; }
  .table-search { padding: 10px 16px; background: #0a0a0f; border: 1px solid #1e1e2e; border-radius: 10px; color: #fff; font-size: 0.85rem; font-family: 'Inter', sans-serif; outline: none; transition: all 0.3s; min-width: 200px; }
  .table-search::placeholder { color: #444; }
  .table-search:focus { border-color: #7C4DFF; box-shadow: 0 0 0 3px rgba(124,77,255,0.1); }
  .table-count { font-size: 0.8rem; color: #888; font-family: 'JetBrains Mono', monospace; }
  .steps-table { width: 100%; border-collapse: collapse; }
  .steps-table th { padding: 12px 16px; text-align: left; font-size: 0.7rem; font-weight: 700; color: #666; text-transform: uppercase; letter-spacing: 0.1em; border-bottom: 1px solid #1e1e2e; cursor: pointer; user-select: none; transition: color 0.2s; white-space: nowrap; }
  .steps-table th:hover { color: #B388FF; }
  .steps-table th.sorted { color: #B388FF; }
  .steps-table th .sort-arrow { font-size: 0.6rem; margin-left: 4px; opacity: 0.5; }
  .steps-table th.sorted .sort-arrow { opacity: 1; }
  .steps-table td { padding: 14px 16px; font-size: 0.85rem; border-bottom: 1px solid #111118; white-space: nowrap; }
  .steps-table tr { transition: background 0.2s; }
  .steps-table tbody tr:hover { background: rgba(124,77,255,0.03); }
  .steps-date { color: #888; font-family: 'JetBrains Mono', monospace; font-size: 0.8rem; }
  .steps-count { color: #B388FF; font-weight: 700; font-family: 'JetBrains Mono', monospace; }
  .goal-badge { font-size: 0.75rem; font-weight: 700; padding: 3px 10px; border-radius: 8px; font-family: 'JetBrains Mono', monospace; display: inline-block; }
  .goal-met { background: rgba(0,230,118,0.12); color: #00E676; border: 1px solid rgba(0,230,118,0.2); }
  .goal-close { background: rgba(255,167,38,0.12); color: #FFA726; border: 1px solid rgba(255,167,38,0.2); }
  .goal-miss { background: rgba(239,83,80,0.12); color: #ef5350; border: 1px solid rgba(239,83,80,0.2); }
  .table-scroll { overflow-x: auto; }

  /* LOADING / EMPTY / TOAST */
  .loading-overlay { text-align: center; padding: 80px 20px; }
  .spinner { width: 40px; height: 40px; border: 3px solid #222; border-top-color: #B388FF; border-radius: 50%; animation: spin 0.8s linear infinite; margin: 0 auto 20px; }
  @keyframes spin { to { transform: rotate(360deg); } }
  .loading-text { color: #555; font-size: 0.9rem; }
  .empty-state { text-align: center; padding: 60px 20px; color: #444; }
  .empty-state-icon { font-size: 3rem; margin-bottom: 16px; }
  .toast { position: fixed; bottom: 30px; left: 50%; transform: translateX(-50%) translateY(100px); background: #1a1a24; border: 1px solid #333; color: #fff; padding: 12px 24px; border-radius: 12px; font-size: 0.85rem; font-weight: 500; z-index: 9999; transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1); box-shadow: 0 8px 32px rgba(0,0,0,0.4); }
  .toast.show { transform: translateX(-50%) translateY(0); }
  .toast.error { border-color: #ef5350; }
  .toast.success { border-color: #B388FF; }

  @media (max-width: 768px) {
    .hero-title { font-size: 2rem; }
    .stats-grid { grid-template-columns: repeat(2, 1fr); }
    .records-grid { grid-template-columns: 1fr; }
    .weekly-grid { grid-template-columns: repeat(4, 1fr); }
    .monthly-stats-grid { grid-template-columns: repeat(2, 1fr); }
    .steps-table th, .steps-table td { padding: 10px 10px; font-size: 0.75rem; }
  }
  @media (max-width: 480px) {
    .weekly-grid { grid-template-columns: repeat(2, 1fr); }
  }
</style>

<div class="steps-app" id="steps-app">
  <div class="hero">
    <h1 class="hero-title">🚶 Steps Dashboard</h1>
    <p class="hero-sub">Powered by Garmin Connect — <span class="last-sync" id="last-sync">loading...</span></p>
    <div class="connection-badge offline" id="connection-badge">
      <span class="connection-dot"></span>
      <span id="connection-text">Connecting...</span>
    </div>
    <div class="hero-actions">
      <button class="btn-sync primary" id="btn-garmin-sync" onclick="triggerGarminSync()">
        <span class="btn-icon">🔄</span>
        <span class="btn-spinner"></span>
        Sync from Garmin
      </button>
      <button class="btn-sync secondary" id="btn-refresh" onclick="refreshData()">
        <span class="btn-icon">↻</span>
        <span class="btn-spinner"></span>
        Refresh Data
      </button>
    </div>
  </div>

  <div class="loading-overlay" id="loading">
    <div class="spinner"></div>
    <div class="loading-text">Fetching your steps...</div>
  </div>

  <div id="main-content" style="display:none;">
    <div class="stats-grid" id="stats-grid"></div>

    <div class="section-header" id="goal-section" style="display:none;"><h2>🎯 Today's Goal Progress</h2><div class="section-line"></div></div>
    <div class="goal-bar-outer" id="goal-bar-container" style="display:none;">
      <div class="goal-bar-label">
        <span id="goal-label-text">Steps toward goal</span>
        <span class="goal-pct" id="goal-pct">0%</span>
      </div>
      <div class="goal-bar-track">
        <div class="goal-bar-fill" id="goal-bar-fill" style="width: 0%"></div>
      </div>
    </div>

    <div class="section-header"><h2>🏆 Step Records</h2><div class="section-line"></div></div>
    <div class="records-grid" id="records-grid"></div>

    <div class="section-header"><h2>📈 Step Trends</h2><div class="section-line"></div></div>
    <div class="chart-container">
      <div class="chart-tabs" id="chart-tabs">
        <button class="chart-tab active" data-range="30" onclick="switchRange(30)">Last 30 Days</button>
        <button class="chart-tab" data-range="60" onclick="switchRange(60)">Last 60 Days</button>
        <button class="chart-tab" data-range="90" onclick="switchRange(90)">All Time</button>
      </div>
      <canvas id="steps-chart"></canvas>
    </div>

    <div class="section-header"><h2>📅 This Week</h2><div class="section-line"></div></div>
    <div class="weekly-grid" id="weekly-grid"></div>

    <div class="section-header"><h2>📊 Monthly Breakdown</h2><div class="section-line"></div></div>
    <div class="monthly-container">
      <div class="month-tabs" id="month-tabs"></div>
      <div class="monthly-stats-grid" id="monthly-stats-grid"></div>
    </div>

    <div class="section-header"><h2>📋 All Days</h2><div class="section-line"></div></div>
    <div class="table-container">
      <div class="table-toolbar">
        <input type="text" class="table-search" id="table-search" placeholder="🔍 Search dates...">
        <span class="table-count" id="table-count"></span>
      </div>
      <div class="table-scroll">
        <table class="steps-table">
          <thead>
            <tr>
              <th onclick="sortTable('date')" id="th-date" class="sorted">Date <span class="sort-arrow">▼</span></th>
              <th onclick="sortTable('total_steps')" id="th-total_steps">Steps <span class="sort-arrow">▼</span></th>
              <th onclick="sortTable('step_goal')" id="th-step_goal">Goal <span class="sort-arrow">▼</span></th>
              <th onclick="sortTable('goal_pct')" id="th-goal_pct">Progress <span class="sort-arrow">▼</span></th>
              <th onclick="sortTable('distance')" id="th-distance">Distance <span class="sort-arrow">▼</span></th>
              <th onclick="sortTable('calories_total')" id="th-calories_total">Calories <span class="sort-arrow">▼</span></th>
            </tr>
          </thead>
          <tbody id="steps-tbody"></tbody>
        </table>
      </div>
    </div>

    <div class="empty-state" id="empty-state" style="display:none;">
      <div class="empty-state-icon">🚶</div>
      <p>No step data found yet. Sync your Garmin data to get started!</p>
    </div>
  </div>
</div>

<div class="toast" id="toast"></div>
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/dist/umd/supabase.min.js"></script>

<script>
const SUPABASE_URL = 'https://uuzrzcnvieygjlihgwnb.supabase.co';
const SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InV1enJ6Y252aWV5Z2psaWhnd25iIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Nzc4MDE3OTEsImV4cCI6MjA5MzM3Nzc5MX0._LP_f3WtKPVEvVCG1Uqh5S5ARHSHF7maopdWIbWg7Mw';
const sb = supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY, {
  global: {
    headers: { 'Cache-Control': 'no-cache', 'Pragma': 'no-cache' },
  },
});
const GITHUB_REPO = 'sans242/sans242.github.io';
const WORKFLOW_FILE = 'sync_garmin.yml';

let allSteps = [];
let filteredSteps = [];
let sortField = 'date';
let sortAsc = false;
let chartRange = 30;

// ── Helpers ──
function formatDate(d) { return d ? new Date(d + 'T00:00:00').toLocaleDateString('en-IN', {day:'2-digit',month:'short',year:'numeric'}) : '—'; }
function formatDateShort(d) { return d ? new Date(d + 'T00:00:00').toLocaleDateString('en-IN', {day:'2-digit',month:'short'}) : ''; }
function getMonthKey(d) { if (!d) return null; return d.substring(0, 7); }
function formatMonthLabel(k) { const [y,m] = k.split('-'); return ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'][parseInt(m)-1] + ' ' + y; }
function getGoalClass(pct) { return pct >= 100 ? 'goal-met' : pct >= 70 ? 'goal-close' : 'goal-miss'; }
function getDayName(d) { return new Date(d + 'T00:00:00').toLocaleDateString('en-IN', {weekday: 'short'}); }

// ── Data Loading ──
async function loadData() {
  try {
    const { data, error } = await sb.from('garmin_daily_steps').select('*').order('date', { ascending: false });
    if (error) throw error;

    allSteps = (data || []).map(r => ({
      ...r,
      goal_pct: r.step_goal && r.step_goal > 0 ? Math.round((r.total_steps / r.step_goal) * 100) : null,
      distanceKm: r.distance ? (r.distance / 1000).toFixed(2) : null,
    }));
    filteredSteps = [...allSteps];

    document.getElementById('connection-badge').className = 'connection-badge online';
    document.getElementById('connection-text').textContent = 'Cloud Synced';
    document.getElementById('loading').style.display = 'none';
    document.getElementById('main-content').style.display = 'block';

    if (allSteps.length === 0) {
      document.getElementById('empty-state').style.display = 'block';
      document.getElementById('last-sync').textContent = 'No data yet';
      return;
    }

    const latest = allSteps.reduce((a, b) => new Date(a.synced_at) > new Date(b.synced_at) ? a : b);
    document.getElementById('last-sync').textContent = 'Last sync: ' + formatDate(latest.synced_at ? latest.synced_at.substring(0,10) : latest.date);

    renderStats();
    renderGoalBar();
    renderRecords();
    renderChart();
    renderWeekly();
    renderMonthly();
    renderTable();
  } catch (err) {
    console.error('Load error:', err);
    document.getElementById('connection-badge').className = 'connection-badge offline';
    document.getElementById('connection-text').textContent = 'Offline';
    document.getElementById('loading').innerHTML = '<div class="empty-state-icon">⚠️</div><p style="color:#ef5350;">Could not connect to database</p>';
    showToast('⚠️ Failed to load data', 'error');
  }
}

// ── Summary Stats ──
function renderStats() {
  const n = allSteps.length;
  const totalSteps = allSteps.reduce((s,r) => s + (r.total_steps||0), 0);
  const avgSteps = n > 0 ? Math.round(totalSteps / n) : 0;
  const best = allSteps.reduce((a,b) => (a.total_steps||0) > (b.total_steps||0) ? a : b);
  const totalDist = allSteps.reduce((s,r) => s + (r.distance||0), 0) / 1000;
  const totalCal = allSteps.reduce((s,r) => s + (r.calories_total||0), 0);

  // Streak: consecutive days meeting goal
  const goalDays = allSteps.filter(r => r.step_goal && r.total_steps >= r.step_goal);
  let streak = 0;
  const sorted = [...allSteps].sort((a,b) => b.date.localeCompare(a.date));
  for (const day of sorted) {
    if (day.step_goal && day.total_steps >= day.step_goal) streak++;
    else break;
  }

  // Days meeting goal
  const metGoal = allSteps.filter(r => r.goal_pct !== null && r.goal_pct >= 100).length;

  document.getElementById('stats-grid').innerHTML = `
    <div class="stat-card"><span class="stat-icon">🚶</span><span class="stat-value">${totalSteps.toLocaleString()}</span><span class="stat-label">Total Steps</span></div>
    <div class="stat-card"><span class="stat-icon">📊</span><span class="stat-value">${avgSteps.toLocaleString()}</span><span class="stat-label">Avg Steps/Day</span></div>
    <div class="stat-card"><span class="stat-icon">🏆</span><span class="stat-value">${(best.total_steps||0).toLocaleString()}</span><span class="stat-label">Best Day</span></div>
    <div class="stat-card"><span class="stat-icon">🔥</span><span class="stat-value">${streak}</span><span class="stat-label">Goal Streak</span></div>
    <div class="stat-card"><span class="stat-icon">🎯</span><span class="stat-value">${metGoal}/${n}</span><span class="stat-label">Days Goal Met</span></div>
    <div class="stat-card"><span class="stat-icon">📏</span><span class="stat-value">${totalDist > 0 ? totalDist.toFixed(1) : '—'}</span><span class="stat-label">Total KM Walked</span></div>
    <div class="stat-card"><span class="stat-icon">🔥</span><span class="stat-value">${totalCal > 0 ? totalCal.toLocaleString() : '—'}</span><span class="stat-label">Total Calories</span></div>
    <div class="stat-card"><span class="stat-icon">📅</span><span class="stat-value">${n}</span><span class="stat-label">Days Tracked</span></div>
  `;
}

// ── Goal Progress Bar (Today) ──
function renderGoalBar() {
  const today = new Date().toISOString().substring(0, 10);
  const todayData = allSteps.find(r => r.date === today);
  if (!todayData || !todayData.step_goal) {
    document.getElementById('goal-section').style.display = 'none';
    document.getElementById('goal-bar-container').style.display = 'none';
    return;
  }
  document.getElementById('goal-section').style.display = 'flex';
  document.getElementById('goal-bar-container').style.display = 'block';
  const pct = Math.min(100, Math.round((todayData.total_steps / todayData.step_goal) * 100));
  document.getElementById('goal-label-text').textContent = `${todayData.total_steps.toLocaleString()} / ${todayData.step_goal.toLocaleString()} steps`;
  document.getElementById('goal-pct').textContent = `${pct}%`;
  setTimeout(() => {
    document.getElementById('goal-bar-fill').style.width = pct + '%';
  }, 100);
}

// ── Records ──
function renderRecords() {
  if (!allSteps.length) return;
  const best = allSteps.reduce((a,b) => (a.total_steps||0) > (b.total_steps||0) ? a : b);
  const worst = allSteps.reduce((a,b) => (a.total_steps||0) < (b.total_steps||0) ? a : b);
  const bestDist = allSteps.filter(r => r.distance).reduce((a,b) => (a.distance||0) > (b.distance||0) ? a : b, {distance:0});
  const bestCal = allSteps.filter(r => r.calories_total).reduce((a,b) => (a.calories_total||0) > (b.calories_total||0) ? a : b, {calories_total:0});

  // Best week
  const sortedAsc = [...allSteps].sort((a,b) => a.date.localeCompare(b.date));
  let bestWeekTotal = 0, bestWeekStart = '';
  for (let i = 0; i <= sortedAsc.length - 7; i++) {
    const weekTotal = sortedAsc.slice(i, i+7).reduce((s,r) => s + (r.total_steps||0), 0);
    if (weekTotal > bestWeekTotal) { bestWeekTotal = weekTotal; bestWeekStart = sortedAsc[i].date; }
  }

  document.getElementById('records-grid').innerHTML = `
    <div class="record-card"><div class="record-icon gold">🏅</div><div class="record-info"><div class="record-title">Best Day</div><div class="record-value">${(best.total_steps||0).toLocaleString()}</div><div class="record-detail">${formatDate(best.date)}</div></div></div>
    <div class="record-card"><div class="record-icon purple">📅</div><div class="record-info"><div class="record-title">Best Week</div><div class="record-value">${bestWeekTotal > 0 ? bestWeekTotal.toLocaleString() : '—'}</div><div class="record-detail">${bestWeekStart ? 'Starting ' + formatDate(bestWeekStart) : '—'}</div></div></div>
    ${bestDist.distance ? `<div class="record-card"><div class="record-icon green">📏</div><div class="record-info"><div class="record-title">Most Distance</div><div class="record-value">${(bestDist.distance/1000).toFixed(2)} km</div><div class="record-detail">${formatDate(bestDist.date)}</div></div></div>` : ''}
    ${bestCal.calories_total ? `<div class="record-card"><div class="record-icon orange">🔥</div><div class="record-info"><div class="record-title">Most Calories</div><div class="record-value">${bestCal.calories_total.toLocaleString()}</div><div class="record-detail">${formatDate(bestCal.date)}</div></div></div>` : ''}
    <div class="record-card"><div class="record-icon red">📉</div><div class="record-info"><div class="record-title">Lowest Day</div><div class="record-value">${(worst.total_steps||0).toLocaleString()}</div><div class="record-detail">${formatDate(worst.date)}</div></div></div>
  `;
}

// ── Trends Chart ──
function switchRange(range) {
  chartRange = range;
  document.querySelectorAll('.chart-tab').forEach(t => t.classList.toggle('active', parseInt(t.getAttribute('data-range')) === range));
  renderChart();
}

function renderChart() {
  const canvas = document.getElementById('steps-chart');
  const ctx = canvas.getContext('2d');
  const dpr = window.devicePixelRatio || 1;

  const sorted = [...allSteps].sort((a,b) => a.date.localeCompare(b.date));
  const recent = sorted.slice(-chartRange);
  if (!recent.length) return;

  const values = recent.map(r => r.total_steps || 0);
  const goals = recent.map(r => r.step_goal || 0);
  const dates = recent.map(r => formatDateShort(r.date));
  const rect = canvas.parentElement.getBoundingClientRect();
  canvas.width = rect.width * dpr; canvas.height = 300 * dpr;
  canvas.style.width = rect.width + 'px'; canvas.style.height = '300px';
  ctx.scale(dpr, dpr);
  const W = rect.width, H = 300;
  const pad = {top:30,right:20,bottom:40,left:60};
  const cW = W-pad.left-pad.right, cH = H-pad.top-pad.bottom;
  ctx.clearRect(0,0,W,H);

  const allVals = [...values, ...goals.filter(g => g > 0)];
  const mn = 0, mx = Math.max(...allVals) * 1.15;
  const rng = mx - mn || 1;

  // Grid
  ctx.strokeStyle = '#1e1e2e'; ctx.lineWidth = 1;
  for (let i = 0; i <= 5; i++) {
    const y = pad.top + (cH / 5) * i;
    ctx.beginPath(); ctx.moveTo(pad.left, y); ctx.lineTo(W - pad.right, y); ctx.stroke();
    const val = mx - (rng / 5) * i;
    ctx.fillStyle = '#555'; ctx.font = '11px JetBrains Mono'; ctx.textAlign = 'right';
    ctx.fillText(Math.round(val).toLocaleString(), pad.left - 8, y + 4);
  }

  // Goal line (if goals exist)
  const avgGoal = goals.filter(g => g > 0);
  if (avgGoal.length > 0) {
    const goalVal = avgGoal[avgGoal.length - 1]; // latest goal
    const goalY = pad.top + cH - ((goalVal - mn) / rng) * cH;
    ctx.setLineDash([6, 4]);
    ctx.strokeStyle = 'rgba(224,64,251,0.4)';
    ctx.lineWidth = 1.5;
    ctx.beginPath(); ctx.moveTo(pad.left, goalY); ctx.lineTo(W - pad.right, goalY); ctx.stroke();
    ctx.setLineDash([]);
    ctx.fillStyle = 'rgba(224,64,251,0.6)'; ctx.font = '10px JetBrains Mono'; ctx.textAlign = 'left';
    ctx.fillText('Goal: ' + goalVal.toLocaleString(), pad.left + 4, goalY - 6);
  }

  // Bars
  const barW = Math.max(2, (cW / values.length) * 0.7);
  const gap = cW / values.length;
  values.forEach((v, i) => {
    const x = pad.left + i * gap + (gap - barW) / 2;
    const barH = (v / rng) * cH;
    const y = pad.top + cH - barH;
    const metGoal = goals[i] > 0 && v >= goals[i];

    // Bar gradient
    const grad = ctx.createLinearGradient(x, y, x, pad.top + cH);
    if (metGoal) {
      grad.addColorStop(0, 'rgba(0,230,118,0.8)');
      grad.addColorStop(1, 'rgba(0,230,118,0.2)');
    } else {
      grad.addColorStop(0, 'rgba(124,77,255,0.8)');
      grad.addColorStop(1, 'rgba(124,77,255,0.2)');
    }

    ctx.fillStyle = grad;
    // Rounded top
    const radius = Math.min(barW / 2, 4);
    ctx.beginPath();
    ctx.moveTo(x, pad.top + cH);
    ctx.lineTo(x, y + radius);
    ctx.quadraticCurveTo(x, y, x + radius, y);
    ctx.lineTo(x + barW - radius, y);
    ctx.quadraticCurveTo(x + barW, y, x + barW, y + radius);
    ctx.lineTo(x + barW, pad.top + cH);
    ctx.closePath();
    ctx.fill();
  });

  // X labels
  const step = Math.max(1, Math.floor(values.length / 10));
  ctx.fillStyle = '#555'; ctx.font = '10px JetBrains Mono'; ctx.textAlign = 'center';
  for (let i = 0; i < values.length; i += step) {
    const x = pad.left + i * gap + gap / 2;
    ctx.fillText(dates[i], x, H - pad.bottom + 18);
  }
  ctx.fillStyle = '#666'; ctx.font = '11px Inter'; ctx.textAlign = 'left';
  ctx.fillText('Daily Steps', pad.left, pad.top - 10);
}

// ── Weekly View ──
function renderWeekly() {
  const today = new Date();
  const dayOfWeek = today.getDay(); // 0=Sun
  const weekStart = new Date(today);
  weekStart.setDate(today.getDate() - dayOfWeek);
  const todayStr = today.toISOString().substring(0, 10);

  let html = '';
  const dayNames = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
  for (let i = 0; i < 7; i++) {
    const d = new Date(weekStart);
    d.setDate(weekStart.getDate() + i);
    const dStr = d.toISOString().substring(0, 10);
    const dayData = allSteps.find(r => r.date === dStr);
    const isToday = dStr === todayStr;
    const steps = dayData ? dayData.total_steps : null;

    html += `<div class="week-day-card ${isToday ? 'today' : ''}">
      <div class="day-name">${dayNames[i]}</div>
      <div class="day-steps">${steps !== null ? steps.toLocaleString() : '—'}</div>
    </div>`;
  }
  document.getElementById('weekly-grid').innerHTML = html;
}

// ── Monthly Breakdown ──
let currentMonth = null;
function getMonthlyData() {
  const m = {};
  allSteps.forEach(r => { const k = getMonthKey(r.date); if (!k) return; if (!m[k]) m[k] = []; m[k].push(r); });
  return m;
}
function setMonth(k) {
  currentMonth = k;
  document.querySelectorAll('.month-tab').forEach(t => t.classList.toggle('active', t.getAttribute('data-month') === k));
  renderMonthDetail();
}
function renderMonthly() {
  if (!allSteps.length) return;
  const byMonth = getMonthlyData();
  const keys = Object.keys(byMonth).sort().reverse();
  if (!keys.length) return;
  if (!currentMonth || !byMonth[currentMonth]) currentMonth = keys[0];

  document.getElementById('month-tabs').innerHTML = keys.map(k => {
    const a = k === currentMonth ? 'active' : '';
    return `<button class="month-tab ${a}" data-month="${k}" onclick="setMonth('${k}')">${formatMonthLabel(k)} (${byMonth[k].length})</button>`;
  }).join('');
  renderMonthDetail();
}
function renderMonthDetail() {
  const days = (getMonthlyData()[currentMonth]) || [];
  if (!days.length) { document.getElementById('monthly-stats-grid').innerHTML = '<div style="text-align:center;color:#444;padding:30px;grid-column:1/-1;">No data this month</div>'; return; }

  const n = days.length;
  const total = days.reduce((s,r) => s + (r.total_steps||0), 0);
  const avg = Math.round(total / n);
  const best = Math.max(...days.map(r => r.total_steps||0));
  const worst = Math.min(...days.map(r => r.total_steps||0));
  const dist = days.reduce((s,r) => s + (r.distance||0), 0) / 1000;
  const cal = days.reduce((s,r) => s + (r.calories_total||0), 0);
  const goalMet = days.filter(r => r.goal_pct !== null && r.goal_pct >= 100).length;

  document.getElementById('monthly-stats-grid').innerHTML = `
    <div class="monthly-stat"><span class="monthly-stat-icon">🚶</span><span class="monthly-stat-val">${total.toLocaleString()}</span><span class="monthly-stat-label">Total Steps</span></div>
    <div class="monthly-stat"><span class="monthly-stat-icon">📊</span><span class="monthly-stat-val">${avg.toLocaleString()}</span><span class="monthly-stat-label">Avg/Day</span></div>
    <div class="monthly-stat"><span class="monthly-stat-icon">🏆</span><span class="monthly-stat-val">${best.toLocaleString()}</span><span class="monthly-stat-label">Best Day</span></div>
    <div class="monthly-stat"><span class="monthly-stat-icon">📉</span><span class="monthly-stat-val">${worst.toLocaleString()}</span><span class="monthly-stat-label">Lowest Day</span></div>
    <div class="monthly-stat"><span class="monthly-stat-icon">🎯</span><span class="monthly-stat-val">${goalMet}/${n}</span><span class="monthly-stat-label">Goal Met</span></div>
    <div class="monthly-stat"><span class="monthly-stat-icon">📏</span><span class="monthly-stat-val">${dist > 0 ? dist.toFixed(1) : '—'}</span><span class="monthly-stat-label">KM Walked</span></div>
    <div class="monthly-stat"><span class="monthly-stat-icon">🔥</span><span class="monthly-stat-val">${cal > 0 ? Math.round(cal).toLocaleString() : '—'}</span><span class="monthly-stat-label">Calories</span></div>
    <div class="monthly-stat"><span class="monthly-stat-icon">📅</span><span class="monthly-stat-val">${n}</span><span class="monthly-stat-label">Days</span></div>
  `;
}

// ── Data Table ──
function sortTable(field) {
  if (sortField === field) sortAsc = !sortAsc;
  else { sortField = field; sortAsc = false; }
  document.querySelectorAll('.steps-table th').forEach(th => th.classList.remove('sorted'));
  const th = document.getElementById(`th-${field}`);
  if (th) { th.classList.add('sorted'); th.querySelector('.sort-arrow').textContent = sortAsc ? '▲' : '▼'; }
  renderTable();
}

function renderTable() {
  const q = (document.getElementById('table-search').value || '').toLowerCase();
  let rows = filteredSteps;
  if (q) rows = rows.filter(r => formatDate(r.date).toLowerCase().includes(q) || r.date.includes(q));
  rows.sort((a,b) => {
    let va, vb;
    switch(sortField) {
      case 'date': va = a.date; vb = b.date; break;
      case 'total_steps': va = a.total_steps||0; vb = b.total_steps||0; break;
      case 'step_goal': va = a.step_goal||0; vb = b.step_goal||0; break;
      case 'goal_pct': va = a.goal_pct||0; vb = b.goal_pct||0; break;
      case 'distance': va = a.distance||0; vb = b.distance||0; break;
      case 'calories_total': va = a.calories_total||0; vb = b.calories_total||0; break;
      default: va = 0; vb = 0;
    }
    return va < vb ? (sortAsc ? -1 : 1) : va > vb ? (sortAsc ? 1 : -1) : 0;
  });
  document.getElementById('table-count').textContent = `${rows.length} days`;
  const tbody = document.getElementById('steps-tbody');
  if (!rows.length) { tbody.innerHTML = '<tr><td colspan="6" style="text-align:center;color:#555;padding:30px;">No data matches</td></tr>'; return; }
  tbody.innerHTML = rows.map(r => {
    const goalPct = r.goal_pct !== null ? r.goal_pct : null;
    const goalClass = goalPct !== null ? getGoalClass(goalPct) : '';
    return `<tr>
      <td class="steps-date">${formatDate(r.date)}</td>
      <td class="steps-count">${(r.total_steps||0).toLocaleString()}</td>
      <td style="color:#888;font-family:'JetBrains Mono',monospace;">${r.step_goal ? r.step_goal.toLocaleString() : '—'}</td>
      <td>${goalPct !== null ? `<span class="goal-badge ${goalClass}">${goalPct}%</span>` : '—'}</td>
      <td style="color:#ccc;font-family:'JetBrains Mono',monospace;">${r.distanceKm ? r.distanceKm + ' km' : '—'}</td>
      <td style="color:#ccc;font-family:'JetBrains Mono',monospace;">${r.calories_total ? Math.round(r.calories_total).toLocaleString() : '—'}</td>
    </tr>`;
  }).join('');
}

// ── Toast ──
function showToast(msg, type='success') {
  const t = document.getElementById('toast');
  t.textContent = msg; t.className = `toast ${type} show`;
  setTimeout(() => t.classList.remove('show'), 3000);
}

// ── Sync & Refresh ──
async function triggerGarminSync() {
  const btn = document.getElementById('btn-garmin-sync');
  let pat = localStorage.getItem('gh_pat');
  if (!pat) {
    pat = prompt('To sync from Garmin, paste your GitHub Personal Access Token.\n\nCreate one at: https://github.com/settings/tokens\nPermission needed: "Actions: Read & Write"\n\nToken (saved locally):');
    if (!pat) return;
    localStorage.setItem('gh_pat', pat.trim());
    pat = pat.trim();
  }
  btn.classList.add('loading'); btn.disabled = true;
  try {
    const res = await fetch(`https://api.github.com/repos/${GITHUB_REPO}/actions/workflows/${WORKFLOW_FILE}/dispatches`, {
      method: 'POST',
      headers: { 'Authorization': `Bearer ${pat}`, 'Accept': 'application/vnd.github+json', 'X-GitHub-Api-Version': '2022-11-28' },
      body: JSON.stringify({ ref: 'main' }),
    });
    if (res.status === 204) {
      showToast('✅ Sync triggered! Will auto-refresh in 2 min.', 'success');
      setTimeout(() => refreshData(), 120000);
    } else if (res.status === 401 || res.status === 403) {
      localStorage.removeItem('gh_pat');
      showToast('❌ Invalid token — try again.', 'error');
    } else {
      showToast(`❌ Sync failed (${res.status})`, 'error');
    }
  } catch (err) { showToast('❌ Could not reach GitHub', 'error'); }
  finally { btn.classList.remove('loading'); btn.disabled = false; }
}

async function refreshData() {
  const btn = document.getElementById('btn-refresh');
  btn.classList.add('loading'); btn.disabled = true;
  try {
    allSteps = [];
    filteredSteps = [];
    await loadData();
    showToast('✅ Data refreshed!', 'success');
  }
  catch(e) { showToast('❌ Refresh failed', 'error'); }
  finally { btn.classList.remove('loading'); btn.disabled = false; }
}

// ── Init ──
document.addEventListener('DOMContentLoaded', () => {
  loadData();
  document.getElementById('table-search').addEventListener('input', renderTable);
  window.addEventListener('resize', () => { if (allSteps.length > 0) renderChart(); });
});
</script>
