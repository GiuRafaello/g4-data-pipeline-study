select
    event_name,
    date,
    sum(event_count) as event_count
from {{ source('bronze', 'ga4_events_bronze') }}
group by event_name, date
