-- create view with only the clean data
drop view if exists  dbo.zillow_data_clean 

create view dbo.zillow_data_clean
as 
select 
    Address,
    zip,
    home_type,
    case when home_type = 'Condominium' then 1 
         when home_type = 'Townhouse'   then 2
         when home_type = 'SingleFamily' then 3
         else -1 
    end as home_type_code,
    bathrooms,
    bedrooms,
    home_size,
    latitude,
    longitude,
    property_size,
    tax_value,
    (2019 - cast( year_built as int) ) as home_age,
    zestimate_amount,
    zestimate_percentile,
    zillow_id,
    City,
    state_id,
    county_name
from 
dbo.zillow_data_input 
where home_type in 
    ('Condominium','SingleFamily','Townhouse')
and zestimate_amount is not null 
and home_size is not null 
and city is not null 
and tax_value is not null 
and bedrooms is not null and bedrooms < 10
and bathrooms is not null and bathrooms < 10 
and year_built is not null 
