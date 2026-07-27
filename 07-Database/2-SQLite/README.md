## Database Schema

Below is the database table structure for `Shipments` in `store.db`:

<div align="center">

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 750 280" width="100%" style="max-width: 750px; background: #0f172a; border-radius: 12px; font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; box-shadow: 0 10px 25px rgba(0,0,0,0.3);">
  <!-- Header Banner -->
  <rect x="0" y="0" width="750" height="55" rx="12" fill="#1e293b"/>
  <rect x="0" y="45" width="750" height="10" fill="#1e293b"/>
  <circle cx="30" cy="28" r="7" fill="#ef4444"/>
  <circle cx="50" cy="28" r="7" fill="#f59e0b"/>
  <circle cx="70" cy="28" r="7" fill="#10b981"/>
  <text x="375" y="33" fill="#f8fafc" font-size="16" font-weight="700" text-anchor="middle" letter-spacing="0.5">TABLE: Shipments</text>

<!-- Table Headers -->
  <rect x="20" y="70" width="710" height="35" rx="6" fill="#334155"/>
  <text x="50" y="92" fill="#94a3b8" font-size="12" font-weight="700" letter-spacing="1">Id</text>
  <text x="150" y="92" fill="#94a3b8" font-size="12" font-weight="700" letter-spacing="1">Product</text>
  <text x="300" y="92" fill="#94a3b8" font-size="12" font-weight="700" letter-spacing="1">Quantity</text>
  <text x="450" y="92" fill="#94a3b8" font-size="12" font-weight="700" letter-spacing="1">Status</text>
  <text x="600" y="92" fill="#94a3b8" font-size="12" font-weight="700" letter-spacing="1">Price</text>

  <!-- Row 1 (With cell blocks & data placeholders) -->
  <!-- Cell Id -->
  <rect x="20" y="110" width="110" height="30" rx="4" fill="#1e293b" stroke="#334155" stroke-dasharray="2,2"/>
  <text x="50" y="130" fill="#38bdf8" font-size="12" font-weight="600">1</text>

  <!-- Cell Product -->
  <rect x="135" y="110" width="145" height="30" rx="4" fill="#1e293b" stroke="#334155" stroke-dasharray="2,2"/>
  <text x="150" y="130" fill="#f8fafc" font-size="12">Laptop</text>

  <!-- Cell Quantity -->
  <rect x="285" y="110" width="135" height="30" rx="4" fill="#1e293b" stroke="#334155" stroke-dasharray="2,2"/>
  <text x="300" y="130" fill="#f8fafc" font-size="12">2</text>

  <!-- Cell Status -->
  <rect x="425" y="110" width="145" height="30" rx="4" fill="#1e293b" stroke="#334155" stroke-dasharray="2,2"/>
  <text x="450" y="130" fill="#10b981" font-size="12" font-weight="600">Delivered</text>

  <!-- Cell Price -->
  <rect x="575" y="110" width="155" height="30" rx="4" fill="#1e293b" stroke="#334155" stroke-dasharray="2,2"/>
  <text x="600" y="130" fill="#f59e0b" font-size="12">$1,200.00</text>

  <!-- Row 1: id -->
  <text x="40" y="127" fill="#38bdf8" font-size="13" font-weight="600">🔑 id</text>
  <rect x="210" y="113" width="70" height="20" rx="4" fill="#1e293b"/><text x="245" y="127" fill="#38bdf8" font-size="11" text-anchor="middle">INTEGER</text>
  <rect x="350" y="113" width="150" height="20" rx="4" fill="#0369a1"/><text x="425" y="127" fill="#f0f9ff" font-size="10" font-weight="600" text-anchor="middle">PRIMARY KEY AUTOINCREMENT</text>
  <text x="560" y="127" fill="#cbd5e1" font-size="12">Unique shipment identifier</text>
  <line x1="20" y1="142" x2="730" y2="142" stroke="#334155" stroke-width="1"/>

  <!-- Row 2: product -->
  <text x="40" y="162" fill="#f8fafc" font-size="13" font-weight="500">product</text>
  <rect x="210" y="148" width="55" height="20" rx="4" fill="#1e293b"/><text x="237" y="162" fill="#a855f7" font-size="11" text-anchor="middle">TEXT</text>
  <rect x="350" y="148" width="75" height="20" rx="4" fill="#334155"/><text x="387" y="162" fill="#e2e8f0" font-size="10" font-weight="600" text-anchor="middle">NOT NULL</text>
  <text x="560" y="162" fill="#cbd5e1" font-size="12">Name of product</text>
  <line x1="20" y1="177" x2="730" y2="177" stroke="#334155" stroke-width="1"/>

  <!-- Row 3: quantity -->
  <text x="40" y="197" fill="#f8fafc" font-size="13" font-weight="500">quantity</text>
  <rect x="210" y="183" width="70" height="20" rx="4" fill="#1e293b"/><text x="245" y="197" fill="#38bdf8" font-size="11" text-anchor="middle">INTEGER</text>
  <rect x="350" y="183" width="75" height="20" rx="4" fill="#334155"/><text x="387" y="197" fill="#e2e8f0" font-size="10" font-weight="600" text-anchor="middle">NOT NULL</text>
  <text x="560" y="197" fill="#cbd5e1" font-size="12">Number of units (1 - 100)</text>
  <line x1="20" y1="212" x2="730" y2="212" stroke="#334155" stroke-width="1"/>

  <!-- Row 4: status -->
  <text x="40" y="232" fill="#f8fafc" font-size="13" font-weight="500">status</text>
  <rect x="210" y="218" width="55" height="20" rx="4" fill="#1e293b"/><text x="237" y="232" fill="#a855f7" font-size="11" text-anchor="middle">TEXT</text>
  <rect x="350" y="218" width="135" height="20" rx="4" fill="#059669"/><text x="417" y="232" fill="#ecfdf5" font-size="10" font-weight="600" text-anchor="middle">NOT NULL / ENUM</text>
  <text x="560" y="232" fill="#cbd5e1" font-size="12">Current shipment state</text>
  <line x1="20" y1="247" x2="730" y2="247" stroke="#334155" stroke-width="1"/>

  <!-- Row 5: price -->
  <text x="40" y="265" fill="#f8fafc" font-size="13" font-weight="500">price</text>
  <rect x="210" y="251" width="55" height="20" rx="4" fill="#1e293b"/><text x="237" y="265" fill="#f59e0b" font-size="11" text-anchor="middle">REAL</text>
  <rect x="350" y="251" width="75" height="20" rx="4" fill="#334155"/><text x="387" y="265" fill="#e2e8f0" font-size="10" font-weight="600" text-anchor="middle">NOT NULL</text>
  <text x="560" y="265" fill="#cbd5e1" font-size="12">Unit price of item</text>
</svg>

</div>

---

## System Architecture & Data Flow

The diagram below displays how the files interact with each other during API requests:

<div align="center">

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 360" width="100%" style="max-width: 800px; background: #0b1329; border-radius: 12px; font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; box-shadow: 0 10px 25px rgba(0,0,0,0.3);">
  
  <!-- Flow Arrows / Lines -->
  <path d="M 180 180 L 260 180" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="6,4" marker-end="url(#arrow)"/>
  <path d="M 440 130 L 520 85" stroke="#a855f7" stroke-width="2.5" marker-end="url(#arrow)"/>
  <path d="M 440 230 L 520 275" stroke="#10b981" stroke-width="2.5" marker-end="url(#arrow)"/>
  <path d="M 660 275 L 720 275" stroke="#f59e0b" stroke-width="2.5" marker-end="url(#arrow)"/>

  <!-- Markers -->
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#38bdf8"/>
    </marker>
  </defs>

  <!-- Client Box -->
  <g transform="translate(30, 130)">
    <rect width="150" height="100" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="75" y="40" fill="#38bdf8" font-size="14" font-weight="700" text-anchor="middle">HTTP Client</text>
    <text x="75" y="65" fill="#94a3b8" font-size="11" text-anchor="middle">Browser / Scalar / cURL</text>
  </g>

  <!-- main.py Box -->
  <g transform="translate(260, 100)">
    <rect width="180" height="160" rx="10" fill="#1e293b" stroke="#6366f1" stroke-width="2"/>
    <rect x="15" y="15" width="150" height="26" rx="5" fill="#4338ca"/>
    <text x="90" y="32" fill="#ffffff" font-size="13" font-weight="700" text-anchor="middle">main.py</text>
    <text x="90" y="65" fill="#cbd5e1" font-size="11" text-anchor="middle">• FastAPI Router</text>
    <text x="90" y="85" fill="#cbd5e1" font-size="11" text-anchor="middle">• Endpoints Definition</text>
    <text x="90" y="105" fill="#cbd5e1" font-size="11" text-anchor="middle">• HTTP Handlers</text>
    <text x="90" y="125" fill="#cbd5e1" font-size="11" text-anchor="middle">• Scalar Docs Route</text>
  </g>

  <!-- schema.py Box -->
  <g transform="translate(520, 35)">
    <rect width="140" height="100" rx="10" fill="#1e293b" stroke="#a855f7" stroke-width="2"/>
    <rect x="10" y="12" width="120" height="24" rx="5" fill="#6b21a8"/>
    <text x="70" y="28" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">schema.py</text>
    <text x="70" y="58" fill="#cbd5e1" font-size="11" text-anchor="middle">• BaseShipment</text>
    <text x="70" y="75" fill="#cbd5e1" font-size="11" text-anchor="middle">• UpdateShipment</text>
    <text x="70" y="92" fill="#cbd5e1" font-size="11" text-anchor="middle">• ShipmentStatus</text>
  </g>

  <!-- database.py Box -->
  <g transform="translate(520, 225)">
    <rect width="140" height="100" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="2"/>
    <rect x="10" y="12" width="120" height="24" rx="5" fill="#047857"/>
    <text x="70" y="28" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle">database.py</text>
    <text x="70" y="58" fill="#cbd5e1" font-size="11" text-anchor="middle">• Database Class</text>
    <text x="70" y="75" fill="#cbd5e1" font-size="11" text-anchor="middle">• CRUD Methods</text>
    <text x="70" y="92" fill="#cbd5e1" font-size="11" text-anchor="middle">• SQLite Context</text>
  </g>

  <!-- store.db Box -->
  <g transform="translate(700, 240)">
    <rect width="80" height="70" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
    <text x="40" y="32" fill="#f59e0b" font-size="12" font-weight="700" text-anchor="middle">store.db</text>
    <text x="40" y="52" fill="#94a3b8" font-size="10" text-anchor="middle">SQLite DB</text>
  </g>
</svg>

</div>

---

## Quick Start Guide

Follow these steps to run the application locally:
1. Make sure you are in `backend-development-journey` directory

```bash
cd 07-Database/2-SQLite
uvicorn main:app --reload
```