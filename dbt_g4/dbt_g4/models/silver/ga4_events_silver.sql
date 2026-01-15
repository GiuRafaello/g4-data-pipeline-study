{{ config(materialized='view') }}

select
    event_name,
    to_date(date, 'YYYYMMDD') as event_date,
    platform,
    nullif(country, '(not set)') as country,
    event_count
from {{ source('bronze', 'ga4_events_bronze') }}

