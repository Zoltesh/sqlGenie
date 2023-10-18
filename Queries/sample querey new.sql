SELECT
    daily_counts.website_id,
    AVG(daily_count) AS avg_daily_count
FROM (
    SELECT
        sales_flat_order.website_id,
        DATE(sales_flat_order.completed_at) AS order_day,
        COUNT(*) AS daily_count
    FROM
        sales_flat_order
    WHERE
        sales_flat_order.status NOT IN ('canceled')

        AND sales_flat_order.website_id IN (--MY_VALUE--, --ANOTHER--, --YEET--)

		--[MY_VALUE] this is a comment for the MY_VALUE variable. The description clarifies what's needed
        AND sales_flat_order.completed_at >= CURDATE()
    GROUP BY
        sales_flat_order.website_id, DATE(sales_flat_order.completed_at)

) AS --DAILY_COUNTS--
	--[DAILY_COUNTS] count of day stuff-- --[ANOTHER] new stuff--
    --[YEET] yeet stuff--

        WHERE mycol = 1
GROUP BY
    daily_counts.website_id;