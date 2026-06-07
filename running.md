---
layout: page
title: Running
subtitle: Garmin Running & Steps Dashboard
---

<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">

<style>
  .container-md, .container { max-width: 100% !important; width: 100% !important; padding: 0 !important; margin: 0 !important; }
  .run-app { font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif; background: #0a0a0f; color: #e0e0e0; min-height: 100vh; padding: 0 20px 60px; }

  /* HERO */
  .hero { text-align: center; padding: 50px 20px 30px; position: relative; overflow: hidden; }
  .hero::before { content: ''; position: absolute; top: -50%; left: -50%; width: 200%; height: 200%; background: radial-gradient(ellipse at center, rgba(0,230,118,0.06) 0%, transparent 60%); pointer-events: none; }
  .hero-title { font-size: 2.8rem; font-weight: 900; background: linear-gradient(135deg, #00E676, #00C853, #69F0AE); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; margin: 0 0 8px; letter-spacing: -0.02em; }
  .hero-sub { color: #666; font-size: 1rem; font-weight: 400; margin: 0; }
  .hero-sub .last-sync { color: #00E676; font-family: 'JetBrains Mono', monospace; font-size: 0.85rem; }
  .connection-badge { display: inline-flex; align-items: center; gap: 6px; padding: 4px 12px; border-radius: 20px; font-size: 0.7rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; margin-top: 12px; }
  .connection-badge.online { background: rgba(0,230,118,0.1); color: #00E676; border: 1px solid rgba(0,230,118,0.2); }
  .connection-badge.offline { background: rgba(245,101,101,0.1); color: #f56565; border: 1px solid rgba(245,101,101,0.2); }
  .connection-dot { width: 6px; height: 6px; border-radius: 50%; background: currentColor; animation: pulse-dot 2s infinite; }
  @keyframes pulse-dot { 0%, 100% { opacity: 1; } 50% { opacity: 0.4; } }

  /* SYNC BUTTONS */
  .hero-actions { display: flex; justify-content: center; gap: 10px; margin-top: 16px; flex-wrap: wrap; }
  .btn-sync { display: inline-flex; align-items: center; gap: 8px; padding: 10px 22px; border-radius: 12px; font-size: 0.8rem; font-weight: 700; font-family: 'Inter', sans-serif; cursor: pointer; transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1); border: 1px solid; text-transform: uppercase; letter-spacing: 0.05em; }
  .btn-sync:active { transform: scale(0.97); }
  .btn-sync.primary { background: linear-gradient(135deg, rgba(0,230,118,0.15), rgba(0,200,83,0.08)); border-color: rgba(0,230,118,0.4); color: #00E676; }
  .btn-sync.primary:hover { background: linear-gradient(135deg, rgba(0,230,118,0.25), rgba(0,200,83,0.15)); box-shadow: 0 4px 20px rgba(0,230,118,0.2); }
  .btn-sync.secondary { background: rgba(255,255,255,0.03); border-color: #2a2a36; color: #888; }
  .btn-sync.secondary:hover { border-color: #444; color: #ccc; background: rgba(255,255,255,0.06); }
  .btn-sync:disabled { opacity: 0.5; cursor: not-allowed; }
  .btn-sync .btn-spinner { width: 14px; height: 14px; border: 2px solid transparent; border-top-color: currentColor; border-radius: 50%; animation: spin 0.6s linear infinite; display: none; }
  .btn-sync.loading .btn-spinner { display: block; }
  .btn-sync.loading .btn-icon { display: none; }

  /* STAT CARDS */
  .stats-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 16px; max-width: 1200px; margin: 30px auto; }
  .stat-card { background: linear-gradient(135deg, #111118, #141420); border: 1px solid #1e1e2e; border-radius: 16px; padding: 24px; text-align: center; transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1); position: relative; overflow: hidden; }
  .stat-card::before { content: ''; position: absolute; inset: 0; background: linear-gradient(135deg, rgba(0,230,118,0.04), transparent); opacity: 0; transition: opacity 0.3s; }
  .stat-card:hover { border-color: rgba(0,230,118,0.3); transform: translateY(-3px); box-shadow: 0 12px 32px rgba(0,0,0,0.3); }
  .stat-card:hover::before { opacity: 1; }
  .stat-icon { font-size: 1.6rem; margin-bottom: 8px; display: block; }
  .stat-value { font-size: 1.8rem; font-weight: 800; color: #00E676; display: block; line-height: 1.1; font-family: 'JetBrains Mono', monospace; position: relative; z-index: 1; }
  .stat-label { font-size: 0.7rem; color: #666; text-transform: uppercase; letter-spacing: 0.1em; margin-top: 6px; display: block; position: relative; z-index: 1; }

  /* SECTION HEADERS */
  .section-header { max-width: 1200px; margin: 40px auto 20px; display: flex; align-items: center; gap: 12px; }
  .section-header h2 { font-size: 1.3rem; font-weight: 800; color: #fff; margin: 0; }
  .section-line { flex: 1; height: 1px; background: linear-gradient(90deg, #1e1e2e, transparent); }

  /* RECORDS */
  .records-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 16px; max-width: 1200px; margin: 0 auto; }
  .record-card { background: linear-gradient(135deg, #111118, #14141e); border: 1px solid #1e1e2e; border-radius: 16px; padding: 20px 24px; display: flex; align-items: center; gap: 16px; transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1); }
  .record-card:hover { border-color: rgba(0,230,118,0.3); transform: translateY(-2px); box-shadow: 0 8px 24px rgba(0,0,0,0.3); }
  .record-icon { width: 52px; height: 52px; border-radius: 14px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; flex-shrink: 0; }
  .record-icon.gold { background: linear-gradient(135deg, rgba(255,215,0,0.15), rgba(255,165,0,0.1)); }
  .record-icon.green { background: linear-gradient(135deg, rgba(0,230,118,0.15), rgba(0,200,83,0.1)); }
  .record-icon.blue { background: linear-gradient(135deg, rgba(66,165,245,0.15), rgba(33,150,243,0.1)); }
  .record-icon.red { background: linear-gradient(135deg, rgba(239,83,80,0.15), rgba(229,57,53,0.1)); }
  .record-icon.purple { background: linear-gradient(135deg, rgba(171,71,188,0.15), rgba(142,36,170,0.1)); }
  .record-icon.orange { background: linear-gradient(135deg, rgba(255,167,38,0.15), rgba(255,143,0,0.1)); }
  .record-info { flex: 1; min-width: 0; }
  .record-title { font-size: 0.8rem; color: #888; text-transform: uppercase; letter-spacing: 0.05em; margin: 0 0 4px; }
  .record-value { font-size: 1.4rem; font-weight: 800; color: #fff; font-family: 'JetBrains Mono', monospace; margin: 0; }
  .record-detail { font-size: 0.75rem; color: #555; margin: 2px 0 0; }

  /* CHART */
  .chart-container { max-width: 1200px; margin: 0 auto; background: linear-gradient(135deg, #111118, #14141e); border: 1px solid #1e1e2e; border-radius: 16px; padding: 24px; }
  .rhr-info { display: flex; gap: 24px; margin-bottom: 16px; flex-wrap: wrap; }
  .rhr-info-item { font-size: 0.8rem; color: #888; font-family: 'JetBrains Mono', monospace; }
  .rhr-info-item span { color: #ef5350; font-weight: 700; }
  .chart-tabs { display: flex; gap: 8px; margin-bottom: 20px; flex-wrap: wrap; }
  .chart-tab { padding: 6px 16px; background: #0a0a0f; border: 1px solid #1e1e2e; border-radius: 10px; color: #888; font-size: 0.75rem; font-weight: 600; cursor: pointer; transition: all 0.3s; font-family: 'Inter', sans-serif; }
  .chart-tab:hover { border-color: #444; color: #ccc; }
  .chart-tab.active { background: linear-gradient(135deg, rgba(0,230,118,0.12), rgba(0,200,83,0.08)); border-color: #00E676; color: #00E676; }
  #speed-chart { width: 100%; height: 300px; display: block; }

  /* MONTHLY STATS */
  .monthly-container { max-width: 1200px; margin: 0 auto; }
  .month-tabs { display: flex; gap: 8px; margin-bottom: 20px; flex-wrap: wrap; justify-content: center; }
  .month-tab { padding: 8px 18px; background: #111118; border: 1px solid #1e1e2e; border-radius: 12px; color: #888; font-size: 0.75rem; font-weight: 600; cursor: pointer; transition: all 0.3s; font-family: 'Inter', sans-serif; }
  .month-tab:hover { border-color: #444; color: #ccc; }
  .month-tab.active { background: linear-gradient(135deg, rgba(0,230,118,0.12), rgba(0,200,83,0.08)); border-color: #00E676; color: #00E676; }
  .monthly-stats-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 14px; margin-bottom: 20px; }
  .monthly-stat { background: linear-gradient(135deg, #111118, #14141e); border: 1px solid #1e1e2e; border-radius: 14px; padding: 18px; text-align: center; transition: all 0.3s; }
  .monthly-stat:hover { border-color: rgba(0,230,118,0.25); transform: translateY(-2px); }
  .monthly-stat-icon { font-size: 1.2rem; display: block; margin-bottom: 4px; }
  .monthly-stat-val { font-size: 1.4rem; font-weight: 800; color: #00E676; font-family: 'JetBrains Mono', monospace; display: block; line-height: 1.2; }
  .monthly-stat-label { font-size: 0.6rem; color: #666; text-transform: uppercase; letter-spacing: 0.1em; margin-top: 4px; display: block; }

  /* RUNS TABLE */
  .table-container { max-width: 1200px; margin: 0 auto; background: linear-gradient(135deg, #111118, #14141e); border: 1px solid #1e1e2e; border-radius: 16px; overflow: hidden; }
  .table-toolbar { display: flex; justify-content: space-between; align-items: center; padding: 16px 20px; border-bottom: 1px solid #1e1e2e; flex-wrap: wrap; gap: 12px; }
  .table-search { padding: 10px 16px; background: #0a0a0f; border: 1px solid #1e1e2e; border-radius: 10px; color: #fff; font-size: 0.85rem; font-family: 'Inter', sans-serif; outline: none; transition: all 0.3s; min-width: 200px; }
  .table-search::placeholder { color: #444; }
  .table-search:focus { border-color: #00E676; box-shadow: 0 0 0 3px rgba(0,230,118,0.1); }
  .table-count { font-size: 0.8rem; color: #888; font-family: 'JetBrains Mono', monospace; }
  .runs-table { width: 100%; border-collapse: collapse; }
  .runs-table th { padding: 12px 16px; text-align: left; font-size: 0.7rem; font-weight: 700; color: #666; text-transform: uppercase; letter-spacing: 0.1em; border-bottom: 1px solid #1e1e2e; cursor: pointer; user-select: none; transition: color 0.2s; white-space: nowrap; }
  .runs-table th:hover { color: #00E676; }
  .runs-table th.sorted { color: #00E676; }
  .runs-table th .sort-arrow { font-size: 0.6rem; margin-left: 4px; opacity: 0.5; }
  .runs-table th.sorted .sort-arrow { opacity: 1; }
  .runs-table td { padding: 14px 16px; font-size: 0.85rem; border-bottom: 1px solid #111118; white-space: nowrap; }
  .runs-table tr { transition: background 0.2s; }
  .runs-table tbody tr:hover { background: rgba(0,230,118,0.03); }
  .run-name { font-weight: 600; color: #eee; max-width: 200px; overflow: hidden; text-overflow: ellipsis; }
  .run-date { color: #888; font-family: 'JetBrains Mono', monospace; font-size: 0.8rem; }
  .run-distance { color: #00E676; font-weight: 700; font-family: 'JetBrains Mono', monospace; }
  .run-pace { color: #69F0AE; font-family: 'JetBrains Mono', monospace; }
  .speed-badge { font-size: 0.75rem; font-weight: 700; padding: 3px 10px; border-radius: 8px; font-family: 'JetBrains Mono', monospace; display: inline-block; }
  .speed-fast { background: rgba(0,230,118,0.12); color: #00E676; border: 1px solid rgba(0,230,118,0.2); }
  .speed-medium { background: rgba(255,167,38,0.12); color: #FFA726; border: 1px solid rgba(255,167,38,0.2); }
  .speed-slow { background: rgba(239,83,80,0.12); color: #ef5350; border: 1px solid rgba(239,83,80,0.2); }
  .table-scroll { overflow-x: auto; }

  /* ═══════ STEPS SECTION (Purple Accent) ═══════ */
  .steps-divider { max-width: 1200px; margin: 60px auto 0; padding: 0; position: relative; }
  .steps-divider-line { height: 2px; background: linear-gradient(90deg, transparent, rgba(124,77,255,0.4), rgba(179,136,255,0.6), rgba(124,77,255,0.4), transparent); border-radius: 2px; }
  .steps-hero { text-align: center; padding: 40px 20px 20px; position: relative; overflow: hidden; }
  .steps-hero::before { content: ''; position: absolute; top: -50%; left: -50%; width: 200%; height: 200%; background: radial-gradient(ellipse at center, rgba(124,77,255,0.06) 0%, transparent 60%); pointer-events: none; }
  .steps-hero-title { font-size: 2.2rem; font-weight: 900; background: linear-gradient(135deg, #7C4DFF, #B388FF, #E040FB); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; margin: 0 0 6px; letter-spacing: -0.02em; }
  .steps-hero-sub { color: #555; font-size: 0.9rem; margin: 0; }

  /* Steps stat cards - purple accent */
  .steps-stats-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 16px; max-width: 1200px; margin: 30px auto; }
  .steps-stat-card { background: linear-gradient(135deg, #111118, #141420); border: 1px solid #1e1e2e; border-radius: 16px; padding: 24px; text-align: center; transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1); position: relative; overflow: hidden; }
  .steps-stat-card::before { content: ''; position: absolute; inset: 0; background: linear-gradient(135deg, rgba(124,77,255,0.04), transparent); opacity: 0; transition: opacity 0.3s; }
  .steps-stat-card:hover { border-color: rgba(124,77,255,0.3); transform: translateY(-3px); box-shadow: 0 12px 32px rgba(0,0,0,0.3); }
  .steps-stat-card:hover::before { opacity: 1; }
  .steps-stat-card .stat-value { color: #B388FF; }

  /* Steps records - purple accent hover */
  .steps-records-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 16px; max-width: 1200px; margin: 0 auto; }
  .steps-records-grid .record-card:hover { border-color: rgba(124,77,255,0.3); }

  /* Steps chart - purple accent */
  .steps-chart-container { max-width: 1200px; margin: 0 auto; background: linear-gradient(135deg, #111118, #14141e); border: 1px solid #1e1e2e; border-radius: 16px; padding: 24px; }
  .steps-chart-tab { padding: 6px 16px; background: #0a0a0f; border: 1px solid #1e1e2e; border-radius: 10px; color: #888; font-size: 0.75rem; font-weight: 600; cursor: pointer; transition: all 0.3s; font-family: 'Inter', sans-serif; }
  .steps-chart-tab:hover { border-color: #444; color: #ccc; }
  .steps-chart-tab.active { background: linear-gradient(135deg, rgba(124,77,255,0.12), rgba(179,136,255,0.08)); border-color: #7C4DFF; color: #B388FF; }
  #steps-chart { width: 100%; height: 300px; display: block; }

  /* Goal Progress Bar */
  .goal-bar-outer { max-width: 1200px; margin: 0 auto; background: linear-gradient(135deg, #111118, #14141e); border: 1px solid #1e1e2e; border-radius: 16px; padding: 24px; }
  .goal-bar-label { display: flex; justify-content: space-between; margin-bottom: 10px; font-size: 0.85rem; color: #888; }
  .goal-bar-label .goal-pct { font-weight: 800; color: #B388FF; font-family: 'JetBrains Mono', monospace; }
  .goal-bar-track { width: 100%; height: 16px; background: #1a1a28; border-radius: 8px; overflow: hidden; position: relative; }
  .goal-bar-fill { height: 100%; border-radius: 8px; background: linear-gradient(90deg, #7C4DFF, #B388FF, #E040FB); transition: width 0.8s cubic-bezier(0.16, 1, 0.3, 1); position: relative; }
  .goal-bar-fill::after { content: ''; position: absolute; inset: 0; background: linear-gradient(90deg, transparent, rgba(255,255,255,0.15), transparent); animation: shimmer 2s infinite; }
  @keyframes shimmer { 0% { transform: translateX(-100%); } 100% { transform: translateX(100%); } }

  /* Weekly Breakdown */
  .weekly-grid { display: grid; grid-template-columns: repeat(7, 1fr); gap: 8px; max-width: 1200px; margin: 0 auto; }
  .week-day-card { background: linear-gradient(135deg, #111118, #14141e); border: 1px solid #1e1e2e; border-radius: 12px; padding: 16px 8px; text-align: center; transition: all 0.3s; }
  .week-day-card:hover { border-color: rgba(124,77,255,0.25); transform: translateY(-2px); }
  .week-day-card .day-name { font-size: 0.65rem; color: #666; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 6px; }
  .week-day-card .day-steps { font-size: 1.1rem; font-weight: 800; color: #B388FF; font-family: 'JetBrains Mono', monospace; }
  .week-day-card.today { border-color: rgba(124,77,255,0.4); box-shadow: 0 0 20px rgba(124,77,255,0.1); }

  /* Steps monthly */
  .steps-monthly-container { max-width: 1200px; margin: 0 auto; }
  .steps-month-tab { padding: 8px 18px; background: #111118; border: 1px solid #1e1e2e; border-radius: 12px; color: #888; font-size: 0.75rem; font-weight: 600; cursor: pointer; transition: all 0.3s; font-family: 'Inter', sans-serif; }
  .steps-month-tab:hover { border-color: #444; color: #ccc; }
  .steps-month-tab.active { background: linear-gradient(135deg, rgba(124,77,255,0.12), rgba(179,136,255,0.08)); border-color: #7C4DFF; color: #B388FF; }
  .steps-monthly-stat { background: linear-gradient(135deg, #111118, #14141e); border: 1px solid #1e1e2e; border-radius: 14px; padding: 18px; text-align: center; transition: all 0.3s; }
  .steps-monthly-stat:hover { border-color: rgba(124,77,255,0.25); transform: translateY(-2px); }
  .steps-monthly-stat .monthly-stat-val { color: #B388FF; }

  /* Steps table */
  .steps-table-container { max-width: 1200px; margin: 0 auto; background: linear-gradient(135deg, #111118, #14141e); border: 1px solid #1e1e2e; border-radius: 16px; overflow: hidden; }
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
  .steps-table-search:focus { border-color: #7C4DFF; box-shadow: 0 0 0 3px rgba(124,77,255,0.1); }

  /* LOADING / EMPTY / TOAST */
  .loading-overlay { text-align: center; padding: 80px 20px; }
  .spinner { width: 40px; height: 40px; border: 3px solid #222; border-top-color: #00E676; border-radius: 50%; animation: spin 0.8s linear infinite; margin: 0 auto 20px; }
  @keyframes spin { to { transform: rotate(360deg); } }
  .loading-text { color: #555; font-size: 0.9rem; }
  .empty-state { text-align: center; padding: 60px 20px; color: #444; }
  .empty-state-icon { font-size: 3rem; margin-bottom: 16px; }
  .toast { position: fixed; bottom: 30px; left: 50%; transform: translateX(-50%) translateY(100px); background: #1a1a24; border: 1px solid #333; color: #fff; padding: 12px 24px; border-radius: 12px; font-size: 0.85rem; font-weight: 500; z-index: 9999; transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1); box-shadow: 0 8px 32px rgba(0,0,0,0.4); }
  .toast.show { transform: translateX(-50%) translateY(0); }
  .toast.error { border-color: #ef5350; }
  .toast.success { border-color: #00E676; }

  @media (max-width: 600px) {
    .hero-title { font-size: 2rem; }
    .steps-hero-title { font-size: 1.6rem; }
    .stats-grid, .steps-stats-grid { grid-template-columns: repeat(2, 1fr); }
    .records-grid, .steps-records-grid { grid-template-columns: 1fr; }
    .monthly-stats-grid { grid-template-columns: repeat(2, 1fr); }
    .runs-table th, .runs-table td, .steps-table th, .steps-table td { padding: 10px 10px; font-size: 0.75rem; }
    .weekly-grid { grid-template-columns: repeat(4, 1fr); }
  }
  @media (max-width: 480px) {
    .weekly-grid { grid-template-columns: repeat(2, 1fr); }
  }
</style>

<div class="run-app" id="run-app">
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

  <div class="loading-overlay" id="loading">
    <div class="spinner"></div>
    <div class="loading-text">Fetching your data...</div>
  </div>

  <div id="main-content" style="display:none;">
    <div class="stats-grid" id="stats-grid"></div>

    <div class="section-header"><h2>🏆 Personal Records</h2><div class="section-line"></div></div>
    <div class="records-grid" id="records-grid"></div>

    <div class="section-header"><h2>📈 Trends</h2><div class="section-line"></div></div>
    <div class="chart-container">
      <div class="chart-tabs" id="chart-tabs">
        <button class="chart-tab active" data-metric="maxSpeed" onclick="switchChart('maxSpeed')">Max Speed</button>
        <button class="chart-tab" data-metric="distance" onclick="switchChart('distance')">Distance</button>
        <button class="chart-tab" data-metric="avgPace" onclick="switchChart('avgPace')">Avg Pace</button>
        <button class="chart-tab" data-metric="avgHr" onclick="switchChart('avgHr')">Avg HR</button>
      </div>
      <canvas id="speed-chart"></canvas>
    </div>

    <div class="section-header"><h2>❤️ Resting Heart Rate</h2><div class="section-line"></div></div>
    <div class="chart-container">
      <div class="rhr-info" id="rhr-info"></div>
      <canvas id="rhr-chart" style="width:100%;height:280px;display:block;"></canvas>
    </div>

    <div class="section-header"><h2>📅 Monthly Breakdown</h2><div class="section-line"></div></div>
    <div class="monthly-container">
      <div class="month-tabs" id="month-tabs"></div>
      <div class="monthly-stats-grid" id="monthly-stats-grid"></div>
    </div>

    <div class="section-header"><h2>📋 All Runs</h2><div class="section-line"></div></div>
    <div class="table-container">
      <div class="table-toolbar">
        <input type="text" class="table-search" id="table-search" placeholder="🔍 Search runs...">
        <span class="table-count" id="table-count"></span>
      </div>
      <div class="table-scroll">
        <table class="runs-table">
          <thead>
            <tr>
              <th onclick="sortRunsTable('date')" id="th-date" class="sorted">Date <span class="sort-arrow">▼</span></th>
              <th onclick="sortRunsTable('name')" id="th-name">Name <span class="sort-arrow">▼</span></th>
              <th onclick="sortRunsTable('distance')" id="th-distance">Distance <span class="sort-arrow">▼</span></th>
              <th onclick="sortRunsTable('duration')" id="th-duration">Duration <span class="sort-arrow">▼</span></th>
              <th onclick="sortRunsTable('avgPace')" id="th-avgPace">Avg Pace <span class="sort-arrow">▼</span></th>
              <th onclick="sortRunsTable('maxSpeed')" id="th-maxSpeed">Max Speed <span class="sort-arrow">▼</span></th>
              <th onclick="sortRunsTable('avgHr')" id="th-avgHr">Avg HR <span class="sort-arrow">▼</span></th>
              <th onclick="sortRunsTable('calories')" id="th-calories">Calories <span class="sort-arrow">▼</span></th>
            </tr>
          </thead>
          <tbody id="runs-tbody"></tbody>
        </table>
      </div>
    </div>

    <div class="empty-state" id="empty-state" style="display:none;">
      <div class="empty-state-icon">🏃</div>
      <p>No runs found yet. Sync your Garmin data to get started!</p>
    </div>

    <!-- ═══════════════════════════════════════════════ -->
    <!--             STEPS SECTION                       -->
    <!-- ═══════════════════════════════════════════════ -->
    <div class="steps-divider"><div class="steps-divider-line"></div></div>
    <div class="steps-hero">
      <h2 class="steps-hero-title">🚶 Daily Steps</h2>
      <p class="steps-hero-sub">Your walking & step tracking data from Garmin</p>
    </div>

    <div id="steps-loading" style="text-align:center;padding:40px 20px;display:none;">
      <div class="spinner" style="border-top-color:#B388FF;"></div>
      <div class="loading-text">Fetching step data...</div>
    </div>

    <div id="steps-content" style="display:none;">
      <div class="steps-stats-grid" id="steps-stats-grid"></div>

      <div class="section-header" id="steps-goal-section" style="display:none;"><h2>🎯 Today's Goal Progress</h2><div class="section-line"></div></div>
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
      <div class="steps-records-grid" id="steps-records-grid"></div>

      <div class="section-header"><h2>📈 Step Trends</h2><div class="section-line"></div></div>
      <div class="steps-chart-container">
        <div class="chart-tabs" id="steps-chart-tabs">
          <button class="steps-chart-tab active" data-range="30" onclick="switchStepsRange(30)">Last 30 Days</button>
          <button class="steps-chart-tab" data-range="60" onclick="switchStepsRange(60)">Last 60 Days</button>
          <button class="steps-chart-tab" data-range="90" onclick="switchStepsRange(90)">All Time</button>
        </div>
        <canvas id="steps-chart"></canvas>
      </div>

      <div class="section-header"><h2>📅 This Week</h2><div class="section-line"></div></div>
      <div class="weekly-grid" id="weekly-grid"></div>

      <div class="section-header"><h2>📊 Steps Monthly Breakdown</h2><div class="section-line"></div></div>
      <div class="steps-monthly-container">
        <div class="month-tabs" id="steps-month-tabs"></div>
        <div class="monthly-stats-grid" id="steps-monthly-stats-grid"></div>
      </div>

      <div class="section-header"><h2>📋 All Days</h2><div class="section-line"></div></div>
      <div class="steps-table-container">
        <div class="table-toolbar">
          <input type="text" class="table-search steps-table-search" id="steps-table-search" placeholder="🔍 Search dates...">
          <span class="table-count" id="steps-table-count"></span>
        </div>
        <div class="table-scroll">
          <table class="steps-table">
            <thead>
              <tr>
                <th onclick="sortStepsTable('date')" id="sth-date" class="sorted">Date <span class="sort-arrow">▼</span></th>
                <th onclick="sortStepsTable('total_steps')" id="sth-total_steps">Steps <span class="sort-arrow">▼</span></th>
                <th onclick="sortStepsTable('step_goal')" id="sth-step_goal">Goal <span class="sort-arrow">▼</span></th>
                <th onclick="sortStepsTable('goal_pct')" id="sth-goal_pct">Progress <span class="sort-arrow">▼</span></th>
                <th onclick="sortStepsTable('distance')" id="sth-distance">Distance <span class="sort-arrow">▼</span></th>
                <th onclick="sortStepsTable('calories_total')" id="sth-calories_total">Calories <span class="sort-arrow">▼</span></th>
              </tr>
            </thead>
            <tbody id="steps-tbody"></tbody>
          </table>
        </div>
      </div>

      <div class="empty-state" id="steps-empty-state" style="display:none;">
        <div class="empty-state-icon">🚶</div>
        <p>No step data found yet. Sync your Garmin data to get started!</p>
      </div>
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

// ═══════════════════════════════════════
//  RUNNING STATE
// ═══════════════════════════════════════
let allRuns = [];
let filteredRuns = [];
let runSortField = 'date';
let runSortAsc = false;
let currentChartMetric = 'maxSpeed';
let currentRunMonth = null;
let rhrData = [];

// ═══════════════════════════════════════
//  STEPS STATE
// ═══════════════════════════════════════
let allSteps = [];
let filteredSteps = [];
let stepsSortField = 'date';
let stepsSortAsc = false;
let stepsChartRange = 30;
let currentStepsMonth = null;

// ── Running Helpers ──
function msToKmh(ms) { return ms ? (ms * 3.6).toFixed(1) : '—'; }
function mToKm(m) { return m ? (m / 1000).toFixed(2) : '—'; }
function secondsToHMS(s) {
  if (!s) return '—';
  const h = Math.floor(s / 3600), m = Math.floor((s % 3600) / 60), sec = Math.floor(s % 60);
  return h > 0 ? `${h}h ${m}m ${sec}s` : `${m}m ${sec}s`;
}
function formatDate(d) { return d ? new Date(d).toLocaleDateString('en-IN', {day:'2-digit',month:'short',year:'numeric'}) : '—'; }
function formatDateShort(d) { return d ? new Date(d).toLocaleDateString('en-IN', {day:'2-digit',month:'short'}) : ''; }
function getSpeedClass(s) { return s >= 15 ? 'speed-fast' : s >= 10 ? 'speed-medium' : 'speed-slow'; }
function getMonthKey(d) { if (!d) return null; const dt = new Date(d); return `${dt.getFullYear()}-${String(dt.getMonth()+1).padStart(2,'0')}`; }
function formatMonthLabel(k) { const [y,m] = k.split('-'); return ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'][parseInt(m)-1] + ' ' + y; }

// ── Steps Helpers ──
function formatStepsDate(d) { return d ? new Date(d + 'T00:00:00').toLocaleDateString('en-IN', {day:'2-digit',month:'short',year:'numeric'}) : '—'; }
function formatStepsDateShort(d) { return d ? new Date(d + 'T00:00:00').toLocaleDateString('en-IN', {day:'2-digit',month:'short'}) : ''; }
function getStepsMonthKey(d) { if (!d) return null; return d.substring(0, 7); }
function getGoalClass(pct) { return pct >= 100 ? 'goal-met' : pct >= 70 ? 'goal-close' : 'goal-miss'; }

// ═══════════════════════════════════════
//  DATA LOADING
// ═══════════════════════════════════════
async function loadData() {
  try {
    // Load running data
    const { data, error } = await sb.from('garmin_activities').select('*').order('start_time', { ascending: false });
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
    } else {
      const latest = allRuns.reduce((a, b) => new Date(a.synced_at) > new Date(b.synced_at) ? a : b);
      document.getElementById('last-sync').textContent = 'Last sync: ' + formatDate(latest.synced_at);

      renderStats();
      renderRecords();
      renderChart();
      await loadRhrData();
      renderMonthlyStats();
      renderRunsTable();
    }

    // Load steps data
    await loadStepsData();

  } catch (err) {
    console.error('Load error:', err);
    document.getElementById('connection-badge').className = 'connection-badge offline';
    document.getElementById('connection-text').textContent = 'Offline';
    document.getElementById('loading').innerHTML = '<div class="empty-state-icon">⚠️</div><p style="color:#ef5350;">Could not connect to database</p>';
    showToast('⚠️ Failed to load data', 'error');
  }
}

async function loadStepsData() {
  try {
    document.getElementById('steps-loading').style.display = 'block';
    const { data, error } = await sb.from('garmin_daily_steps').select('*').order('date', { ascending: false });
    if (error) throw error;

    allSteps = (data || []).map(r => ({
      ...r,
      goal_pct: r.step_goal && r.step_goal > 0 ? Math.round((r.total_steps / r.step_goal) * 100) : null,
      distanceKm: r.distance ? (r.distance / 1000).toFixed(2) : null,
    }));
    filteredSteps = [...allSteps];

    document.getElementById('steps-loading').style.display = 'none';
    document.getElementById('steps-content').style.display = 'block';

    if (allSteps.length === 0) {
      document.getElementById('steps-empty-state').style.display = 'block';
      return;
    }

    renderStepsStats();
    renderGoalBar();
    renderStepsRecords();
    renderStepsChart();
    renderWeekly();
    renderStepsMonthly();
    renderStepsTable();
  } catch (e) {
    console.warn('Steps load skipped:', e);
    document.getElementById('steps-loading').style.display = 'none';
    document.getElementById('steps-content').style.display = 'block';
    document.getElementById('steps-empty-state').style.display = 'block';
  }
}

// ═══════════════════════════════════════
//  RUNNING: SUMMARY STATS
// ═══════════════════════════════════════
function renderStats() {
  const n = allRuns.length;
  const totalDist = allRuns.reduce((s,r) => s + r.distanceKm, 0);
  const totalTime = allRuns.reduce((s,r) => s + (r.duration||0), 0);
  const totalSteps = allRuns.reduce((s,r) => s + (r.steps||0), 0);
  const totalCal = allRuns.reduce((s,r) => s + (r.calories||0), 0);
  const wp = allRuns.filter(r => r.paceMinKm > 0);
  const avgPace = wp.length > 0 ? wp.reduce((s,r) => s + r.paceMinKm, 0) / wp.length : 0;
  const pm = Math.floor(avgPace), ps = Math.round((avgPace - pm)*60);
  const wh = allRuns.filter(r => r.avg_hr);
  const avgHr = wh.length > 0 ? Math.round(wh.reduce((s,r) => s + r.avg_hr, 0) / wh.length) : 0;
  const avgStepsPerRun = n > 0 ? Math.round(totalSteps / n) : 0;

  document.getElementById('stats-grid').innerHTML = `
    <div class="stat-card"><span class="stat-icon">🏃</span><span class="stat-value">${n}</span><span class="stat-label">Total Runs</span></div>
    <div class="stat-card"><span class="stat-icon">📏</span><span class="stat-value">${totalDist.toFixed(1)}</span><span class="stat-label">Total KM</span></div>
    <div class="stat-card"><span class="stat-icon">⏱️</span><span class="stat-value">${secondsToHMS(totalTime)}</span><span class="stat-label">Total Time</span></div>
    <div class="stat-card"><span class="stat-icon">💨</span><span class="stat-value">${pm}:${String(ps).padStart(2,'0')}</span><span class="stat-label">Avg Pace /km</span></div>
    <div class="stat-card"><span class="stat-icon">👟</span><span class="stat-value">${totalSteps > 0 ? totalSteps.toLocaleString() : '—'}</span><span class="stat-label">Total Steps</span></div>
    <div class="stat-card"><span class="stat-icon">🦶</span><span class="stat-value">${avgStepsPerRun > 0 ? avgStepsPerRun.toLocaleString() : '—'}</span><span class="stat-label">Avg Steps/Run</span></div>
    <div class="stat-card"><span class="stat-icon">🔥</span><span class="stat-value">${totalCal > 0 ? totalCal.toLocaleString() : '—'}</span><span class="stat-label">Calories Burned</span></div>
    <div class="stat-card"><span class="stat-icon">❤️</span><span class="stat-value">${avgHr || '—'}</span><span class="stat-label">Avg Heart Rate</span></div>
  `;
}

// ═══════════════════════════════════════
//  RUNNING: PERSONAL RECORDS
// ═══════════════════════════════════════
function renderRecords() {
  if (!allRuns.length) return;
  const lg = allRuns.reduce((a,b) => a.distanceKm > b.distanceKm ? a : b);
  const fs = allRuns.reduce((a,b) => a.maxSpeedKmh > b.maxSpeedKmh ? a : b);
  const wp = allRuns.filter(r => r.paceMinKm > 0);
  const bp = wp.length > 0 ? wp.reduce((a,b) => a.paceMinKm < b.paceMinKm ? a : b) : null;
  const wh = allRuns.filter(r => r.max_hr);
  const hh = wh.length > 0 ? wh.reduce((a,b) => a.max_hr > b.max_hr ? a : b) : null;
  const mc = allRuns.reduce((a,b) => (a.calories||0) > (b.calories||0) ? a : b);
  const lt = allRuns.reduce((a,b) => (a.duration||0) > (b.duration||0) ? a : b);
  const bpm = bp ? Math.floor(bp.paceMinKm) : 0;
  const bps = bp ? Math.round((bp.paceMinKm - bpm)*60) : 0;

  document.getElementById('records-grid').innerHTML = `
    <div class="record-card"><div class="record-icon gold">🏅</div><div class="record-info"><div class="record-title">Longest Run</div><div class="record-value">${lg.distanceKm.toFixed(2)} km</div><div class="record-detail">${lg.activity_name} — ${formatDate(lg.start_time)}</div></div></div>
    <div class="record-card"><div class="record-icon green">⚡</div><div class="record-info"><div class="record-title">Fastest Max Speed</div><div class="record-value">${fs.maxSpeedKmh.toFixed(1)} km/h</div><div class="record-detail">${fs.activity_name} — ${formatDate(fs.start_time)}</div></div></div>
    ${bp ? `<div class="record-card"><div class="record-icon blue">💨</div><div class="record-info"><div class="record-title">Best Avg Pace</div><div class="record-value">${bpm}:${String(bps).padStart(2,'0')} /km</div><div class="record-detail">${bp.activity_name} — ${formatDate(bp.start_time)}</div></div></div>` : ''}
    ${hh ? `<div class="record-card"><div class="record-icon red">❤️</div><div class="record-info"><div class="record-title">Highest Max HR</div><div class="record-value">${hh.max_hr} bpm</div><div class="record-detail">${hh.activity_name} — ${formatDate(hh.start_time)}</div></div></div>` : ''}
    <div class="record-card"><div class="record-icon orange">🔥</div><div class="record-info"><div class="record-title">Most Calories</div><div class="record-value">${(mc.calories||0).toLocaleString()} cal</div><div class="record-detail">${mc.activity_name} — ${formatDate(mc.start_time)}</div></div></div>
    <div class="record-card"><div class="record-icon purple">⏱️</div><div class="record-info"><div class="record-title">Longest Duration</div><div class="record-value">${secondsToHMS(lt.duration)}</div><div class="record-detail">${lt.activity_name} — ${formatDate(lt.start_time)}</div></div></div>
  `;
}

// ═══════════════════════════════════════
//  RUNNING: TRENDS CHART
// ═══════════════════════════════════════
function switchChart(metric) {
  currentChartMetric = metric;
  document.querySelectorAll('#chart-tabs .chart-tab').forEach(t => t.classList.toggle('active', t.getAttribute('data-metric') === metric));
  renderChart();
}

function renderChart() {
  const canvas = document.getElementById('speed-chart');
  const ctx = canvas.getContext('2d');
  const dpr = window.devicePixelRatio || 1;
  const sorted = [...allRuns].sort((a,b) => new Date(a.start_time) - new Date(b.start_time));
  if (!sorted.length) return;

  let values, label, unit, color;
  switch (currentChartMetric) {
    case 'maxSpeed': values = sorted.map(r => r.maxSpeedKmh); label = 'Max Speed'; unit = 'km/h'; color = '#00E676'; break;
    case 'distance': values = sorted.map(r => r.distanceKm); label = 'Distance'; unit = 'km'; color = '#42A5F5'; break;
    case 'avgPace': values = sorted.map(r => r.paceMinKm > 0 ? r.paceMinKm : null); label = 'Avg Pace'; unit = 'min/km'; color = '#FFA726'; break;
    case 'avgHr': values = sorted.map(r => r.avg_hr || null); label = 'Avg HR'; unit = 'bpm'; color = '#ef5350'; break;
  }
  const dates = sorted.map(r => formatDateShort(r.start_time));
  const rect = canvas.parentElement.getBoundingClientRect();
  canvas.width = rect.width * dpr; canvas.height = 300 * dpr;
  canvas.style.width = rect.width + 'px'; canvas.style.height = '300px';
  ctx.scale(dpr, dpr);
  const W = rect.width, H = 300;
  const pad = {top:30,right:20,bottom:40,left:55};
  const cW = W-pad.left-pad.right, cH = H-pad.top-pad.bottom;
  ctx.clearRect(0,0,W,H);

  const valid = values.filter(v => v != null && v > 0);
  if (!valid.length) return;
  const mn = Math.min(...valid)*0.9, mx = Math.max(...valid)*1.1, rng = mx-mn||1;

  ctx.strokeStyle = '#1e1e2e'; ctx.lineWidth = 1;
  for (let i=0;i<=5;i++) {
    const y = pad.top+(cH/5)*i;
    ctx.beginPath(); ctx.moveTo(pad.left,y); ctx.lineTo(W-pad.right,y); ctx.stroke();
    const val = mx-(rng/5)*i;
    ctx.fillStyle='#555'; ctx.font='11px JetBrains Mono'; ctx.textAlign='right';
    if (currentChartMetric==='avgPace') { const m=Math.floor(val),s=Math.round((val-m)*60); ctx.fillText(`${m}:${String(s).padStart(2,'0')}`,pad.left-8,y+4); }
    else ctx.fillText(val.toFixed(1),pad.left-8,y+4);
  }

  const pts=[];
  for (let i=0;i<values.length;i++) {
    if (values[i]==null) continue;
    pts.push({x:pad.left+(i/Math.max(values.length-1,1))*cW, y:pad.top+cH-((values[i]-mn)/rng)*cH, val:values[i], label:dates[i]});
  }
  if (pts.length<2) return;

  const grad = ctx.createLinearGradient(0,pad.top,0,H-pad.bottom);
  grad.addColorStop(0,color+'30'); grad.addColorStop(1,color+'05');
  ctx.beginPath(); ctx.moveTo(pts[0].x,H-pad.bottom); ctx.lineTo(pts[0].x,pts[0].y);
  for (let i=1;i<pts.length;i++) { const cx=(pts[i-1].x+pts[i].x)/2; ctx.bezierCurveTo(cx,pts[i-1].y,cx,pts[i].y,pts[i].x,pts[i].y); }
  ctx.lineTo(pts[pts.length-1].x,H-pad.bottom); ctx.closePath(); ctx.fillStyle=grad; ctx.fill();

  ctx.beginPath(); ctx.moveTo(pts[0].x,pts[0].y);
  for (let i=1;i<pts.length;i++) { const cx=(pts[i-1].x+pts[i].x)/2; ctx.bezierCurveTo(cx,pts[i-1].y,cx,pts[i].y,pts[i].x,pts[i].y); }
  ctx.strokeStyle=color; ctx.lineWidth=2.5; ctx.stroke();

  pts.forEach(p => { ctx.beginPath(); ctx.arc(p.x,p.y,3.5,0,Math.PI*2); ctx.fillStyle=color; ctx.fill(); ctx.beginPath(); ctx.arc(p.x,p.y,2,0,Math.PI*2); ctx.fillStyle='#0a0a0f'; ctx.fill(); });
  const step = Math.max(1,Math.floor(pts.length/10));
  ctx.fillStyle='#555'; ctx.font='10px JetBrains Mono'; ctx.textAlign='center';
  for (let i=0;i<pts.length;i+=step) ctx.fillText(pts[i].label,pts[i].x,H-pad.bottom+18);
  ctx.fillStyle='#666'; ctx.font='11px Inter'; ctx.textAlign='left';
  ctx.fillText(`${label} (${unit})`,pad.left,pad.top-10);
}

// ═══════════════════════════════════════
//  RUNNING: MONTHLY BREAKDOWN
// ═══════════════════════════════════════
function getRunMonthlyData() {
  const m = {};
  allRuns.forEach(r => { const k = getMonthKey(r.start_time); if (!k) return; if (!m[k]) m[k]=[]; m[k].push(r); });
  return m;
}
function setRunMonth(k) {
  currentRunMonth = k;
  document.querySelectorAll('#month-tabs .month-tab').forEach(t => t.classList.toggle('active', t.getAttribute('data-month') === k));
  renderRunMonthDetail();
}
function renderMonthlyStats() {
  if (!allRuns.length) return;
  const byMonth = getRunMonthlyData();
  const keys = Object.keys(byMonth).sort().reverse();
  if (!keys.length) return;
  if (!currentRunMonth || !byMonth[currentRunMonth]) currentRunMonth = keys[0];

  document.getElementById('month-tabs').innerHTML = keys.map(k => {
    const a = k === currentRunMonth ? 'active' : '';
    return `<button class="month-tab ${a}" data-month="${k}" onclick="setRunMonth('${k}')">${formatMonthLabel(k)} (${byMonth[k].length})</button>`;
  }).join('');
  renderRunMonthDetail();
}
function renderRunMonthDetail() {
  const runs = (getRunMonthlyData()[currentRunMonth]) || [];
  if (!runs.length) { document.getElementById('monthly-stats-grid').innerHTML = '<div style="text-align:center;color:#444;padding:30px;grid-column:1/-1;">No runs this month</div>'; return; }

  const n = runs.length;
  const dist = runs.reduce((s,r) => s + r.distanceKm, 0);
  const time = runs.reduce((s,r) => s + (r.duration||0), 0);
  const steps = runs.reduce((s,r) => s + (r.steps||0), 0);
  const cal = runs.reduce((s,r) => s + (r.calories||0), 0);
  const wp = runs.filter(r => r.paceMinKm > 0);
  const ap = wp.length ? wp.reduce((s,r) => s + r.paceMinKm, 0)/wp.length : 0;
  const pm = Math.floor(ap), ps = Math.round((ap-pm)*60);
  const topSpd = Math.max(...runs.map(r => r.maxSpeedKmh), 0);
  const wh = runs.filter(r => r.avg_hr);
  const ah = wh.length ? Math.round(wh.reduce((s,r) => s + r.avg_hr, 0)/wh.length) : 0;
  const avgSteps = n > 0 ? Math.round(steps / n) : 0;

  document.getElementById('monthly-stats-grid').innerHTML = `
    <div class="monthly-stat"><span class="monthly-stat-icon">🏃</span><span class="monthly-stat-val">${n}</span><span class="monthly-stat-label">Runs</span></div>
    <div class="monthly-stat"><span class="monthly-stat-icon">📏</span><span class="monthly-stat-val">${dist.toFixed(1)}</span><span class="monthly-stat-label">Total KM</span></div>
    <div class="monthly-stat"><span class="monthly-stat-icon">⏱️</span><span class="monthly-stat-val">${secondsToHMS(time)}</span><span class="monthly-stat-label">Time</span></div>
    <div class="monthly-stat"><span class="monthly-stat-icon">💨</span><span class="monthly-stat-val">${ap > 0 ? pm+':'+String(ps).padStart(2,'0') : '—'}</span><span class="monthly-stat-label">Avg Pace /km</span></div>
    <div class="monthly-stat"><span class="monthly-stat-icon">⚡</span><span class="monthly-stat-val">${topSpd.toFixed(1)}</span><span class="monthly-stat-label">Top Speed km/h</span></div>
    <div class="monthly-stat"><span class="monthly-stat-icon">👟</span><span class="monthly-stat-val">${steps > 0 ? steps.toLocaleString() : '—'}</span><span class="monthly-stat-label">Total Steps</span></div>
    <div class="monthly-stat"><span class="monthly-stat-icon">🦶</span><span class="monthly-stat-val">${avgSteps > 0 ? avgSteps.toLocaleString() : '—'}</span><span class="monthly-stat-label">Avg Steps/Run</span></div>
    <div class="monthly-stat"><span class="monthly-stat-icon">❤️</span><span class="monthly-stat-val">${ah || '—'}</span><span class="monthly-stat-label">Avg HR</span></div>
    <div class="monthly-stat"><span class="monthly-stat-icon">🔥</span><span class="monthly-stat-val">${cal > 0 ? Math.round(cal).toLocaleString() : '—'}</span><span class="monthly-stat-label">Calories</span></div>
  `;
}

// ═══════════════════════════════════════
//  RUNNING: RUNS TABLE
// ═══════════════════════════════════════
function sortRunsTable(field) {
  if (runSortField === field) runSortAsc = !runSortAsc;
  else { runSortField = field; runSortAsc = false; }
  document.querySelectorAll('.runs-table th').forEach(th => th.classList.remove('sorted'));
  const th = document.getElementById(`th-${field}`);
  if (th) { th.classList.add('sorted'); th.querySelector('.sort-arrow').textContent = runSortAsc ? '▲' : '▼'; }
  renderRunsTable();
}
function renderRunsTable() {
  const q = (document.getElementById('table-search').value||'').toLowerCase();
  let rows = filteredRuns;
  if (q) rows = rows.filter(r => (r.activity_name||'').toLowerCase().includes(q) || formatDate(r.start_time).toLowerCase().includes(q));
  rows.sort((a,b) => {
    let va,vb;
    switch(runSortField) {
      case 'date': va=new Date(a.start_time);vb=new Date(b.start_time);break;
      case 'name': va=(a.activity_name||'').toLowerCase();vb=(b.activity_name||'').toLowerCase();break;
      case 'distance': va=a.distanceKm;vb=b.distanceKm;break;
      case 'duration': va=a.duration||0;vb=b.duration||0;break;
      case 'avgPace': va=a.paceMinKm||999;vb=b.paceMinKm||999;break;
      case 'maxSpeed': va=a.maxSpeedKmh;vb=b.maxSpeedKmh;break;
      case 'avgHr': va=a.avg_hr||0;vb=b.avg_hr||0;break;
      case 'calories': va=a.calories||0;vb=b.calories||0;break;
      default: va=0;vb=0;
    }
    return va<vb ? (runSortAsc?-1:1) : va>vb ? (runSortAsc?1:-1) : 0;
  });
  document.getElementById('table-count').textContent = `${rows.length} runs`;
  const tbody = document.getElementById('runs-tbody');
  if (!rows.length) { tbody.innerHTML = '<tr><td colspan="8" style="text-align:center;color:#555;padding:30px;">No runs match</td></tr>'; return; }
  tbody.innerHTML = rows.map(r => {
    const pm=Math.floor(r.paceMinKm), ps=Math.round((r.paceMinKm-pm)*60);
    const pace = r.paceMinKm > 0 ? `${pm}:${String(ps).padStart(2,'0')}` : '—';
    return `<tr>
      <td class="run-date">${formatDate(r.start_time)}</td>
      <td class="run-name" title="${r.activity_name||''}">${r.activity_name||'Run'}</td>
      <td class="run-distance">${r.distanceKm.toFixed(2)} km</td>
      <td style="color:#ccc;font-family:'JetBrains Mono',monospace;">${secondsToHMS(r.duration)}</td>
      <td class="run-pace">${pace} /km</td>
      <td><span class="speed-badge ${getSpeedClass(r.maxSpeedKmh)}">${r.maxSpeedKmh.toFixed(1)} km/h</span></td>
      <td style="color:#ef5350;font-family:'JetBrains Mono',monospace;">${r.avg_hr ? '♥ '+Math.round(r.avg_hr) : '—'}</td>
      <td style="color:#ccc;font-family:'JetBrains Mono',monospace;">${r.calories ? Math.round(r.calories) : '—'}</td>
    </tr>`;
  }).join('');
}

// ═══════════════════════════════════════
//  RUNNING: RESTING HR
// ═══════════════════════════════════════
async function loadRhrData() {
  try {
    const { data, error } = await sb.from('garmin_resting_hr').select('*').order('date', { ascending: true });
    if (error) throw error;
    rhrData = data || [];
    if (rhrData.length > 0) renderRhrChart();
  } catch (e) { console.warn('RHR load skipped:', e); }
}

function renderRhrChart() {
  if (!rhrData.length) return;
  const canvas = document.getElementById('rhr-chart');
  const ctx = canvas.getContext('2d');
  const dpr = window.devicePixelRatio || 1;
  const rect = canvas.parentElement.getBoundingClientRect();
  canvas.width = rect.width * dpr; canvas.height = 280 * dpr;
  canvas.style.width = rect.width + 'px'; canvas.style.height = '280px';
  ctx.scale(dpr, dpr);
  const W = rect.width, H = 280;
  const pad = {top:30,right:20,bottom:40,left:50};
  const cW = W-pad.left-pad.right, cH = H-pad.top-pad.bottom;
  ctx.clearRect(0,0,W,H);

  const values = rhrData.map(d => d.resting_hr);
  const dates = rhrData.map(d => formatDateShort(d.date));
  const minY = 40, maxY = 70;
  const rng = maxY - minY;

  const avg = Math.round(values.reduce((s,v)=>s+v,0)/values.length);
  const min = Math.min(...values), max = Math.max(...values);
  const latest = values[values.length-1];
  document.getElementById('rhr-info').innerHTML = `
    <div class="rhr-info-item">Latest: <span>${latest} bpm</span></div>
    <div class="rhr-info-item">Avg: <span>${avg} bpm</span></div>
    <div class="rhr-info-item">Min: <span>${min} bpm</span></div>
    <div class="rhr-info-item">Max: <span>${max} bpm</span></div>
    <div class="rhr-info-item">${rhrData.length} days</div>
  `;

  ctx.strokeStyle='#1e1e2e'; ctx.lineWidth=1;
  for (let i=0;i<=5;i++) {
    const y=pad.top+(cH/5)*i;
    ctx.beginPath(); ctx.moveTo(pad.left,y); ctx.lineTo(W-pad.right,y); ctx.stroke();
    const val=maxY-(rng/5)*i;
    ctx.fillStyle='#555'; ctx.font='11px JetBrains Mono'; ctx.textAlign='right';
    ctx.fillText(val.toFixed(0),pad.left-8,y+4);
  }

  const pts=[];
  for (let i=0;i<values.length;i++) {
    const x=pad.left+(i/Math.max(values.length-1,1))*cW;
    const clamped = Math.max(minY, Math.min(maxY, values[i]));
    const y=pad.top+cH-((clamped-minY)/rng)*cH;
    pts.push({x,y,val:values[i],label:dates[i]});
  }
  if (pts.length<2) return;

  const grad=ctx.createLinearGradient(0,pad.top,0,H-pad.bottom);
  grad.addColorStop(0,'rgba(239,83,80,0.25)'); grad.addColorStop(1,'rgba(239,83,80,0.02)');
  ctx.beginPath(); ctx.moveTo(pts[0].x,H-pad.bottom); ctx.lineTo(pts[0].x,pts[0].y);
  for (let i=1;i<pts.length;i++){const cx=(pts[i-1].x+pts[i].x)/2;ctx.bezierCurveTo(cx,pts[i-1].y,cx,pts[i].y,pts[i].x,pts[i].y);}
  ctx.lineTo(pts[pts.length-1].x,H-pad.bottom); ctx.closePath(); ctx.fillStyle=grad; ctx.fill();

  ctx.beginPath(); ctx.moveTo(pts[0].x,pts[0].y);
  for (let i=1;i<pts.length;i++){const cx=(pts[i-1].x+pts[i].x)/2;ctx.bezierCurveTo(cx,pts[i-1].y,cx,pts[i].y,pts[i].x,pts[i].y);}
  ctx.strokeStyle='#ef5350'; ctx.lineWidth=2.5; ctx.stroke();

  pts.forEach(p=>{ctx.beginPath();ctx.arc(p.x,p.y,3,0,Math.PI*2);ctx.fillStyle='#ef5350';ctx.fill();ctx.beginPath();ctx.arc(p.x,p.y,1.5,0,Math.PI*2);ctx.fillStyle='#0a0a0f';ctx.fill();});

  const step=Math.max(1,Math.floor(pts.length/10));
  ctx.fillStyle='#555'; ctx.font='10px JetBrains Mono'; ctx.textAlign='center';
  for (let i=0;i<pts.length;i+=step) ctx.fillText(pts[i].label,pts[i].x,H-pad.bottom+18);
  ctx.fillStyle='#666'; ctx.font='11px Inter'; ctx.textAlign='left';
  ctx.fillText('Resting HR (bpm)',pad.left,pad.top-10);
}

// ═══════════════════════════════════════
//  STEPS: SUMMARY STATS
// ═══════════════════════════════════════
function renderStepsStats() {
  const n = allSteps.length;
  const totalSteps = allSteps.reduce((s,r) => s + (r.total_steps||0), 0);
  const avgSteps = n > 0 ? Math.round(totalSteps / n) : 0;
  const best = allSteps.reduce((a,b) => (a.total_steps||0) > (b.total_steps||0) ? a : b);
  const totalDist = allSteps.reduce((s,r) => s + (r.distance||0), 0) / 1000;
  const totalCal = allSteps.reduce((s,r) => s + (r.calories_total||0), 0);

  let streak = 0;
  const sorted = [...allSteps].sort((a,b) => b.date.localeCompare(a.date));
  for (const day of sorted) {
    if (day.step_goal && day.total_steps >= day.step_goal) streak++;
    else break;
  }
  const metGoal = allSteps.filter(r => r.goal_pct !== null && r.goal_pct >= 100).length;

  document.getElementById('steps-stats-grid').innerHTML = `
    <div class="steps-stat-card"><span class="stat-icon">🚶</span><span class="stat-value">${totalSteps.toLocaleString()}</span><span class="stat-label">Total Steps</span></div>
    <div class="steps-stat-card"><span class="stat-icon">📊</span><span class="stat-value">${avgSteps.toLocaleString()}</span><span class="stat-label">Avg Steps/Day</span></div>
    <div class="steps-stat-card"><span class="stat-icon">🏆</span><span class="stat-value">${(best.total_steps||0).toLocaleString()}</span><span class="stat-label">Best Day</span></div>
    <div class="steps-stat-card"><span class="stat-icon">🔥</span><span class="stat-value">${streak}</span><span class="stat-label">Goal Streak</span></div>
    <div class="steps-stat-card"><span class="stat-icon">🎯</span><span class="stat-value">${metGoal}/${n}</span><span class="stat-label">Days Goal Met</span></div>
    <div class="steps-stat-card"><span class="stat-icon">📏</span><span class="stat-value">${totalDist > 0 ? totalDist.toFixed(1) : '—'}</span><span class="stat-label">Total KM Walked</span></div>
    <div class="steps-stat-card"><span class="stat-icon">🔥</span><span class="stat-value">${totalCal > 0 ? totalCal.toLocaleString() : '—'}</span><span class="stat-label">Total Calories</span></div>
    <div class="steps-stat-card"><span class="stat-icon">📅</span><span class="stat-value">${n}</span><span class="stat-label">Days Tracked</span></div>
  `;
}

// ═══════════════════════════════════════
//  STEPS: GOAL BAR
// ═══════════════════════════════════════
function renderGoalBar() {
  const today = new Date().toISOString().substring(0, 10);
  const todayData = allSteps.find(r => r.date === today);
  if (!todayData || !todayData.step_goal) {
    document.getElementById('steps-goal-section').style.display = 'none';
    document.getElementById('goal-bar-container').style.display = 'none';
    return;
  }
  document.getElementById('steps-goal-section').style.display = 'flex';
  document.getElementById('goal-bar-container').style.display = 'block';
  const pct = Math.min(100, Math.round((todayData.total_steps / todayData.step_goal) * 100));
  document.getElementById('goal-label-text').textContent = `${todayData.total_steps.toLocaleString()} / ${todayData.step_goal.toLocaleString()} steps`;
  document.getElementById('goal-pct').textContent = `${pct}%`;
  setTimeout(() => { document.getElementById('goal-bar-fill').style.width = pct + '%'; }, 100);
}

// ═══════════════════════════════════════
//  STEPS: RECORDS
// ═══════════════════════════════════════
function renderStepsRecords() {
  if (!allSteps.length) return;
  const best = allSteps.reduce((a,b) => (a.total_steps||0) > (b.total_steps||0) ? a : b);
  const worst = allSteps.reduce((a,b) => (a.total_steps||0) < (b.total_steps||0) ? a : b);
  const bestDist = allSteps.filter(r => r.distance).reduce((a,b) => (a.distance||0) > (b.distance||0) ? a : b, {distance:0});
  const bestCal = allSteps.filter(r => r.calories_total).reduce((a,b) => (a.calories_total||0) > (b.calories_total||0) ? a : b, {calories_total:0});

  const sortedAsc = [...allSteps].sort((a,b) => a.date.localeCompare(b.date));
  let bestWeekTotal = 0, bestWeekStart = '';
  for (let i = 0; i <= sortedAsc.length - 7; i++) {
    const weekTotal = sortedAsc.slice(i, i+7).reduce((s,r) => s + (r.total_steps||0), 0);
    if (weekTotal > bestWeekTotal) { bestWeekTotal = weekTotal; bestWeekStart = sortedAsc[i].date; }
  }

  document.getElementById('steps-records-grid').innerHTML = `
    <div class="record-card"><div class="record-icon gold">🏅</div><div class="record-info"><div class="record-title">Best Day</div><div class="record-value">${(best.total_steps||0).toLocaleString()}</div><div class="record-detail">${formatStepsDate(best.date)}</div></div></div>
    <div class="record-card"><div class="record-icon purple">📅</div><div class="record-info"><div class="record-title">Best Week</div><div class="record-value">${bestWeekTotal > 0 ? bestWeekTotal.toLocaleString() : '—'}</div><div class="record-detail">${bestWeekStart ? 'Starting ' + formatStepsDate(bestWeekStart) : '—'}</div></div></div>
    ${bestDist.distance ? `<div class="record-card"><div class="record-icon green">📏</div><div class="record-info"><div class="record-title">Most Distance</div><div class="record-value">${(bestDist.distance/1000).toFixed(2)} km</div><div class="record-detail">${formatStepsDate(bestDist.date)}</div></div></div>` : ''}
    ${bestCal.calories_total ? `<div class="record-card"><div class="record-icon orange">🔥</div><div class="record-info"><div class="record-title">Most Calories</div><div class="record-value">${bestCal.calories_total.toLocaleString()}</div><div class="record-detail">${formatStepsDate(bestCal.date)}</div></div></div>` : ''}
    <div class="record-card"><div class="record-icon red">📉</div><div class="record-info"><div class="record-title">Lowest Day</div><div class="record-value">${(worst.total_steps||0).toLocaleString()}</div><div class="record-detail">${formatStepsDate(worst.date)}</div></div></div>
  `;
}

// ═══════════════════════════════════════
//  STEPS: CHART
// ═══════════════════════════════════════
function switchStepsRange(range) {
  stepsChartRange = range;
  document.querySelectorAll('#steps-chart-tabs .steps-chart-tab').forEach(t => t.classList.toggle('active', parseInt(t.getAttribute('data-range')) === range));
  renderStepsChart();
}

function renderStepsChart() {
  const canvas = document.getElementById('steps-chart');
  const ctx = canvas.getContext('2d');
  const dpr = window.devicePixelRatio || 1;

  const sorted = [...allSteps].sort((a,b) => a.date.localeCompare(b.date));
  const recent = sorted.slice(-stepsChartRange);
  if (!recent.length) return;

  const values = recent.map(r => r.total_steps || 0);
  const goals = recent.map(r => r.step_goal || 0);
  const dates = recent.map(r => formatStepsDateShort(r.date));
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

  ctx.strokeStyle = '#1e1e2e'; ctx.lineWidth = 1;
  for (let i = 0; i <= 5; i++) {
    const y = pad.top + (cH / 5) * i;
    ctx.beginPath(); ctx.moveTo(pad.left, y); ctx.lineTo(W - pad.right, y); ctx.stroke();
    const val = mx - (rng / 5) * i;
    ctx.fillStyle = '#555'; ctx.font = '11px JetBrains Mono'; ctx.textAlign = 'right';
    ctx.fillText(Math.round(val).toLocaleString(), pad.left - 8, y + 4);
  }

  const avgGoal = goals.filter(g => g > 0);
  if (avgGoal.length > 0) {
    const goalVal = avgGoal[avgGoal.length - 1];
    const goalY = pad.top + cH - ((goalVal - mn) / rng) * cH;
    ctx.setLineDash([6, 4]);
    ctx.strokeStyle = 'rgba(224,64,251,0.4)';
    ctx.lineWidth = 1.5;
    ctx.beginPath(); ctx.moveTo(pad.left, goalY); ctx.lineTo(W - pad.right, goalY); ctx.stroke();
    ctx.setLineDash([]);
    ctx.fillStyle = 'rgba(224,64,251,0.6)'; ctx.font = '10px JetBrains Mono'; ctx.textAlign = 'left';
    ctx.fillText('Goal: ' + goalVal.toLocaleString(), pad.left + 4, goalY - 6);
  }

  const barW = Math.max(2, (cW / values.length) * 0.7);
  const gap = cW / values.length;
  values.forEach((v, i) => {
    const x = pad.left + i * gap + (gap - barW) / 2;
    const barH = (v / rng) * cH;
    const y = pad.top + cH - barH;
    const metGoal = goals[i] > 0 && v >= goals[i];

    const grad = ctx.createLinearGradient(x, y, x, pad.top + cH);
    if (metGoal) {
      grad.addColorStop(0, 'rgba(0,230,118,0.8)');
      grad.addColorStop(1, 'rgba(0,230,118,0.2)');
    } else {
      grad.addColorStop(0, 'rgba(124,77,255,0.8)');
      grad.addColorStop(1, 'rgba(124,77,255,0.2)');
    }

    ctx.fillStyle = grad;
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

  const step = Math.max(1, Math.floor(values.length / 10));
  ctx.fillStyle = '#555'; ctx.font = '10px JetBrains Mono'; ctx.textAlign = 'center';
  for (let i = 0; i < values.length; i += step) {
    const x = pad.left + i * gap + gap / 2;
    ctx.fillText(dates[i], x, H - pad.bottom + 18);
  }
  ctx.fillStyle = '#666'; ctx.font = '11px Inter'; ctx.textAlign = 'left';
  ctx.fillText('Daily Steps', pad.left, pad.top - 10);
}

// ═══════════════════════════════════════
//  STEPS: WEEKLY
// ═══════════════════════════════════════
function renderWeekly() {
  const today = new Date();
  const dayOfWeek = today.getDay();
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

// ═══════════════════════════════════════
//  STEPS: MONTHLY
// ═══════════════════════════════════════
function getStepsMonthlyData() {
  const m = {};
  allSteps.forEach(r => { const k = getStepsMonthKey(r.date); if (!k) return; if (!m[k]) m[k] = []; m[k].push(r); });
  return m;
}
function setStepsMonth(k) {
  currentStepsMonth = k;
  document.querySelectorAll('#steps-month-tabs .steps-month-tab').forEach(t => t.classList.toggle('active', t.getAttribute('data-month') === k));
  renderStepsMonthDetail();
}
function renderStepsMonthly() {
  if (!allSteps.length) return;
  const byMonth = getStepsMonthlyData();
  const keys = Object.keys(byMonth).sort().reverse();
  if (!keys.length) return;
  if (!currentStepsMonth || !byMonth[currentStepsMonth]) currentStepsMonth = keys[0];

  document.getElementById('steps-month-tabs').innerHTML = keys.map(k => {
    const a = k === currentStepsMonth ? 'active' : '';
    return `<button class="steps-month-tab ${a}" data-month="${k}" onclick="setStepsMonth('${k}')">${formatMonthLabel(k)} (${byMonth[k].length})</button>`;
  }).join('');
  renderStepsMonthDetail();
}
function renderStepsMonthDetail() {
  const days = (getStepsMonthlyData()[currentStepsMonth]) || [];
  if (!days.length) { document.getElementById('steps-monthly-stats-grid').innerHTML = '<div style="text-align:center;color:#444;padding:30px;grid-column:1/-1;">No data this month</div>'; return; }

  const n = days.length;
  const total = days.reduce((s,r) => s + (r.total_steps||0), 0);
  const avg = Math.round(total / n);
  const best = Math.max(...days.map(r => r.total_steps||0));
  const worst = Math.min(...days.map(r => r.total_steps||0));
  const dist = days.reduce((s,r) => s + (r.distance||0), 0) / 1000;
  const cal = days.reduce((s,r) => s + (r.calories_total||0), 0);
  const goalMet = days.filter(r => r.goal_pct !== null && r.goal_pct >= 100).length;

  document.getElementById('steps-monthly-stats-grid').innerHTML = `
    <div class="steps-monthly-stat"><span class="monthly-stat-icon">🚶</span><span class="monthly-stat-val">${total.toLocaleString()}</span><span class="monthly-stat-label">Total Steps</span></div>
    <div class="steps-monthly-stat"><span class="monthly-stat-icon">📊</span><span class="monthly-stat-val">${avg.toLocaleString()}</span><span class="monthly-stat-label">Avg/Day</span></div>
    <div class="steps-monthly-stat"><span class="monthly-stat-icon">🏆</span><span class="monthly-stat-val">${best.toLocaleString()}</span><span class="monthly-stat-label">Best Day</span></div>
    <div class="steps-monthly-stat"><span class="monthly-stat-icon">📉</span><span class="monthly-stat-val">${worst.toLocaleString()}</span><span class="monthly-stat-label">Lowest Day</span></div>
    <div class="steps-monthly-stat"><span class="monthly-stat-icon">🎯</span><span class="monthly-stat-val">${goalMet}/${n}</span><span class="monthly-stat-label">Goal Met</span></div>
    <div class="steps-monthly-stat"><span class="monthly-stat-icon">📏</span><span class="monthly-stat-val">${dist > 0 ? dist.toFixed(1) : '—'}</span><span class="monthly-stat-label">KM Walked</span></div>
    <div class="steps-monthly-stat"><span class="monthly-stat-icon">🔥</span><span class="monthly-stat-val">${cal > 0 ? Math.round(cal).toLocaleString() : '—'}</span><span class="monthly-stat-label">Calories</span></div>
    <div class="steps-monthly-stat"><span class="monthly-stat-icon">📅</span><span class="monthly-stat-val">${n}</span><span class="monthly-stat-label">Days</span></div>
  `;
}

// ═══════════════════════════════════════
//  STEPS: TABLE
// ═══════════════════════════════════════
function sortStepsTable(field) {
  if (stepsSortField === field) stepsSortAsc = !stepsSortAsc;
  else { stepsSortField = field; stepsSortAsc = false; }
  document.querySelectorAll('.steps-table th').forEach(th => th.classList.remove('sorted'));
  const th = document.getElementById(`sth-${field}`);
  if (th) { th.classList.add('sorted'); th.querySelector('.sort-arrow').textContent = stepsSortAsc ? '▲' : '▼'; }
  renderStepsTable();
}

function renderStepsTable() {
  const q = (document.getElementById('steps-table-search').value || '').toLowerCase();
  let rows = filteredSteps;
  if (q) rows = rows.filter(r => formatStepsDate(r.date).toLowerCase().includes(q) || r.date.includes(q));
  rows.sort((a,b) => {
    let va, vb;
    switch(stepsSortField) {
      case 'date': va = a.date; vb = b.date; break;
      case 'total_steps': va = a.total_steps||0; vb = b.total_steps||0; break;
      case 'step_goal': va = a.step_goal||0; vb = b.step_goal||0; break;
      case 'goal_pct': va = a.goal_pct||0; vb = b.goal_pct||0; break;
      case 'distance': va = a.distance||0; vb = b.distance||0; break;
      case 'calories_total': va = a.calories_total||0; vb = b.calories_total||0; break;
      default: va = 0; vb = 0;
    }
    return va < vb ? (stepsSortAsc ? -1 : 1) : va > vb ? (stepsSortAsc ? 1 : -1) : 0;
  });
  document.getElementById('steps-table-count').textContent = `${rows.length} days`;
  const tbody = document.getElementById('steps-tbody');
  if (!rows.length) { tbody.innerHTML = '<tr><td colspan="6" style="text-align:center;color:#555;padding:30px;">No data matches</td></tr>'; return; }
  tbody.innerHTML = rows.map(r => {
    const goalPct = r.goal_pct !== null ? r.goal_pct : null;
    const goalClass = goalPct !== null ? getGoalClass(goalPct) : '';
    return `<tr>
      <td class="steps-date">${formatStepsDate(r.date)}</td>
      <td class="steps-count">${(r.total_steps||0).toLocaleString()}</td>
      <td style="color:#888;font-family:'JetBrains Mono',monospace;">${r.step_goal ? r.step_goal.toLocaleString() : '—'}</td>
      <td>${goalPct !== null ? `<span class="goal-badge ${goalClass}">${goalPct}%</span>` : '—'}</td>
      <td style="color:#ccc;font-family:'JetBrains Mono',monospace;">${r.distanceKm ? r.distanceKm + ' km' : '—'}</td>
      <td style="color:#ccc;font-family:'JetBrains Mono',monospace;">${r.calories_total ? Math.round(r.calories_total).toLocaleString() : '—'}</td>
    </tr>`;
  }).join('');
}

// ═══════════════════════════════════════
//  SHARED: TOAST, SYNC, REFRESH
// ═══════════════════════════════════════
function showToast(msg, type='success') {
  const t = document.getElementById('toast');
  t.textContent = msg; t.className = `toast ${type} show`;
  setTimeout(() => t.classList.remove('show'), 3000);
}

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
    allRuns = []; filteredRuns = []; rhrData = [];
    allSteps = []; filteredSteps = [];
    await loadData();
    showToast('✅ Data refreshed!', 'success');
  }
  catch(e) { showToast('❌ Refresh failed', 'error'); }
  finally { btn.classList.remove('loading'); btn.disabled = false; }
}

// ── Init ──
document.addEventListener('DOMContentLoaded', () => {
  loadData();
  document.getElementById('table-search').addEventListener('input', renderRunsTable);
  document.getElementById('steps-table-search').addEventListener('input', renderStepsTable);
  window.addEventListener('resize', () => {
    if (allRuns.length > 0) { renderChart(); renderRhrChart(); }
    if (allSteps.length > 0) renderStepsChart();
  });
});
</script>
