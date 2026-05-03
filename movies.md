---
layout: page
title: Movies
subtitle: IMDB Top 100 — My Watchlist
---

<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">

<style>
  /* RESET */
  .container-md, .container {
    max-width: 100% !important;
    width: 100% !important;
    padding: 0 !important;
    margin: 0 !important;
  }

  .movies-app {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    background: #0a0a0f;
    color: #e0e0e0;
    min-height: 100vh;
    padding: 0 20px 60px;
  }

  /* HERO HEADER */
  .hero {
    text-align: center;
    padding: 50px 20px 30px;
    position: relative;
    overflow: hidden;
  }
  .hero::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(ellipse at center, rgba(255,215,0,0.06) 0%, transparent 60%);
    pointer-events: none;
  }
  .hero-title {
    font-size: 2.8rem;
    font-weight: 900;
    background: linear-gradient(135deg, #FFD700, #FFA500, #FFD700);
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

  /* STATS BAR */
  .stats-bar {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 30px;
    margin: 30px auto 20px;
    max-width: 700px;
    flex-wrap: wrap;
  }
  .stat-item {
    text-align: center;
  }
  .stat-number {
    font-size: 2rem;
    font-weight: 800;
    color: #FFD700;
    display: block;
    line-height: 1;
  }
  .stat-label {
    font-size: 0.75rem;
    color: #666;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-top: 4px;
  }
  .stat-divider {
    width: 1px;
    height: 40px;
    background: #222;
  }

  /* PROGRESS BAR */
  .progress-container {
    max-width: 700px;
    margin: 0 auto 30px;
  }
  .progress-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 8px;
  }
  .progress-text {
    font-size: 0.85rem;
    color: #888;
    font-weight: 500;
  }
  .progress-pct {
    font-size: 0.85rem;
    color: #FFD700;
    font-weight: 700;
    font-family: 'JetBrains Mono', monospace;
  }
  .progress-track {
    width: 100%;
    height: 6px;
    background: #1a1a24;
    border-radius: 3px;
    overflow: hidden;
  }
  .progress-fill {
    height: 100%;
    background: linear-gradient(90deg, #FFD700, #FFA500);
    border-radius: 3px;
    transition: width 0.6s cubic-bezier(0.16, 1, 0.3, 1);
    width: 0%;
    box-shadow: 0 0 12px rgba(255,215,0,0.3);
  }

  /* SEARCH */
  .search-container {
    max-width: 700px;
    margin: 0 auto 30px;
    position: relative;
  }
  .search-icon {
    position: absolute;
    left: 16px;
    top: 50%;
    transform: translateY(-50%);
    color: #555;
    font-size: 1rem;
    pointer-events: none;
  }
  .search-input {
    width: 100%;
    padding: 14px 16px 14px 44px;
    background: #111118;
    border: 1px solid #222;
    border-radius: 12px;
    color: #fff;
    font-size: 0.95rem;
    font-family: 'Inter', sans-serif;
    outline: none;
    transition: all 0.3s;
    box-sizing: border-box;
  }
  .search-input::placeholder { color: #444; }
  .search-input:focus {
    border-color: #FFD700;
    box-shadow: 0 0 0 3px rgba(255,215,0,0.1);
  }

  /* FILTER TABS */
  .filter-tabs {
    display: flex;
    justify-content: center;
    gap: 8px;
    margin-bottom: 30px;
    flex-wrap: wrap;
  }
  .filter-tab {
    padding: 8px 20px;
    background: #111118;
    border: 1px solid #222;
    border-radius: 20px;
    color: #888;
    font-size: 0.8rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s;
    user-select: none;
    font-family: 'Inter', sans-serif;
  }
  .filter-tab:hover { border-color: #444; color: #ccc; }
  .filter-tab.active {
    background: linear-gradient(135deg, rgba(255,215,0,0.15), rgba(255,165,0,0.1));
    border-color: #FFD700;
    color: #FFD700;
  }

  /* MOVIE GRID */
  .movie-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
    gap: 16px;
    max-width: 1400px;
    margin: 0 auto;
  }
  @media (max-width: 600px) {
    .movie-grid { grid-template-columns: 1fr; }
    .hero-title { font-size: 2rem; }
  }

  /* MOVIE CARD */
  .movie-card {
    background: #111118;
    border: 1px solid #1a1a24;
    border-radius: 12px;
    padding: 18px 20px;
    display: flex;
    align-items: center;
    gap: 16px;
    cursor: pointer;
    transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    position: relative;
    overflow: hidden;
    user-select: none;
  }
  .movie-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: linear-gradient(135deg, rgba(255,215,0,0.03), transparent);
    opacity: 0;
    transition: opacity 0.3s;
  }
  .movie-card:hover {
    border-color: #2a2a36;
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(0,0,0,0.3);
  }
  .movie-card:hover::before { opacity: 1; }

  .movie-card.watched {
    border-color: rgba(255,215,0,0.2);
    background: linear-gradient(135deg, #111118, #14141e);
  }
  .movie-card.watched .movie-rank {
    background: linear-gradient(135deg, #FFD700, #FFA500);
    color: #000;
  }

  /* RANK BADGE */
  .movie-rank {
    flex-shrink: 0;
    width: 42px;
    height: 42px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 10px;
    font-weight: 800;
    font-size: 0.9rem;
    background: #1a1a24;
    color: #555;
    transition: all 0.3s;
    font-family: 'JetBrains Mono', monospace;
    position: relative;
    z-index: 1;
  }

  /* MOVIE INFO */
  .movie-info {
    flex: 1;
    min-width: 0;
    position: relative;
    z-index: 1;
  }
  .movie-title {
    font-weight: 700;
    font-size: 0.95rem;
    color: #eee;
    margin: 0 0 4px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    transition: color 0.3s;
  }
  .movie-card.watched .movie-title {
    color: #FFD700;
  }
  .movie-meta {
    display: flex;
    align-items: center;
    gap: 10px;
    flex-wrap: wrap;
  }
  .movie-year {
    font-size: 0.8rem;
    color: #666;
    font-weight: 500;
  }
  .movie-director {
    font-size: 0.75rem;
    color: #555;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    max-width: 150px;
  }
  .movie-rating {
    font-size: 0.75rem;
    font-weight: 700;
    color: #FFD700;
    background: rgba(255,215,0,0.1);
    padding: 2px 8px;
    border-radius: 6px;
    font-family: 'JetBrains Mono', monospace;
  }

  /* CHECKBOX */
  .check-area {
    flex-shrink: 0;
    position: relative;
    z-index: 1;
  }
  .check-box {
    width: 28px;
    height: 28px;
    border-radius: 8px;
    border: 2px solid #333;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.3s;
    background: transparent;
  }
  .movie-card.watched .check-box {
    border-color: #FFD700;
    background: linear-gradient(135deg, #FFD700, #FFA500);
  }
  .check-box svg {
    width: 16px;
    height: 16px;
    opacity: 0;
    transform: scale(0.5);
    transition: all 0.3s;
  }
  .movie-card.watched .check-box svg {
    opacity: 1;
    transform: scale(1);
  }

  /* EMPTY STATE */
  .empty-state {
    text-align: center;
    padding: 60px 20px;
    color: #444;
  }
  .empty-state-icon {
    font-size: 3rem;
    margin-bottom: 16px;
  }

  /* TOAST */
  .toast {
    position: fixed;
    bottom: 30px;
    left: 50%;
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
  .toast.error { border-color: #9b2c2c; }
  .toast.success { border-color: #FFD700; }

  /* LOADING */
  .loading-overlay {
    text-align: center;
    padding: 80px 20px;
  }
  .spinner {
    width: 40px;
    height: 40px;
    border: 3px solid #222;
    border-top-color: #FFD700;
    border-radius: 50%;
    animation: spin 0.8s linear infinite;
    margin: 0 auto 20px;
  }
  @keyframes spin { to { transform: rotate(360deg); } }
  .loading-text {
    color: #555;
    font-size: 0.9rem;
  }

  /* Connection indicator */
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
    background: rgba(72,187,120,0.1);
    color: #48bb78;
    border: 1px solid rgba(72,187,120,0.2);
  }
  .connection-badge.offline {
    background: rgba(245,101,101,0.1);
    color: #f56565;
    border: 1px solid rgba(245,101,101,0.2);
  }
  .connection-dot {
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: currentColor;
    animation: pulse-dot 2s infinite;
  }
  @keyframes pulse-dot {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.4; }
  }
</style>

<div class="movies-app" id="movies-app">

  <!-- HERO -->
  <div class="hero">
    <h1 class="hero-title">🎬 IMDB Top 100</h1>
    <p class="hero-sub">The greatest films ever made — track your journey</p>
    <div class="connection-badge offline" id="connection-badge">
      <span class="connection-dot"></span>
      <span id="connection-text">Connecting...</span>
    </div>
  </div>

  <!-- STATS -->
  <div class="stats-bar">
    <div class="stat-item">
      <span class="stat-number" id="watched-count">0</span>
      <span class="stat-label">Watched</span>
    </div>
    <div class="stat-divider"></div>
    <div class="stat-item">
      <span class="stat-number" id="remaining-count">100</span>
      <span class="stat-label">Remaining</span>
    </div>
    <div class="stat-divider"></div>
    <div class="stat-item">
      <span class="stat-number" id="pct-count">0%</span>
      <span class="stat-label">Complete</span>
    </div>
  </div>

  <!-- PROGRESS -->
  <div class="progress-container">
    <div class="progress-header">
      <span class="progress-text">Progress</span>
      <span class="progress-pct" id="progress-label">0 / 100</span>
    </div>
    <div class="progress-track">
      <div class="progress-fill" id="progress-fill"></div>
    </div>
  </div>

  <!-- SEARCH -->
  <div class="search-container">
    <span class="search-icon">🔍</span>
    <input type="text" class="search-input" id="search-input" placeholder="Search movies, directors, years...">
  </div>

  <!-- FILTERS -->
  <div class="filter-tabs">
    <button class="filter-tab active" data-filter="all" onclick="setFilter('all')">All (100)</button>
    <button class="filter-tab" data-filter="watched" onclick="setFilter('watched')">✓ Watched</button>
    <button class="filter-tab" data-filter="unwatched" onclick="setFilter('unwatched')">○ Unwatched</button>
  </div>

  <!-- MOVIE GRID -->
  <div class="movie-grid" id="movie-grid"></div>

  <!-- EMPTY STATE -->
  <div class="empty-state" id="empty-state" style="display:none;">
    <div class="empty-state-icon">🎞️</div>
    <p>No movies match your search</p>
  </div>

</div>

<!-- TOAST -->
<div class="toast" id="toast"></div>

<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/dist/umd/supabase.min.js"></script>

<script>
// ========== SUPABASE CONFIG ==========
const SUPABASE_URL = 'https://uuzrzcnvieygjlihgwnb.supabase.co';
const SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InV1enJ6Y252aWV5Z2psaWhnd25iIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Nzc4MDE3OTEsImV4cCI6MjA5MzM3Nzc5MX0._LP_f3WtKPVEvVCG1Uqh5S5ARHSHF7maopdWIbWg7Mw';

const supabaseClient = supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);

// ========== IMDB TOP 100 MOVIES ==========
const MOVIES = [
  { rank: 1, title: "The Shawshank Redemption", year: 1994, director: "Frank Darabont", rating: 9.3 },
  { rank: 2, title: "The Godfather", year: 1972, director: "Francis Ford Coppola", rating: 9.2 },
  { rank: 3, title: "The Dark Knight", year: 2008, director: "Christopher Nolan", rating: 9.0 },
  { rank: 4, title: "The Godfather Part II", year: 1974, director: "Francis Ford Coppola", rating: 9.0 },
  { rank: 5, title: "12 Angry Men", year: 1957, director: "Sidney Lumet", rating: 9.0 },
  { rank: 6, title: "Schindler's List", year: 1993, director: "Steven Spielberg", rating: 9.0 },
  { rank: 7, title: "The Lord of the Rings: The Return of the King", year: 2003, director: "Peter Jackson", rating: 9.0 },
  { rank: 8, title: "Pulp Fiction", year: 1994, director: "Quentin Tarantino", rating: 8.9 },
  { rank: 9, title: "The Lord of the Rings: The Fellowship of the Ring", year: 2001, director: "Peter Jackson", rating: 8.9 },
  { rank: 10, title: "The Good, the Bad and the Ugly", year: 1966, director: "Sergio Leone", rating: 8.8 },
  { rank: 11, title: "Forrest Gump", year: 1994, director: "Robert Zemeckis", rating: 8.8 },
  { rank: 12, title: "Fight Club", year: 1999, director: "David Fincher", rating: 8.8 },
  { rank: 13, title: "The Lord of the Rings: The Two Towers", year: 2002, director: "Peter Jackson", rating: 8.8 },
  { rank: 14, title: "Inception", year: 2010, director: "Christopher Nolan", rating: 8.8 },
  { rank: 15, title: "Star Wars: Episode V - The Empire Strikes Back", year: 1980, director: "Irvin Kershner", rating: 8.7 },
  { rank: 16, title: "The Matrix", year: 1999, director: "The Wachowskis", rating: 8.7 },
  { rank: 17, title: "Goodfellas", year: 1990, director: "Martin Scorsese", rating: 8.7 },
  { rank: 18, title: "One Flew Over the Cuckoo's Nest", year: 1975, director: "Milos Forman", rating: 8.7 },
  { rank: 19, title: "Se7en", year: 1995, director: "David Fincher", rating: 8.6 },
  { rank: 20, title: "Seven Samurai", year: 1954, director: "Akira Kurosawa", rating: 8.6 },
  { rank: 21, title: "It's a Wonderful Life", year: 1946, director: "Frank Capra", rating: 8.6 },
  { rank: 22, title: "The Silence of the Lambs", year: 1991, director: "Jonathan Demme", rating: 8.6 },
  { rank: 23, title: "Saving Private Ryan", year: 1998, director: "Steven Spielberg", rating: 8.6 },
  { rank: 24, title: "City of God", year: 2002, director: "Fernando Meirelles", rating: 8.6 },
  { rank: 25, title: "Interstellar", year: 2014, director: "Christopher Nolan", rating: 8.7 },
  { rank: 26, title: "Life Is Beautiful", year: 1997, director: "Roberto Benigni", rating: 8.6 },
  { rank: 27, title: "The Usual Suspects", year: 1995, director: "Bryan Singer", rating: 8.5 },
  { rank: 28, title: "Spirited Away", year: 2001, director: "Hayao Miyazaki", rating: 8.6 },
  { rank: 29, title: "Léon: The Professional", year: 1994, director: "Luc Besson", rating: 8.5 },
  { rank: 30, title: "The Green Mile", year: 1999, director: "Frank Darabont", rating: 8.6 },
  { rank: 31, title: "Hara-Kiri", year: 1962, director: "Masaki Kobayashi", rating: 8.6 },
  { rank: 32, title: "The Pianist", year: 2002, director: "Roman Polanski", rating: 8.5 },
  { rank: 33, title: "Terminator 2: Judgment Day", year: 1991, director: "James Cameron", rating: 8.6 },
  { rank: 34, title: "Back to the Future", year: 1985, director: "Robert Zemeckis", rating: 8.5 },
  { rank: 35, title: "Whiplash", year: 2014, director: "Damien Chazelle", rating: 8.5 },
  { rank: 36, title: "Psycho", year: 1960, director: "Alfred Hitchcock", rating: 8.5 },
  { rank: 37, title: "The Lion King", year: 1994, director: "Roger Allers", rating: 8.5 },
  { rank: 38, title: "Gladiator", year: 2000, director: "Ridley Scott", rating: 8.5 },
  { rank: 39, title: "American History X", year: 1998, director: "Tony Kaye", rating: 8.5 },
  { rank: 40, title: "The Departed", year: 2006, director: "Martin Scorsese", rating: 8.5 },
  { rank: 41, title: "The Prestige", year: 2006, director: "Christopher Nolan", rating: 8.5 },
  { rank: 42, title: "Casablanca", year: 1942, director: "Michael Curtiz", rating: 8.5 },
  { rank: 43, title: "Grave of the Fireflies", year: 1988, director: "Isao Takahata", rating: 8.5 },
  { rank: 44, title: "Rear Window", year: 1954, director: "Alfred Hitchcock", rating: 8.5 },
  { rank: 45, title: "Alien", year: 1979, director: "Ridley Scott", rating: 8.5 },
  { rank: 46, title: "Cinema Paradiso", year: 1988, director: "Giuseppe Tornatore", rating: 8.5 },
  { rank: 47, title: "Apocalypse Now", year: 1979, director: "Francis Ford Coppola", rating: 8.4 },
  { rank: 48, title: "Memento", year: 2000, director: "Christopher Nolan", rating: 8.4 },
  { rank: 49, title: "The Great Dictator", year: 1940, director: "Charlie Chaplin", rating: 8.4 },
  { rank: 50, title: "Django Unchained", year: 2012, director: "Quentin Tarantino", rating: 8.5 },
  { rank: 51, title: "The Lives of Others", year: 2006, director: "Florian Henckel von Donnersmarck", rating: 8.4 },
  { rank: 52, title: "Paths of Glory", year: 1957, director: "Stanley Kubrick", rating: 8.4 },
  { rank: 53, title: "WALL·E", year: 2008, director: "Andrew Stanton", rating: 8.4 },
  { rank: 54, title: "Sunset Boulevard", year: 1950, director: "Billy Wilder", rating: 8.4 },
  { rank: 55, title: "The Shining", year: 1980, director: "Stanley Kubrick", rating: 8.4 },
  { rank: 56, title: "Witness for the Prosecution", year: 1957, director: "Billy Wilder", rating: 8.4 },
  { rank: 57, title: "Princess Mononoke", year: 1997, director: "Hayao Miyazaki", rating: 8.4 },
  { rank: 58, title: "Oldboy", year: 2003, director: "Park Chan-wook", rating: 8.4 },
  { rank: 59, title: "Spider-Man: Into the Spider-Verse", year: 2018, director: "Bob Persichetti", rating: 8.4 },
  { rank: 60, title: "Aliens", year: 1986, director: "James Cameron", rating: 8.4 },
  { rank: 61, title: "Dr. Strangelove", year: 1964, director: "Stanley Kubrick", rating: 8.4 },
  { rank: 62, title: "Once Upon a Time in the West", year: 1968, director: "Sergio Leone", rating: 8.4 },
  { rank: 63, title: "American Beauty", year: 1999, director: "Sam Mendes", rating: 8.3 },
  { rank: 64, title: "Darkest Hour", year: 2017, director: "Joe Wright", rating: 7.4 },
  { rank: 65, title: "The Dark Knight Rises", year: 2012, director: "Christopher Nolan", rating: 8.4 },
  { rank: 66, title: "Parasite", year: 2019, director: "Bong Joon-ho", rating: 8.5 },
  { rank: 67, title: "Avengers: Endgame", year: 2019, director: "Anthony Russo", rating: 8.4 },
  { rank: 68, title: "Joker", year: 2019, director: "Todd Phillips", rating: 8.4 },
  { rank: 69, title: "Your Name", year: 2016, director: "Makoto Shinkai", rating: 8.4 },
  { rank: 70, title: "Coco", year: 2017, director: "Lee Unkrich", rating: 8.4 },
  { rank: 71, title: "The Intouchables", year: 2011, director: "Olivier Nakache", rating: 8.5 },
  { rank: 72, title: "Modern Times", year: 1936, director: "Charlie Chaplin", rating: 8.5 },
  { rank: 73, title: "Toy Story", year: 1995, director: "John Lasseter", rating: 8.3 },
  { rank: 74, title: "Amadeus", year: 1984, director: "Milos Forman", rating: 8.4 },
  { rank: 75, title: "2001: A Space Odyssey", year: 1968, director: "Stanley Kubrick", rating: 8.3 },
  { rank: 76, title: "Full Metal Jacket", year: 1987, director: "Stanley Kubrick", rating: 8.3 },
  { rank: 77, title: "Braveheart", year: 1995, director: "Mel Gibson", rating: 8.4 },
  { rank: 78, title: "Reservoir Dogs", year: 1992, director: "Quentin Tarantino", rating: 8.3 },
  { rank: 79, title: "A Clockwork Orange", year: 1971, director: "Stanley Kubrick", rating: 8.3 },
  { rank: 80, title: "Requiem for a Dream", year: 2000, director: "Darren Aronofsky", rating: 8.3 },
  { rank: 81, title: "3 Idiots", year: 2009, director: "Rajkumar Hirani", rating: 8.4 },
  { rank: 82, title: "Eternal Sunshine of the Spotless Mind", year: 2004, director: "Michel Gondry", rating: 8.3 },
  { rank: 83, title: "The Hunt", year: 2012, director: "Thomas Vinterberg", rating: 8.3 },
  { rank: 84, title: "Singin' in the Rain", year: 1952, director: "Gene Kelly", rating: 8.3 },
  { rank: 85, title: "Toy Story 3", year: 2010, director: "Lee Unkrich", rating: 8.3 },
  { rank: 86, title: "Star Wars: Episode IV - A New Hope", year: 1977, director: "George Lucas", rating: 8.6 },
  { rank: 87, title: "Ikiru", year: 1952, director: "Akira Kurosawa", rating: 8.3 },
  { rank: 88, title: "Good Will Hunting", year: 1997, director: "Gus Van Sant", rating: 8.3 },
  { rank: 89, title: "North by Northwest", year: 1959, director: "Alfred Hitchcock", rating: 8.3 },
  { rank: 90, title: "Come and See", year: 1985, director: "Elem Klimov", rating: 8.4 },
  { rank: 91, title: "Dangal", year: 2016, director: "Nitesh Tiwari", rating: 8.3 },
  { rank: 92, title: "Inglourious Basterds", year: 2009, director: "Quentin Tarantino", rating: 8.4 },
  { rank: 93, title: "The Kid", year: 1921, director: "Charlie Chaplin", rating: 8.3 },
  { rank: 94, title: "The Father", year: 2020, director: "Florian Zeller", rating: 8.3 },
  { rank: 95, title: "Vertigo", year: 1958, director: "Alfred Hitchcock", rating: 8.3 },
  { rank: 96, title: "Capernaum", year: 2018, director: "Nadine Labaki", rating: 8.4 },
  { rank: 97, title: "1917", year: 2019, director: "Sam Mendes", rating: 8.3 },
  { rank: 98, title: "Hamilton", year: 2020, director: "Thomas Kail", rating: 8.3 },
  { rank: 99, title: "Metropolis", year: 1927, director: "Fritz Lang", rating: 8.3 },
  { rank: 100, title: "M", year: 1931, director: "Fritz Lang", rating: 8.3 }
];

// ========== STATE ==========
let watchedSet = new Set();
let currentFilter = 'all';
let searchQuery = '';
let dbConnected = false;

// ========== INIT ==========
async function init() {
  renderMovies();
  await loadWatchedFromDB();
  document.getElementById('search-input').addEventListener('input', (e) => {
    searchQuery = e.target.value.toLowerCase();
    renderMovies();
  });
}

// ========== SUPABASE OPERATIONS ==========
async function loadWatchedFromDB() {
  try {
    const { data, error } = await supabaseClient
      .from('watched_movies')
      .select('movie_rank, watched')
      .eq('watched', true);

    if (error) throw error;

    watchedSet.clear();
    if (data) {
      data.forEach(row => watchedSet.add(row.movie_rank));
    }

    dbConnected = true;
    updateConnectionBadge(true);
    renderMovies();
    updateStats();
  } catch (err) {
    console.error('DB load error:', err);
    dbConnected = false;
    updateConnectionBadge(false);
    showToast('⚠️ Could not connect to database', 'error');
  }
}

async function toggleWatched(rank) {
  const isWatched = watchedSet.has(rank);
  if (isWatched) {
    watchedSet.delete(rank);
  } else {
    watchedSet.add(rank);
  }

  // Update UI immediately
  updateCardUI(rank);
  updateStats();

  // Persist to DB
  if (dbConnected) {
    try {
      const { error } = await supabaseClient
        .from('watched_movies')
        .upsert({ movie_rank: rank, watched: !isWatched, updated_at: new Date().toISOString() },
                 { onConflict: 'movie_rank' });

      if (error) throw error;
    } catch (err) {
      console.error('DB save error:', err);
      // Revert on failure
      if (isWatched) watchedSet.add(rank);
      else watchedSet.delete(rank);
      updateCardUI(rank);
      updateStats();
      showToast('⚠️ Failed to save — please try again', 'error');
    }
  }
}

// ========== RENDERING ==========
function renderMovies() {
  const grid = document.getElementById('movie-grid');
  const empty = document.getElementById('empty-state');

  let filtered = MOVIES.filter(m => {
    if (currentFilter === 'watched' && !watchedSet.has(m.rank)) return false;
    if (currentFilter === 'unwatched' && watchedSet.has(m.rank)) return false;
    if (searchQuery) {
      const q = searchQuery;
      return (
        m.title.toLowerCase().includes(q) ||
        m.director.toLowerCase().includes(q) ||
        String(m.year).includes(q) ||
        String(m.rank).includes(q)
      );
    }
    return true;
  });

  if (filtered.length === 0) {
    grid.innerHTML = '';
    empty.style.display = 'block';
    return;
  }
  empty.style.display = 'none';

  grid.innerHTML = filtered.map(m => {
    const isWatched = watchedSet.has(m.rank);
    return `
      <div class="movie-card ${isWatched ? 'watched' : ''}"
           id="card-${m.rank}"
           onclick="toggleWatched(${m.rank})">
        <div class="movie-rank">${m.rank}</div>
        <div class="movie-info">
          <div class="movie-title" title="${m.title}">${m.title}</div>
          <div class="movie-meta">
            <span class="movie-year">${m.year}</span>
            <span class="movie-director">${m.director}</span>
            <span class="movie-rating">⭐ ${m.rating}</span>
          </div>
        </div>
        <div class="check-area">
          <div class="check-box">
            <svg viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="20 6 9 17 4 12"></polyline>
            </svg>
          </div>
        </div>
      </div>
    `;
  }).join('');
}

function updateCardUI(rank) {
  const card = document.getElementById(`card-${rank}`);
  if (!card) return;
  if (watchedSet.has(rank)) {
    card.classList.add('watched');
  } else {
    card.classList.remove('watched');
  }
}

function updateStats() {
  const watched = watchedSet.size;
  const total = MOVIES.length;
  const remaining = total - watched;
  const pct = Math.round((watched / total) * 100);

  document.getElementById('watched-count').textContent = watched;
  document.getElementById('remaining-count').textContent = remaining;
  document.getElementById('pct-count').textContent = pct + '%';
  document.getElementById('progress-label').textContent = `${watched} / ${total}`;
  document.getElementById('progress-fill').style.width = pct + '%';

  // Update filter tab counts
  document.querySelector('[data-filter="all"]').textContent = `All (${total})`;
  document.querySelector('[data-filter="watched"]').textContent = `✓ Watched (${watched})`;
  document.querySelector('[data-filter="unwatched"]').textContent = `○ Unwatched (${remaining})`;
}

function updateConnectionBadge(online) {
  const badge = document.getElementById('connection-badge');
  const text = document.getElementById('connection-text');
  if (online) {
    badge.className = 'connection-badge online';
    text.textContent = 'Cloud Synced';
  } else {
    badge.className = 'connection-badge offline';
    text.textContent = 'Offline Mode';
  }
}

// ========== FILTERS ==========
function setFilter(filter) {
  currentFilter = filter;
  document.querySelectorAll('.filter-tab').forEach(tab => {
    tab.classList.toggle('active', tab.getAttribute('data-filter') === filter);
  });
  renderMovies();
}

// ========== TOAST ==========
function showToast(message, type = 'success') {
  const toast = document.getElementById('toast');
  toast.textContent = message;
  toast.className = `toast ${type} show`;
  setTimeout(() => { toast.classList.remove('show'); }, 3000);
}

// ========== START ==========
init();
</script>
