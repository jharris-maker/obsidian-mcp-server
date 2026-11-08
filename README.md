# 🛡️ ObsidianScrub™ & CMMC 2.0 Zero-Trust MCP Server (`obsidian-mcp-server`)

[![MCP Compatible](https://img.shields.io/badge/MCP-Model_Context_Protocol-10b981?style=for-the-badge)](https://modelcontextprotocol.io)
[![CMMC 2.0 Level 2](https://img.shields.io/badge/NIST_SP_800--171-CMMC_2.0_Level_2-d4af37?style=for-the-badge)](https://buy.stripe.com/9B67sMe6ba1TaWz4Zm9ws01)
[![SAM.gov Verified](https://img.shields.io/badge/CAGE_9YGC1-UEI_VX7HZR2UPDT5-38bdf8?style=for-the-badge)](https://obsidianridgedefense.com)

**Deterministic Zero-Trust CUI/PII/Secret Sanitization, NIST SP 800-171 Rev 2 (110-Control) Compliance Auditing, and Smart-Contract / Repository Security Scanning for Claude Desktop, Cursor, Windsurf, and Autonomous Agent Pipelines.**

Built by **Obsidian Ridge Defense Labs · Harris Legacy Venturez LLC** (`SAM.gov UEI: VX7HZR2UPDT5` · `CAGE Code: 9YGC1`).

---

## ⚡ Instant Self-Serve Digital Arsenal & API Keys (30-Second Auto-Delivery)

Need turnkey compliance packages, full repository security audits, or high-volume production API keys right now? Click any link below for **instant checkout and 30-second automated delivery**:

| Product / Service | Price | Instant Worldwide Stripe Checkout |
| :--- | :---: | :--- |
| 🛡️ **Turnkey NIST SP 800-171 / CMMC 2.0 (110-Control) SSP + POA&M + SPRS Pack** | **`$49`** | [**👉 Instant Checkout ($49)**](https://buy.stripe.com/9B67sMe6ba1TaWz4Zm9ws01) |
| 🔍 **5-Minute GitHub Repo Security, Secret & ERC-4626 Invariant Audit + `.patch` Fix** | **`$99`** | [**👉 Instant Checkout ($99)**](https://buy.stripe.com/dRm28s1jp3DvaWz0J69ws05) |
| 📋 **Section 889 & NDAA FY2026 Supply-Chain Telemetry Audit Kit** | **`$99`** | [**👉 Instant Checkout ($99)**](https://buy.stripe.com/fZueVe9PVde56Gj3Vi9ws02) |
| 🔐 **ObsidianScrub™ Zero-Trust CUI/PII/Secret Sanitizer MCP & API Key (`10K calls/mo`)** | **`$149`** | [**👉 Instant Checkout ($149)**](https://buy.stripe.com/aFa28saTZ2zr3u70J69ws06) |
| 🐳 **Air-Gapped Zero-Trust RAG & Local LLM Docker Deployment Blueprint** | **`$149`** | [**👉 Instant Checkout ($149)**](https://buy.stripe.com/fZu14o1jp1vn7KnezW9ws03) |
| 🛰️ **NVIDIA Cosmos + Isaac Lab Annotated Synthetic Edge-Case Dataset Pack (`10K frames`)** | **`$299`** | [**👉 Instant Checkout ($299)**](https://buy.stripe.com/8x200k8LRa1TggT4Zm9ws07) |
| 🚀 **DoD SBIR / STTR Phase I & BAA Technical Volume Blueprint Pack** | **`$299`** | [**👉 Instant Checkout ($299)**](https://buy.stripe.com/28E5kE7HNfmdc0DgI49ws04) |
| 🏛️ **7-Day Dedicated Sovereign Enclave Benchmark (`FAR 13.201` P-Card / Corp Card)** | **`$2,500`** | [**👉 Instant Checkout ($2,500)**](https://buy.stripe.com/28E5kEd27a1TfcPajG9ws00) |

---

## 🛠️ MCP Tools Included

1. **`scrub_cui_and_secrets(text)`**
   - Deterministically redacts Controlled Unclassified Information (`CUI`), SSNs, API keys (`sk_live_`, `ghp_`, AWS AKIA), JWTs, emails, and defense contract identifiers before prompts leave your perimeter, returning a cryptographic `SHA-256` audit receipt.
2. **`calculate_sprs_cmmc_score(implemented_controls_count)`**
   - Computes your official DoD Supplier Performance Risk System (`SPRS`) score (`-203` to `+110`) across all 110 NIST SP 800-171 Rev 2 controls and maps required POA&M remediation items.
3. **`audit_code_security_invariants(code_snippet, language)`**
   - Runs static pattern & invariant checks for hardcoded credentials, SQL/command injection, CEI reentrancy, and ERC-4626 vault share rounding vulnerabilities.
4. **`get_compliance_arsenal_links(sku)`**
   - Returns direct self-serve checkout links for instant CMMC/NDAA/Zero-Trust engineering bundles.

---

## 🚀 Quickstart (Claude Desktop / Cursor / Smithery)

Add to your `claude_desktop_config.json` or `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "obsidian-security": {
      "command": "python",
      "args": ["server.py"],
      "env": {
        "OBSIDIAN_API_KEY": "free-tier-preview"
      }
    }
  }
}
```
