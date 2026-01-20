{{ config(materialized='table') }}

select
    cast(data_evento as date)       as data_evento,
    upper(trim(origem))             as origem,
    lower(trim(canal))              as canal,
    valor                            as valor,
    fonte                            as fonte,
    current_timestamp               as dt_carga
from {{ source('bronze', 'excel_events_bronze') }}
where valor is not null
