#!/usr/bin/env python3
"""
ObsidianScrub & CMMC 2.0 Zero-Trust Security MCP Server (JSON-RPC 2.0 over stdio).
Built by Obsidian Ridge Defense Labs · Harris Legacy Venturez LLC (CAGE: 9YGC1 · UEI: VX7HZR2UPDT5).
"""
import sys
import json
import re
import hashlib

ARSENAL_LINKS = {
    "cmmc-ssp-49": {
        "name": "Turnkey NIST SP 800-171 / CMMC 2.0 (110-Control) SSP + POA&M + SPRS Pack",
        "price_usd": 49,
        "checkout_url": "https://buy.stripe.com/9B67sMe6ba1TaWz4Zm9ws01",
    },
    "repo-audit-99": {
        "name": "5-Minute GitHub Repo Security, Secret & ERC-4626 Invariant Audit + .patch Fix",
        "price_usd": 99,
        "checkout_url": "https://buy.stripe.com/dRm28s1jp3DvaWz0J69ws05",
    },
    "ndaa-audit-99": {
        "name": "Section 889 & NDAA FY2026 Supply-Chain Telemetry Audit Kit",
        "price_usd": 99,
        "checkout_url": "https://buy.stripe.com/fZueVe9PVde56Gj3Vi9ws02",
    },
    "obsidianscrub-149": {
        "name": "ObsidianScrub Zero-Trust CUI/PII/Secret Sanitizer MCP & API Key (10K calls/mo)",
        "price_usd": 149,
        "checkout_url": "https://buy.stripe.com/aFa28saTZ2zr3u70J69ws06",
    },
    "zero-trust-149": {
        "name": "Air-Gapped Zero-Trust RAG & Local LLM Docker Deployment Blueprint",
        "price_usd": 149,
        "checkout_url": "https://buy.stripe.com/fZu14o1jp1vn7KnezW9ws03",
    },
    "cosmos-pack-299": {
        "name": "NVIDIA Cosmos + Isaac Lab Annotated Synthetic Edge-Case Dataset Pack",
        "price_usd": 299,
        "checkout_url": "https://buy.stripe.com/8x200k8LRa1TggT4Zm9ws07",
    },
    "sbir-grant-299": {
        "name": "DoD SBIR / STTR Phase I & BAA Technical Volume Blueprint Pack",
        "price_usd": 299,
        "checkout_url": "https://buy.stripe.com/28E5kE7HNfmdc0DgI49ws04",
    },
    "enclave-2500": {
        "name": "7-Day Dedicated Sovereign Enclave Benchmark (FAR 13.201 P-Card / Corp Card)",
        "price_usd": 2500,
        "checkout_url": "https://buy.stripe.com/28E5kEd27a1TfcPajG9ws00",
    },
}

PATTERNS = [
    ("API_SECRET_KEY", re.compile(r"\b(?:sk_live_|rk_live_|ghp_|github_pat_|AKIA)[A-Za-z0-9_\-]{12,}\b")),
    ("SSN", re.compile(r"\b\d{3}-\d{2}-\d{4}\b")),
    ("EMAIL", re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")),
    ("IPV4_INTERNAL", re.compile(r"\b(?:10\.\d{1,3}|192\.168|172\.(?:1[6-9]|2\d|3[01]))\.\d{1,3}\.\d{1,3}\b")),
]

def scrub_cui_and_secrets(text: str) -> dict:
    sanitized = str(text or "")
    redactions = []
    for label, pat in PATTERNS:
        matches = pat.findall(sanitized)
        if matches:
            redactions.append({"type": label, "count": len(matches)})
            sanitized = pat.sub(f"<REDACTED_{label}>", sanitized)
    receipt_sha = hashlib.sha256(sanitized.encode("utf-8")).hexdigest()
    return {
        "sanitized_text": sanitized,
        "redactions": redactions,
        "sha256_receipt": receipt_sha,
        "upgrade_unlimited_api_key_url": "https://buy.stripe.com/aFa28saTZ2zr3u70J69ws06",
    }

def calculate_sprs_cmmc_score(implemented_controls: int = 85) -> dict:
    implemented = max(0, min(110, int(implemented_controls)))
    missing = 110 - implemented
    # Official DoD SPRS weighting approximation (-203 to +110)
    estimated_sprs = 110 - (missing * 3)
    return {
        "total_nist_800_171_controls": 110,
        "implemented_controls": implemented,
        "missing_controls": missing,
        "estimated_sprs_score": max(-203, estimated_sprs),
        "cmmc_level_2_ready": missing == 0,
        "turnkey_110_control_ssp_poam_pack_49_url": "https://buy.stripe.com/9B67sMe6ba1TaWz4Zm9ws01",
        "section_889_supply_chain_kit_99_url": "https://buy.stripe.com/fZueVe9PVde56Gj3Vi9ws02",
    }

def audit_code_security_invariants(code_snippet: str) -> dict:
    code = str(code_snippet or "")
    findings = []
    if re.search(r"(?:sk_live_|ghp_|AKIA|password\s*=\s*['\"][^'\"]+['\"])", code, re.I):
        findings.append("HIGH: Potential hardcoded credential or API secret detected.")
    if "subprocess.Popen" in code and "shell=True" in code:
        findings.append("HIGH: Command injection vector via shell=True.")
    if ".call{value:" in code:
        findings.append("CRITICAL: Potential Solidity CEI reentrancy vector on external value call.")
    return {
        "findings_count": len(findings),
        "findings": findings or ["PASS: No obvious static secret or CEI reentrancy patterns in snippet."],
        "full_repo_audit_and_patch_99_url": "https://buy.stripe.com/dRm28s1jp3DvaWz0J69ws05",
    }

TOOLS_SPEC = [
    {
        "name": "scrub_cui_and_secrets",
        "description": "Deterministically redact CUI, PII, SSNs, and API secrets from text with a SHA-256 receipt.",
        "inputSchema": {
            "type": "object",
            "properties": {"text": {"type": "string"}},
            "required": ["text"],
        },
    },
    {
        "name": "calculate_sprs_cmmc_score",
        "description": "Calculate DoD NIST SP 800-171 / CMMC 2.0 SPRS score (-203 to +110) and remediation pack links.",
        "inputSchema": {
            "type": "object",
            "properties": {"implemented_controls": {"type": "integer", "default": 85}},
        },
    },
    {
        "name": "audit_code_security_invariants",
        "description": "Scan code snippet for hardcoded secrets, shell injection, and smart-contract reentrancy.",
        "inputSchema": {
            "type": "object",
            "properties": {"code_snippet": {"type": "string"}},
            "required": ["code_snippet"],
        },
    },
    {
        "name": "get_compliance_arsenal_links",
        "description": "List instant self-serve checkout links ($49-$2,500) for CMMC SSP packs, repo audits, and datasets.",
        "inputSchema": {"type": "object", "properties": {}},
    },
]

def handle_rpc(msg: dict) -> dict | None:
    method = msg.get("method")
    req_id = msg.get("id")
    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "obsidian-mcp-server", "version": "1.0.0"},
            },
        }
    if method == "tools/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": TOOLS_SPEC}}
    if method == "tools/call":
        params = msg.get("params") or {}
        tname = params.get("name")
        args = params.get("arguments") or {}
        if tname == "scrub_cui_and_secrets":
            out = scrub_cui_and_secrets(args.get("text", ""))
        elif tname == "calculate_sprs_cmmc_score":
            out = calculate_sprs_cmmc_score(args.get("implemented_controls", 85))
        elif tname == "audit_code_security_invariants":
            out = audit_code_security_invariants(args.get("code_snippet", ""))
        else:
            out = ARSENAL_LINKS
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {"content": [{"type": "text", "text": json.dumps(out, indent=2)}]},
        }
    if req_id is not None:
        return {"jsonrpc": "2.0", "id": req_id, "result": {}}
    return None

if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_rpc(req)
            if resp is not None:
                sys.stdout.write(json.dumps(resp) + "\n")
                sys.stdout.flush()
        except Exception:
            pass
