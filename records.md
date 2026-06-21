---
layout: page
title: Race Records
subtitle: Official Garmin Personal Bests
---

<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">

<style>
  .container-md, .container { max-width: 100% !important; width: 100% !important; padding: 0 !important; margin: 0 !important; }
  .records-app { font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif; background: #0a0a0f; color: #e0e0e0; min-height: 100vh; padding: 0 20px 60px; }

  /* HERO */
  .hero { text-align: center; padding: 50px 20px 30px; position: relative; overflow: hidden; }
  .hero::before { content: ''; position: absolute; top: -50%; left: -50%; width: 200%; height: 200%; background: radial-gradient(ellipse at center, rgba(255,193,7,0.06) 0%, transparent 60%); pointer-events: none; }
  .hero-title { font-size: 2.8rem; font-weight: 900; background: linear-gradient(135deg, #FFD54F, #FFC107, #FF8F00, #FFB300); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; margin: 0 0 8px; letter-spacing: -0.02em; }
  .hero-sub { color: #666; font-size: 1rem; font-weight: 400; margin: 0; }
  .hero-sub .last-sync { color: #FFD54F; font-family: 'JetBrains Mono', monospace; font-size: 0.85rem; }
  .hero-nav { display: flex; justify-content: center; gap: 10px; margin-top: 16px; flex-wrap: wrap; }
  .hero-nav a { display: inline-flex; align-items: center; gap: 8px; padding: 10px 22px; border-radius: 12px; font-size: 0.8rem; font-weight: 700; font-family: 'Inter', sans-serif; cursor: pointer; transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1); border: 1px solid; text-transform: uppercase; letter-spacing: 0.05em; text-decoration: none; }
  .hero-nav a.primary { background: linear-gradient(135deg, rgba(0,230,118,0.15), rgba(0,200,83,0.08)); border-color: rgba(0,230,118,0.4); color: #00E676; }
  .hero-nav a.primary:hover { background: linear-gradient(135deg, rgba(0,230,118,0.25), rgba(0,200,83,0.15)); box-shadow: 0 4px 20px rgba(0,230,118,0.2); }

  /* CONNECTION BADGE */
  .connection-badge { display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; border-radius: 20px; font-size: 0.7rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; margin-top: 12px; }
  .connection-badge.online { background: rgba(255,193,7,0.1); color: #FFD54F; border: 1px solid rgba(255,193,7,0.2); }
  .connection-badge.offline { background: rgba(245,101,101,0.1); color: #f56565; border: 1px solid rgba(245,101,101,0.2); }
  .connection-dot { width: 6px; height: 6px; border-radius: 50%; background: currentColor; animation: pulse-dot 2s infinite; }
  @keyframes pulse-dot { 0%, 100% { opacity: 1; } 50% { opacity: 0.4; } }

  /* SECTION HEADERS */
  .section-header { max-width: 1200px; margin: 40px auto 20px; display: flex; align-items: center; gap: 12px; }
  .section-header h2 { font-size: 1.3rem; font-weight: 800; color: #fff; margin: 0; }
  .section-line { flex: 1; height: 1px; background: linear-gradient(90deg, #1e1e2e, transparent); }

  /* PR SHOWCASE - Hero cards for each distance */
  .pr-showcase { max-width: 1200px; margin: 30px auto; display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 20px; }
  .pr-card { background: linear-gradient(135deg, #111118, #14141e); border: 1px solid #1e1e2e; border-radius: 20px; padding: 0; overflow: hidden; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1); position: relative; }
  .pr-card::before { content: ''; position: absolute; inset: 0; border-radius: 20px; opacity: 0; transition: opacity 0.4s; pointer-events: none; }
  .pr-card:hover { transform: translateY(-4px); box-shadow: 0 16px 48px rgba(0,0,0,0.4); }
  .pr-card:hover::before { opacity: 1; }
  .pr-card-header { padding: 24px 24px 12px; display: flex; align-items: center; gap: 16px; position: relative; z-index: 1; }
  .pr-distance-badge { min-width: 64px; height: 64px; border-radius: 16px; display: flex; align-items: center; justify-content: center; font-size: 1.1rem; font-weight: 900; font-family: 'JetBrains Mono', monospace; flex-shrink: 0; line-height: 1.2; text-align: center; }
  .pr-card-header-text { flex: 1; }
  .pr-card-header-text h3 { font-size: 1.1rem; font-weight: 800; color: #fff; margin: 0 0 2px; }
  .pr-card-header-text .pr-distance-label { font-size: 0.7rem; color: #666; text-transform: uppercase; letter-spacing: 0.1em; margin: 0; }
  .pr-card-body { padding: 0 24px 24px; position: relative; z-index: 1; }
  .pr-time { font-size: 2.4rem; font-weight: 900; font-family: 'JetBrains Mono', monospace; margin: 8px 0 4px; line-height: 1.1; }
  .pr-pace { font-size: 0.85rem; color: #888; font-family: 'JetBrains Mono', monospace; margin: 0 0 12px; }
  .pr-meta { display: flex; gap: 16px; flex-wrap: wrap; }
  .pr-meta-item { font-size: 0.75rem; color: #555; }
  .pr-meta-item span { color: #aaa; font-weight: 600; }
  .pr-garmin-badge { display: inline-block; padding: 2px 8px; border-radius: 6px; font-size: 0.6rem; font-weight: 700; font-family: 'JetBrains Mono', monospace; text-transform: uppercase; letter-spacing: 0.05em; background: rgba(0,230,118,0.1); color: #69F0AE; border: 1px solid rgba(0,230,118,0.2); }

  /* Color themes for each distance */
  .pr-card.gold { border-color: rgba(255,215,0,0.15); }
  .pr-card.gold:hover { border-color: rgba(255,215,0,0.4); }
  .pr-card.gold::before { background: linear-gradient(135deg, rgba(255,215,0,0.04), transparent); }
  .pr-card.gold .pr-distance-badge { background: linear-gradient(135deg, rgba(255,215,0,0.2), rgba(255,165,0,0.12)); color: #FFD54F; }
  .pr-card.gold .pr-time { color: #FFD54F; }

  .pr-card.emerald { border-color: rgba(0,230,118,0.15); }
  .pr-card.emerald:hover { border-color: rgba(0,230,118,0.4); }
  .pr-card.emerald::before { background: linear-gradient(135deg, rgba(0,230,118,0.04), transparent); }
  .pr-card.emerald .pr-distance-badge { background: linear-gradient(135deg, rgba(0,230,118,0.2), rgba(0,200,83,0.12)); color: #69F0AE; }
  .pr-card.emerald .pr-time { color: #69F0AE; }

  .pr-card.sapphire { border-color: rgba(66,165,245,0.15); }
  .pr-card.sapphire:hover { border-color: rgba(66,165,245,0.4); }
  .pr-card.sapphire::before { background: linear-gradient(135deg, rgba(66,165,245,0.04), transparent); }
  .pr-card.sapphire .pr-distance-badge { background: linear-gradient(135deg, rgba(66,165,245,0.2), rgba(33,150,243,0.12)); color: #90CAF9; }
  .pr-card.sapphire .pr-time { color: #90CAF9; }

  .pr-card.ruby { border-color: rgba(239,83,80,0.15); }
  .pr-card.ruby:hover { border-color: rgba(239,83,80,0.4); }
  .pr-card.ruby::before { background: linear-gradient(135deg, rgba(239,83,80,0.04), transparent); }
  .pr-card.ruby .pr-distance-badge { background: linear-gradient(135deg, rgba(239,83,80,0.2), rgba(229,57,53,0.12)); color: #ef9a9a; }
  .pr-card.ruby .pr-time { color: #ef9a9a; }

  .pr-card.amethyst { border-color: rgba(171,71,188,0.15); }
  .pr-card.amethyst:hover { border-color: rgba(171,71,188,0.4); }
  .pr-card.amethyst::before { background: linear-gradient(135deg, rgba(171,71,188,0.04), transparent); }
  .pr-card.amethyst .pr-distance-badge { background: linear-gradient(135deg, rgba(171,71,188,0.2), rgba(142,36,170,0.12)); color: #CE93D8; }
  .pr-card.amethyst .pr-time { color: #CE93D8; }

  .pr-card.amber { border-color: rgba(255,167,38,0.15); }
  .pr-card.amber:hover { border-color: rgba(255,167,38,0.4); }
  .pr-card.amber::before { background: linear-gradient(135deg, rgba(255,167,38,0.04), transparent); }
  .pr-card.amber .pr-distance-badge { background: linear-gradient(135deg, rgba(255,167,38,0.2), rgba(255,143,0,0.12)); color: #FFE082; }
  .pr-card.amber .pr-time { color: #FFE082; }

  .pr-card.teal { border-color: rgba(38,198,218,0.15); }
  .pr-card.teal:hover { border-color: rgba(38,198,218,0.4); }
  .pr-card.teal::before { background: linear-gradient(135deg, rgba(38,198,218,0.04), transparent); }
  .pr-card.teal .pr-distance-badge { background: linear-gradient(135deg, rgba(38,198,218,0.2), rgba(0,172,193,0.12)); color: #80DEEA; }
  .pr-card.teal .pr-time { color: #80DEEA; }

  .pr-card.pink { border-color: rgba(236,64,122,0.15); }
  .pr-card.pink:hover { border-color: rgba(236,64,122,0.4); }
  .pr-card.pink::before { background: linear-gradient(135deg, rgba(236,64,122,0.04), transparent); }
  .pr-card.pink .pr-distance-badge { background: linear-gradient(135deg, rgba(236,64,122,0.2), rgba(194,24,91,0.12)); color: #F48FB1; }
  .pr-card.pink .pr-time { color: #F48FB1; }

  /* NO RECORD STATE */
  .pr-card.no-record { opacity: 0.4; }
  .pr-card.no-record .pr-time { color: #444; }

  /* ALL RECORDS TABLE */
  .records-table-container { max-width: 1200px; margin: 0 auto; background: linear-gradient(135deg, #111118, #14141e); border: 1px solid #1e1e2e; border-radius: 16px; overflow: hidden; }
  .records-table { width: 100%; border-collapse: collapse; }
  .records-table th { padding: 14px 18px; text-align: left; font-size: 0.7rem; font-weight: 700; color: #666; text-transform: uppercase; letter-spacing: 0.1em; border-bottom: 1px solid #1e1e2e; white-space: nowrap; }
  .records-table td { padding: 16px 18px; font-size: 0.85rem; border-bottom: 1px solid #111118; white-space: nowrap; }
  .records-table tr { transition: background 0.2s; }
  .records-table tbody tr:hover { background: rgba(255,193,7,0.03); }
  .rt-distance { color: #FFD54F; font-weight: 700; font-family: 'JetBrains Mono', monospace; }
  .rt-time { color: #fff; font-weight: 800; font-family: 'JetBrains Mono', monospace; font-size: 1rem; }
  .rt-pace { color: #69F0AE; font-family: 'JetBrains Mono', monospace; }
  .rt-speed { font-family: 'JetBrains Mono', monospace; color: #90CAF9; }
  .rt-run { color: #ccc; font-weight: 600; max-width: 200px; overflow: hidden; text-overflow: ellipsis; }
  .rt-date { color: #888; font-family: 'JetBrains Mono', monospace; font-size: 0.8rem; }
  .table-scroll { overflow-x: auto; }

  /* RAW DATA SECTION */
  .raw-records-grid { max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 16px; }
  .raw-record-card { background: linear-gradient(135deg, #111118, #14141e); border: 1px solid #1e1e2e; border-radius: 16px; padding: 20px 24px; display: flex; align-items: center; gap: 16px; transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1); }
  .raw-record-card:hover { border-color: rgba(255,193,7,0.3); transform: translateY(-2px); box-shadow: 0 8px 24px rgba(0,0,0,0.3); }
  .raw-record-icon { width: 52px; height: 52px; border-radius: 14px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; flex-shrink: 0; background: linear-gradient(135deg, rgba(255,193,7,0.15), rgba(255,143,0,0.1)); }
  .raw-record-info { flex: 1; min-width: 0; }
  .raw-record-title { font-size: 0.75rem; color: #888; text-transform: uppercase; letter-spacing: 0.05em; margin: 0 0 4px; }
  .raw-record-value { font-size: 1.3rem; font-weight: 800; color: #FFD54F; font-family: 'JetBrains Mono', monospace; margin: 0; }
  .raw-record-detail { font-size: 0.7rem; color: #555; margin: 2px 0 0; }

  /* LOADING / EMPTY / TOAST */
  .loading-overlay { text-align: center; padding: 80px 20px; }
  .spinner { width: 40px; height: 40px; border: 3px solid #222; border-top-color: #FFD54F; border-radius: 50%; animation: spin 0.8s linear infinite; margin: 0 auto 20px; }
  @keyframes spin { to { transform: rotate(360deg); } }
  .loading-text { color: #555; font-size: 0.9rem; }
  .empty-state { text-align: center; padding: 60px 20px; color: #444; }
  .empty-state-icon { font-size: 3rem; margin-bottom: 16px; }
  .toast { position: fixed; bottom: 30px; left: 50%; transform: translateX(-50%) translateY(100px); background: #1a1a24; border: 1px solid #333; color: #fff; padding: 12px 24px; border-radius: 12px; font-size: 0.85rem; font-weight: 500; z-index: 9999; transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1); box-shadow: 0 8px 32px rgba(0,0,0,0.4); }
  .toast.show { transform: translateX(-50%) translateY(0); }
  .toast.error { border-color: #ef5350; }
  .toast.success { border-color: #FFD54F; }

  /* INFO BOX */
  .info-box { max-width: 1200px; margin: 20px auto; padding: 16px 20px; background: linear-gradient(135deg, #111118, #14141e); border: 1px solid #1e1e2e; border-radius: 12px; font-size: 0.75rem; color: #555; line-height: 1.6; display: flex; align-items: flex-start; gap: 10px; }
  .info-box-icon { font-size: 1.2rem; flex-shrink: 0; margin-top: 2px; }
  .info-box a { color: #FFD54F; text-decoration: none; }
  .info-box a:hover { text-decoration: underline; }

  @media (max-width: 768px) {
    .hero-title { font-size: 2rem; }
    .pr-showcase { grid-template-columns: 1fr; }
    .raw-records-grid { grid-template-columns: 1fr; }
    .pr-time { font-size: 1.8rem; }
    .records-table th, .records-table td { padding: 10px 12px; font-size: 0.75rem; }
  }
</style>

<div class="records-app" id="records-app">
  <div class="hero">
    <h1 class="hero-title">🏅 Race Records</h1>
    <p class="hero-sub">Official Garmin Personal Bests — <span class="last-sync" id="last-sync">loading...</span></p>
    <div class="connection-badge offline" id="connection-badge">
      <span class="connection-dot"></span>
      <span id="connection-text">Connecting...</span>
    </div>
    <div class="hero-nav">
      <a href="/running" class="primary">🏃 Back to Running Dashboard</a>
    </div>
  </div>

  <div class="loading-overlay" id="loading">
    <div class="spinner"></div>
    <div class="loading-text">Loading your personal records...</div>
  </div>

  <div id="main-content" style="display:none;">
    <div class="section-header"><h2>🏅 Personal Best Times</h2><div class="section-line"></div></div>
    <div class="pr-showcase" id="pr-showcase"></div>

    <div class="info-box">
      <span class="info-box-icon">ℹ️</span>
      <div>These are your <strong style="color:#aaa;">official Garmin Connect personal records</strong> — the actual best split times recorded by your watch, not estimated or prorated. Sync from the <a href="/running">Running Dashboard</a> to update.</div>
    </div>

    <div class="section-header"><h2>📊 All Records at a Glance</h2><div class="section-line"></div></div>
    <div class="records-table-container">
      <div class="table-scroll">
        <table class="records-table">
          <thead>
            <tr>
              <th>Distance</th>
              <th>Best Time</th>
              <th>Avg Pace</th>
              <th>Avg Speed</th>
              <th>Date</th>
            </tr>
          </thead>
          <tbody id="records-tbody"></tbody>
        </table>
      </div>
    </div>

    <div class="section-header" style="margin-top:40px;"><h2>🏆 All Garmin Records</h2><div class="section-line"></div></div>
    <div class="raw-records-grid" id="raw-records-grid" style="margin-bottom: 40px;"></div>

    <div class="section-header" style="margin-top:40px;"><h2>⏱️ Computed Top 5 Performances</h2><div class="section-line"></div></div>
    <div class="info-box" style="margin-bottom: 20px;">
      <span class="info-box-icon">💡</span>
      <div>These top 5 leaderboards are <strong>computed from all your running activities</strong>. Only runs that closely match the target distance are included.</div>
    </div>
    <div id="top5-showcase"></div>

    <div class="empty-state" id="empty-state" style="display:none;">
      <div class="empty-state-icon">🏅</div>
      <p>No personal records found. Sync your Garmin data from the <a href="/running" style="color:#FFD54F;">Running Dashboard</a> first!</p>
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

// ═══════════════════════════════════════
//  RACE DISTANCE CONFIG
// ═══════════════════════════════════════
// Maps Garmin PR type keys to display info
const RACE_DISTANCES = {
  // Garmin uses various type keys — we map all known ones
  'pr_running_1k':          { name: '1K',             meters: 1000,     theme: 'emerald',  icon: '🟢', order: 1 },
  'pr_running_1_mile':      { name: '1 Mile',         meters: 1609.34,  theme: 'gold',     icon: '🥇', order: 2 },
  'pr_running_2_km':        { name: '2K',             meters: 2000,     theme: 'sapphire', icon: '🔵', order: 3 },
  'pr_running_5k':          { name: '5K',             meters: 5000,     theme: 'amber',    icon: '🟠', order: 4 },
  'pr_running_10k':         { name: '10K',            meters: 10000,    theme: 'teal',     icon: '🏃', order: 5 },
  'pr_running_half_marathon':{ name: 'Half Marathon', meters: 21097.5,  theme: 'amethyst', icon: '🟣', order: 6 },
  'pr_running_marathon':    { name: 'Marathon',       meters: 42195,    theme: 'ruby',     icon: '🔴', order: 7 },
  // Alternative key formats Garmin might use
  '1k':                     { name: '1K',             meters: 1000,     theme: 'emerald',  icon: '🟢', order: 1 },
  '1km':                    { name: '1K',             meters: 1000,     theme: 'emerald',  icon: '🟢', order: 1 },
  '1mile':                  { name: '1 Mile',         meters: 1609.34,  theme: 'gold',     icon: '🥇', order: 2 },
  '1_mile':                 { name: '1 Mile',         meters: 1609.34,  theme: 'gold',     icon: '🥇', order: 2 },
  '2k':                     { name: '2K',             meters: 2000,     theme: 'sapphire', icon: '🔵', order: 3 },
  '2km':                    { name: '2K',             meters: 2000,     theme: 'sapphire', icon: '🔵', order: 3 },
  '5k':                     { name: '5K',             meters: 5000,     theme: 'amber',    icon: '🟠', order: 4 },
  '5km':                    { name: '5K',             meters: 5000,     theme: 'amber',    icon: '🟠', order: 4 },
  '10k':                    { name: '10K',            meters: 10000,    theme: 'teal',     icon: '🏃', order: 5 },
  '10km':                   { name: '10K',            meters: 10000,    theme: 'teal',     icon: '🏃', order: 5 },
  'half_marathon':          { name: 'Half Marathon',  meters: 21097.5,  theme: 'amethyst', icon: '🟣', order: 6 },
  'marathon':               { name: 'Marathon',       meters: 42195,    theme: 'ruby',     icon: '🔴', order: 7 },
};

// Non-distance records we display differently
const OTHER_RECORD_TYPES = {
  'pr_running_longest_run':    { name: 'Longest Run',        icon: '📏', unit: 'distance' },
  'pr_running_max_distance':   { name: 'Longest Run',        icon: '📏', unit: 'distance' },
  'longest_run':               { name: 'Longest Run',        icon: '📏', unit: 'distance' },
  'max_distance':              { name: 'Longest Run',        icon: '📏', unit: 'distance' },
  'pr_running_most_ascent':    { name: 'Most Elevation Gain',icon: '⛰️', unit: 'distance' },
  'most_ascent':               { name: 'Most Elevation Gain',icon: '⛰️', unit: 'distance' },
};

let allPRs = [];

// ── Helpers ──
function formatDate(d) {
  if (!d) return '—';
  const dt = new Date(d);
  if (isNaN(dt.getTime())) return '—';
  return dt.toLocaleDateString('en-IN', {day:'2-digit',month:'short',year:'numeric'});
}

function msToTimeStr(ms) {
  if (!ms || ms <= 0) return '—';
  const totalSec = Math.floor(ms / 1000);
  const h = Math.floor(totalSec / 3600);
  const m = Math.floor((totalSec % 3600) / 60);
  const s = totalSec % 60;
  if (h > 0) return `${h}:${String(m).padStart(2,'0')}:${String(s).padStart(2,'0')}`;
  return `${m}:${String(s).padStart(2,'0')}`;
}

function paceFromMs(ms, distMeters) {
  if (!ms || !distMeters || distMeters <= 0) return '—';
  const totalMin = (ms / 1000) / 60;
  const paceMinPerKm = totalMin / (distMeters / 1000);
  const pm = Math.floor(paceMinPerKm);
  const ps = Math.round((paceMinPerKm - pm) * 60);
  return `${pm}:${String(ps).padStart(2,'0')} /km`;
}

function speedFromMs(ms, distMeters) {
  if (!ms || !distMeters) return '—';
  const hours = ms / 1000 / 3600;
  const km = distMeters / 1000;
  return (km / hours).toFixed(1) + ' km/h';
}

function normalizeTypeKey(key) {
  if (!key) return key;
  return key.toLowerCase().replace(/\s+/g, '_').replace(/-/g, '_');
}

// ═══════════════════════════════════════
//  RENDER
// ═══════════════════════════════════════
function renderPRShowcase(distanceRecords) {
  if (!distanceRecords.length) {
    document.getElementById('pr-showcase').innerHTML = `
      <div style="text-align:center;color:#444;padding:40px;grid-column:1/-1;">
        No distance PRs found yet. Sync your Garmin data to see your personal bests!
      </div>`;
    return;
  }

  let html = '';
  distanceRecords.forEach(rec => {
    const config = rec._config;
    html += `
      <div class="pr-card ${config.theme}">
        <div class="pr-card-header">
          <div class="pr-distance-badge">${config.icon}<br>${config.name}</div>
          <div class="pr-card-header-text">
            <h3>${config.name} Personal Best</h3>
            <p class="pr-distance-label">${(config.meters / 1000).toFixed(config.meters < 1500 ? 1 : 2)} km</p>
          </div>
        </div>
        <div class="pr-card-body">
          <div class="pr-time">${msToTimeStr(rec.value_ms)}</div>
          <div class="pr-pace">${paceFromMs(rec.value_ms, config.meters)} · ${speedFromMs(rec.value_ms, config.meters)}</div>
          <div class="pr-meta">
            ${rec.pr_date ? `<div class="pr-meta-item">📅 <span>${formatDate(rec.pr_date)}</span></div>` : ''}
            ${rec.activity_name ? `<div class="pr-meta-item">🏷️ <span>${rec.activity_name}</span></div>` : ''}
            <div class="pr-meta-item"><span class="pr-garmin-badge">Garmin Official</span></div>
          </div>
        </div>
      </div>
    `;
  });

  document.getElementById('pr-showcase').innerHTML = html;
}

function renderRecordsTable(distanceRecords) {
  const tbody = document.getElementById('records-tbody');
  if (!distanceRecords.length) {
    tbody.innerHTML = '<tr><td colspan="5" style="text-align:center;color:#555;padding:30px;">No distance records found</td></tr>';
    return;
  }

  tbody.innerHTML = distanceRecords.map(rec => {
    const config = rec._config;
    return `<tr>
      <td class="rt-distance">${config.icon} ${config.name}</td>
      <td class="rt-time">${msToTimeStr(rec.value_ms)}</td>
      <td class="rt-pace">${paceFromMs(rec.value_ms, config.meters)}</td>
      <td class="rt-speed">${speedFromMs(rec.value_ms, config.meters)}</td>
      <td class="rt-date">${formatDate(rec.pr_date)}</td>
    </tr>`;
  }).join('');
}

function renderRawRecords(otherRecords) {
  if (!otherRecords.length) {
    document.getElementById('raw-records-grid').innerHTML = '';
    return;
  }

  document.getElementById('raw-records-grid').innerHTML = otherRecords.map(rec => {
    const config = rec._otherConfig;
    let valueStr = '—';
    if (config && config.unit === 'distance') {
      // value_ms is stored as meters * 1000. To get km, divide by 1,000,000.
      valueStr = rec.value_ms ? (rec.value_ms / 1000000).toFixed(2) + ' km' : '—';
    } else {
      valueStr = msToTimeStr(rec.value_ms);
    }
    const displayName = config ? config.name : rec.pr_type;
    const icon = config ? config.icon : '🏆';
    return `
      <div class="raw-record-card">
        <div class="raw-record-icon">${icon}</div>
        <div class="raw-record-info">
          <div class="raw-record-title">${displayName}</div>
          <div class="raw-record-value">${valueStr}</div>
          <div class="raw-record-detail">${rec.pr_date ? formatDate(rec.pr_date) : '—'}${rec.activity_name ? ' · ' + rec.activity_name : ''}</div>
        </div>
      </div>`;
  }).join('');
}

function renderTop5Leaderboards(allRuns) {
  let html = '';

  const TOP5_DISTANCES = [
    { key: '1k', name: '1K', meters: 1000, theme: 'emerald', icon: '🟢', tolerance: 0.15 },
    { key: '1mile', name: '1 Mile', meters: 1609.34, theme: 'gold', icon: '🥇', tolerance: 0.15 },
    { key: '2k', name: '2K', meters: 2000, theme: 'sapphire', icon: '🔵', tolerance: 0.15 },
    { key: '5k', name: '5K', meters: 5000, theme: 'amber', icon: '🟠', tolerance: 0.15 },
    { key: '10k', name: '10K', meters: 10000, theme: 'teal', icon: '🏃', tolerance: 0.15 },
    { key: 'half_marathon', name: 'Half Marathon', meters: 21097.5, theme: 'amethyst', icon: '🟣', tolerance: 0.15 },
    { key: 'marathon', name: 'Marathon', meters: 42195, theme: 'ruby', icon: '🔴', tolerance: 0.15 }
  ];

  TOP5_DISTANCES.forEach(rd => {
    const minDist = rd.meters * (1 - rd.tolerance);
    const maxDist = rd.meters * (1 + rd.tolerance);

    const candidates = [];
    allRuns.forEach(r => {
      if (!r.duration || !r.distance || r.duration <= 0 || !r.avg_speed || r.avg_speed <= 0) return;
      
      if (r.distance >= minDist && r.distance <= maxDist) {
        const estimatedTime = rd.meters / r.avg_speed;
        candidates.push({ ...r, estimatedTime, method: 'exact' });
      }
    });

    candidates.sort((a, b) => a.estimatedTime - b.estimatedTime);
    const top5 = candidates.slice(0, 5);

    const rowsHtml = [];
    for (let i = 0; i < 5; i++) {
      if (i < top5.length) {
        const rec = top5[i];
        
        rowsHtml.push(`
          <tr>
            <td style="color:#888;font-weight:700;font-family:'JetBrains Mono', monospace;">#${i + 1}</td>
            <td class="rt-time">${msToTimeStr(rec.estimatedTime * 1000)}</td>
            <td class="rt-pace">${paceFromMs(rec.estimatedTime * 1000, rd.meters)}</td>
            <td class="rt-run">${rec.activity_name || 'Run'}</td>
            <td class="rt-date">${formatDate(rec.start_time)}</td>
          </tr>
        `);
      } else {
        rowsHtml.push(`
          <tr>
            <td style="color:#444;font-weight:700;font-family:'JetBrains Mono', monospace;">#${i + 1}</td>
            <td class="rt-time" style="color:#444;">N/A</td>
            <td class="rt-pace" style="color:#444;">N/A</td>
            <td class="rt-run" style="color:#444;">—</td>
            <td class="rt-date" style="color:#444;">—</td>
          </tr>
        `);
      }
    }

    html += `
      <div class="records-table-container" style="margin-bottom: 24px;">
        <div style="padding: 16px 18px; border-bottom: 1px solid #1e1e2e; background: rgba(255,255,255,0.02); display: flex; align-items: center; gap: 12px;">
          <div class="pr-distance-badge" style="width:40px;height:40px;min-width:40px;font-size:1rem;background:linear-gradient(135deg, rgba(255,255,255,0.1), transparent);">${rd.icon}</div>
          <h3 style="margin:0;font-size:1rem;color:#fff;">Top 5 ${rd.name} Runs</h3>
        </div>
        <div class="table-scroll">
          <table class="records-table">
            <thead>
              <tr>
                <th style="width: 50px;">Rank</th>
                <th>Computed Time</th>
                <th>Avg Pace</th>
                <th>Run Name</th>
                <th>Date</th>
              </tr>
            </thead>
            <tbody>
              ${rowsHtml.join('')}
            </tbody>
          </table>
        </div>
      </div>
    `;
  });

  document.getElementById('top5-showcase').innerHTML = html;
}

// ═══════════════════════════════════════
//  DATA LOADING
// ═══════════════════════════════════════
async function loadData() {
  try {
    const [prsRes, runsRes] = await Promise.all([
      sb.from('garmin_personal_records').select('pr_type, value_ms, activity_id, activity_name, pr_date, synced_at'),
      sb.from('garmin_activities').select('activity_name, start_time, duration, distance, avg_speed').eq('activity_type', 'running')
    ]);
    
    if (prsRes.error) throw prsRes.error;
    if (runsRes.error) throw runsRes.error;

    allPRs = prsRes.data || [];
    const allRuns = runsRes.data || [];

    document.getElementById('connection-badge').className = 'connection-badge online';
    document.getElementById('connection-text').textContent = 'Cloud Synced';
    document.getElementById('loading').style.display = 'none';
    document.getElementById('main-content').style.display = 'block';

    if (allPRs.length === 0) {
      document.getElementById('empty-state').style.display = 'block';
      document.getElementById('last-sync').textContent = 'No data yet';
      return;
    }

    const latest = allPRs.reduce((a, b) => (a.synced_at || '') > (b.synced_at || '') ? a : b);
    document.getElementById('last-sync').textContent = 'Last sync: ' + formatDate(latest.synced_at);

    // Separate distance-based PRs from other record types
    const distanceRecords = [];
    const otherRecords = [];

    allPRs.forEach(pr => {
      const normalized = normalizeTypeKey(pr.pr_type);
      const config = RACE_DISTANCES[normalized];
      const otherConfig = OTHER_RECORD_TYPES[normalized];

      if (config) {
        // Check if we already have this distance (dedup by name)
        const existing = distanceRecords.find(d => d._config.name === config.name);
        if (!existing || (pr.value_ms && existing.value_ms && pr.value_ms < existing.value_ms)) {
          if (existing) {
            distanceRecords.splice(distanceRecords.indexOf(existing), 1);
          }
          distanceRecords.push({ ...pr, _config: config });
        }
      } else if (otherConfig) {
        const existing = otherRecords.find(d => d._otherConfig && d._otherConfig.name === otherConfig.name);
        if (!existing) {
          otherRecords.push({ ...pr, _otherConfig: otherConfig });
        }
      } else {
        // Unknown type — show it in "other" section
        otherRecords.push({ ...pr, _otherConfig: { name: pr.pr_type, icon: '🏆', unit: 'time' } });
      }
    });

    // Sort distance records by order
    distanceRecords.sort((a, b) => a._config.order - b._config.order);

    renderPRShowcase(distanceRecords);
    renderRecordsTable(distanceRecords);
    renderRawRecords(otherRecords);
    renderTop5Leaderboards(allRuns);
  } catch (err) {
    console.error('Load error:', err);
    document.getElementById('connection-badge').className = 'connection-badge offline';
    document.getElementById('connection-text').textContent = 'Offline';
    document.getElementById('loading').innerHTML = '<div class="empty-state-icon">⚠️</div><p style="color:#ef5350;">Could not connect to database</p>';
    showToast('⚠️ Failed to load data', 'error');
  }
}

function showToast(msg, type='success') {
  const t = document.getElementById('toast');
  t.textContent = msg; t.className = `toast ${type} show`;
  setTimeout(() => t.classList.remove('show'), 3000);
}

// ── Init ──
document.addEventListener('DOMContentLoaded', () => {
  loadData();
});
</script>
