{{ config(materialized='table') }}

select
    event_date,
    event_name,
    sum(event_count) as total_events
from {{ ref('ga4_events_silver') }}
group by
    event_date,
    event_name
order by
    event_date,
    event_name
