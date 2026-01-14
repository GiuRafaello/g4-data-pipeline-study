select
    id,
    response_date
from {{ ref('forms_responses_bronze') }}
