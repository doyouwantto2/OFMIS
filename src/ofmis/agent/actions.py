from langchain.tools import tool


@tool
def submit(code_hash: str, vuln_type: str, poc: str, evidence: str) -> str:
    """Submit a vulnerability claim.

    Use ONLY when you have a reproducible PoC.

    Args:
        code_hash: hash of the target code
        vuln_type: e.g. buffer_overflow, sql_injection, xss
        poc: proof-of-concept input or steps
        evidence: CID/hash of supporting evidence (logs, traces)
    """
    return f"submitted claim for {code_hash}"


@tool
def dispute(claim_id: str, counter_evidence: str, reason: str) -> str:
    """Open a dispute against an existing claim.

    Use ONLY when you have concrete counter-evidence.

    Args:
        claim_id: the claim being disputed
        counter_evidence: CID/hash of counter-evidence
        reason: why the claim is wrong
    """
    return f"opened dispute on {claim_id}"


@tool
def verdict(dispute_id: str, choice: str, reasoning: str) -> str:
    """Cast a verdict on an open dispute.

    Args:
        dispute_id: the dispute to vote on
        choice: "valid" or "invalid"
        reasoning: justification for your vote
    """
    return f"cast verdict {choice} on {dispute_id}"


ACTION_TOOLS = [submit, dispute, verdict]
