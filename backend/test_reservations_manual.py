import asyncio
from app.services.reservations import calculate_total_revenue

async def main():
    result_a = await calculate_total_revenue("prop-001", "tenant-a")
    print("tenant-a:", result_a)

    result_b = await calculate_total_revenue("prop-001", "tenant-b")
    print("tenant-b:", result_b)

if __name__ == "__main__":
    asyncio.run(main())