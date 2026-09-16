from langchain.tools import tool


@tool
def scan_code(repo_path: str) -> str:
    """Scan source code for suspicious patterns."""
    return "found: strcpy without bounds check at line 42"


@tool
def read_file(path: str) -> str:
    """Read a file's content."""
    with open(path) as f:
        return f.read()


@tool
def create_poc(vuln_type: str, target: str) -> str:
    """Generate a proof-of-concept for a suspected vulnerability."""
    return "poc: input='A'*1000, expected=segfault"


@tool
def verify_poc(poc: str) -> str:
    """Run a PoC in a sandbox and report the result."""
    return "result: reproduced"


@tool
def read_claim(claim_id: str) -> str:
    """Read a claim and its evidence from chain."""
    return "claim: buffer_overflow, poc: 'AAAA...', evidence: ipfs://Qm..."


@tool
def list_open_disputes() -> str:
    """List all disputes awaiting verdict."""
    return "disputes: [d1, d2, d3]"


@tool
def read_dispute(dispute_id: str) -> str:
    """Read all evidence for a dispute."""
    return "claim: ..., counter: ..., sandbox: ..."


SUPPORT_TOOLS = [
    scan_code, read_file, create_poc, verify_poc,
    read_claim, list_open_disputes, read_dispute,
]
