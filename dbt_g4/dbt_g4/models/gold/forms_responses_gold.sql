select
    id,
    response_date::date as response_date
from {{ ref('forms_responses_silver') }}
