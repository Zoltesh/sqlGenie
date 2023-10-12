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
		--VARIABLE_START
        AND sales_flat_order.website_id IN (--MY_VALUE--)
		--VARIABLE_END
		--DESCRIPTION_START
		--[MY_VALUE] this is a super duper long comment to see if the words wrap. I'm wondering if the comment has to be multiline how my program will handle it
		--DESCRIPTION_END
        AND sales_flat_order.completed_at >= CURDATE()
    GROUP BY
        sales_flat_order.website_id, DATE(sales_flat_order.completed_at)
		--VARIABLE_START
) AS --DAILY_COUNTS--
		--VARIABLE_END
	--DESCRIPTION_START
	--[DAILY_COUNTS] count of day stuff
	--DESCRIPTION_END
GROUP BY
    daily_counts.website_id;