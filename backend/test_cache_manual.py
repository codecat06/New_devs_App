import asyncio
from app.services.cache import get_revenue_summary

async def main():
    print("=== First round ===")
    result_a1 = await get_revenue_summary("prop-001", "tenant-a")
    print("tenant-a first:", result_a1)

    result_b1 = await get_revenue_summary("prop-001", "tenant-b")
    print("tenant-b first:", result_b1)

    print("\n=== Second round (should come from cache) ===")
    result_a2 = await get_revenue_summary("prop-001", "tenant-a")
    print("tenant-a second:", result_a2)

    result_b2 = await get_revenue_summary("prop-001", "tenant-b")
    print("tenant-b second:", result_b2)

    print("\n=== Assertions ===")
    assert result_a1["tenant_id"] == "tenant-a"
    assert result_b1["tenant_id"] == "tenant-b"

    assert result_a1["total"] == result_a2["total"]
    assert result_b1["total"] == result_b2["total"]

    assert result_a1["total"] != result_b1["total"], "Cross-tenant leak detected: both tenants got same data"
    assert result_a2["total"] != result_b2["total"], "Cross-tenant leak detected from cache"

    print("PASS: No cross-tenant cache leakage detected.")

if __name__ == "__main__":
    asyncio.run(main())