-- Average resolution time by issue type

SELECT
    issue_type,
    COUNT(ticket_id) AS total_tickets,
    AVG(resolution_time_hours) AS avg_resolution_hours
FROM support_tickets
GROUP BY issue_type
ORDER BY avg_resolution_hours DESC;
