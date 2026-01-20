{{ config(materialized='table') }}

select
    d.data_evento as date,
    d.origem,
    sum(d.valor) as total_valor
from (

    select
        event_date as data_evento,
        'ga4' as origem,
        event_count as valor
    from {{ ref('ga4_events_daily_gold') }}

    union all

    select
        data_evento,
        'excel' as origem,
        valor
    from {{ ref('excel_events_gold') }}

) d
group by 1, 2
