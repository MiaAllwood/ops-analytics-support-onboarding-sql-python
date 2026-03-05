-- Identify tickets exceeding 4 hour SLA

SELECT
    ticket_id,
    issue_type,
    country,
    resolution_time_hours,
    CASE
        WHEN resolution_time_hours > 4 THEN 'SLA Breach'
        ELSE 'Within SLA'
    END AS sla_status
FROM support_tickets
ORDER BY resolution_time_hours DESC;
