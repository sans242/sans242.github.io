---
layout: page
title: Running
subtitle: Garmin Running Dashboard
---

<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">

<style>
  /* ═══════════════════════════════════════════════════════════════════════════
     RESET & BASE
     ═══════════════════════════════════════════════════════════════════════════ */
  .container-md, .container {
    max-width: 100% !important;
    width: 100% !important;
    padding: 0 !important;
    margin: 0 !important;
  }

  .run-app {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    background: #0a0a0f;
    color: #e0e0e0;
    min-height: 100vh;
    padding: 0 20px 60px;
  }

  /* ═══════════════════════════════════════════════════════════════════════════
     HERO
     ═══════════════════════════════════════════════════════════════════════════ */
  .hero {
    text-align: center;
    padding: 50px 20px 30px;
    position: relative;
    overflow: hidden;
  }
  .hero::before {
    content: '';
    position: absolute;
    top: -50%; left: -50%;
    width: 200%; height: 200%;
    background: radial-gradient(ellipse at center, rgba(0,230,118,0.06) 0%, transparent 60%);
    pointer-events: none;
  }
  .hero-title {
    font-size: 2.8rem;
    font-weight: 900;
    background: linear-gradient(135deg, #00E676, #00C853, #69F0AE);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin: 0 0 8px;
    letter-spacing: -0.02em;
  }
  .hero-sub {
    color: #666;
    font-size: 1rem;
    font-weight: 400;
    margin: 0;
  }
  .hero-sub .last-sync {
    color: #00E676;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.85rem;
  }

  /* Connection Badge */
  .connection-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 0.7rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-top: 12px;
  }
  .connection-badge.online {
    background: rgba(0,230,118,0.1);
    color: #00E676;
    border: 1px solid rgba(0,230,118,0.2);
  }
  .connection-badge.offline {
    background: rgba(245,101,101,0.1);
    color: #f56565;
    border: 1px solid rgba(245,101,101,0.2);
  }
  .connection-dot {
    width: 6px; height: 6px;
    border-radius: 50%;
    background: currentColor;
    animation: pulse-dot 2s infinite;
  }
  @keyframes pulse-dot {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.4; }
  }

  /* Sync Buttons */
  .hero-actions {
    display: flex;
    justify-content: center;
    gap: 10px;
    margin-top: 16px;
    flex-wrap: wrap;
  }
  .btn-sync {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 10px 22px;
    border-radius: 12px;
    font-size: 0.8rem;
    font-weight: 700;
    font-family: 'Inter', sans-serif;
    cursor: pointer;
    transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    border: 1px solid;
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }
  .btn-sync:active { transform: scale(0.97); }
  .btn-sync.primary {
    background: linear-gradient(135deg, rgba(0,230,118,0.15), rgba(0,200,83,0.08));
    border-color: rgba(0,230,118,0.4);
    color: #00E676;
  }
  .btn-sync.primary:hover {
    background: linear-gradient(135deg, rgba(0,230,118,0.25), rgba(0,200,83,0.15));
    box-shadow: 0 4px 20px rgba(0,230,118,0.2);
  }
  .btn-sync.secondary {
    background: rgba(255,255,255,0.03);
    border-color: #2a2a36;
    color: #888;
  }
  .btn-sync.secondary:hover {
    border-color: #444;
    color: #ccc;
    background: rgba(255,255,255,0.06);
  }
  .btn-sync:disabled {
    opacity: 0.5;
    cursor: not-allowed;
  }
  .btn-sync .btn-spinner {
    width: 14px; height: 14px;
    border: 2px solid transparent;
    border-top-color: currentColor;
    border-radius: 50%;
    animation: spin 0.6s linear infinite;
    display: none;
  }
  .btn-sync.loading .btn-spinner { display: block; }
  .btn-sync.loading .btn-icon { display: none; }

  /* ═══════════════════════════════════════════════════════════════════════════
     STATS CARDS
     ═══════════════════════════════════════════════════════════════════════════ */
  .stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 16px;
    max-width: 1200px;
    margin: 30px auto;
  }
  .stat-card {
    background: linear-gradient(135deg, #111118, #141420);
    border: 1px solid #1e1e2e;
    border-radius: 16px;
    padding: 24px;
    text-align: center;
    transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    position: relative;
    overflow: hidden;
  }
  .stat-card::before {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(135deg, rgba(0,230,118,0.04), transparent);
    opacity: 0;
    transition: opacity 0.3s;
  }
  .stat-card:hover {
    border-color: rgba(0,230,118,0.3);
    transform: translateY(-3px);
    box-shadow: 0 12px 32px rgba(0,0,0,0.3);
  }
  .stat-card:hover::before { opacity: 1; }

  .stat-icon {
    font-size: 1.6rem;
    margin-bottom: 8px;
    display: block;
  }
  .stat-value {
    font-size: 2rem;
    font-weight: 800;
    color: #00E676;
    display: block;
    line-height: 1.1;
    font-family: 'JetBrains Mono', monospace;
    position: relative;
    z-index: 1;
  }
  .stat-label {
    font-size: 0.75rem;
    color: #666;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-top: 6px;
    display: block;
    position: relative;
    z-index: 1;
  }

  /* ═══════════════════════════════════════════════════════════════════════════
     SECTION HEADERS
     ═══════════════════════════════════════════════════════════════════════════ */
  .section-header {
    max-width: 1200px;
    margin: 40px auto 20px;
    display: flex;
    align-items: center;
    gap: 12px;
  }
  .section-header h2 {
    font-size: 1.3rem;
    font-weight: 800;
    color: #fff;
    margin: 0;
  }
  .section-line {
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, #1e1e2e, transparent);
  }

  /* ═══════════════════════════════════════════════════════════════════════════
     RECORDS (Personal Bests)
     ═══════════════════════════════════════════════════════════════════════════ */
  .records-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 16px;
    max-width: 1200px;
    margin: 0 auto;
  }
  .record-card {
    background: linear-gradient(135deg, #111118, #14141e);
    border: 1px solid #1e1e2e;
    border-radius: 16px;
    padding: 20px 24px;
    display: flex;
    align-items: center;
    gap: 16px;
    transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  }
  .record-card:hover {
    border-color: rgba(0,230,118,0.3);
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(0,0,0,0.3);
  }
  .record-icon {
    width: 52px; height: 52px;
    border-radius: 14px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.5rem;
    flex-shrink: 0;
  }
  .record-icon.gold { background: linear-gradient(135deg, rgba(255,215,0,0.15), rgba(255,165,0,0.1)); }
  .record-icon.green { background: linear-gradient(135deg, rgba(0,230,118,0.15), rgba(0,200,83,0.1)); }
  .record-icon.blue { background: linear-gradient(135deg, rgba(66,165,245,0.15), rgba(33,150,243,0.1)); }
  .record-icon.red { background: linear-gradient(135deg, rgba(239,83,80,0.15), rgba(229,57,53,0.1)); }
  .record-icon.purple { background: linear-gradient(135deg, rgba(171,71,188,0.15), rgba(142,36,170,0.1)); }
  .record-icon.orange { background: linear-gradient(135deg, rgba(255,167,38,0.15), rgba(255,143,0,0.1)); }

  .record-info { flex: 1; min-width: 0; }
  .record-title {
    font-size: 0.8rem;
    color: #888;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin: 0 0 4px;
  }
  .record-value {
    font-size: 1.4rem;
    font-weight: 800;
    color: #fff;
    font-family: 'JetBrains Mono', monospace;
    margin: 0;
  }
  .record-detail {
    font-size: 0.75rem;
    color: #555;
    margin: 2px 0 0;
  }

  /* ═══════════════════════════════════════════════════════════════════════════
     CHART
     ═══════════════════════════════════════════════════════════════════════════ */
  .chart-container {
    max-width: 1200px;
    margin: 0 auto;
    background: linear-gradient(135deg, #111118, #14141e);
    border: 1px solid #1e1e2e;
    border-radius: 16px;
    padding: 24px;
    position: relative;
    overflow: hidden;
  }
  .chart-tabs {
    display: flex;
    gap: 8px;
    margin-bottom: 20px;
    flex-wrap: wrap;
  }
  .chart-tab {
    padding: 6px 16px;
    background: #0a0a0f;
    border: 1px solid #1e1e2e;
    border-radius: 10px;
    color: #888;
    font-size: 0.75rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s;
    font-family: 'Inter', sans-serif;
  }
  .chart-tab:hover { border-color: #444; color: #ccc; }
  .chart-tab.active {
    background: linear-gradient(135deg, rgba(0,230,118,0.12), rgba(0,200,83,0.08));
    border-color: #00E676;
    color: #00E676;
  }
  #speed-chart {
    width: 100%;
    height: 300px;
    display: block;
  }

  /* ═══════════════════════════════════════════════════════════════════════════
     RUNS TABLE
     ═══════════════════════════════════════════════════════════════════════════ */
  .table-container {
    max-width: 1200px;
    margin: 0 auto;
    background: linear-gradient(135deg, #111118, #14141e);
    border: 1px solid #1e1e2e;
    border-radius: 16px;
    overflow: hidden;
  }
  .table-toolbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 16px 20px;
    border-bottom: 1px solid #1e1e2e;
    flex-wrap: wrap;
    gap: 12px;
  }
  .table-search {
    padding: 10px 16px;
    background: #0a0a0f;
    border: 1px solid #1e1e2e;
    border-radius: 10px;
    color: #fff;
    font-size: 0.85rem;
    font-family: 'Inter', sans-serif;
    outline: none;
    transition: all 0.3s;
    min-width: 200px;
  }
  .table-search::placeholder { color: #444; }
  .table-search:focus {
    border-color: #00E676;
    box-shadow: 0 0 0 3px rgba(0,230,118,0.1);
  }
  .table-count {
    font-size: 0.8rem;
    color: #888;
    font-family: 'JetBrains Mono', monospace;
  }

  .runs-table {
    width: 100%;
    border-collapse: collapse;
  }
  .runs-table th {
    padding: 12px 16px;
    text-align: left;
    font-size: 0.7rem;
    font-weight: 700;
    color: #666;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    border-bottom: 1px solid #1e1e2e;
    cursor: pointer;
    user-select: none;
    transition: color 0.2s;
    white-space: nowrap;
  }
  .runs-table th:hover { color: #00E676; }
  .runs-table th.sorted { color: #00E676; }
  .runs-table th .sort-arrow {
    font-size: 0.6rem;
    margin-left: 4px;
    opacity: 0.5;
  }
  .runs-table th.sorted .sort-arrow { opacity: 1; }

  .runs-table td {
    padding: 14px 16px;
    font-size: 0.85rem;
    border-bottom: 1px solid #111118;
    white-space: nowrap;
  }
  .runs-table tr {
    transition: background 0.2s;
  }
  .runs-table tbody tr:hover {
    background: rgba(0,230,118,0.03);
  }
  .run-name {
    font-weight: 600;
    color: #eee;
    max-width: 200px;
    overflow: hidden;
    text-overflow: ellipsis;
  }
  .run-date { color: #888; font-family: 'JetBrains Mono', monospace; font-size: 0.8rem; }
  .run-distance { color: #00E676; font-weight: 700; font-family: 'JetBrains Mono', monospace; }
  .run-duration { color: #ccc; font-family: 'JetBrains Mono', monospace; }
  .run-pace { color: #69F0AE; font-family: 'JetBrains Mono', monospace; }

  .speed-badge {
    font-size: 0.75rem;
    font-weight: 700;
    padding: 3px 10px;
    border-radius: 8px;
    font-family: 'JetBrains Mono', monospace;
    display: inline-block;
  }
  .speed-fast {
    background: rgba(0,230,118,0.12);
    color: #00E676;
    border: 1px solid rgba(0,230,118,0.2);
  }
  .speed-medium {
    background: rgba(255,167,38,0.12);
    color: #FFA726;
    border: 1px solid rgba(255,167,38,0.2);
  }
  .speed-slow {
    background: rgba(239,83,80,0.12);
    color: #ef5350;
    border: 1px solid rgba(239,83,80,0.2);
  }
  .hr-badge {
    font-size: 0.8rem;
    color: #ef5350;
    font-family: 'JetBrains Mono', monospace;
  }

  .table-scroll {
    overflow-x: auto;
  }

  /* ═══════════════════════════════════════════════════════════════════════════
     LOADING / EMPTY
     ═══════════════════════════════════════════════════════════════════════════ */
  .loading-overlay {
    text-align: center;
    padding: 80px 20px;
  }
  .spinner {
    width: 40px; height: 40px;
    border: 3px solid #222;
    border-top-color: #00E676;
    border-radius: 50%;
    animation: spin 0.8s linear infinite;
    margin: 0 auto 20px;
  }
  @keyframes spin { to { transform: rotate(360deg); } }
  .loading-text { color: #555; font-size: 0.9rem; }

  .empty-state {
    text-align: center;
    padding: 60px 20px;
    color: #444;
  }
  .empty-state-icon { font-size: 3rem; margin-bottom: 16px; }

  /* Toast */
  .toast {
    position: fixed;
    bottom: 30px; left: 50%;
    transform: translateX(-50%) translateY(100px);
    background: #1a1a24;
    border: 1px solid #333;
    color: #fff;
    padding: 12px 24px;
    border-radius: 12px;
    font-size: 0.85rem;
    font-weight: 500;
    z-index: 9999;
    transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    box-shadow: 0 8px 32px rgba(0,0,0,0.4);
  }
  .toast.show { transform: translateX(-50%) translateY(0); }
  .toast.error { border-color: #ef5350; }
  .toast.success { border-color: #00E676; }

  /* Responsive */
  @media (max-width: 600px) {
    .hero-title { font-size: 2rem; }
    .stats-grid { grid-template-columns: repeat(2, 1fr); }
    .records-grid { grid-template-columns: 1fr; }
    .runs-table th, .runs-table td { padding: 10px 10px; font-size: 0.75rem; }
  }
</style>

<div class="run-app" id="run-app">

  <!-- HERO -->
  <div class="hero">
    <h1 class="hero-title">🏃 Running Dashboard</h1>
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

  <!-- LOADING -->
  <div class="loading-overlay" id="loading">
    <div class="spinner"></div>
    <div class="loading-text">Fetching your runs...</div>
  </div>

  <!-- MAIN CONTENT (hidden until loaded) -->
  <div id="main-content" style="display:none;">

    <!-- SUMMARY STATS -->
    <div class="stats-grid" id="stats-grid"></div>

    <!-- PERSONAL RECORDS -->
    <div class="section-header">
      <h2>🏆 Personal Records</h2>
      <div class="section-line"></div>
    </div>
    <div class="records-grid" id="records-grid"></div>

    <!-- CHART -->
    <div class="section-header">
      <h2>📈 Trends</h2>
      <div class="section-line"></div>
    </div>
    <div class="chart-container">
      <div class="chart-tabs" id="chart-tabs">
        <button class="chart-tab active" data-metric="maxSpeed" onclick="switchChart('maxSpeed')">Max Speed</button>
        <button class="chart-tab" data-metric="distance" onclick="switchChart('distance')">Distance</button>
        <button class="chart-tab" data-metric="avgPace" onclick="switchChart('avgPace')">Avg Pace</button>
        <button class="chart-tab" data-metric="avgHr" onclick="switchChart('avgHr')">Avg HR</button>
      </div>
      <canvas id="speed-chart"></canvas>
    </div>

    <!-- RUNS TABLE -->
    <div class="section-header">
      <h2>📋 All Runs</h2>
      <div class="section-line"></div>
    </div>
    <div class="table-container">
      <div class="table-toolbar">
        <input type="text" class="table-search" id="table-search" placeholder="🔍 Search runs...">
        <span class="table-count" id="table-count"></span>
      </div>
      <div class="table-scroll">
        <table class="runs-table">
          <thead>
            <tr>
              <th onclick="sortTable('date')" id="th-date" class="sorted">Date <span class="sort-arrow">▼</span></th>
              <th onclick="sortTable('name')" id="th-name">Name <span class="sort-arrow">▼</span></th>
              <th onclick="sortTable('distance')" id="th-distance">Distance <span class="sort-arrow">▼</span></th>
              <th onclick="sortTable('duration')" id="th-duration">Duration <span class="sort-arrow">▼</span></th>
              <th onclick="sortTable('avgPace')" id="th-avgPace">Avg Pace <span class="sort-arrow">▼</span></th>
              <th onclick="sortTable('maxSpeed')" id="th-maxSpeed">Max Speed <span class="sort-arrow">▼</span></th>
              <th onclick="sortTable('avgHr')" id="th-avgHr">Avg HR <span class="sort-arrow">▼</span></th>
              <th onclick="sortTable('calories')" id="th-calories">Calories <span class="sort-arrow">▼</span></th>
            </tr>
          </thead>
          <tbody id="runs-tbody"></tbody>
        </table>
      </div>
    </div>

    <!-- EMPTY STATE -->
    <div class="empty-state" id="empty-state" style="display:none;">
      <div class="empty-state-icon">🏃</div>
      <p>No runs found yet. Sync your Garmin data to get started!</p>
    </div>

  </div>
</div>

<div class="toast" id="toast"></div>

<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/dist/umd/supabase.min.js"></script>

<script>
// ═══════════════════════════════════════════════════════════════════════════
// CONFIG
// ═══════════════════════════════════════════════════════════════════════════
const SUPABASE_URL = 'https://uuzrzcnvieygjlihgwnb.supabase.co';
const SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InV1enJ6Y252aWV5Z2psaWhnd25iIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Nzc4MDE3OTEsImV4cCI6MjA5MzM3Nzc5MX0._LP_f3WtKPVEvVCG1Uqh5S5ARHSHF7maopdWIbWg7Mw';

const sb = supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);

// ═══════════════════════════════════════════════════════════════════════════
// STATE
// ═══════════════════════════════════════════════════════════════════════════
let allRuns = [];
let filteredRuns = [];
let sortField = 'date';
let sortAsc = false;
let currentChartMetric = 'maxSpeed';

// ═══════════════════════════════════════════════════════════════════════════
// HELPERS
// ═══════════════════════════════════════════════════════════════════════════
function msToKmh(ms) {
  return ms ? (ms * 3.6).toFixed(1) : '—';
}
function mToKm(m) {
  return m ? (m / 1000).toFixed(2) : '—';
}
function secondsToHMS(s) {
  if (!s) return '—';
  const h = Math.floor(s / 3600);
  const m = Math.floor((s % 3600) / 60);
  const sec = Math.floor(s % 60);
  if (h > 0) return `${h}h ${m}m ${sec}s`;
  return `${m}m ${sec}s`;
}
function secondsToPace(avgSpeedMs) {
  // pace = min/km
  if (!avgSpeedMs || avgSpeedMs <= 0) return '—';
  const paceSeconds = 1000 / avgSpeedMs; // seconds per km
  const min = Math.floor(paceSeconds / 60);
  const sec = Math.floor(paceSeconds % 60);
  return `${min}:${String(sec).padStart(2, '0')}`;
}
function formatDate(dateStr) {
  if (!dateStr) return '—';
  const d = new Date(dateStr);
  return d.toLocaleDateString('en-IN', { day: '2-digit', month: 'short', year: 'numeric' });
}
function formatDateShort(dateStr) {
  if (!dateStr) return '';
  const d = new Date(dateStr);
  return d.toLocaleDateString('en-IN', { day: '2-digit', month: 'short' });
}
function getSpeedClass(maxSpeedKmh) {
  if (maxSpeedKmh >= 15) return 'speed-fast';
  if (maxSpeedKmh >= 10) return 'speed-medium';
  return 'speed-slow';
}

// ═══════════════════════════════════════════════════════════════════════════
// DATA LOADING
// ═══════════════════════════════════════════════════════════════════════════
async function loadData() {
  try {
    const { data, error } = await sb
      .from('garmin_activities')
      .select('*')
      .order('start_time', { ascending: false });

    if (error) throw error;

    allRuns = (data || []).map(r => ({
      ...r,
      distanceKm: r.distance ? r.distance / 1000 : 0,
      maxSpeedKmh: r.max_speed ? r.max_speed * 3.6 : 0,
      avgSpeedKmh: r.avg_speed ? r.avg_speed * 3.6 : 0,
      paceMinKm: r.avg_speed && r.avg_speed > 0 ? (1000 / r.avg_speed) / 60 : 0,
    }));

    filteredRuns = [...allRuns];

    document.getElementById('connection-badge').className = 'connection-badge online';
    document.getElementById('connection-text').textContent = 'Cloud Synced';
    document.getElementById('loading').style.display = 'none';
    document.getElementById('main-content').style.display = 'block';

    if (allRuns.length === 0) {
      document.getElementById('empty-state').style.display = 'block';
      document.getElementById('last-sync').textContent = 'No data yet';
      return;
    }

    // Last sync
    const latestSync = allRuns.reduce((a, b) =>
      new Date(a.synced_at) > new Date(b.synced_at) ? a : b
    );
    document.getElementById('last-sync').textContent =
      'Last sync: ' + formatDate(latestSync.synced_at);

    renderStats();
    renderRecords();
    renderTable();
    renderChart();

  } catch (err) {
    console.error('Load error:', err);
    document.getElementById('connection-badge').className = 'connection-badge offline';
    document.getElementById('connection-text').textContent = 'Offline';
    document.getElementById('loading').innerHTML = `
      <div class="empty-state-icon">⚠️</div>
      <p style="color:#ef5350;">Could not connect to database</p>
    `;
    showToast('⚠️ Failed to load data', 'error');
  }
}

// ═══════════════════════════════════════════════════════════════════════════
// SUMMARY STATS
// ═══════════════════════════════════════════════════════════════════════════
function renderStats() {
  const totalRuns = allRuns.length;
  const totalDist = allRuns.reduce((s, r) => s + r.distanceKm, 0);
  const totalTime = allRuns.reduce((s, r) => s + (r.duration || 0), 0);
  const avgPace = allRuns.filter(r => r.paceMinKm > 0).length > 0
    ? allRuns.filter(r => r.paceMinKm > 0).reduce((s, r) => s + r.paceMinKm, 0) / allRuns.filter(r => r.paceMinKm > 0).length
    : 0;
  const totalCalories = allRuns.reduce((s, r) => s + (r.calories || 0), 0);
  const avgHr = allRuns.filter(r => r.avg_hr).length > 0
    ? Math.round(allRuns.filter(r => r.avg_hr).reduce((s, r) => s + r.avg_hr, 0) / allRuns.filter(r => r.avg_hr).length)
    : 0;

  const paceMin = Math.floor(avgPace);
  const paceSec = Math.round((avgPace - paceMin) * 60);

  document.getElementById('stats-grid').innerHTML = `
    <div class="stat-card">
      <span class="stat-icon">🏃</span>
      <span class="stat-value">${totalRuns}</span>
      <span class="stat-label">Total Runs</span>
    </div>
    <div class="stat-card">
      <span class="stat-icon">📏</span>
      <span class="stat-value">${totalDist.toFixed(1)}</span>
      <span class="stat-label">Total KM</span>
    </div>
    <div class="stat-card">
      <span class="stat-icon">⏱️</span>
      <span class="stat-value">${secondsToHMS(totalTime)}</span>
      <span class="stat-label">Total Time</span>
    </div>
    <div class="stat-card">
      <span class="stat-icon">💨</span>
      <span class="stat-value">${paceMin}:${String(paceSec).padStart(2,'0')}</span>
      <span class="stat-label">Avg Pace (min/km)</span>
    </div>
    <div class="stat-card">
      <span class="stat-icon">🔥</span>
      <span class="stat-value">${totalCalories.toLocaleString()}</span>
      <span class="stat-label">Calories Burned</span>
    </div>
    <div class="stat-card">
      <span class="stat-icon">❤️</span>
      <span class="stat-value">${avgHr || '—'}</span>
      <span class="stat-label">Avg Heart Rate</span>
    </div>
  `;
}

// ═══════════════════════════════════════════════════════════════════════════
// PERSONAL RECORDS
// ═══════════════════════════════════════════════════════════════════════════
function renderRecords() {
  if (allRuns.length === 0) return;

  // Longest run
  const longest = allRuns.reduce((a, b) => a.distanceKm > b.distanceKm ? a : b);
  // Fastest max speed
  const fastestSpeed = allRuns.reduce((a, b) => a.maxSpeedKmh > b.maxSpeedKmh ? a : b);
  // Best average pace (lowest min/km)
  const runsWithPace = allRuns.filter(r => r.paceMinKm > 0);
  const bestPace = runsWithPace.length > 0
    ? runsWithPace.reduce((a, b) => a.paceMinKm < b.paceMinKm ? a : b)
    : null;
  // Highest max HR
  const runsWithHr = allRuns.filter(r => r.max_hr);
  const highestHr = runsWithHr.length > 0
    ? runsWithHr.reduce((a, b) => a.max_hr > b.max_hr ? a : b)
    : null;
  // Most calories
  const mostCalories = allRuns.reduce((a, b) => (a.calories || 0) > (b.calories || 0) ? a : b);
  // Longest duration
  const longestTime = allRuns.reduce((a, b) => (a.duration || 0) > (b.duration || 0) ? a : b);

  const bestPaceMin = bestPace ? Math.floor(bestPace.paceMinKm) : 0;
  const bestPaceSec = bestPace ? Math.round((bestPace.paceMinKm - bestPaceMin) * 60) : 0;

  document.getElementById('records-grid').innerHTML = `
    <div class="record-card">
      <div class="record-icon gold">🏅</div>
      <div class="record-info">
        <div class="record-title">Longest Run</div>
        <div class="record-value">${longest.distanceKm.toFixed(2)} km</div>
        <div class="record-detail">${longest.activity_name} — ${formatDate(longest.start_time)}</div>
      </div>
    </div>
    <div class="record-card">
      <div class="record-icon green">⚡</div>
      <div class="record-info">
        <div class="record-title">Fastest Max Speed</div>
        <div class="record-value">${fastestSpeed.maxSpeedKmh.toFixed(1)} km/h</div>
        <div class="record-detail">${fastestSpeed.activity_name} — ${formatDate(fastestSpeed.start_time)}</div>
      </div>
    </div>
    ${bestPace ? `
    <div class="record-card">
      <div class="record-icon blue">💨</div>
      <div class="record-info">
        <div class="record-title">Best Average Pace</div>
        <div class="record-value">${bestPaceMin}:${String(bestPaceSec).padStart(2,'0')} /km</div>
        <div class="record-detail">${bestPace.activity_name} — ${formatDate(bestPace.start_time)}</div>
      </div>
    </div>
    ` : ''}
    ${highestHr ? `
    <div class="record-card">
      <div class="record-icon red">❤️</div>
      <div class="record-info">
        <div class="record-title">Highest Max HR</div>
        <div class="record-value">${highestHr.max_hr} bpm</div>
        <div class="record-detail">${highestHr.activity_name} — ${formatDate(highestHr.start_time)}</div>
      </div>
    </div>
    ` : ''}
    <div class="record-card">
      <div class="record-icon orange">🔥</div>
      <div class="record-info">
        <div class="record-title">Most Calories</div>
        <div class="record-value">${(mostCalories.calories || 0).toLocaleString()} cal</div>
        <div class="record-detail">${mostCalories.activity_name} — ${formatDate(mostCalories.start_time)}</div>
      </div>
    </div>
    <div class="record-card">
      <div class="record-icon purple">⏱️</div>
      <div class="record-info">
        <div class="record-title">Longest Duration</div>
        <div class="record-value">${secondsToHMS(longestTime.duration)}</div>
        <div class="record-detail">${longestTime.activity_name} — ${formatDate(longestTime.start_time)}</div>
      </div>
    </div>
  `;
}

// ═══════════════════════════════════════════════════════════════════════════
// CHART — Vanilla Canvas
// ═══════════════════════════════════════════════════════════════════════════
function switchChart(metric) {
  currentChartMetric = metric;
  document.querySelectorAll('.chart-tab').forEach(t =>
    t.classList.toggle('active', t.getAttribute('data-metric') === metric)
  );
  renderChart();
}

function renderChart() {
  const canvas = document.getElementById('speed-chart');
  const ctx = canvas.getContext('2d');
  const dpr = window.devicePixelRatio || 1;

  // Sort by date ascending for chart
  const sorted = [...allRuns].sort((a, b) =>
    new Date(a.start_time) - new Date(b.start_time)
  );

  if (sorted.length === 0) return;

  // Extract values based on metric
  let values, label, unit, color;
  switch (currentChartMetric) {
    case 'maxSpeed':
      values = sorted.map(r => r.maxSpeedKmh);
      label = 'Max Speed'; unit = 'km/h';
      color = '#00E676';
      break;
    case 'distance':
      values = sorted.map(r => r.distanceKm);
      label = 'Distance'; unit = 'km';
      color = '#42A5F5';
      break;
    case 'avgPace':
      values = sorted.map(r => r.paceMinKm > 0 ? r.paceMinKm : null);
      label = 'Avg Pace'; unit = 'min/km';
      color = '#FFA726';
      break;
    case 'avgHr':
      values = sorted.map(r => r.avg_hr || null);
      label = 'Avg HR'; unit = 'bpm';
      color = '#ef5350';
      break;
  }

  const dates = sorted.map(r => formatDateShort(r.start_time));

  // Canvas sizing
  const rect = canvas.parentElement.getBoundingClientRect();
  canvas.width = rect.width * dpr;
  canvas.height = 300 * dpr;
  canvas.style.width = rect.width + 'px';
  canvas.style.height = '300px';
  ctx.scale(dpr, dpr);

  const W = rect.width;
  const H = 300;
  const pad = { top: 30, right: 20, bottom: 40, left: 55 };
  const chartW = W - pad.left - pad.right;
  const chartH = H - pad.top - pad.bottom;

  // Clear
  ctx.clearRect(0, 0, W, H);

  // Filter valid values for range calculation
  const validValues = values.filter(v => v !== null && v !== undefined && v > 0);
  if (validValues.length === 0) return;

  const minVal = Math.min(...validValues) * 0.9;
  const maxVal = Math.max(...validValues) * 1.1;
  const range = maxVal - minVal || 1;

  // Grid lines
  ctx.strokeStyle = '#1e1e2e';
  ctx.lineWidth = 1;
  const gridLines = 5;
  for (let i = 0; i <= gridLines; i++) {
    const y = pad.top + (chartH / gridLines) * i;
    ctx.beginPath();
    ctx.moveTo(pad.left, y);
    ctx.lineTo(W - pad.right, y);
    ctx.stroke();

    // Y-axis labels
    const val = maxVal - (range / gridLines) * i;
    ctx.fillStyle = '#555';
    ctx.font = '11px JetBrains Mono';
    ctx.textAlign = 'right';
    if (currentChartMetric === 'avgPace') {
      const m = Math.floor(val);
      const s = Math.round((val - m) * 60);
      ctx.fillText(`${m}:${String(s).padStart(2,'0')}`, pad.left - 8, y + 4);
    } else {
      ctx.fillText(val.toFixed(1), pad.left - 8, y + 4);
    }
  }

  // Plot points & line
  const points = [];
  for (let i = 0; i < values.length; i++) {
    if (values[i] === null || values[i] === undefined) continue;
    const x = pad.left + (i / Math.max(values.length - 1, 1)) * chartW;
    const y = pad.top + chartH - ((values[i] - minVal) / range) * chartH;
    points.push({ x, y, val: values[i], label: dates[i] });
  }

  if (points.length < 2) return;

  // Gradient fill
  const gradient = ctx.createLinearGradient(0, pad.top, 0, H - pad.bottom);
  gradient.addColorStop(0, color + '30');
  gradient.addColorStop(1, color + '05');

  ctx.beginPath();
  ctx.moveTo(points[0].x, H - pad.bottom);
  ctx.lineTo(points[0].x, points[0].y);
  for (let i = 1; i < points.length; i++) {
    const cp1x = (points[i-1].x + points[i].x) / 2;
    ctx.bezierCurveTo(cp1x, points[i-1].y, cp1x, points[i].y, points[i].x, points[i].y);
  }
  ctx.lineTo(points[points.length-1].x, H - pad.bottom);
  ctx.closePath();
  ctx.fillStyle = gradient;
  ctx.fill();

  // Line
  ctx.beginPath();
  ctx.moveTo(points[0].x, points[0].y);
  for (let i = 1; i < points.length; i++) {
    const cp1x = (points[i-1].x + points[i].x) / 2;
    ctx.bezierCurveTo(cp1x, points[i-1].y, cp1x, points[i].y, points[i].x, points[i].y);
  }
  ctx.strokeStyle = color;
  ctx.lineWidth = 2.5;
  ctx.stroke();

  // Dots
  points.forEach(p => {
    ctx.beginPath();
    ctx.arc(p.x, p.y, 3.5, 0, Math.PI * 2);
    ctx.fillStyle = color;
    ctx.fill();
    ctx.beginPath();
    ctx.arc(p.x, p.y, 2, 0, Math.PI * 2);
    ctx.fillStyle = '#0a0a0f';
    ctx.fill();
  });

  // X-axis labels (show ~10 labels max)
  const labelStep = Math.max(1, Math.floor(points.length / 10));
  ctx.fillStyle = '#555';
  ctx.font = '10px JetBrains Mono';
  ctx.textAlign = 'center';
  for (let i = 0; i < points.length; i += labelStep) {
    ctx.fillText(points[i].label, points[i].x, H - pad.bottom + 18);
  }

  // Unit label
  ctx.fillStyle = '#666';
  ctx.font = '11px Inter';
  ctx.textAlign = 'left';
  ctx.fillText(`${label} (${unit})`, pad.left, pad.top - 10);
}

// ═══════════════════════════════════════════════════════════════════════════
// RUNS TABLE
// ═══════════════════════════════════════════════════════════════════════════
function sortTable(field) {
  if (sortField === field) {
    sortAsc = !sortAsc;
  } else {
    sortField = field;
    sortAsc = false;
  }

  // Update header styles
  document.querySelectorAll('.runs-table th').forEach(th => th.classList.remove('sorted'));
  const th = document.getElementById(`th-${field}`);
  if (th) {
    th.classList.add('sorted');
    th.querySelector('.sort-arrow').textContent = sortAsc ? '▲' : '▼';
  }

  renderTable();
}

function renderTable() {
  const search = (document.getElementById('table-search').value || '').toLowerCase();

  let rows = filteredRuns;
  if (search) {
    rows = rows.filter(r =>
      (r.activity_name || '').toLowerCase().includes(search) ||
      formatDate(r.start_time).toLowerCase().includes(search)
    );
  }

  // Sort
  rows.sort((a, b) => {
    let va, vb;
    switch (sortField) {
      case 'date': va = new Date(a.start_time); vb = new Date(b.start_time); break;
      case 'name': va = (a.activity_name || '').toLowerCase(); vb = (b.activity_name || '').toLowerCase(); break;
      case 'distance': va = a.distanceKm; vb = b.distanceKm; break;
      case 'duration': va = a.duration || 0; vb = b.duration || 0; break;
      case 'avgPace': va = a.paceMinKm || 999; vb = b.paceMinKm || 999; break;
      case 'maxSpeed': va = a.maxSpeedKmh; vb = b.maxSpeedKmh; break;
      case 'avgHr': va = a.avg_hr || 0; vb = b.avg_hr || 0; break;
      case 'calories': va = a.calories || 0; vb = b.calories || 0; break;
      default: va = 0; vb = 0;
    }
    if (va < vb) return sortAsc ? -1 : 1;
    if (va > vb) return sortAsc ? 1 : -1;
    return 0;
  });

  document.getElementById('table-count').textContent = `${rows.length} runs`;

  const tbody = document.getElementById('runs-tbody');
  if (rows.length === 0) {
    tbody.innerHTML = `<tr><td colspan="8" style="text-align:center;color:#555;padding:30px;">No runs match your search</td></tr>`;
    return;
  }

  tbody.innerHTML = rows.map(r => {
    const paceMin = Math.floor(r.paceMinKm);
    const paceSec = Math.round((r.paceMinKm - paceMin) * 60);
    const paceStr = r.paceMinKm > 0 ? `${paceMin}:${String(paceSec).padStart(2,'0')}` : '—';
    const speedClass = getSpeedClass(r.maxSpeedKmh);

    return `
      <tr>
        <td class="run-date">${formatDate(r.start_time)}</td>
        <td class="run-name" title="${r.activity_name || ''}">${r.activity_name || 'Run'}</td>
        <td class="run-distance">${r.distanceKm.toFixed(2)} km</td>
        <td class="run-duration">${secondsToHMS(r.duration)}</td>
        <td class="run-pace">${paceStr} /km</td>
        <td><span class="speed-badge ${speedClass}">${r.maxSpeedKmh.toFixed(1)} km/h</span></td>
        <td class="hr-badge">${r.avg_hr ? `♥ ${Math.round(r.avg_hr)}` : '—'}</td>
        <td style="color:#ccc;font-family:'JetBrains Mono',monospace;">${r.calories ? Math.round(r.calories) : '—'}</td>
      </tr>
    `;
  }).join('');
}

// ═══════════════════════════════════════════════════════════════════════════
// TOAST
// ═══════════════════════════════════════════════════════════════════════════
function showToast(message, type = 'success') {
  const toast = document.getElementById('toast');
  toast.textContent = message;
  toast.className = `toast ${type} show`;
  setTimeout(() => toast.classList.remove('show'), 3000);
}

// ═══════════════════════════════════════════════════════════════════════════
// SYNC & REFRESH
// ═══════════════════════════════════════════════════════════════════════════
const GITHUB_REPO = 'sans242/sans242.github.io';
const WORKFLOW_FILE = 'sync_garmin.yml';

async function triggerGarminSync() {
  const btn = document.getElementById('btn-garmin-sync');

  // Get or prompt for GitHub PAT
  let pat = localStorage.getItem('gh_pat');
  if (!pat) {
    pat = prompt(
      'To trigger sync, you need a GitHub Personal Access Token (PAT) with "actions:write" permission.\n\n' +
      'Create one at: https://github.com/settings/tokens\n\n' +
      'Paste your token (it will be saved locally):'
    );
    if (!pat) return;
    localStorage.setItem('gh_pat', pat.trim());
    pat = pat.trim();
  }

  btn.classList.add('loading');
  btn.disabled = true;

  try {
    const res = await fetch(
      `https://api.github.com/repos/${GITHUB_REPO}/actions/workflows/${WORKFLOW_FILE}/dispatches`,
      {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${pat}`,
          'Accept': 'application/vnd.github+json',
          'X-GitHub-Api-Version': '2022-11-28',
        },
        body: JSON.stringify({ ref: 'master' }),
      }
    );

    if (res.status === 204) {
      showToast('✅ Sync triggered! Data will update in ~2 minutes.', 'success');
      // Auto-refresh data after 2 minutes
      setTimeout(() => refreshData(), 120000);
    } else if (res.status === 401 || res.status === 403) {
      localStorage.removeItem('gh_pat');
      showToast('❌ Invalid token. Please try again.', 'error');
    } else {
      const body = await res.text();
      console.error('GitHub API error:', res.status, body);
      showToast(`❌ Sync failed (${res.status})`, 'error');
    }
  } catch (err) {
    console.error('Sync trigger error:', err);
    showToast('❌ Could not reach GitHub API', 'error');
  } finally {
    btn.classList.remove('loading');
    btn.disabled = false;
  }
}

async function refreshData() {
  const btn = document.getElementById('btn-refresh');
  btn.classList.add('loading');
  btn.disabled = true;

  try {
    await loadData();
    showToast('✅ Data refreshed!', 'success');
  } catch (err) {
    showToast('❌ Refresh failed', 'error');
  } finally {
    btn.classList.remove('loading');
    btn.disabled = false;
  }
}

// ═══════════════════════════════════════════════════════════════════════════
// INIT
// ═══════════════════════════════════════════════════════════════════════════
document.addEventListener('DOMContentLoaded', () => {
  loadData();
  document.getElementById('table-search').addEventListener('input', renderTable);
  window.addEventListener('resize', () => {
    if (allRuns.length > 0) renderChart();
  });
});
</script>
