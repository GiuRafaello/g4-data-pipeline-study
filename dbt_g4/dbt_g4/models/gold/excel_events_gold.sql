{{ config(materialized='table') }}

select
    data_evento,
    origem,
    canal,
    valor,
    fonte
from {{ ref('excel_events_silver') }}
