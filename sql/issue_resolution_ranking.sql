-- Rank issue types by average resolution time

WITH issue_resolution AS (
    SELECT
        issue_type,
        AVG(resolution_time_hours) AS avg_resolution_hours
    FROM support_tickets
    GROUP BY issue_type
)

SELECT
    issue_type,
    avg_resolution_hours,
    RANK() OVER (ORDER BY avg_resolution_hours DESC) AS resolution_rank
FROM issue_resolution;
